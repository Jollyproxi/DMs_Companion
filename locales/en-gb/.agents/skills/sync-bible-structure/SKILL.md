---
name: sync-bible-structure
description: "Use when: generating or updating the Setting Bible (generate-Bible, update-bible) and setting_structure.json (generate-structure-json, update-structure-json), synchronising lore edits between the ten-tome modules and the master documents."
argument-hint: "Specify operation: generate-Bible, generate-structure-json, update-bible, or update-structure-json"
user-invocable: true
disable-model-invocation: false
---

# Skill: Master Canon Synchronisation (`sync-bible-structure`)

This skill governs the lifecycle of the two master artefacts of the D&D world:
1. **The Setting Bible** (`SETTING_BIBLE.md` or any existing monolithic master document): the single continuous narrative text for reading the entire canon.
2. **The Structural Schema** (`setting_structure.json`): the machine-readable ontological and taxonomic map of the ten tomes, modules, regions/subfolders, and key concepts.

The skill handles full generation and bidirectional incremental alignment between individual modular files across the ten tomes and the master documents, guaranteeing fidelity to canon without unapproved edits.

Consult the supporting reference files:
- [structure-json-format](./references/structure-json-format.md): JSON schema standard, required fields, and concept extraction rules.
- [bible-conventions](./references/bible-conventions.md): heading transposition rules, compilation order, and table formatting.

---

## Matrix of Supported Operations

| Argument / Command | Target Artefact | Mode | Primary Purpose |
| :--- | :--- | :--- | :--- |
| **`generate-Bible`** | `SETTING_BIBLE.md` | Monolithic / Full | Compiles all files from the 10 tomes into one master narrative document. |
| **`generate-structure-json`** | `setting_structure.json` | Full Scan | Scans the tome directory tree and builds the taxonomic JSON from scratch. |
| **`update-bible`** | `SETTING_BIBLE.md` | Incremental / Delta | Updates only the sections in the Bible corresponding to modified modules. |
| **`update-structure-json`** | `setting_structure.json` | Incremental / Delta | Synchronises the JSON with added, renamed, or updated modules. |

> **📌 Linked Proper Names Rule**: every proper name of a setting entity (PCs, NPCs, factions, houses, cities, locations, magic items, customs, festivals, events…) appearing in produced text must be a **Markdown link** to the entity's canonical `.md` file (e.g. `[Name](relative/path/file.md)`), never plain text. Exceptions: headings, file names, frontmatter, code blocks, Mermaid nodes, and `.mw` sources. Entity without a sheet: never invent it — use `[TO_BE_DEFINED_BY_DM: missing sheet for <Name>]` and flag the gap. Checking and conversion: `link-proper-names` skill.

---

## 1. Procedure: `generate-Bible` (Master Compilation)

Use this procedure to regenerate or create `SETTING_BIBLE.md` from scratch by assembling the individual modules.

### Operational Steps:
1. **Detect Target File**:
   - Check the workspace root for an existing master file (e.g. `SETTING_BIBLE.md` or equivalent master document already named in the repository).
   - If no master file exists, create `SETTING_BIBLE.md`.
2. **Determine Tome Order**:
   - Read `setting_structure.json` if present to retrieve the official order of tomes and modules.
   - Otherwise, sort numerically prefixed folders: `01_cosmology` (including optional `<planes>/`, `<pantheon>/` subfolders), `02_geography` (including `regions/` or the custom subfolder name adopted for macro-areas, sorted numerically), `03_society_and_politics` (including optional `peoples/` or custom-named subfolder and `customs_festivals_and_events/`: `customs/` = 3.5.x, `festivals_and_occurrences/` = 3.6.x, `events/` = 3.7.x), `04_law_and_statutes` (with branches `01_legal_order_and_sources/` … `10_law_of_war_and_adventurers/` = 4.1.x … 4.10.x, plus any extra branches `11_+` or jurisdictions), `05_characters` (`<Non_Player_Characters>/` and any grouping subfolders), `06_locations` (including optional grouping subfolders), `07_factions` (including optional grouping subfolders), `<08_unique_magic_items>` (or custom Tome VIII name, including optional category subfolders), `09_chronicles` (`<campaigns>/.../<sessions>/`), `10_timeline` (`historical_chronology/` = 10.1.x, `occurrence_register/` = 10.2.x, `calendar/` = 10.3.x; `.mw` sources in `markwhen/` and `exports/` are excluded from the Bible).
3. **Compose Monolithic Text**:
   - Insert the canonical header with metadata and status badge:
     ```markdown
     ### SETTING BIBLE: [SETTING_NAME]
     
     > 📜 **Monolithic Master Canon Document**
     > *Canon Version:* [VERSION] | *Last Compiled:* [TODAY_DATE]
     > 🛡️ *Verified: [DATE_V] | Modified: [TODAY_DATE]*
     ```
   - For each tome, insert an H5 heading (e.g. `##### 1. Cosmology & Metaphysical Architecture`).
   - For each modular file, adjust the heading hierarchy as defined in [bible-conventions](./references/bible-conventions.md):
     - The module's H1 heading becomes `###### *X.Y Module Title*` (or `### X.Y Module Title`).
     - Faithfully preserve Markdown tables, Mermaid diagrams, and `**NOTE FOR THE DUNGEON MASTER:**` boxes.
     - Preserve all `[TO_BE_DEFINED_BY_DM]` markers.
4. **Write & Report**:
   - Save the compiled master file.
   - Provide the DM with a summary: number of tomes processed, files included, and total document size.

---

## 2. Procedure: `generate-structure-json` (Complete Taxonomic Mapping)

Use this procedure to scan all workspace files and produce a complete, up-to-date machine-readable map in JSON format.

### Operational Steps:
1. **Acquire General Info**:
   - Read the root `README.md` or Bible header to extract `setting_name`, `description`, and determine `source_document`.
   - Set the initial version to `"1.0.0"` (or retain the current version if already present).
2. **Systematic Scan of the 10 Tomes**:
   - Iterate through directories `01_` to `10_`:
     - Extract `id`, `code`, `title`, and `description` from each tome's `README.md`.
     - Gather all `.md` module files inside the folder (excluding `README.md`).
     - For each `.md` module:
       - `id`: snake_case slug derived from the filename without its numerical prefix.
       - `code`: hierarchical numbering (e.g. `"1.1"` for `01_cosmology/01_planar_structure.md`).
       - `title`: extracted from the file's first `#` heading.
       - `file`: normalised relative path using `/`.
       - `key_concepts`: extract 3 to 7 key points drawn from subheadings and bold definitions.
       - `tables`: detect and include titles of any Markdown tables present.
       - `dm_notes`: extract the contents of any DM-only notes.
   - Handle canonical, optional, and custom-named subfolders (`01_cosmology/<planes_or_pantheon>/`, `02_geography/<regions_or_custom>/`, `03_society_and_politics/<peoples_or_custom>/` and `customs_festivals_and_events/`, `04_law_and_statutes/` including extra branches and jurisdictions, `05_characters/<Non_Player_Characters>/`, `06_locations/<groups>/`, `07_factions/<groups>/`, `<08_unique_magic_items>/<categories>/`, `09_chronicles/<campaigns>/`, `10_timeline/` with `markwhen/` sources) by populating the dedicated properties defined in [structure-json-format](./references/structure-json-format.md).
3. **Syntax Validation & Output**:
   - Generate `setting_structure.json` indented with 2 spaces.
   - Verify the JSON is strictly valid with no duplicate keys or stray characters.
   - Report the total number of indexed modules and sub-structures to the DM.

---

## 3. Procedure: `update-bible` (Incremental Synchronisation)

Use this procedure when one or more atomic modules have been edited or added, to align the monolithic Bible without regenerating the entire file.

### Operational Steps:
1. **Identify Modified Files**:
   - Locate target modules named by the DM or detect files where `Modified > Verified` by inspecting badges or `REVIEW_STATUS.md`.
2. **Locate Section in Master File**:
   - Open the master Bible file.
   - For each modified module, find its section anchor via hierarchical code (`X.Y`) or module title.
3. **Targeted Section Update**:
   - If the section exists: replace outdated text with the new modular version (adjusting heading levels per [bible-conventions](./references/bible-conventions.md)).
   - If the module is new: insert the new section in the proper ordinal position within its tome.
   - Leave all other sections strictly untouched.
4. **Update Master Metadata**:
   - Update the header metadata line:
     `> 🛡️ *Verified: [DATE_V] | Modified: [TODAY_DATE]*`
5. **Alignment Report**:
   - List the updated sections in the Bible for the DM.

---

## 4. Procedure: `update-structure-json` (JSON Delta Synchronisation)

Use this procedure to keep `setting_structure.json` synchronised when new files are added, modules renamed, or contents enriched.

### Operational Steps:
1. **Load Current State**:
   - Read the existing `setting_structure.json` file.
2. **Detect Delta**:
   - Compare physical files on disk across the 10-tome folders against the list in the `structure` array.
   - Identify:
     - ➕ **Added Modules**: `.md` files on disk absent from JSON.
     - 🔄 **Modified Modules**: files with changed titles, tables, or key concepts.
     - ➖ **Removed or Renamed Modules**: JSON paths no longer present on disk.
3. **Apply Changes to JSON**:
   - For added modules: create a new object with `id`, `code`, `title`, `file`, `key_concepts`, `tables`, `dm_notes` and sort appropriately.
   - For modified modules: update `title`, `key_concepts`, and `tables`, preserving any pre-existing custom annotations.
   - For removed/moved modules: update the `file` path or remove the obsolete entry (confirming with the DM before deleting).
4. **Bump Version**:
   - Increment the version following SemVer (e.g. `"1.0.0"` to `"1.0.1"` for content changes, or `"1.1.0"` for new modules/regions).
5. **Save & Diff**:
   - Rewrite formatted `setting_structure.json`.
   - Show the DM an exact summary of entities added, updated, or removed.

---

## Structured Interaction

If invoked without clear arguments or if conflicts arise during an update, ask the DM which operation to run (using the environment's structured question tool such as `vscode_askQuestions` / `AskUserQuestion` if available, otherwise in chat) offering these options:
- `generate-Bible` — Compile all modules from the 10 tomes into the monolithic master document
- `generate-structure-json` — Regenerate `setting_structure.json` in full by scanning the archive
- `update-bible` — Synchronise only recently modified or added modules into the Bible
- `update-structure-json` — Incrementally update `setting_structure.json` with file changes

---

## Final Quality & Validation Criteria

Upon completing each operation:
1. **JSON Syntax Check**: Whenever modifying `setting_structure.json`, ensure strictly valid JSON.
2. **Link & Path Verification**: `file` paths in JSON and cross-references in the Bible must point to existing files.
3. **Zero Hallucinations**: Never insert concepts, NPCs, or factions undocumented in source files or unapproved by the DM.
4. **Integration with Other Skills**:
   - After major structural changes, suggest running `validate-structure`.
   - After updating the Bible or modules, remind the DM to refresh the dashboard with `review-status`.
