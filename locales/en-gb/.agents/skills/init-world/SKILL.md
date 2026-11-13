---
name: init-world
description: "Use when: initialising a new D&D setting or campaign repository, guiding the DM through defining the world's coordinates, and generating the modular ten-tome architecture."
argument-hint: "Start the interview to configure and generate the world directory tree"
user-invocable: true
disable-model-invocation: false
---

# Skill: Initialising a World (`init-world`)

This skill guides the Dungeon Master through interactive configuration and generation of the folder scaffolding for a fantasy setting following the standard ten-tome architecture described in [world-architecture](./references/world-architecture.md).

> **📌 Linked Proper Names Rule**: every proper name of a setting entity (PCs, NPCs, factions, houses, cities, locations, magic items, customs, festivals, events…) appearing in produced text must be a **Markdown link** to the entity's canonical `.md` file (e.g. `[Name](relative/path/file.md)`), never plain text. Exceptions: headings, file names, frontmatter, code blocks, Mermaid nodes, and `.mw` sources. Entity without a sheet: never invent it — use `[TO_BE_DEFINED_BY_DM: missing sheet for <Name>]` and flag the gap. Checking and conversion: `link-proper-names` skill.

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
6. **`macro_areas_folder`**: *What would you like to name the regions/macro-areas subfolder inside `02_geography/`?*
   - Suggested options or custom name (e.g. *`regions/`* default, *`provinces/`*, *`continents/`*, *`realms/`*, *`marches/`*, *Other — specify folder name*).
7. **`peoples_subfolder`**: *Would you like to include the optional peoples/species subfolder inside `03_society_and_politics/`?*
   - Options: *Yes, use default `peoples/`*, *Yes, with a custom name (e.g. `species/`, `races/`, `lineages/`, `cultures/`)*, *No (only if needed later)*.
8. **`advanced_customisation`**: *For the remaining tomes, would you like to use the standard names or customise folders / enable optional subfolders?*
   - Options: *Use standard names and layout* (recommended), *Customise on request* — if selected, ask the DM which customisations they want (from: `<planes>/` and `<pantheon>/` in `01_cosmology/`; extra branches `11_+` or jurisdictions in `04_law_and_statutes/`; `Player_Characters/`/`Non_Player_Characters/` names, PC grouping by campaign or party, and `<npc_groups>/` in `05_characters/`; `<location_groups>/` in `06_locations/`; `<faction_groups>/` in `07_factions/`; Tome VIII name `08_...` and `<categories>/`; `<campaigns>/` and `<sessions>/` in `09_chronicles/`).

---

## 2. Generating the Directory Tree

Once the DM's answers are received, generate the modular structure using file-writing tools or the terminal:

1. **Root Files**:
   - `README.md`: General world index and navigation summary.
   - `setting_structure.json`: Hierarchical schema with metadata, tomes, and folders.
   - `SETTING_BIBLE.md`: Master source document containing the agreed premise.

2. **The Ten Founding Tomes**:
   - `01_cosmology/README.md` (with optional `<planes>/`, `<pantheon>/` subfolders if selected, each with `README.md`)
   - `02_geography/README.md` (with macro-areas subfolder: `regions/` or the custom name chosen by the DM, with its own `README.md`)
   - `03_society_and_politics/README.md` (with optional `peoples/` or custom-named subfolder if selected, and `customs_festivals_and_events/` subfolder containing `customs/`, `festivals_and_occurrences/`, `events/`, each with `README.md`)
   - `04_law_and_statutes/README.md` (with subfolders `01_legal_order_and_sources/`, `02_civil_rights_and_status/`, `03_dynastic_law_and_succession/`, `04_contracts_and_pacts/`, `05_treaties_and_diplomacy/`, `06_criminal_law_and_offences/`, `07_courts_and_procedure/`, `08_arcane_and_religious_law/`, `09_property_trade_and_taxation/`, `10_law_of_war_and_adventurers/`, plus any custom branches `11_+` or jurisdictional subfolders, each with `README.md`)
   - `05_characters/README.md` (with `<Player_Characters>/` [default `Player_Characters/`] and `<Non_Player_Characters>/` [default `Non_Player_Characters/`], plus optional `<npc_groups>/`, each with `README.md`)
   - `06_locations/README.md` (with optional `<location_groups>/` subfolders if selected, each with `README.md`)
   - `07_factions/README.md` (with optional `<faction_groups>/` subfolders if selected, each with `README.md`)
   - `<08_unique_magic_items>/README.md` (default `08_unique_magic_items/` or custom name, with optional `<categories>/` subfolders if selected, each with `README.md`)
   - `09_chronicles/README.md` (with `<campaigns>/<campaign_name>/<sessions>/` subfolders — default `campaigns/` and `sessions/` — each with `README.md`)
   - `10_timeline/README.md` (with `historical_chronology/`, `occurrence_register/`, `markwhen/` — containing `README.md`, `general_timeline.mw`, `epochs/`, `campaigns/` —, `calendar/`, `exports/README.md`)

3. **Initialising README Files**:
   Each directory receives a `README.md` with an initial thematic index and status badge:
   `> 🛡️ *Verified: [TODAY_DATE] | Modified: [TODAY_DATE]*`

4. **Final Validation**:
   Once creation is complete, invoke the `validate-structure` skill to certify that the directory tree is complete and free of broken links.
