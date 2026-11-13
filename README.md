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

Replace `<lang>` with `it`, `en-gb`, `fr`, or `de`, and `<owner>` with the repository owner.

### Option 1 — Clone a single language branch and copy into your repo

```bash
git clone --depth 1 -b <lang> https://github.com/<owner>/DMs_Companion.git dms-companion
```

Copy the contents of `dms-companion/` (`AGENTS.md`, `CLAUDE.md`, `.github/agents/`, `.agents/skills/`) into the root of your own campaign repository (or into your user-level AI config directory).

### Option 2 — Install skills via Agent Skills CLI (`npx skills`)

```bash
# Install all skills from a language branch
npx skills add https://github.com/<owner>/DMs_Companion/tree/<lang>

# Or install directly from a locale skills folder on main
npx skills add https://github.com/<owner>/DMs_Companion/tree/main/locales/<lang>/.agents/skills
```

*(Remember to also copy `AGENTS.md` and/or `.github/agents/*.agent.md` if you want the full Archivist persona and workflow orchestration.)*

### Option 3 — Download ZIP from GitHub

Switch the branch selector on GitHub from `main` to `it`, `en-gb`, `fr`, or `de`, click **Code → Download ZIP**, and extract the files into your campaign folder.

---

## Multi-Harness Compatibility

Every language package ships with harness-agnostic entrypoints and graceful fallbacks:

| Harness / Framework | Discovered Files | Notes |
| :--- | :--- | :--- |
| **VS Code / GitHub Copilot** | `.github/agents/*.agent.md`, `.agents/skills/*/SKILL.md`, `AGENTS.md` | Full custom-agent picker + `/slash` skill commands + structured `vscode_askQuestions` prompts. |
| **OpenAI Codex CLI / Cursor / OpenCode / Gemini CLI** | `AGENTS.md`, `.agents/skills/*/SKILL.md` | Reads `AGENTS.md` instructions and standard Agent Skills automatically; prompts fall back to chat. |
| **Claude Code** | `CLAUDE.md` (`@AGENTS.md`), `.agents/skills/*/SKILL.md` | Copy or symlink `.agents/skills/*` into `.claude/skills/` if not auto-detected; uses `AskUserQuestion` or chat. |
| **Optional Extensions & MCPs** | `graphify/*`, `@markwhen/mw` / Markwhen extension | Enhanced cross-link graphing and timeline HTML/SVG rendering when installed; all skills work without them. |

---

## What's Inside Each Language Package

Each locale provides **1 Archivist agent** and **11 modular skills** designed around a standard **Ten-Tome World Architecture**:

1. **World Scaffolding & Validation** (`init-world`, `validate-structure`): Interactive world setup and tree/link diagnostics.
2. **Chronicles & Session Minutes** (`session-minutes`): Post-session DM interview or rough-note structuring, Mermaid PC-hook diagrams, and campaign index updates.
3. **Character Dossiers & Unique Magic Items** (`character-dossier`, `magic-item`): 5-module PC dossiers, NPC sheets, and 4-section magic item records.
4. **Lore Auditing & Review Dashboard** (`step-by-step-audit`, `full-file-audit`, `review-status`): Atomic or full-file fact-checking with visible `🛡️` verification timestamps and dashboard tracking.
5. **Master Canon Synchronisation** (`sync-bible-structure`): Compiles all ten tomes into a monolithic Setting Bible and a machine-readable JSON taxonomy.
6. **Customs, Festivals, Events & Markwhen Timelines** (`custom-festival-event`, `timeline-markwhen`): Structured cultural/historical sheets synced with `.mw` graphical timelines.

---

## Maintaining Language Branches (`Opzione B` Workflow)

Edit translations on `main` inside `locales/<lang>/`, then synchronise the orphan branches:

* **Automatic (GitHub Actions)**: Pushing changes under `locales/**` to `main` triggers [`.github/workflows/sync-language-branches.yml`](.github/workflows/sync-language-branches.yml), updating `it`, `en-gb`, `fr`, and `de` cleanly.
* **Local Sync**:
  * PowerShell (Windows): `./scripts/sync-branches.ps1`
  * Bash (macOS / Linux): `./scripts/sync-branches.sh`

---

## Licence

Released under the [CC BY-NC-SA 4.0 Licence](LICENSE).
