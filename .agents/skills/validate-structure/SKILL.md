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
Verifies the presence of the canonical directories (accepting equivalent legacy naming already established in an existing repository):
1. `01_cosmology`
2. `02_geography`
3. `03_society_and_politics` (with `customs_festivals_and_events/` subfolder containing `customs/`, `festivals_and_occurrences/`, `events/`)
4. `04_law_and_succession`
5. `05_characters` (with `Player_Characters/` and `Non_Player_Characters/` subfolders)
6. `06_locations`
7. `07_factions`
8. `08_unique_magic_items`
9. `09_chronicles` (with `campaigns/` subfolder)
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
   - Validate the 10-tome directories (including `customs_festivals_and_events/` and `10_timeline/` subfolders).
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
