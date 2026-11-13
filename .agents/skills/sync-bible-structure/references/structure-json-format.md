# Specification and Format of `setting_structure.json`

The `setting_structure.json` file serves as the machine-readable ontological and taxonomic map of the entire setting. It acts as a structured index for AI agents, visualisation tools, validation scripts, and rapid queries.

---

## 1. Root Document Schema

```json
{
  "setting_name": "Setting Name",
  "version": "1.0.0",
  "source_document": "SETTING_BIBLE.md",
  "description": "Concise 2–3 sentence summary of the setting's core pillars.",
  "structure": [
    /* Array of the 10 canonical tomes */
  ]
}
```

### Root Fields
* `setting_name` *(string)*: Official title of the setting.
* `version` *(string, SemVer)*: Current canon version (e.g. `"1.0.0"`). Bumped (`patch` for fixes/edits to existing modules, `minor` for adding new modules/regions/factions).
* `source_document` *(string)*: Relative path to the monolithic Setting Bible master file.
* `description` *(string)*: High-level overview of the architecture and theme (cosmology, society, central conflicts).
* `structure` *(array)*: Ordered list of chapter/tome objects (`01` to `10`).

---

## 2. Tome / Chapter Object

Each element of the `structure` array represents one of the ten architectural tomes:

```json
{
  "id": "cosmology",
  "code": "01",
  "title": "Cosmology & Metaphysical Architecture",
  "folder": "01_cosmology",
  "index": "01_cosmology/README.md",
  "description": "Summary of the topics covered in this tome.",
  "modules": [
    /* Array of individual modular files */
  ]
}
```

### Tome Fields
* `id` *(string)*: Unique snake_case identifier without numerical prefix (e.g. `"cosmology"`, `"geography"`, `"law_and_statutes"`).
* `code` *(string)*: Two-digit tome number (`"01"`–`"10"`).
* `title` *(string)*: Formal tome title extracted from its `README.md`.
* `folder` *(string)*: Directory name relative to the root (e.g. `"01_cosmology"`).
* `index` *(string)*: Relative path to the tome's hub `README.md`.
* `description` *(string)*: Description of the subject covered in the tome.
* `modules` *(array)*: List of individual modules belonging to the tome.

---

## 3. Module Object

Each element of the `modules` array describes an atomic `.md` file:

```json
{
  "id": "planar_structure",
  "code": "1.1",
  "title": "Planar and Cosmic Structure",
  "file": "01_cosmology/01_planar_structure.md",
  "key_concepts": [
    "Material Plane and planar boundaries",
    "Celestial spheres and outer realms",
    "Subterranean depths and deep rifts",
    "Elemental planes and liminal gates"
  ],
  "tables": [
    "Summary Table of the Planes"
  ],
  "dm_notes": "Detail of relevance to the DM (optional)"
}
```

### Module Fields
* `id` *(string)*: Unique snake_case identifier derived from the filename (without numerical prefix or extension).
* `code` *(string)*: Hierarchical decimal code (e.g. `"1.1"`, `"2.3"`, `"7.8"`).
* `title` *(string)*: Exact module title (matching the `.md` file's H1 heading).
* `file` *(string)*: Relative path of the Markdown file from the workspace root.
* `key_concepts` *(array of strings)*: 3 to 7 concise bullet summaries capturing the core rules, lore, and institutions introduced in the module.
* `tables` *(array of strings, optional)*: Titles of Markdown tables present in the document. Omit or leave empty if none exist.
* `dm_notes` *(string, optional)*: Summary of any `NOTE FOR THE DUNGEON MASTER` boxes or special narrative hooks.

---

## 4. Special Substructures (Regions, NPCs, Campaigns, Events, Timeline)

For tomes containing canonical subdirectories:

### A. Tome 02 (Geography — `regions/` or Custom Subfolder)
If a regional or macro-area subdirectory exists:
```json
"regions_folder": "02_geography/regions",
"regions_index": "02_geography/regions/README.md",
"region_modules": [
  {
    "number": 1,
    "title": "1st Region — Northern March",
    "distinguishing_trait": "Harsh climate / Mining frontier",
    "file": "02_geography/regions/01_northern_march.md"
  }
]
```
*(Both the subfolder name and keys are customisable: any macro-area folder name chosen in the workspace, e.g. `provinces/`, `continents/`, `realms/`, may use the standard `regions_folder` / `regions_index` / `region_modules` keys or matching `<name>_folder` / `<name>_index` / `<name>_modules` keys.)*

### B. Tome 05 (Characters — `<Player_Characters>/` and `<Non_Player_Characters>/`)
```json
"subfolders": {
  "player_characters": "05_characters/Player_Characters",
  "non_player_characters": "05_characters/Non_Player_Characters"
}
```
*(If the DM customises folder names — e.g. `PCs/`, `NPCs/`, `Heroes/`, NPC grouping subfolders, or `<Campaign_or_Party>/` — paths record the actual directories on disk.)*

### C. Tome 09 (Chronicles — `<campaigns>/` Subfolder)
```json
"campaigns_folder": "09_chronicles/campaigns",
"active_campaigns": [
  {
    "id": "campaign_name",
    "index": "09_chronicles/campaigns/campaign_name/README.md",
    "total_sessions": 12
  }
]
```
*(If `campaigns/` or `sessions/` use custom names — e.g. `expeditions/`, `adventures/`, `one_shots/`, `logs/` — keys record the actual paths on disk.)*

### D. Tome 03 (Society & Politics — `customs_festivals_and_events/` Sub-series and optional `peoples/`)
```json
"peoples_folder": "03_society_and_politics/peoples",
"peoples_modules": [
  {
    "id": "example_people",
    "code": "3.8.1",
    "title": "Name of the People / Species",
    "file": "03_society_and_politics/peoples/01_example_people.md"
  }
],
"customs_festivals_events_folder": "03_society_and_politics/customs_festivals_and_events",
"customs_festivals_events_index": "03_society_and_politics/customs_festivals_and_events/README.md",
"custom_modules": [
  {
    "id": "farewell_ceremony",
    "code": "3.5.1",
    "title": "The Farewell Ceremony",
    "file": "03_society_and_politics/customs_festivals_and_events/customs/01_farewell_ceremony.md"
  }
],
"festival_occurrence_modules": [
  {
    "id": "guard_tournament",
    "code": "3.6.1",
    "title": "The Guard Tournament",
    "file": "03_society_and_politics/customs_festivals_and_events/festivals_and_occurrences/01_guard_tournament.md",
    "periodicity": "variable",
    "trigger": "Return of military expeditions or rotation of ranks"
  }
],
"event_modules": [
  {
    "id": "siege_of_citadel",
    "code": "3.7.1",
    "title": "The Siege of the Citadel",
    "file": "03_society_and_politics/customs_festivals_and_events/events/01_siege_of_citadel.md",
    "occurrence_status": "concluded"
  }
]
```
* `periodicity` *(string, optional)* for festivals: `"fixed"`, `"variable"`, or `"mixed"`.
* `trigger` *(string, optional)*: conditions triggering the recurring event.
* `occurrence_status` *(string, optional)* for events: `"planned"`, `"ongoing"`, or `"concluded"`.

### D2. Tome 04 (Law & Statutes — Subfolders `01_` … `10_`)
```json
{
  "id": "law_and_statutes",
  "code": "04",
  "title": "Law & Statutes",
  "folder": "04_law_and_statutes",
  "index": "04_law_and_statutes/README.md",
  "description": "Legal order, civil rights, succession, contracts, treaties, criminal law, courts, arcane law, taxation, and law of war.",
  "modules": [],
  "branches": [
    {
      "id": "legal_order_and_sources",
      "code": "4.1",
      "title": "Legal Order & Sources of Law",
      "folder": "04_law_and_statutes/01_legal_order_and_sources",
      "index": "04_law_and_statutes/01_legal_order_and_sources/README.md",
      "modules": [
        {
          "id": "general_framework",
          "code": "4.1.1",
          "title": "General Framework of the Legal Order",
          "file": "04_law_and_statutes/01_legal_order_and_sources/01_general_framework.md"
        }
      ]
    }
  ]
}
```
*(Any extra branches `11_<branch>/` use codes `4.11.x`…; any jurisdictional subfolders inside a branch are nested under `"subfolders"` or `"jurisdictions"`.)*

### D3. Optional Subfolders (Tomes I, VI, VII, VIII)
When optional custom subfolders exist inside Tomes `01_cosmology/` (`<planes>/`, `<pantheon>/`), `06_locations/` (`<location_groups>/`), `07_factions/` (`<faction_groups>/`), or `<08_unique_magic_items>/` (`<categories>/`), each tome records its actual `"folder"` and `"index"` and exposes a `"subfolders"` (or `"groups"`) array with `{ "id", "title", "folder", "index", "modules": [...] }`.

### E. Tome 10 (Timeline)
```json
{
  "id": "timeline",
  "code": "10",
  "title": "Timeline & World Chronology",
  "folder": "10_timeline",
  "index": "10_timeline/README.md",
  "description": "Historical chronology, occurrence register, calendar, and Markwhen graphical timeline.",
  "modules": [],
  "historical_chronology_folder": "10_timeline/historical_chronology",
  "historical_chronology_modules": [
    {
      "id": "epoch_name",
      "code": "10.1.1",
      "title": "Title of the historical epoch or period",
      "file": "10_timeline/historical_chronology/01_epoch_name.md"
    }
  ],
  "occurrence_register_folder": "10_timeline/occurrence_register",
  "occurrence_register_modules": [
    {
      "id": "period_name",
      "code": "10.2.1",
      "title": "Title of the register period",
      "file": "10_timeline/occurrence_register/01_period_name.md"
    }
  ],
  "calendar_folder": "10_timeline/calendar",
  "calendar_modules": [
    {
      "id": "calendar",
      "code": "10.3.1",
      "title": "The World Calendar",
      "file": "10_timeline/calendar/01_calendar.md"
    }
  ],
  "markwhen_folder": "10_timeline/markwhen",
  "markwhen_files": [
    "10_timeline/markwhen/general_timeline.mw",
    "10_timeline/markwhen/epochs/<epoch_name>.mw",
    "10_timeline/markwhen/campaigns/<campaign_name>.mw"
  ],
  "exports_folder": "10_timeline/exports"
}
```
* `.mw` files and exports are **not** transposed into the Bible: they appear solely under `markwhen_files` and the folder properties.
* The tome's `modules` array remains empty: Tome 10 `.md` files reside in their dedicated arrays (`historical_chronology_modules`, `occurrence_register_modules`, `calendar_modules`), much like `region_modules` in Tome 02 and the sub-series in Tome 03.

---

## 5. Parsing & Automatic Extraction Rules

When running `generate-structure-json` or `update-structure-json`:
1. **Module Title**: Extracted from the first `# Title` in the Markdown file.
2. **Key Concepts**:
   - Identified from bullet lists (`* Concept: explanation`), `##` and `###` subheadings, or bold terms `**Term**`.
   - Normalised as concise, self-explanatory phrases.
3. **Tables**: Detected via column separator rows `| :--- | :--- |` preceded by a `## Table...` heading or caption.
4. **DM Notes**: Detected via `**NOTE FOR THE DUNGEON MASTER:**` or `> ⚠️ **DM Note:**` markers.
5. **Numerical Code**: If a file is named `03_flow_of_magic.md` inside `01_cosmology`, its code is `"1.3"`.
6. **Sub-series Codes**: Sheets inside `customs_festivals_and_events/` use third-level codes per subfolder (`3.5.x` customs, `3.6.x` festivals/occurrences, `3.7.x` events; `3.8.x` for optional `peoples/` or custom-named folder). Branches inside `04_law_and_statutes/` use `4.1.x` … `4.10.x` (and `4.11.x+` for extra custom branches; `4.Y.1` for `01_general_framework.md`, `4.Y.2+` for individual acts `02_<entry_slug>.md`). Files in `10_timeline/` use `10.1.x` (historical chronology), `10.2.x` (occurrence register), `10.3.x` (calendar).
7. **Typological Fields**: For festivals/occurrences extract `periodicity` and `trigger` from their template sections; for one-off events extract `occurrence_status`.
