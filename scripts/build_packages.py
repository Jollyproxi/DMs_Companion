"""Build one installable ZIP per language and AI harness."""

import argparse
from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile


ROOT = Path(__file__).resolve().parents[1]
LANGUAGES = ("de", "en-gb", "fr", "it")
# Root instructions, native skills directory, optional native agent definition.
HARNESSES = {
    "copilot": ("AGENTS.md", ".agents/skills", ".github/agents/*.agent.md"),
    "antigravity": ("AGENTS.md", ".agents/skills", ".agents/agents/*.md"),
    "codex": ("AGENTS.md", ".agents/skills", ".codex/agents/*.toml"),
    "claude-code": ("CLAUDE.md", ".claude/skills", ".claude/agents/*.md"),
    "cursor": ("AGENTS.md", ".cursor/skills", None),
    "opencode": ("AGENTS.md", ".agents/skills", None),
    "gemini-cli": ("GEMINI.md", ".gemini/skills", None),
}


def build_packages(output):
    output.mkdir(parents=True, exist_ok=True)
    for language in LANGUAGES:
        locale = ROOT / "locales" / language
        skills = locale / ".agents/skills"
        if not any(skills.glob("*/SKILL.md")):
            raise ValueError(f"No skills found in {skills}")
        skill_files = sorted(path for path in skills.rglob("*") if path.is_file())
        guide, = sorted(set(locale.glob("*.md")) - {locale / "AGENTS.md", locale / "CLAUDE.md"})
        for harness, (instructions, skill_dir, agent_pattern) in HARNESSES.items():
            source = "CLAUDE.md" if harness == "claude-code" else "AGENTS.md"
            files = {instructions: locale / source}
            if agent_pattern:
                agent, = locale.glob(agent_pattern)
                files[agent.relative_to(locale).as_posix()] = agent
            for path in skill_files:
                files[f"{skill_dir}/{path.relative_to(skills).as_posix()}"] = path

            archive = output / f"DMs_Companion-{language}-{harness}.zip"
            with ZipFile(archive, "w", compression=ZIP_DEFLATED) as package:
                for name, path in files.items():
                    data = path.read_bytes()
                    if path.suffix == ".md":
                        data = data.replace(b".agents/skills", skill_dir.encode())
                    package.writestr(name, data)
                package.write(guide, f"docs/DMs_Companion/{guide.name}")
                package.write(ROOT / "LICENSE", "docs/DMs_Companion/LICENSE")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("output", type=Path, help="directory for the ZIP files")
    build_packages(parser.parse_args().output)
