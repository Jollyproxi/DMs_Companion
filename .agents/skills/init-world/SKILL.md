---
name: init-world
description: "Use when: initialising a new D&D setting or campaign repository, guiding the DM through defining the world's coordinates, and generating the modular ten-tome architecture."
argument-hint: "Start the interview to configure and generate the world directory tree"
user-invocable: true
disable-model-invocation: false
---

# Skill: Initialising a World (`init-world`)

This skill guides the Dungeon Master through interactive configuration and generation of the folder scaffolding for a fantasy setting following the standard ten-tome architecture described in [world-architecture](./references/world-architecture.md).

---

## 1. Guided Procedure (Initial Interview)

Before creating files or directories, ask the DM the following questions (using the environment's structured question tool, such as `vscode_askQuestions` or `AskUserQuestion`, if available; otherwise directly in chat):

1. **`name_premise`**: *What is the name of the setting and its core theme?*
   - Suggested options or free-text entry (e.g. *Classic High Fantasy*, *Gothic Dark Fantasy*, *Political & Arcane Intrigue*, *Other — specify*).
2. **`planar_peculiarities`**: *What cosmological peculiarities or special planes characterise the world?*
   - Multi-select options: *Subterranean depths / Underdark*, *Liminal planes / Mists*, *Fey or astral realms*, *Celestial spheres / Elemental planes*, *Other (specify)*.
3. **`key_factions`**: *What are the 2–3 dominant factions, noble houses, or kingdoms at the outset?* (Free text).
4. **`initial_campaign`**: *Would you like to initialise a first campaign and its PC party straight away?*
   - Options: *Yes (specify campaign name)*, *No (setting only for now)*.
5. **`customs_festivals_events`**: *Are there any everyday-life customs, recurring festivals, or historical events to register straight away?*
   - Multi-select options: *Customs (e.g. greeting/farewell rituals)*, *Recurring festivals/events*, *One-off events (historical or ongoing)*, *None for now (structure only)*.
   - Collected entries are catalogued using the `custom-festival-event` skill under `03_society_and_politics/customs_festivals_and_events/` and recorded in `10_timeline/`.

---

## 2. Generating the Directory Tree

Once the DM's answers are received, generate the modular structure using file-writing tools or the terminal:

1. **Root Files**:
   - `README.md`: General world index and navigation summary.
   - `setting_structure.json`: Hierarchical schema with metadata, tomes, and folders.
   - `SETTING_BIBLE.md`: Master source document containing the agreed premise.

2. **The Ten Founding Tomes**:
   - `01_cosmology/README.md`
   - `02_geography/README.md` (with optional `regions/` subfolder or chosen macro-area naming)
   - `03_society_and_politics/README.md` (with `customs_festivals_and_events/` subfolder containing `customs/`, `festivals_and_occurrences/`, `events/`, each with `README.md`)
   - `04_law_and_succession/README.md`
   - `05_characters/README.md` (with `Player_Characters/` and `Non_Player_Characters/` subfolders, each with `README.md`)
   - `06_locations/README.md`
   - `07_factions/README.md`
   - `08_unique_magic_items/README.md`
   - `09_chronicles/README.md` (with `campaigns/<campaign_name>/sessions/` subfolders, each with `README.md`)
   - `10_timeline/README.md` (with `historical_chronology/`, `occurrence_register/`, `markwhen/` — containing `README.md`, `general_timeline.mw`, `epochs/`, `campaigns/` —, `calendar/`, `exports/README.md`)

3. **Initialising README Files**:
   Each directory receives a `README.md` with an initial thematic index and status badge:
   `> 🛡️ *Verified: [TODAY_DATE] | Modified: [TODAY_DATE]*`

4. **Final Validation**:
   Once creation is complete, invoke the `validate-structure` skill to certify that the directory tree is complete and free of broken links.
