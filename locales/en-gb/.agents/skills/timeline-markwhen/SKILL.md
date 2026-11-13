---
name: timeline-markwhen
description: "Use when: creating, generating, updating, validating, or exporting Markwhen (.mw) graphical timeline files under 10_timeline/markwhen/ (general_timeline.mw, epochs/<epoch>.mw, campaigns/<campaign>.mw), synchronising dates, statuses, and tags with historical_chronology/, occurrence_register/, session minutes, and setting_structure.json, or producing graphical renders in 10_timeline/exports/."
argument-hint: "Specify operation: create-mw, update-mw, validate-mw, or export-mw (e.g. 'create-mw epoch: First Age', 'update-mw campaign: Chronicles of the North')"
user-invocable: true
disable-model-invocation: false
---

# Skill: Markwhen Graphical Timeline Management (`timeline-markwhen`)

This skill governs the full lifecycle of **Markwhen (`.mw`)** sources under `10_timeline/markwhen/` and their derived exports under `10_timeline/exports/`. It keeps the world's graphical time representation synchronised with historical chronology (`10_timeline/historical_chronology/`), the occurrence register (`10_timeline/occurrence_register/`), the calendar (`10_timeline/calendar/`), customs/festivals/events sheets (`03_society_and_politics/customs_festivals_and_events/`), and campaign minutes (`09_chronicles/campaigns/`).

Consult the attached technical references:
- [mw-syntax-and-templates](./references/mw-syntax-and-templates.md): canonical Markwhen syntax, YAML header, tag taxonomy, and templates for `general_timeline.mw`, `epochs/<epoch>.mw`, and `campaigns/<campaign>.mw`.
- [sync-and-export](./references/sync-and-export.md): bidirectional mapping rules with Tome 10, indexing in `setting_structure.json`, validation checklist, and export pipeline for `10_timeline/exports/`.

> **📌 Linked Proper Names Rule**: every proper name of a setting entity (PCs, NPCs, factions, houses, cities, locations, magic items, customs, festivals, events…) appearing in produced text must be a **Markdown link** to the entity's canonical `.md` file (e.g. `[Name](relative/path/file.md)`), never plain text. Exceptions: headings, file names, frontmatter, code blocks, Mermaid nodes, and `.mw` sources. Entity without a sheet: never invent it — use `[TO_BE_DEFINED_BY_DM: missing sheet for <Name>]` and flag the gap. Checking and conversion: `link-proper-names` skill.

---

## 1. Golden Rule: Notarial Fidelity (Zero Hallucinations)

- **No Invention**: Never independently invent dates, world years, epoch names, durations, participants, or outcomes not expressly supplied by the DM or already attested in canonical files.
- **Handling Missing Dates or Details**:
  - **Mandatory inquiry before writing**: in Markwhen, every visible event requires a date before `:`. If an event does not yet have a date/world year in canonical files, **stop and always ask the DM** (using the environment's structured question tool such as `vscode_askQuestions` or `AskUserQuestion` if available, otherwise directly in chat) for a canonical date or a **provisional year** before writing the entry into the `.mw` file.
  - If the DM provides a provisional year, insert the event with that year, add the `#provisional_date` tag, and note `- [TO_BE_DEFINED_BY_DM: final date to be confirmed]` in the sub-bullets so the event appears on the timeline while remaining flagged for consolidation.

---

## 2. Architecture of `10_timeline/markwhen/`

```text
10_timeline/
├── markwhen/
│   ├── README.md                     # Index of .mw sources and summary of conventions
│   ├── general_timeline.mw           # General index/legend (NOT an aggregate of sources)
│   ├── epochs/
│   │   └── <epoch_slug>.mw           # One .mw source per historical epoch/period
│   └── campaigns/
│       └── <campaign_slug>.mw        # Everything relevant to the campaign (past, present, planned)
└── exports/
    ├── README.md                     # Register of derived graphical renders
    └── <filename>.(html|svg|png|pdf)
```

- **Role of `general_timeline.mw`**: holds the configuration header and tag/colour legend, the world calendar summary, and the commented index of sources in `epochs/` and `campaigns/`. It does not duplicate individual events from specific files.
- **Exclusion from the Bible**: `.mw` files and `exports/` contents are **excluded from the Setting Bible** and indexed solely in `setting_structure.json` (`markwhen_files` field in Tome `10`).

---

## 3. Sub-Operations Matrix

| Command / Argument | Primary Target | Mode | Purpose |
| :--- | :--- | :--- | :--- |
| **`create-mw`** *(or `generate-mw`)* | `general_timeline.mw`, `epochs/*.mw`, `campaigns/*.mw` | Initialisation / From Scratch | Creates the `markwhen/` layout, generates `general_timeline.mw`, or creates a new epoch or campaign `.mw` file from canonical modules. |
| **`update-mw`** | Existing `.mw` files + `markwhen/README.md` | Incremental / Delta | Inserts new events/occurrences, updates status tags (`#planned` → `#ongoing` → `#historical`), adds sessions, and updates the legend. |
| **`validate-mw`** | `10_timeline/markwhen/**/*.mw` | Diagnostics / Technical Audit | Checks Markwhen syntax, mandatory tags, relative links to sheets/minutes, and alignment with Tome 10 and `setting_structure.json`. |
| **`export-mw`** | `10_timeline/exports/` | Render / Derivation | Exports `.mw` sources into derived visualisations (HTML/SVG/PNG/PDF via optional `mw` CLI or manual IDE/web export) and updates `exports/README.md`. |

---

## 4. Procedure 1: `create-mw` (Initialising & Generating `.mw` Sources)

Use this procedure to initialise `10_timeline/markwhen/` or create a new `.mw` file for a historical epoch or campaign.

### Operational Steps:
1. **Detect Context & Sources**:
   - Read `10_timeline/README.md`, `10_timeline/calendar/`, and `10_timeline/markwhen/README.md`.
   - Based on the requested target (`general`, `epoch`, `campaign`, or `all`), inspect the pertinent sources:
     - For an **epoch**: `10_timeline/historical_chronology/`, `10_timeline/occurrence_register/`, and sheets in `03_society_and_politics/customs_festivals_and_events/`.
     - For a **campaign**: `09_chronicles/<campaigns>/<campaign_name>/README.md`, minutes in `<sessions>/`, PC dossiers (`05_characters/<Player_Characters>/<Campaign_or_Party>/`), and related historical/ongoing events.
2. **Preliminary Interview**:
   - If essential coordinates are missing (e.g. epoch name/slug, start/end year, current campaign year), ask the DM before generating the file (via the environment's structured question tool if available, otherwise in chat).
3. **Generate Files from Templates**:
   - Apply templates from [mw-syntax-and-templates](./references/mw-syntax-and-templates.md):
     - Create `10_timeline/markwhen/epochs/` and `10_timeline/markwhen/campaigns/` subfolders if missing.
     - Generate `general_timeline.mw` with header, tag/colour definitions, calendar notes, and `.mw` file map.
     - Generate `epochs/<epoch_slug>.mw` or `campaigns/<campaign_slug>.mw` ordering events chronologically by world year (`YYYY`, `YYYY-MM`, `YYYY-MM-DD`, or ranges `start/end`) and grouping them in thematic or phase `section` blocks.
     - Include under each event the relative Markdown link to its canonical sheet or session minutes.
4. **Propagate Indices & JSON**:
   - Update `10_timeline/markwhen/README.md` listing the new `.mw` files created and updating the `Modified` date in the `🛡️` badge.
   - Propose updating `markwhen_files` in `setting_structure.json` (`update-structure-json`).

---

## 5. Procedure 2: `update-mw` (Incremental Update)

Use this procedure after recording session minutes (`session-minutes`), creating/modifying a sheet in `customs_festivals_and_events/` (`custom-festival-event`), or upon direct DM request.

### Operational Steps:
1. **Identify Temporal Delta**:
   - Determine what changed:
     - **New event / new occurrence**: date/world year, title, type (`#custom`, `#festival`, `#event`, `#occurrence`), status (`#planned`, `#ongoing`, `#historical`), and thematic tags (`#faction_<slug>`, `#location_<slug>`, `#PC_<slug>`, `#NPC_<slug>`, `#campaign_<slug>`).
     - **Status transition**: moving an existing entry from `#planned` to `#ongoing` or `#historical` (with an outcome summary).
     - **New campaign session**: dated events surfaced in `09_chronicles/campaigns/<name>/sessions/XX_title.md`.
2. **Update `.mw` Sources**:
   - Open the relevant epoch `.mw` file in `10_timeline/markwhen/epochs/` and insert or update the event line while keeping chronological order.
   - If the event concerns a campaign, also update `10_timeline/markwhen/campaigns/<campaign_slug>.mw` adding the relative link to the minutes or sheet.
   - If new tags (e.g. a new faction or campaign) or fixed calendar recurrences were introduced, update the header and legend in `10_timeline/markwhen/general_timeline.mw`.
3. **Cross-Alignment with Tome 10**:
   - Ensure the same entry/occurrence and tags appear in `10_timeline/historical_chronology/` (if `#historical`) or `10_timeline/occurrence_register/` (if `#occurrence`, `#ongoing`, or `#planned`), proposing alignment if missing.

---

## 6. Procedure 3: `validate-mw` (Diagnostics & Consistency Check)

Use this procedure to verify formal and structural correctness of `.mw` sources against the checklist in [sync-and-export](./references/sync-and-export.md).

### Checks Performed:
1. **Markwhen Syntax**: validity of the YAML header (`---`, no `#Category` keys lacking `:`, no `dateFormat`), proper closing of `section` / `endSection` (or `group` / `endGroup`) blocks, and valid date formats (`YYYY`, `YYYY-MM`, `YYYY-MM-DD`, `date1/date2`) before colons `:`.
2. **Tag Taxonomy**: every event must carry at least one **type** tag (`#custom`, `#festival`, `#event`, `#occurrence`) and one **status** tag (`#historical`, `#ongoing`, `#planned`).
3. **Relative Link Integrity**: verify that all Markdown links `[Text](../../...)` in event descriptions resolve to existing files in the workspace.
4. **Bidirectional Consistency with Tome 10 & JSON**:
   - Compare events in `.mw` files with `historical_chronology/` and `occurrence_register/`, flagging date or status-tag discrepancies.
   - Verify that every `.mw` file on disk is listed under `markwhen_files` in `setting_structure.json`.
5. **Diagnostic Report**: output a status table (`OK` / `WARN` / `ERROR`) and ask the DM (via structured tool if available, or in chat) whether to apply automatic fixes.

---

## 7. Procedure 4: `export-mw` (Graphical Exports in `10_timeline/exports/`)

Use this procedure when the DM requests generating or updating rendered timeline views.

### Operational Steps:
1. **Check Optional Tools (`mw` CLI / Extension / Web App)**:
   - Check whether the Markwhen CLI (`@markwhen/mw`) is available in the environment or guide the DM via the Markwhen editor extension or `markwhen.com`, following [sync-and-export](./references/sync-and-export.md).
2. **Generate & Export**:
   - Export the requested `.mw` sources into `10_timeline/exports/` using standard naming (`timeline_<slug>_<format>.<ext>`).
3. **Update Exports Index**:
   - Update `10_timeline/exports/README.md` with the table of generated renders (file, source `.mw`, generation date) and advance `Modified` in the `🛡️` badge.

---

## 8. Structured Interaction

If invoked without specific arguments or with partial parameters, ask the DM (using the environment's structured question tool such as `vscode_askQuestions` / `AskUserQuestion` if available, otherwise in chat) which operation to run:
- `create-mw` — Initialise `general_timeline.mw` or create a new `.mw` file per epoch or campaign
- `update-mw` — Add new events/occurrences or update statuses and tags in existing `.mw` files
- `validate-mw` — Check `.mw` syntax, tags, relative links, and alignment with Tome 10 and JSON
- `export-mw` — Export `.mw` sources into derived renders inside `10_timeline/exports/`
