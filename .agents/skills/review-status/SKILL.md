---
name: review-status
description: "Use when: generating or updating the lore review status dashboard (REVIEW_STATUS.md), calculating verification percentages, tracking completed files, and spotting paragraphs modified after the last audit."
argument-hint: "Generate or update the workspace review status dashboard"
user-invocable: true
disable-model-invocation: false
---

# Skill: Lore Review Status Dashboard (`review-status`)

This skill generates, updates, and maintains the tracking and monitoring file `REVIEW_STATUS.md` at the workspace root, giving the Dungeon Master an instant view of fact-checking coverage and sections requiring re-verification.

---

## 1. Status Classification Criteria

The skill scans the Markdown files inside the canonical world folders (`01_cosmology`, `02_geography`, `03_society_and_politics` including the `customs_festivals_and_events/` sub-series, `04_law_and_succession`, `05_characters`, `06_locations`, `07_factions`, `08_unique_magic_items`, `09_chronicles`, `10_timeline`) and inspects the badges:

```markdown
> 🛡️ *Verified: [DATE_V] | Modified: [DATE_M]*
```

### Compliance States:
* 🟢 **Fully Verified**: All document sections carry badges with `DATE_V >= DATE_M` and contain no `[TO_BE_DEFINED_BY_DM]` placeholders.
* 🟡 **Partially Verified / Incomplete**: Some sections carry badges while others lack them or contain `[TO_BE_DEFINED_BY_DM]` markers.
* 🟠 **Modified Post-Audit (Needs Re-check)**: One or more sections show `DATE_M > DATE_V`, indicating edits after a session or outside the last formal audit.
* ⚪ **Unverified**: No verification badge present in the file.

---

## 2. Structure of `REVIEW_STATUS.md`

Save `REVIEW_STATUS.md` at the workspace root using this structure:

```markdown
# Canon Review Status & Register

This register tracks the progress of the formal lore audit, logging sections validated by the Dungeon Master and those altered over the course of sessions.

* **Last General Audit:** [DATE]
* **Overall Canon Coverage:** [PERCENTAGE]%

---

## 1. Sector Summary Table

| Section / Tome | Total Files | Verified 🟢 | Post-Audit 🟠 | Partial 🟡 | Unverified ⚪ | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **01 Cosmology** | X | A | B | C | D | [Icon] |
| **02 Geography** | X | A | B | C | D | [Icon] |
| **03 Society & Politics** | X | A | B | C | D | [Icon] |
| **03· Customs, Festivals & Events** | X | A | B | C | D | [Icon] |
| **04 Law & Succession** | X | A | B | C | D | [Icon] |
| **05 Characters (PCs & NPCs)** | X | A | B | C | D | [Icon] |
| **06 Locations** | X | A | B | C | D | [Icon] |
| **07 Factions** | X | A | B | C | D | [Icon] |
| **08 Unique Magic Items** | X | A | B | C | D | [Icon] |
| **09 Campaign Chronicles** | X | A | B | C | D | [Icon] |
| **10 Timeline & Occurrences** | X | A | B | C | D | [Icon] |

---

## 2. Priority Items Awaiting Inspection

### Files with Post-Audit Changes (🟠)
* [path/file.md](path/file.md) — *Modified on [DATE] (Verified on [DATE])*

### Files with Explicit Gaps (🟡 `[TO_BE_DEFINED_BY_DM]`)
* [path/file.md](path/file.md) — *Section [Name]: [doubt description]*

---

## 3. Audit Session History
* **YYYY-MM-DD**: [Full / Partial] audit carried out on [folder or file] via `[step-by-step-audit / full-file-audit]`.
```

---

## 3. Operational Procedure

1. **Scan**: Recursively locate all relevant `.md` files in the workspace, excluding technical directories (e.g. `.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Parse Flags**: Extract `🛡️` badges, `Verified` and `Modified` dates, and `[TO_BE_DEFINED_BY_DM]` markers from each file.
3. **Compute Statistics**: Calculate counts and percentages for each of the ten canonical tomes (reporting the `customs_festivals_and_events/` sub-series separately).
4. **Write/Update**: Populate or update `REVIEW_STATUS.md` at the workspace root.
