"""Render and check the standalone campaign archivist instructions."""

import argparse
import json
from pathlib import Path
import sys
import tomllib


ROOT = Path(__file__).resolve().parents[1]
CLIENTS = {
    "it": ("Specifiche del client", "Usa {tool} se disponibile e consentito, altrimenti chiedi in chat.",
           "Per invocare una skill non rilevata, leggi il suo `SKILL.md` in `.agents/skills/`.",
           "Se operi come subagente, inoltra le domande per il Master alla conversazione principale."),
    "en-gb": ("Client-specific instructions", "Use {tool} when available and permitted, otherwise ask in chat.",
              "For a skill that is not discovered, read its `SKILL.md` in `.agents/skills/`.",
              "When acting as a subagent, relay questions for the GM to the parent conversation."),
    "fr": ("Consignes propres au client", "Utilisez {tool} si l’outil est disponible et autorisé, sinon posez la question dans le chat.",
           "Pour une compétence non détectée, lisez son fichier `SKILL.md` dans `.agents/skills/`.",
           "En tant que sous-agent, transmettez les questions destinées au MJ à la conversation principale."),
    "de": ("Clientspezifische Anweisungen", "Verwende {tool}, falls verfügbar und zulässig, andernfalls frage im Chat.",
           "Lies bei einem nicht erkannten Skill dessen `SKILL.md` in `.agents/skills/`.",
           "Leite als Subagent Fragen an die SL an die übergeordnete Unterhaltung weiter."),
}


def markdown_header(path):
    source = path.read_text(encoding="utf-8")
    if not source.startswith("---\n"):
        raise ValueError(f"Expected YAML frontmatter in {path}")
    return source[:source.index("\n---\n", 4) + len("\n---\n")]


def render(package):
    title, ask, skill_fallback, relay = CLIENTS[package.name]
    common = (package / "AGENTS.md").read_text(encoding="utf-8").rstrip()

    def instructions(tool, *notes):
        return common + f"\n\n## {title}\n\n" + "".join(
            f"- {note}\n" for note in (ask.format(tool=tool), *notes)
        )

    codex, = (package / ".codex/agents").glob("*.toml")
    codex_text = codex.read_text(encoding="utf-8")
    metadata = codex_text.split("\ndeveloper_instructions = ", 1)[0]
    codex_agent = tomllib.loads(codex_text)
    slug = codex_agent["name"]
    antigravity = package / f".agents/agents/{slug}.md"
    vscode = package / f".github/agents/{slug}.agent.md"
    claude = instructions("`AskUserQuestion`", skill_fallback)
    claude_header = (
        f"---\nname: {slug}\n"
        f"description: {json.dumps(codex_agent['description'], ensure_ascii=False)}\n"
        "model: inherit\n---\n\n"
    )
    codex_body = instructions("`request_user_input` / `request_user_input_async`", relay)
    codex_lines = "\n".join(
        json.dumps(line, ensure_ascii=False)[1:-1] for line in codex_body.splitlines()
    )
    codex_string = f'"""\n{codex_lines}\n"""'
    antigravity_body = instructions(
        "`ask_question`",
        "`ask_question`: `questions[]` → `question`, `options` (≥ 2), `is_multi_select`. "
        "`toolSummary`, `toolAction`.",
    )

    return {
        antigravity: markdown_header(antigravity) + "\n" + antigravity_body,
        vscode: markdown_header(vscode) + "\n" + instructions("`vscode_askQuestions`"),
        codex: f"{metadata}\ndeveloper_instructions = {codex_string}\n",
        package / "CLAUDE.md": claude,
        package / f".claude/agents/{slug}.md": claude_header + claude,
    }


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="Report drift without writing files")
    args = parser.parse_args()
    drift = False
    total = 0
    for locale in CLIENTS:
        for path, expected in render(ROOT / "locales" / locale).items():
            total += 1
            if path.is_file() and path.read_text(encoding="utf-8") == expected:
                continue
            if args.check:
                print(f"Out of sync: {path.relative_to(ROOT)}", file=sys.stderr)
                drift = True
            else:
                path.parent.mkdir(parents=True, exist_ok=True)
                path.write_text(expected, encoding="utf-8", newline="\n")
    if drift:
        return 1
    print(f"{total} standalone agent files {'verified' if args.check else 'synchronised'}.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
