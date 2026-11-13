# Markwhen Syntax and Templates (`.mw`)

Operational reference for writing and updating `.mw` files in `10_timeline/markwhen/`.

---

## 1. Canonical Markwhen Syntax

### YAML Header (`---`)

Every `.mw` file begins with a YAML block between `---` lines defining `title`, `description`, `timezone: UTC` (recommended to prevent historical LMT offsets on ancient years), and the colour palette for standard tags (descriptive headings must be written as `//` comments, never as `#CategoryName` without `:`, so the YAML parser is not broken; ISO `YYYY-MM-DD` format is native and does not require `dateFormat`):

```yaml
---
title: "Timeline Title"
description: "Brief description of the .mw file"
timezone: UTC

// Type
#custom: #8b5cf6
#festival: #f59e0b
#event: #ef4444
#occurrence: #ec4899

// Status
#historical: #64748b
#ongoing: #10b981
#planned: #3b82f6
#provisional_date: #eab308
---
```

### Date Formats (World Years)

Dates use **world years** expressed in ISO format (`YYYY`, `YYYY-MM`, `YYYY-MM-DD`), with 4-digit years (optionally zero-padded for years `< 1000`, e.g. `0512-03-01` or `512-03-01` consistently within the same file):

- **Single day**: `512-03-01: Solstice Feast #festival #historical`
- **Approximate month**: `512-03: Council Summons #event #historical`
- **Single year**: `514: Guard Tournament #festival #occurrence #ongoing`
- **Date range**: `512-03-01/512-03-07: Autumn Fair #festival #historical` or `512/513: Siege of the Citadel #event #historical`
- **Undefined date**: never invent numbers or omit the event; **always ask the DM first** (via the structured question tool if available, or in chat) for a date or a **provisional year**, and if provisional, tag it `#provisional_date` with a note `- [TO_BE_DEFINED_BY_DM: final date to be confirmed]`.

### Descriptions, Sub-bullets & Relative Links

Beneath the event line (indented or on immediately following lines before the blank line), include:

- A brief notarial summary or outcome (if `#historical` / `#ongoing`).
- Relative Markdown links (without backticks) to canonical sheets or minutes, anchored to the `.mw` file's location:
  - From `10_timeline/markwhen/general_timeline.mw`: `../../03_society_and_politics/...`
  - From `10_timeline/markwhen/epochs/<epoch>.mw` or `campaigns/<campaign>.mw`: `../../../03_society_and_politics/...` and `../../../09_chronicles/campaigns/...`

Complete entry example:

```text
514-06-12: Guard Tournament — Edition 514 #festival #occurrence #ongoing #location_high_citadel
- Status: ongoing.
- Canonical sheet: [The Guard Tournament](../../../03_society_and_politics/customs_festivals_and_events/festivals_and_occurrences/01_guard_tournament.md)
- Related minutes: [Session 02](../../../09_chronicles/campaigns/Chronicles%20of%20the%20North/sessions/02_session.md)
```

### Groupings (`section` / `endSection`)

Use `section Section Name` ... `endSection` to logically group events (e.g. by historical sub-period in epoch files, or by story arc / act in campaign files).

---

## 2. Mandatory Tag Taxonomy

Every event in a `.mw` file must carry **at least 1 Type tag** and **1 Status tag**, plus optional thematic and campaign tags:

| Category | Allowed Tags | Usage Rule |
| :--- | :--- | :--- |
| **Type** *(mandatory)* | `#custom` `#festival` `#event` `#occurrence` | `#occurrence` accompanies `#festival` or `#event` when logging a specific dated instance. |
| **Status** *(mandatory)* | `#historical` `#ongoing` `#planned` | Aligned with the status field of the occurrence register and sheets. |
| **Thematic** *(optional)* | `#faction_<slug>` `#location_<slug>` `#PC_<slug>` `#NPC_<slug>` | Use `snake_case` matching `id` values in `setting_structure.json`. |
| **Campaign** *(optional/mandatory in campaigns/)* | `#campaign_<slug>` | Mandatory for events affecting a specific campaign. |

---

## 3. Template 1: `10_timeline/markwhen/general_timeline.mw`

`general_timeline.mw` is the **general index/legend** (it does not duplicate events from individual files):

```text
---
title: "General Timeline — Legend & Chronological Index"
description: "General index, tag legend, and world calendar conventions. Individual events live in epochs/ and campaigns/."
timezone: UTC

// Type
#custom: #8b5cf6
#festival: #f59e0b
#event: #ef4444
#occurrence: #ec4899

// Status
#historical: #64748b
#ongoing: #10b981
#planned: #3b82f6
#provisional_date: #eab308
---

// ============================================================================
// CALENDAR LEGEND & CONVENTIONS
// - Dates expressed in World Years (format YYYY, YYYY-MM, YYYY-MM-DD).
// - Calendar mapping: [World Calendar](../calendar/README.md)
// - Fixed recurrences: [TO_BE_DEFINED_BY_DM: list of fixed annual recurrences]
// ============================================================================

// ============================================================================
// INDEX OF EPOCH SOURCES (10_timeline/markwhen/epochs/)
// - [Epoch 01](epochs/01_<epoch_slug>.mw) — [Historical Chronology](../historical_chronology/01_<epoch_slug>.md)
// ============================================================================

// ============================================================================
// INDEX OF CAMPAIGN SOURCES (10_timeline/markwhen/campaigns/)
// - [Campaign](campaigns/<campaign_slug>.mw) — [Campaign Hub](../../09_chronicles/campaigns/<Campaign_Name>/README.md)
// ============================================================================

section Overview of Epochs
// List only macro time spans for epochs (without duplicating individual events)
// [TO_BE_DEFINED_BY_DM: year range Epoch 1]: First Age #historical
endSection
```

---

## 4. Template 2: `10_timeline/markwhen/epochs/<NN_epoch_slug>.mw`

```text
---
title: "Epoch: [Epoch Name]"
description: "Markwhen chronology of [Epoch Name] — synchronised with historical_chronology and occurrence_register."
timezone: UTC

#custom: #8b5cf6
#festival: #f59e0b
#event: #ef4444
#occurrence: #ec4899
#historical: #64748b
#ongoing: #10b981
#planned: #3b82f6
#provisional_date: #eab308
---

// Synchronised canonical sources:
// - Historical chronology: [../../historical_chronology/NN_<epoch_slug>.md](../../historical_chronology/NN_<epoch_slug>.md)
// - Occurrence register: [../../occurrence_register/NN_<epoch_slug>.md](../../occurrence_register/NN_<epoch_slug>.md)

section Historical & Founding Events
// Example:
// 512/513: Siege of the Citadel #event #historical #faction_northern_watch
// - Outcome: [canonical summary]
// - Sheet: [The Siege of the Citadel](../../../03_society_and_politics/customs_festivals_and_events/events/01_siege_of_citadel.md)
endSection

section Occurrences & Evolving Entries
// Example:
// 514: Guard Tournament #festival #occurrence #ongoing
// - Sheet: [The Guard Tournament](../../../03_society_and_politics/customs_festivals_and_events/festivals_and_occurrences/01_guard_tournament.md)
endSection
```

---

## 5. Template 3: `10_timeline/markwhen/campaigns/<campaign_slug>.mw`

```text
---
title: "Campaign: [Campaign Name]"
description: "Complete timeline of [Campaign Name]: PC backgrounds, played sessions, and upcoming/planned events."
timezone: UTC

#custom: #8b5cf6
#festival: #f59e0b
#event: #ef4444
#occurrence: #ec4899
#historical: #64748b
#ongoing: #10b981
#planned: #3b82f6
#provisional_date: #eab308
#campaign_<campaign_slug>: #f43f5e
---

// Campaign hub: [../../../09_chronicles/campaigns/<Campaign_Name>/README.md](../../../09_chronicles/campaigns/<Campaign_Name>/README.md)

section PC Backgrounds & Backstory
// Prior events relevant to the campaign's PCs (#historical #campaign_<campaign_slug>)
endSection

section Session Chronicles
// Events occurring in recorded sessions (#historical or #ongoing)
// Linked to ../../../09_chronicles/campaigns/<Campaign_Name>/sessions/XX_title.md
endSection

section Ongoing & Planned Events
// Time windows, deadlines, and future occurrences (#ongoing / #planned)
endSection
```
