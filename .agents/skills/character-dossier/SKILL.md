---
name: character-dossier
description: "Use when: creating, updating, or modularising five-module Player Character (PC) dossiers or Non-Player Character (NPC) sheets according to canonical campaign standards."
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

## 2. Creating a PC Dossier (5 Modules)

When the DM introduces or documents a new Player Character:

1. **Guided Acquisition (if needed)**: Confirm exact name, class, level, and campaign/party with the DM.
2. **Create Directory**:
   `05_characters/<Player_Characters>/<Campaign_or_Party>/<PC_Name>/` *(default: `05_characters/Player_Characters/<Campaign>/<PC_Name>/`, respecting custom folder names in the workspace)*
3. **Generate Modular Files**:
   - `README.md`: Character hub with role, moral traits, and index of the 5 files.
   - `01_profile_and_traits.md`: Biographical data, class, level, traits, and appearance.
   - `02_integrated_backstory.md`: Past, turning points, and roots in the world.
   - `03_relationships_and_dynamics.md`: Bonds with party companions, factions, and NPCs.
   - `04_equipment_and_abilities.md`: Signature items, weapons, focuses, and unique abilities.
   - `05_dm_hooks_and_secrets.md`: Hooks reserved for the DM, mysteries, and revelations.
4. **Structure**:
   - Header with role, faction (linked to Tome VII `07_factions/`), residence (linked to Tome VI `06_locations/`), alignment, and status.
   - Sections for Appearance & Temperament, Narrative Role, and DM Secrets & Hooks.
   - **Update Campaign & Party Hubs**:
   Add the new PC to `README.md` in `05_characters/<Player_Characters>/<Campaign_or_Party>/README.md` and to the general index `05_characters/README.md`.

---

## 3. Creating or Updating an NPC Sheet

When the DM introduces a notable Non-Player Character:

1. Organise NPCs by **frame and primary reference location**, based on their stable territorial or narrative connection documented in canon. First encounter and current whereabouts are separate facts and do not automatically determine placement. Keep one canonical sheet; factions, campaigns and other locations link to it.
2. `05_characters/<Non_Player_Characters>/<Frame>/<Reference_location>/<NPC_Name>.md` (default: `05_characters/Non_Player_Characters/<Frame>/<Reference_location>/<NPC_Name>.md`).
3. If the reference is ambiguous, ask the DM; in direct drafting use `TO_BE_DEFINED_BY_DM/` at the unknown level (frame or location), without inventing affiliations. Use `Cross_Frame/` and/or `Itinerant/` for explicitly cross-frame or itinerant NPCs only when documented. Reuse canonical frame and location names and respect custom tome names.
4. **Structure**:
   - Header with role, faction (linked to Tome VII `07_factions/`), residence (linked to Tome VI `06_locations/`), alignment, and status.
   - Sections for Appearance & Temperament, Narrative Role, and DM Secrets & Hooks.
   - **Reference frame:** [Link to the canonical sheet in Tome II]
   - **Primary reference location:** [Link to the canonical sheet in Tome VI and reason for the connection]
   - **Current whereabouts:** [Location link, if known; separate from primary reference]
   - **First encounter:** [Links to minutes and location, if documented]
5. Create or update the tome, NPC, frame and location `README.md` files; indexes list the frame, primary location and link to the unique sheet.
6. When reorganising existing sheets, prepare a source → destination map from canon and apply authorised moves. Recalculate outgoing relative links and update all incoming references (minutes, dossiers, locations, factions, timelines), old and new READMEs, the Bible and JSON. Do not duplicate sheets or rewrite the historical first-encounter location. Flag unresolved cases and check links after moving.

---

## 4. Post-Session Cross-Updates

When a session introduces new developments for a PC (e.g. newly uncovered hook, shifted bond, wound, or item acquired):
1. Locate the specific module to update (e.g. `03_relationships_and_dynamics.md` for a pact, `05_dm_hooks_and_secrets.md` for a revealed lead).
2. Apply the edit while preserving prior information.
3. Advance the `Modified: [TODAY_DATE]` field while leaving `Verified` untouched.
