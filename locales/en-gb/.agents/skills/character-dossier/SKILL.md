---
name: character-dossier
description: "Use when: creating, updating, or modularising six-module Player Character (PC) dossiers or Non-Player Character (NPC) sheets according to canonical campaign standards."
argument-hint: "Specify type (PC or NPC), character name, and operation (create, update module, sheet)"
user-invocable: true
disable-model-invocation: false
---

# Skill: Character Dossier Management (PC & NPC)

This skill governs the creation, modularisation, and systematic updating of Player Character (PC) dossiers and Non-Player Character (NPC) sheets, ensuring formal rigour, cross-linking, and fidelity to canon without ever inventing details unauthorised by the Dungeon Master.

Full templates are available in [dossier-template](./references/dossier-template.md).

> **📌 Linked Proper Names Rule**: every proper name of a setting entity (PCs, NPCs, factions, houses, cities, locations, magic items, customs, festivals, events…) appearing in produced text must be a **Markdown link** to the entity's canonical `.md` file (e.g. `[Name](relative/path/file.md)`), never plain text. Exceptions: headings, file names, frontmatter, code blocks, Mermaid nodes, and `.mw` sources. Entity without a sheet: never invent it — use `[TO_BE_DEFINED_BY_DM: missing sheet for <Name>]` and flag the gap. Checking and conversion: `link-proper-names` skill.

---

## 1. Compilation Rules (Zero Hallucinations)

- **Verified Data Only**: Populate only fields provided by the DM or already logged in session minutes.
- **Missing Fields**: Insert `[TO_BE_DEFINED_BY_DM: missing element]` (e.g. unchosen subclass, patron deity, or undisclosed DM secret).
- **Structured Interaction**: If the DM supplies partial details for a new character, ask for essential fields (Type: PC or NPC; Target campaign; Martial/arcane/social role; Alignment or moral code) using the environment's structured question tool (`vscode_askQuestions`, `AskUserQuestion`) if available, otherwise directly in chat.
- **Temporal Tracking**: Every created or modified file or module must include the status badge:
  `> 🛡️ *Verified: YYYY-MM-DD | Modified: YYYY-MM-DD*`
  If the file is modified after a session, update only the `Modified` date.

---

## 2. Creating a PC Dossier (6 Modules)

When the DM introduces or documents a new Player Character:

1. **Guided Acquisition (if needed)**: Confirm exact name, class, level, and campaign/party with the DM.
2. **Create Directory**:
   `05_characters/<Player_Characters>/<Campaign_or_Party>/<PC_Name>/` *(default: `05_characters/Player_Characters/<Campaign>/<PC_Name>/`, respecting custom folder names in the workspace)*
3. **Generate Modular Files**:
   - `README.md`: Character hub with role, moral traits, and index of the 6 files.
   - `01_profile_and_traits.md`: Biographical data, class, level, traits, and appearance.
   - `02_integrated_backstory.md`: Past, turning points, and roots in the world.
   - `03_relationships_and_dynamics.md`: Bonds with party companions, factions, and NPCs.
   - `04_equipment_and_abilities.md`: Signature items, weapons, focuses, and unique abilities.
   - `05_rumours_and_beliefs.md` — Rumours and beliefs.
   - `06_dm_hooks_and_secrets.md`: Hooks reserved for the DM, mysteries, and revelations.
4. **Structure**:
   - Header with role, faction (linked to Tome VII `07_factions/`), residence (linked to Tome VI `06_locations/`), alignment, and status.
   - Sections for Appearance & Temperament, Narrative Role, and DM Secrets & Hooks.
   - **Update Campaign & Party Hubs**:
   Add the new PC to `README.md` in `05_characters/<Player_Characters>/<Campaign_or_Party>/README.md` and to the general index `05_characters/README.md`.

---

## 3. Creating or Updating an NPC Sheet

## NPC archive convention

Follow the project’s NPC archive convention. Read the project instructions and the character volume index. For existing projects without an explicit rule, follow the established layout and indexes and flag conflicts or ambiguities to the GM.

Look up the existing sheet through indexes, files and any aliases. Keep one canonical file per identity and link to it from campaigns, factions and other locations. For geographical or narrative levels, use the documented stable connection and record its basis. First encounter (location and session record) and current whereabouts are separate fields.

Flag unresolved information and retain confirmed levels. Use a provisional location where the project defines one, otherwise ask the GM to resolve hierarchical placement. Use itinerant or cross-cutting categories only when supported by both the project and canon. In a flat archive, record these details in the sheet or index as specified.

Before an authorised move, map each source to its destination and check that the destination is free. Update old and new indexes, all incoming references and outgoing relative links. Preserve first-encounter history, refresh the derived documents required by the project, and verify canonical link targets and a single surviving sheet.

Dante retains `<Cornice>/<Luogo_riferimento>/<Nome_PNG>.md` under its NPC root.

Use the [template](./references/dossier-template.md) and update the required indexes.

---

## 4. Post-Session Cross-Updates

When a session introduces new developments for a PC (e.g. newly uncovered hook, shifted bond, wound, or item acquired):
1. Locate the specific module to update (e.g. `03_relationships_and_dynamics.md` for a pact, `06_dm_hooks_and_secrets.md` for a revealed lead).
2. Apply the edit while preserving prior information.
3. Advance the `Modified: [TODAY_DATE]` field while leaving `Verified` untouched.

In an existing dossier preserve the hooks, rename the former module 05 to 06, create the new 05 and update the index and incoming links including fragments. If 06 already exists, compare contents before moving files. Check that links still resolve on repeat runs.

## Gossip and rumours

For each documented role add a bullet summarising the version with a relative link to it. Include the subject’s stance when documented.
