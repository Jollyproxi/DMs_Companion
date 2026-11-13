---
name: link-proper-names
description: "Use when: verifying or converting proper names of people, places, cities, items, factions, customs, and events into Markdown links to their canonical .md files; scanning files, folders, or the entire archive to detect unlinked names and restore compliance with the linked proper names rule."
argument-hint: "Path of the file or folder to scan (or 'entire archive')"
user-invocable: true
disable-model-invocation: false
---

# Skill: Mandatory Linking of Proper Names (`link-proper-names`)

This skill enforces the universal rule whereby every proper name of a setting entity must be a Markdown link to the entity's canonical `.md` file: it scans documents, detects names appearing as plain text, classifies them, and proposes or applies their conversion into links, reporting sheetless entities to the DM.

---

## 1. Reference Rule

- Every **proper name** of a setting entity — people (PCs, NPCs), houses, factions, guilds, cities, locations, regions, planes, magic items, customs, festivals, events, epochs, laws, institutions — appearing in produced text must be a **Markdown link** to that entity's canonical `.md` file, with the proper name as the link text: `[Name](relative/path/file.md)`.
- The path is **relative to the file being written** and must point to a file that actually exists on disk.
- The link text is the entity's proper name in its canonical form (that of the sheet's H1 title or file name).
- **Exceptions** (names allowed without a link):
  1. Headings and file names.
  2. YAML frontmatter, code blocks, commands, and paths.
  3. Labels of Mermaid diagrams and Markwhen `.mw` sources (where Markdown links are not rendered).
  4. Generic designations not referring to registered entities.
- **Entity Without a Sheet**: never invent the sheet. Insert the placeholder `[TO_BE_DEFINED_BY_DM: missing sheet for <Name>]` and flag the gap, or — in interactive mode — ask the DM whether to register the entity with the relevant skill (`character-dossier`, `magic-item`, `custom-festival-event`, etc.).

---

## 2. Building the Entity Index

Before scanning, build the `name → canonical file path` map:

1. **Preferred source**: if `setting_structure.json` is present at the workspace root, use it as the index (module names and associated paths).
2. **Direct sweep**: otherwise (or for completeness) scan the ten tomes — `05_characters/` (PCs and NPCs), `06_locations/`, `07_factions/`, `08_unique_magic_items/`, `03_society_and_politics/customs_festivals_and_events/`, `02_geography/` (regions), `01_cosmology/` (planes), `04_law_and_succession/` (laws, treaties), `10_timeline/historical_chronology/` (epochs, historical events) — collecting H1 titles and file names.
3. **Canonical names**: for each sheet the proper name is the document title (H1) or the file name without extension; also record any variants or aliases explicitly documented in the sheet.
4. **Homonyms**: if two entities share the same name, flag the ambiguity and ask the DM which sheet to link.

---

## 3. Operational Procedure

1. **Determine the Scope**: single file, folder, or entire archive (excluding technical directories such as `.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Scan the Text**: analyse `.md` files line by line, excluding the §1 exceptions (frontmatter, code blocks, Mermaid labels, `.mw` sources, headings).
3. **Classify Every Occurrence**:
   - ✅ **Already Linked**: the name is already a valid link (verify the target exists on disk).
   - 🔗 **To Be Linked**: bare name with an existing sheet → convert into a link.
   - ⚠️ **No Sheet**: bare name of an unregistered entity → placeholder `[TO_BE_DEFINED_BY_DM: ...]`.
   - ❓ **Ambiguous**: homonym or uncertain match → consult the DM.
4. **Report the Result** to the DM as a table (`file:line | name | status | proposed action`).
5. **Apply on Confirmation**: convert names into correct relative links (recompute the path based on the file's location); for ⚠️ cases insert the placeholder and propose registration with the relevant skill; for ❓ cases await the DM's decision.
6. **Final Summary**: list the modified files, the converted names, and the outstanding gaps.

---

## 4. Integration with Other Skills

- **`validate-structure`**: this skill constitutes **pillar E** of the structural diagnostics (coverage of linked proper names); run it together with checks A–D for a complete audit.
- **Audit skills (`step-by-step-audit`, `full-file-audit`)**: during the audit, also verify that proper names are linked and restore compliance alongside the DM-approved corrections.
- **Sheet-creation skills (`character-dossier`, `magic-item`, `custom-festival-event`)**: every new sheet makes its name linkable; upon creation, flag in which existing files the new name should be linked and propose updating the references.
- **`sync-bible-structure`**: in the Setting Bible proper names follow the same convention, remaining links to their source modules.
- **`review-status`**: outstanding gaps (names without sheets) can be tracked in the `REVIEW_STATUS.md` dashboard as entries awaiting registration.
