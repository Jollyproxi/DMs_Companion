# Campaign Archivist — Usage Guide (British English)

Everything you need to put the **Campaign Archivist** to work at your table: installation, first steps, a complete reference of all **11 skills**, typical workflows, troubleshooting, and FAQ.

* Localised copies of this guide: [Italiano](https://github.com/<owner>/DMs_Companion/blob/main/locales/it/GUIDA-UTILIZZO.md) · [Français](https://github.com/<owner>/DMs_Companion/blob/main/locales/fr/GUIDE-UTILISATION.md) · [Deutsch](https://github.com/<owner>/DMs_Companion/blob/main/locales/de/NUTZUNGSANLEITUNG.md) — see also the project-level [USAGE.md](https://github.com/<owner>/DMs_Companion/blob/main/USAGE.md) on the `main` branch.

---

## 1. Installation

**Prerequisites**: an AI coding assistant (see the harness table below) and, recommended but not required, a Git repository for your campaign/world.

### Option 1 — Copy this branch into your campaign (recommended)

You are reading the `en-gb` package (either cloned with `git clone --depth 1 -b en-gb …` or downloaded as ZIP). Copy its contents into the root of **your own campaign repository** (or into your user-level AI config directory to make the toolkit available in every project):

* `AGENTS.md`, `CLAUDE.md`
* `.github/agents/`
* `.agents/skills/`
* `USAGE.md` (this guide)

### Option 2 — Install skills via Agent Skills CLI (`npx skills`)

```bash
# All skills from this language branch
npx skills add https://github.com/<owner>/DMs_Companion/tree/en-gb

# Or straight from the locale folder on main
npx skills add https://github.com/<owner>/DMs_Companion/tree/main/locales/en-gb/.agents/skills
```

*(Remember to also copy `AGENTS.md` and/or `.github/agents/*.agent.md` if you want the full Archivist persona and workflow orchestration.)*

### What the Installed Files Do

| File / Folder | Purpose |
| :--- | :--- |
| `AGENTS.md` | Universal rules and workflows, read by every harness. |
| `CLAUDE.md` | Claude Code entry point; imports `AGENTS.md`. |
| `.github/agents/campaign-archivist.agent.md` | The *Campaign Archivist* persona (agent picker entry in VS Code). |
| `.agents/skills/<skill>/SKILL.md` | The 11 modular skills (plus `references/` templates). |
| `USAGE.md` | This guide. |

### Harness Notes

| Harness | What Happens |
| :--- | :--- |
| **VS Code / GitHub Copilot** | The *Campaign Archivist* appears in the chat agent picker; skills are available as `/slash` commands; follow-up questions come as structured prompts (`vscode_askQuestions`). |
| **Claude Code** | `CLAUDE.md` is auto-loaded. If skills are not detected, copy or symlink `.agents/skills/*` into `.claude/skills/`. |
| **OpenAI Codex CLI / Cursor / OpenCode / Gemini CLI / Antigravity** | `AGENTS.md` and `.agents/skills/` are auto-discovered; just ask in natural language. |
| **Optional extras** | Graphify MCP (cross-link graphing) and the Markwhen CLI/extension (`@markwhen/mw`) for timeline rendering. Everything works without them. |

---

## 2. First Five Minutes

1. **Open your campaign repository** in your AI assistant.
2. **Select the *Campaign Archivist*** in the agent picker (VS Code) or mention it in chat (other harnesses).
3. **Tell it where you are**:
   * *New world* → `/init-world` and answer the guided interview: it generates the ten-tome folder tree, the root index, and the master-file seeds.
   * *Existing world* → `/validate-structure` first. The Archivist adapts to the folders you already have, including legacy names (`06_location/`, `07_factions/`, `08_oggetti magici peculiari/`, `cornici/`, …).
4. **Sanity-check the result**: the master files (`SETTING_BIBLE.md`, `REVIEW_STATUS.md`, `setting_structure.json`) live at the world root; the lore lives inside the ten tomes.
5. **Try one real task**: paste last session's rough notes and let the Archivist draft the minutes.

---

## 3. How the Toolkit Thinks

### The Golden Rule: Notarial Fidelity (Zero Hallucinations)

The Archivist organises **only** what you provide or have already canonised. It never invents characters, places, dates, plot twists, or numbers.

* **Missing information** → it asks you directly (interactive mode) or inserts a clearly visible placeholder `[TO_BE_DEFINED_BY_DM: description of missing detail]` that you can search for later.
* **Creativity on demand only** → it brainstorms (names, options, ideas) **only** when you explicitly ask (e.g. *"Give me 3 options for…"*, *"Invent a coherent name"*).

### The Ten-Tome Architecture

| Tome | Contents |
| :--- | :--- |
| `01_cosmology/` | Planes, celestial mechanics, flow of magic, cosmic ethics. |
| `02_geography/` | Cartography, territories, subterranean regions, regional dossiers (`regions/`). |
| `03_society_and_politics/` | Civil order, economy, social classes, justice; `customs_festivals_and_events/` (`customs/`, `festivals_and_occurrences/`, `events/`). |
| `04_law_and_succession/` | Fundamental laws, dynastic succession, pacts, treaties, courts. |
| `05_characters/` | Modular PC dossiers (`Player_Characters/<Campaign>/<PC_Name>/`) and NPC sheets (`Non_Player_Characters/`). |
| `06_locations/` | Adventure hubs, cities, strongholds, area hazards. |
| `07_factions/` | Noble houses, covens, guilds, orders, power hierarchies. |
| `08_unique_magic_items/` | Unique artefacts, relics, legal registers, properties. |
| `09_chronicles/` | Campaign hub: summary table + progressive session minutes (`campaigns/<name>/sessions/`). |
| `10_timeline/` | Cross-cutting chronology: `historical_chronology/`, `occurrence_register/`, `markwhen/` (`general_timeline.mw`, `epochs/`, `campaigns/`), `calendar/`, `exports/`. |

### Verification Badges

Every validated section carries a standard badge:

```markdown
> 🛡️ *Verified: YYYY-MM-DD | Modified: YYYY-MM-DD*
```

* **New text** → `Verified: UNVERIFIED | Modified: [TODAY]` until you review it.
* **Post-session edits** touch only `Modified`: when it is newer than `Verified`, the section needs re-review.
* **During an audit** both dates are aligned to today.

---

## 4. Skill Reference

Invoke skills with their slash command where available (VS Code, Claude Code), or simply mention the skill name in chat — the Archivist routes the request for you.

| # | Skill | What It Is For |
| :-: | :--- | :--- |
| 1 | `init-world` | Guided setup and scaffolding of a new world. |
| 2 | `validate-structure` | Structural health check of the archive. |
| 3 | `session-minutes` | Post-session minutes from rough notes or interview. |
| 4 | `character-dossier` | 5-module PC dossiers and NPC sheets. |
| 5 | `magic-item` | 4-section magic item records. |
| 6 | `step-by-step-audit` | Interactive fact-check, claim by claim. |
| 7 | `full-file-audit` | Audit of an entire file or folder. |
| 8 | `review-status` | Review dashboard built from the `🛡️` badges. |
| 9 | `sync-bible-structure` | Master Setting Bible + machine-readable JSON. |
| 10 | `custom-festival-event` | Customs, festivals/occurrences, one-off events. |
| 11 | `timeline-markwhen` | Graphical Markwhen timelines (`.mw`). |

### 4.1 `init-world` — World Scaffolding

* **When**: you start a brand-new world or campaign repository.
* **How**: `/init-world` — *“Start the interview to configure and generate the world directory tree.”*
* **Result**: the ten-tome folder tree with `README.md` indexes, the master-file seeds (`SETTING_BIBLE.md`, `setting_structure.json`, …), and the world premise recorded.

### 4.2 `validate-structure` — Structural Diagnostics

* **When**: before/after big reorganisations, or whenever something looks misplaced.
* **How**: `/validate-structure` — *“Run the archive structural compliance check.”*
* **Result**: a report of missing folders, absent `README.md` indexes, broken Markdown links, and stray `.md` files that belong inside one of the ten tomes.

### 4.3 `session-minutes` — Chronicles & Session Minutes

* **When**: right after a game session.
* **How**: paste your rough notes, or write *“start interview”* (`/session-minutes`) to be guided question by question.
* **Result**: a formal minute file in `09_chronicles/campaigns/<name>/sessions/NN_title.md` — notarial synopsis, Mermaid diagram of the PC hooks, salient phases, optional mechanics register — plus the updated campaign summary table.

### 4.4 `character-dossier` — PC Dossiers & NPC Sheets

* **When**: a new player character joins, an NPC is fleshed out, or a dossier module needs updating.
* **How**: `/character-dossier` — *“Specify type (PC or NPC), character name, and operation (create, update module, sheet).”*
* **Result**: a 5-module PC dossier (`01_profile_and_traits`, `02_integrated_backstory`, `03_relationships_and_dynamics`, `04_equipment_and_abilities`, `05_dm_hooks_and_secrets`) under `05_characters/Player_Characters/<Campaign>/<PC_Name>/`, or an NPC sheet under `05_characters/Non_Player_Characters/`, both registered in the indexes.

### 4.5 `magic-item` — Unique Magic Items

* **When**: a unique artefact, relic, or arcane focus enters the canon.
* **How**: `/magic-item` — *“Name of the magic item and details to record or update.”*
* **Result**: a 4-section record in `08_unique_magic_items/`: technical sheet, manufacture, mechanics, and legal status.

### 4.6 `step-by-step-audit` — Atomic Fact-Checking

* **When**: you want to verify lore claim by claim with the assistant asking you each point.
* **How**: `/step-by-step-audit` — *“Specify the file or topic to review and granularity (atomic or section).”*
* **Result**: an interactive review with no invented corrections; verified sections get their badge updated.

### 4.7 `full-file-audit` — Whole-File Audit

* **When**: an entire document or folder needs organic review.
* **How**: `/full-file-audit` — *“Path of the file or folder to verify (e.g. `05_characters/` or a single `.md`).”*
* **Result**: a structured audit of the whole target, inconsistencies flagged, fixes proposed for your approval.

### 4.8 `review-status` — Review Dashboard

* **When**: you want an overview of what is verified and what is stale.
* **How**: `/review-status` — *“Generate or update the workspace review status dashboard.”*
* **Result**: `REVIEW_STATUS.md` at the world root, with per-file percentages and modified-after-audit paragraphs flagged.

### 4.9 `sync-bible-structure` — Master Canon Synchronisation

* **When**: after canon changes, or when you want a single narrative master document / a machine-readable map.
* **How**: `/sync-bible-structure` with an operation — `generate-Bible`, `generate-structure-json`, `update-Bible`, or `update-structure-json`.
* **Result**: `SETTING_BIBLE.md` (monolithic narrative compilation of the ten tomes) and `setting_structure.json` (hierarchical taxonomy with metadata).

### 4.10 `custom-festival-event` — Customs, Festivals & Events

* **When**: a session introduces a custom, a recurring festival/occurrence, or a one-off event (revolt, cataclysm, historical upheaval).
* **How**: `/custom-festival-event` — *“Specify type and entry (e.g. 'custom: farewell ceremony', 'festival: solstice feast', 'event: siege of the citadel').”*
* **Result**: a typological sheet in `03_society_and_politics/customs_festivals_and_events/`, aligned with `10_timeline/` (chronology and occurrence register).

### 4.11 `timeline-markwhen` — Graphical Timelines

* **When**: you want to create, update, validate, or render the Markwhen timeline sources.
* **How**: `/timeline-markwhen` with an operation — `create-mw`, `update-mw`, `validate-mw`, or `export-mw` (e.g. *“create-mw epoch: First Age”*, *“update-mw campaign: Chronicles of the North”*).
* **Result**: `.mw` sources under `10_timeline/markwhen/` (`general_timeline.mw`, `epochs/`, `campaigns/`) kept in sync with chronology, occurrence register, and minutes; rendered exports in `10_timeline/exports/`.

---

## 5. Typical Workflows

### A. Setting Up a New World

`init-world` (guided interview) → `validate-structure` (sanity check) → add your first lore sheets → `sync-bible-structure` (`generate-Bible`, `generate-structure-json`) whenever you want the master documents.

### B. After a Game Session (the Core Loop)

1. `session-minutes` — paste the notes (or “start interview”); the minute is saved and the campaign index updated.
2. The Archivist lists every impacted file and drafts the cross-updates (dossiers, NPC sheets, indexes): approve them one by one.
3. New custom/festival/event mentioned? → `custom-festival-event` proposes the sheet; recurrences of known events are registered in `10_timeline/`.
4. `timeline-markwhen` (`update-mw`, or `create-mw` for new campaigns/epochs) keeps the `.mw` sources in sync.
5. If the session changed canonical lore → `sync-bible-structure` (`update-Bible`, `update-structure-json`).
6. The badges already show what changed (`Modified` > `Verified`): your next review starts from there.

### C. Adding Content Between Sessions

PC/NPC → `character-dossier` · Artefact → `magic-item` · Custom/festival/event → `custom-festival-event` · Big reshuffle → `validate-structure`.

### D. A Review / Audit Pass

`review-status` (see what is stale) → `step-by-step-audit` or `full-file-audit` on the targets → `review-status` again to refresh the dashboard.

---

## 6. Troubleshooting

* **The agent or skills don't show up in VS Code** — the files must sit at the **workspace root**: `.github/agents/` and `.agents/skills/`. Reload the window and reopen the agent picker.
* **Claude Code doesn't detect the skills** — copy or symlink `.agents/skills/*` into `.claude/skills/`; `CLAUDE.md` already imports `AGENTS.md`.
* **No structured question dialog appears** — that is expected outside VS Code: the Archivist falls back to plain chat and asks the same questions as text.
* **`export-mw` can't render** — install the Markwhen CLI (`npx @markwhen/mw`) or use the Markwhen VS Code extension / `markwhen.com`; exports are optional and never block the `.mw` sources.
* **The assistant invented lore** — that violates the golden rule: point it back to `AGENTS.md`, delete the invented text, and run a `step-by-step-audit` on the affected section.
* **Placeholders are piling up** — search for `[TO_BE_DEFINED_BY_DM:` and resolve them during an audit, or ask the Archivist to list them all.
* **Legacy folder names** (`06_location/`, `07_factions/`, …) — no problem: the Archivist adapts to what exists. Only the ten-tome *roles* are fixed, not the spellings.

---

## 7. FAQ

* **Do I need all 11 skills?** No. Install them all (they are self-contained) and use only what you need.
* **Can I run several campaigns in one world?** Yes — `09_chronicles/campaigns/<name>/` keeps each campaign's minutes separate; shared lore lives in the other tomes.
* **Can I use it for paid campaigns, streams, or actual plays?** Yes. The non-commercial clause applies to selling the toolkit itself, never to the games you run with it.
* **Can I repackage or sell the skills?** No — CC BY-NC-SA 4.0 (see `LICENSE` on the `main` branch).
* **How do I update to a new release?** Re-clone (or `git pull`) this branch and re-copy the files; merge any local customisation of `AGENTS.md` back in.
* **Where do I report bugs or harness findings?** GitHub Issues — see `CONTRIBUTING.md` on the `main` branch.

---

*DMs_Companion is free to use and share under CC BY-NC-SA 4.0. If it saves you prep time, you can support the project via [GitHub Sponsors](https://github.com/sponsors/Jollyproxi) or [Buy Me a Coffee](https://buymeacoffee.com/jollyproxi) — entirely optional.*
