# Markwhen Graphical Timeline Conventions

Compilation standard for Markwhen sources stored in `10_timeline/markwhen/`, the world's graphical timeline.

---

## 1. Structure of the `markwhen/` Folder

```text
10_timeline/markwhen/
├── README.md                   # Index of .mw sources and summary of conventions
├── general_timeline.mw         # General index/legend (NOT an aggregate of sources)
├── epochs/
│   └── <epoch_name>.mw         # One source per historical epoch/period
└── campaigns/
    └── <campaign_name>.mw      # One source per campaign: everything relevant to that campaign
```

- `general_timeline.mw` is the **index/legend**: it holds the tag legend, date conventions, and links to epoch and campaign sources. It does not duplicate the content of other files.
- Files in `epochs/` are the authoritative chronology sources, viewable individually.
- Files in `campaigns/` hold **everything relevant** to the campaign (past and future), with links to minutes in `09_chronicles/`.

---

## 2. Basic Syntax

One event per line, with date, title, and tags:

```text
512-03-01: Solstice Feast #festival #historical
512/513: Siege of the Citadel #event #historical #faction_northern_watch
514: Guard Tournament #festival #occurrence #ongoing
```

- **Intervals**: `start_date/end_date` (e.g. `512-03-01/512-03-07`).
- **Approximate dates**: year only (e.g. `512`) or year and approximate month (`512-03`).
- **Tags**: `#tag` suffixes on the same event line.
- **Links to sheets**: inside event descriptions/sub-bullets, use relative Markdown links to canonical sheets (e.g. `[Guard Tournament](../../../03_society_and_politics/customs_festivals_and_events/festivals_and_occurrences/01_guard_tournament.md)`), adjusting the path to the `.mw` file's location.

---

## 3. Date Convention

- Dates use **world years** formatted as ISO dates (e.g. `512-03-01`, `512`, `512/513`).
- Mapping to the world's actual calendar (months, seasons, intercalary days) is documented in `10_timeline/calendar/` and summarised in the `general_timeline.mw` legend.
- If an event has fixed periodicity, its date/recurrence must also be stated in the calendar legend.

---

## 4. Tag Taxonomy

| Category | Tags | Usage |
| :--- | :--- | :--- |
| **Type** | `#custom` `#festival` `#event` `#occurrence` | Nature of the entry; `#occurrence` marks an individual dated instance of a recurring event. |
| **Status** | `#historical` `#ongoing` `#planned` | Status of the occurrence matching the sheet model. |
| **Thematic** | `#faction_<slug>` `#location_<slug>` `#PC_<slug>` `#NPC_<slug>` | Filters by actor or setting (e.g. `#faction_merchants_league`, `#location_high_harbour`). |
| **Campaign** | `#campaign_<name>` | Isolates items relevant to a specific campaign. |

The same tag categories must be used in entries inside `10_timeline/historical_chronology/` and `10_timeline/occurrence_register/` so both representations remain synchronised.

---

## 5. Update Rules

1. **New entry or occurrence**: append the line to the proper epoch source in `epochs/`; if relevant to a campaign, add it to `campaigns/<name>.mw` as well.
2. **Status transition** (planned → ongoing → concluded): update the status tag on the event line and the outcome in its notes.
3. **Legend**: if new tags or calendar entries are introduced, update `general_timeline.mw`.
4. **Canon exclusions**: `.mw` files and `exports/` contents are **excluded from the Setting Bible**; they are indexed solely in `setting_structure.json` (dedicated Tome `10` substructure).
5. **Zero hallucinations**: no event, date, or outcome unapproved by the DM.
