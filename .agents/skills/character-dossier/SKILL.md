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

1. **Guided Acquisition (if needed)**: Confirm exact name, class, level, and campaign with the DM.
2. **Create Directory**:
   `05_characters/Player_Characters/<Campaign>/<PC_Name>/`
3. **Generate Modular Files**:
   - `README.md`: Character hub with role, moral traits, and index of the 5 files.
   - `01_profile_and_traits.md`: Biographical data, class, level, traits, and appearance.
   - `02_integrated_backstory.md`: Past, turning points, and roots in the world.
   - `03_relationships_and_dynamics.md`: Bonds with party companions, factions, and NPCs.
   - `04_equipment_and_abilities.md`: Signature items, weapons, focuses, and unique abilities.
   - `05_dm_hooks_and_secrets.md`: Hooks reserved for the DM, mysteries, and revelations.
4. **Update Campaign & Party Hubs**:
   Add the new PC to `README.md` in `05_characters/Player_Characters/<Campaign>/README.md` and to the general index `05_characters/README.md`.

---

## 3. Creating or Updating an NPC Sheet

When the DM introduces a notable Non-Player Character:

1. **Guided Acquisition**: If essential details are missing, clarify faction affiliation, living status, and whereabouts with the DM.
2. **Path**:
   `05_characters/Non_Player_Characters/<NPC_Name>.md`
3. **Structure**:
   - Header with role, faction (linked to `07_factions/`), residence (linked to `06_locations/`), alignment, and status.
   - Sections for Appearance & Temperament, Narrative Role, and DM Secrets & Hooks.
4. **Update NPC Index**:
   Add the entry to the relationship table in `05_characters/Non_Player_Characters/README.md`.

---

## 4. Post-Session Cross-Updates

When a session introduces new developments for a PC (e.g. newly uncovered hook, shifted bond, wound, or item acquired):
1. Locate the specific module to update (e.g. `03_relationships_and_dynamics.md` for a pact, `05_dm_hooks_and_secrets.md` for a revealed lead).
2. Apply the edit while preserving prior information.
3. Advance the `Modified: [TODAY_DATE]` field while leaving `Verified` untouched.
