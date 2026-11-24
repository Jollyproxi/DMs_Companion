# DMs_Companion

A portable, multi-harness **AI Campaign Archivist** and modular **Agent Skills** toolkit for Dungeon Masters running Dungeons & Dragons and tabletop RPG campaigns.

**DMs_Companion** is designed as a drop-in companion library that you can copy, install, or adapt into **your own** worldbuilding and campaign repositories — across **VS Code Copilot**, **Claude Code**, **OpenAI Codex CLI**, **Cursor**, **Gemini CLI / Antigravity**, **OpenCode**, and other Agent-Skills-compatible environments.

Its guiding principle is **notarial fidelity (zero hallucinations)**: the assistant organises session notes, character dossiers, magic items, customs, historical timelines, and setting bibles strictly from what the DM provides or has already canonised — flagging missing information instead of inventing lore.

---

## Available Languages (Branch-per-Language Distribution)

The `main` branch holds only this project overview, the source localisations under [`locales/`](locales), and branch-sync automation. Each language is also published directly to the root of its own standalone orphan Git branch so you can grab ready-to-use files cleanly:

| Language | Branch | Source Folder | Agent Persona | Skills Path |
| :--- | :--- | :--- | :--- | :--- |
| **Italiano** | `it` | [`locales/it/`](locales/it) | *Archivista di Campagna* | [`locales/it/.agents/skills/`](locales/it/.agents/skills) |
| **British English** | `en-gb` | [`locales/en-gb/`](locales/en-gb) | *Campaign Archivist* | [`locales/en-gb/.agents/skills/`](locales/en-gb/.agents/skills) |
| **Français** | `fr` | [`locales/fr/`](locales/fr) | *Archiviste de Campagne* | [`locales/fr/.agents/skills/`](locales/fr/.agents/skills) |
| **Deutsch** | `de` | [`locales/de/`](locales/de) | *Kampagnen-Archivar* | [`locales/de/.agents/skills/`](locales/de/.agents/skills) |

> **Why separate branches?** AI harnesses auto-discover agents and skills from fixed paths (`.agents/skills/`, `.github/agents/`, `AGENTS.md`). Keeping each language on its own branch ensures you can clone, download, or install a single language cleanly without mixing four languages into your AI's context window or overwriting your world's own `README.md`.

---

## Quick Start: Copy or Install into Your Campaign

> **New here?** The [Usage Guide](USAGE.md) walks you through installation, first steps, every skill, typical workflows, and troubleshooting. Localised: [Italiano](locales/it/GUIDA-UTILIZZO.md) · [British English](locales/en-gb/USAGE.md) · [Français](locales/fr/GUIDE-UTILISATION.md) · [Deutsch](locales/de/NUTZUNGSANLEITUNG.md).

Choose your language once in the Bash shell where you will run the installation commands.

```bash
dms_lang=en-gb  # Language: it | en-gb | fr | de
```

### Option 1 — Clone a single language branch and copy into your repo

```bash
git clone --depth 1 -b "$dms_lang" https://github.com/Jollyproxi/DMs_Companion.git dms-companion
```

Copy the contents of `dms-companion/` (`AGENTS.md`, `CLAUDE.md`, `.github/agents/`, `.agents/skills/`) into the root of your own campaign repository (or into your user-level AI config directory).

### Option 2 — Install skills via Agent Skills CLI (`npx skills`)

```bash
# Install all skills from a language branch
npx skills add "https://github.com/Jollyproxi/DMs_Companion/tree/$dms_lang"

# Or install directly from a locale skills folder on main
npx skills add "https://github.com/Jollyproxi/DMs_Companion/tree/main/locales/$dms_lang/.agents/skills"
```

*(Remember to also copy `AGENTS.md` and/or `.github/agents/*.agent.md` if you want the full Archivist persona and workflow orchestration.)*

### Option 3 — Download ZIP from GitHub

From [GitHub Releases](https://github.com/Jollyproxi/DMs_Companion/releases), download `DMs_Companion-LANGUAGE-HARNESS.zip` for your setup (for example, `DMs_Companion-it-codex.zip`). Extract its contents, including hidden folders, at the root of your campaign repository. Merge any existing instruction files you want to keep.

To download a full language branch, switch the branch selector on GitHub from `main` to `it`, `en-gb`, `fr`, or `de`, click **Code → Download ZIP**, and extract the files into your campaign folder.

Each language package also ships its own usage guide at the branch root (`USAGE.md` / `GUIDA-UTILIZZO.md` / `GUIDE-UTILISATION.md` / `NUTZUNGSANLEITUNG.md`) — see the [Usage Guide](USAGE.md) on `main` for the full walkthrough.

---

## Multi-Harness Compatibility

Every language package ships with harness-agnostic entrypoints and graceful fallbacks:

| Harness / Framework | Discovered Files | Notes |
| :--- | :--- | :--- |
| **VS Code / GitHub Copilot** | `.github/agents/*.agent.md`, `.agents/skills/*/SKILL.md`, `AGENTS.md` | Full custom-agent picker + `/slash` skill commands + structured `vscode_askQuestions` prompts. |
| **Google Antigravity (App, IDE, CLI)** | `.agents/agents/*.md`, `.agents/skills/*/SKILL.md`, `AGENTS.md` | Native custom agent (primary agent + subagent) and auto-discovered skills under the user's global `~/.gemini/config/` or the workspace `.agents/`; structured `ask_question` prompts with the same button and checkbox behaviour as VS Code. |
| **OpenAI Codex** | `AGENTS.md`, `.agents/skills/*/SKILL.md`, `.codex/agents/*.toml` | Uses structured questions through `request_user_input` or `request_user_input_async` when available and permitted, with chat as a fallback. |
| **Cursor / OpenCode / Gemini CLI** | `AGENTS.md`, `.agents/skills/*/SKILL.md` | Reads `AGENTS.md` instructions and standard Agent Skills automatically; prompts fall back to chat. |
| **Claude Code** | `CLAUDE.md`, `.claude/agents/*.md`, `.agents/skills/*/SKILL.md` | Copy or symlink `.agents/skills/*` into `.claude/skills/` if not auto-detected; uses `AskUserQuestion` or chat. |
| **Optional Extensions & MCPs** | `graphify/*`, `@markwhen/mw` / Markwhen extension | Enhanced cross-link graphing and timeline HTML/SVG rendering when installed; all skills work without them. |

---

## What's Inside Each Language Package

Each locale provides **1 Archivist agent** and **14 modular skills** designed around a standard **Ten-Tome World Architecture**:

1. **World Scaffolding & Validation** (`init-world`, `validate-structure`, `link-proper-names`): Interactive world setup, tree/link diagnostics, and mandatory proper-name linking.
2. **Chronicles & Session Minutes** (`session-minutes`, `transcription-glossary`): Pre-transcription spelling-only proper-name glossary export, post-session DM interview, rough-note structuring, or import from the included **NotebookLM/LLM structured session-transcription prompt**, Mermaid PC-hook diagrams, and campaign index updates.
3. **Character Dossiers & Unique Magic Items** (`character-dossier`, `magic-item`): 6-module PC dossiers, NPC sheets, and 4-section magic item records.
4. **Lore Auditing & Review Dashboard** (`step-by-step-audit`, `full-file-audit`, `review-status`): Atomic or full-file fact-checking with visible `🛡️` verification timestamps and dashboard tracking.
5. **Master Canon Synchronisation** (`sync-bible-structure`): Compiles all ten tomes into a monolithic Setting Bible and a machine-readable JSON taxonomy.
6. **Customs, Festivals, Events & Markwhen Timelines** (`custom-festival-event`, `timeline-markwhen`): Structured cultural/historical sheets synced with `.mw` graphical timelines.

7. **Campaign Knowledge** (`campaign-knowledge`): Consult and update who knows individual facts in-world. Collect gossip and rumours separately, with local variants and links to the people and events involved.

---

## Maintaining Language Branches

Edit translations on `main` inside `locales/<lang>/`, then let the pipeline synchronise the orphan branches:

* **Automatic**: Pushing changes under `locales/**` to `main` triggers [`.github/workflows/sync-language-branches.yml`](.github/workflows/sync-language-branches.yml), which publishes each `locales/<lang>/` tree to the root of its `it`, `en-gb`, `fr`, or `de` branch.
* **Manual**: Run the same workflow on demand from the **Actions** tab (*Sync Language Branches → Run workflow*).

### Building a versioned release

Run `python scripts/build_packages.py dist` to build the ZIPs locally, or run **Build release packages** from the Actions tab to download a preview. Each of the four languages has a separate ZIP for Copilot, Antigravity, Codex, Claude Code, Cursor, OpenCode and Gemini CLI. Each archive places the instructions and skills at the campaign root in the layout for that harness. The localised guide and licence are under `docs/DMs_Companion/`.

Merge feature pull requests into `main`. When you are ready to publish, open a GitHub pull request with **base** `release` and **compare** `main`. Use **Create a merge commit** to keep the promoted commits in the release branch history.

Merging the release pull request builds and checks the packages, then publishes them in a GitHub Release tagged `release-<run-number>` at the merged commit. Pull requests and manual workflow runs build preview packages.

---

## Work in Progress & Contributions

**DMs_Companion is still a work in progress.** The core skills and the Archivist persona are functional and usable today, but expect rough edges, evolving conventions, and occasional restructuring as the toolkit matures.

Contributions are very welcome — whether that's bug reports, translation fixes, new harness compatibility notes, or improvements to the skills themselves. That said, this is a solo-maintained project, and **reviews may take a while**: I want to give each contribution proper attention to preserve the project's principles, so please be patient if responses aren't immediate. A slow "yes, carefully reviewed" is worth more than a fast "merged and broken". See [CONTRIBUTING.md](CONTRIBUTING.md) for guidelines and contribution terms.

### Contributions & Licence

By submitting a contribution (pull request, patch, or translation), you agree that:

1. your contribution is licensed under the [CC BY-NC-SA 4.0 Licence](LICENSE), like the rest of the project; and
2. you grant the project maintainer the right to **relicense** your contribution as part of future versions of DMs_Companion under a different licence (e.g. a dual-licensing model).

You retain the copyright of your work. This keeps a future licence change possible without having to track down every past contributor.

---

## Support the Project

DMs_Companion is and will remain **free to use and share**. If it saves you prep time at your table, you can support its development with an optional donation:

* **[GitHub Sponsors](https://github.com/sponsors/Jollyproxi)** — one-off or recurring sponsorships.
* **[Buy Me a Coffee](https://buymeacoffee.com/jollyproxi)** — one-off tips.

Donations are entirely optional. Using the toolkit, reporting issues, and telling other DMs about it is support too.

---

## Licence

DMs_Companion is licensed under [CC BY-NC-SA 4.0](LICENSE). You are free to **use, copy, share, and adapt** it, as long as you:

* give appropriate credit;
* **don't use it commercially** — selling the toolkit, repackaging its skills for paid marketplaces, or distributing it as part of a paid product is not permitted;
* share any derivative work under the same licence.

Using the toolkit to run your own campaigns is always fine — **even paid campaigns, streams, or actual plays**. The non-commercial restriction applies to selling the toolkit itself, not to the games you run with it.
