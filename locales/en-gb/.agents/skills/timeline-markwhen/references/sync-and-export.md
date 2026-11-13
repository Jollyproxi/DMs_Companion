# Markwhen Synchronisation, Validation & Export

Alignment rules across `10_timeline/markwhen/`, the other setting modules, `setting_structure.json`, and `10_timeline/exports/`.

---

## 1. Bidirectional Mapping Between Modules and `.mw` Files

Each event inside `.mw` files maps to a canonical documentary source:

| Canonical Source | Destination in `markwhen/` | Required Tags |
| :--- | :--- | :--- |
| `10_timeline/historical_chronology/*.md` | `epochs/<epoch>.mw` (and `campaigns/<campaign>.mw` if relevant) | `#event` (or `#festival`/`#custom`) + `#historical` |
| `10_timeline/occurrence_register/*.md` | `epochs/<epoch>.mw` + optional `campaigns/<campaign>.mw` | `#festival #occurrence` or `#event` + `#historical` / `#ongoing` / `#planned` |
| `03_society_and_politics/customs_festivals_and_events/festivals_and_occurrences/*.md` (*Known Occurrences* table) | `epochs/<epoch>.mw` + `general_timeline.mw` (if fixed calendar recurrence) | `#festival #occurrence` + matching status |
| `03_society_and_politics/customs_festivals_and_events/events/*.md` | `epochs/<epoch>.mw` + optional `campaigns/<campaign>.mw` | `#event` + matching status (`concluded` → `#historical`) |
| `09_chronicles/campaigns/<name>/sessions/*.md` | `campaigns/<campaign_slug>.mw` (and `epochs/<epoch>.mw` if historically significant) | `#event` or `#occurrence` + `#campaign_<slug>` + status |
| `10_timeline/calendar/*.md` | `general_timeline.mw` (commented calendar legend section) | — |

### Sheet Status → Markwhen Tag Conversion Rule

- Sheet / Register with status `concluded` or past event → `#historical`
- Sheet / Register with status `ongoing` → `#ongoing`
- Sheet / Register with status `planned` → `#planned`

---

## 2. Synchronisation with `setting_structure.json`

`.mw` sources and renders in `exports/`:

1. **Must NEVER be included in the Setting Bible** (`SETTING_BIBLE.md`).
2. **Must be indexed in `setting_structure.json`** inside the Tome `10` (`id: "timeline"`) object under `markwhen_files`:

```json
"markwhen_folder": "10_timeline/markwhen",
"markwhen_files": [
  "10_timeline/markwhen/general_timeline.mw",
  "10_timeline/markwhen/epochs/01_first_age.mw",
  "10_timeline/markwhen/campaigns/chronicles_of_the_north.mw"
],
"exports_folder": "10_timeline/exports"
```

When `create-mw` adds or removes a `.mw` file, update `10_timeline/markwhen/README.md` and propose (or execute upon confirmation) updating `markwhen_files` in `setting_structure.json`.

---

## 3. Validation Checklist (`validate-mw`)

When running `validate-mw`, verify the following in order:

1. **Folder Structure & Index**:
   - Existence of `10_timeline/markwhen/README.md` and `10_timeline/markwhen/general_timeline.mw`.
   - Every `.mw` file inside `epochs/` and `campaigns/` must appear in both `10_timeline/markwhen/README.md` and the commented index of `general_timeline.mw`.
2. **Markwhen Syntax**:
   - YAML header enclosed cleanly between two `---` lines, free of `#Category` keys lacking `:` and free of `dateFormat: yyyy-MM-dd` (ISO format is native; specify `timezone: UTC` instead).
   - Balanced `section` / `endSection` (and `group` / `endGroup`) blocks.
   - Valid date format before `:` on event lines (no fabricated dates or uncommented free text in place of a date).
3. **Tag Coverage**:
   - Each event line carries at least 1 type tag (`#custom`, `#festival`, `#event`, `#occurrence`) and 1 status tag (`#historical`, `#ongoing`, `#planned`).
   - All tags used in `epochs/*.mw` and `campaigns/*.mw` are documented in the legend of `general_timeline.mw`.
4. **Markdown Links**:
   - Relative paths in event sub-bullets (e.g. `../../../03_society_and_politics/...`) resolve to existing files on disk and encode spaces with `%20`.
5. **Alignment with Tome 10 & `setting_structure.json`**:
   - Every entry in `historical_chronology/` and `occurrence_register/` has a counterpart in the epoch's `.mw` file.
   - The `markwhen_files` array of Tome 10 in `setting_structure.json` exactly matches the `.mw` files on disk.

---

## 4. Export Pipeline (`export-mw`) *(Optional)*

The `10_timeline/exports/` folder holds derived renders (excluded from the Bible).

### Mode A — Via Markwhen CLI (`@markwhen/mw`)

If Node.js / `npx` or the `mw` command is available in the environment:

- **Interactive HTML Timeline**:
  `npx @markwhen/mw <file_path.mw> -o 10_timeline/exports/<filename>.html`
- Always check command availability first (`command -v mw` on macOS/Linux or `Get-Command mw` in PowerShell, or `npx --version`).

### Mode B — Via IDE Extension (`Markwhen`) or Web App

If the DM prefers exporting to PNG/SVG/PDF using the editor's Markwhen extension or `markwhen.com`:

1. Prepare and validate the `.mw` source file, ensuring the YAML header includes `title` and complete tag colours.
2. Specify the canonical save filename in `10_timeline/exports/`:
   - `timeline_epoch_<slug>.(html|svg|png|pdf)`
   - `timeline_campaign_<slug>.(html|svg|png|pdf)`
3. Update `10_timeline/exports/README.md` with a summary table:

```markdown
## Exported Files

| Exported Render | Source `.mw` | Format | Last Updated |
| :--- | :--- | :--- | :--- |
| [timeline_campaign_...](timeline_campaign_....html) | [campaigns/....mw](../markwhen/campaigns/....mw) | HTML | YYYY-MM-DD |
```
