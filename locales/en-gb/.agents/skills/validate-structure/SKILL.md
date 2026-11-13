---
name: validate-structure
description: "Use when: verifying the structural integrity of a D&D world repository, detecting missing directories, absent README indices, broken Markdown links, unlinked proper names, and misplaced files."
argument-hint: "Runs the archive structural compliance check"
user-invocable: true
disable-model-invocation: false
---

# Skill: World Structure Validation (`validate-structure`)

This skill performs a thorough diagnostic audit of the repository's file tree, ensuring compliance with the standard D&D architecture and promptly identifying technical anomalies.

> **📌 Linked Proper Names Rule**: every proper name of a setting entity (PCs, NPCs, factions, houses, cities, locations, magic items, customs, festivals, events…) appearing in produced text must be a **Markdown link** to the entity's canonical `.md` file (e.g. `[Name](relative/path/file.md)`), never plain text. Exceptions: headings, file names, frontmatter, code blocks, Mermaid nodes, and `.mw` sources. Entity without a sheet: never invent it — use `[TO_BE_DEFINED_BY_DM: missing sheet for <Name>]` and flag the gap. Checking and conversion: `link-proper-names` skill.

---

## 1. Diagnostic Verification Criteria

The skill checks the five pillars of structural integrity:

### A. Compliance of the Ten Tomes
Verifies the presence of the canonical directories (accepting equivalent legacy naming or DM-customised names in the repository):
1. `01_cosmology` *(with optional custom subfolders for planes/spheres and pantheon/deities)*
2. `02_geography` *(with optional `regions/` subfolder or custom macro-area folder name, e.g. `provinces/`, `continents/`, `realms/`)*
3. `03_society_and_politics` *(with optional `peoples/` or custom-named subfolder, and mandatory `customs_festivals_and_events/` subfolder containing `customs/`, `festivals_and_occurrences/`, `events/`)*
4. `04_law_and_statutes` *(with subfolders `01_legal_order_and_sources/` … `10_law_of_war_and_adventurers/`, plus any custom extra branches `11_+` or jurisdictional subfolders)*
5. `05_characters` *(with `<Player_Characters>/` [default `Player_Characters/`, e.g. `PCs/`, `Heroes/`] grouped by `<Campaign_or_Party>/`, and `<Non_Player_Characters>/` [default `Non_Player_Characters/`, e.g. `NPCs/`] with optional grouping subfolders)*
6. `06_locations` *(with optional custom `<location_groups>/` subfolders by type or macro-area)*
7. `07_factions` *(with optional custom `<faction_groups>/` subfolders by type)*
8. `08_unique_magic_items` *(or custom Tome VIII folder name, e.g. `08_magic_items/`, `08_artefacts_and_relics/`, with optional `<categories>/` subfolders)*
9. `09_chronicles` *(with `<campaigns>/` [default `campaigns/`, e.g. `expeditions/`, `adventures/`, `one_shots/`] and `<sessions>/` [default `sessions/`, e.g. `logs/`, `chapters/`])*
10. `10_timeline` (with `historical_chronology/`, `occurrence_register/`, `markwhen/`, `calendar/`, `exports/` subfolders)

### B. Presence and Validity of Indices (`README.md`)
Verifies that each main folder and subfolder contains an operational `README.md` acting as a section hub and index.

### C. Broken Markdown Link Detection
Scans relative links in `.md` files (e.g. `[Name](../../05_characters/...)`) to verify that target files actually exist on disk, reporting invalid paths or unsynchronised renames.

### D. Orphan or Misplaced Files
Identifies `.md` files saved at the project root or in non-canonical paths that belong inside one of the ten specific tomes (excluding canonical root master files such as `README.md`, `AGENTS.md`, `CLAUDE.md`, `SETTING_BIBLE.md`, `REVIEW_STATUS.md`). For syntactic and cross-reference validation of `.mw` sources in `10_timeline/markwhen/`, integrates with the `timeline-markwhen` skill (`validate-mw`).

### E. Coverage of Linked Proper Names
Verifies that every proper name of a registered entity (PCs, NPCs, factions, houses, cities, locations, magic items, customs, festivals, events…) appears in the text as a **Markdown link** to the entity's canonical `.md` file and not as plain text (linked proper names rule, subject to the established exceptions). In-depth scanning and conversion are delegated to the `link-proper-names` skill, of which this pillar is the surface-level diagnostic check.

---

## 2. Operational Procedure

1. **Filesystem Scan**:
   - Inspect folders and `.md` files in the workspace, excluding technical directories (`.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Execute Tests A–E**:
   - Validate the 10-tome directories and their canonical, optional, or custom-named subfolders (`<planes>/`, `<pantheon>/`, `<regions>/`, `peoples/`, `customs_festivals_and_events/`, `04_law_and_statutes/`, `05_characters/`, `<location_groups>/`, `<faction_groups>/`, `<categories>/`, `<campaigns>/<sessions>/`, and `10_timeline/`).
   - Check for missing `README.md` files.
   - Parse `[Text](path)` link strings and verify target existence via relative path.
   - Inspect the root directory for orphan files.
   - Check that proper names of registered entities appear as links and not as plain text (delegate in-depth analysis to `link-proper-names`).
3. **Produce Diagnostic Report**:
   - Present a concise summary to the DM:
     - 🟢 **Directory Tree Compliance**: [OK / Missing Tome Alerts]
     - 🟢 **README Index Coverage**: [OK / List of folders lacking README]
     - 🔗 **Link Integrity**: [OK / List of broken links with file and line]
     - 🏷️ **Linked Proper Names**: [OK / List of unlinked names with file and line]
     - 📂 **File Placement**: [OK / Orphan files suggested for relocation]
4. **Automated Repair Proposal**:
   - If anomalies are found, ask the DM (using the environment's structured question tool such as `vscode_askQuestions` / `AskUserQuestion` if available, otherwise in chat) how to proceed:
     - `Automatically repair anomalies (generate missing READMEs and fix paths)`
     - `Show report only without modifying files`
