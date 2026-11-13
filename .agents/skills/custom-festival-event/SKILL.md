---
name: custom-festival-event
description: "Use when: recording everyday-life customs and peculiarities, recurring festivals and events (occurrences), and unique one-off events of the setting; creating or updating sheets under 03_society_and_politics/customs_festivals_and_events/ and maintaining 10_timeline/ (historical chronology, occurrence register, and Markwhen graphical timeline)."
argument-hint: "Specify type and entry (e.g. 'custom: farewell ceremony', 'festival: solstice feast', 'event: siege of the citadel')"
user-invocable: true
disable-model-invocation: false
---

# Skill: Customs, Festivals & Events (`custom-festival-event`)

This skill manages the `03_society_and_politics/customs_festivals_and_events/` sub-series and its link with Tome `10_timeline/`: it catalogues everyday-life peculiarities, recurring festivals and occurrences, and unique one-off events to the same notarial standards as the rest of the archive.

---

## 1. Golden Rule (Zero Hallucinations)

- Never invent customs, dates, rituals, participants, or outcomes not provided by the DM or already documented in canonical files.
- Missing detail: in interactive mode ask the DM (using the environment's structured question tool such as `vscode_askQuestions` or `AskUserQuestion` if available, otherwise directly in chat); in direct drafting mode insert `[TO_BE_DEFINED_BY_DM: description]`.

---

## 2. Typological Taxonomy

Classification follows the **nature** of the entry, not merely its frequency:

| Type | Subfolder | Nature | Examples |
| :--- | :--- | :--- | :--- |
| **Custom** | `customs/` | Everyday-life peculiarities: social behaviours, rituals, codified forms and manners (structures and ways of a rite). | Greeting or official farewell ceremonies; hospitality rituals; table manners; forms of address. |
| **Festival / Occurrence** | `festivals_and_occurrences/` | **Recurring institutional or ritual** events with **fixed** (calendar) or **trigger-based variable** periodicity (conditions that spark it, advanceable schedules). | Winter Solstice Feast; Guard Selection Tournament (upon expeditions returning); elections (scheduled intervals, bringable forward). |
| **One-Off Event** | `events/` | Inherently **unique or non-repeatable**: historical upheavals, rebellions, cataclysms, turning points. May be **historical (past)** or **imminent/ongoing** (outcome decided in sessions). Even if similar events might recur, it stays here by nature. | Siege of a citadel; miners' uprising; broken pact; natural catastrophe. |

If an entry seems hybrid (e.g. an institutional rite that escalated into an upheaval), classify it by its primary nature and cross-link the related sheet.

---

## 3. Folder Structure & Filenames

```text
03_society_and_politics/customs_festivals_and_events/
├── README.md                       # Sub-series index (one section per type)
├── customs/
│   ├── README.md
│   └── 01_<entry_slug>.md          # Sequential numerical prefix per subfolder
├── festivals_and_occurrences/
│   ├── README.md
│   └── 01_<entry_slug>.md
└── events/
    ├── README.md
    └── 01_<entry_slug>.md
```

- Filenames: `NN_slug_in_snake_case.md`, sequential numbering per subfolder (e.g. `01_farewell_ceremony.md`, `02_...`).
- Each subfolder and the parent folder receive an index `README.md`, updated with every new sheet.

---

## 4. Sheet Template — Custom

```markdown
# [Custom Name]

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

## Overview
What it is, where and when it is practised, who is expected to observe it.

## Formalism & Manner
Step-by-step structure of the rite/behaviour: gestures, wording, sequence of acts, timing, tone.

## Variants & Degrees
Differences by social rank, faction, region, or setting (court, town square, public ceremony...).

## Meaning & Sanctions
Symbolic and historical value of the custom; consequences of breaches (social, legal, ritual).

## Links & DM Hooks
Connections to NPCs, factions, locations, or other sheets (relative links). Hooks reserved for the DM.

## Mechanical Effects *(optional)*
Any game mechanics (modifiers, advantage, inspiration). Fill in only where applicable.
```

---

## 5. Sheet Template — Festival / Occurrence

```markdown
# [Festival / Recurring Event Name]

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

## Overview
What it is, who celebrates/presides over it, meaning, and standing in the world's culture.

## Periodicity & Trigger
- **Periodicity**: fixed (calendar) / trigger-based variable / mixed.
- **Trigger**: conditions that initiate the event (e.g. "return of a campaign", "death of an officeholder", "council decree").

## Time Windows
Expected schedules, notice periods, possibilities and causes for bringing forward or postponing (e.g. snap elections due to special circumstances).

## Proceedings
Rituals, phases, ceremonies, duration, sequence of acts.

## Participants & Roles
Who presides, who takes part, entry requirements, excluded groups, institutional roles involved.

## Known Occurrences
| Edition / Date | Status | Outcome | Timeline |
| :--- | :--- | :--- | :--- |
| [world year or date] | planned / ongoing / concluded | [outcome] | [link to 10_timeline] |

## Links & DM Hooks
Connections to related NPCs, factions, locations, customs, or events. Hooks reserved for the DM.

## Mechanical Effects *(optional)*
Any game mechanics. Fill in only where applicable.
```

---

## 6. Sheet Template — One-Off Event

```markdown
# [Event Name]

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

## Overview
What happened (or will happen): nature of the upheaval and historical placement. Specify whether **historical** or **ongoing**.

## Causes & Premises
Context, tensions, decisions, or coincidences that paved the way for the event.

## Proceedings
Phases of the event in sequence.

## Consequences & Fallout
Impacts on locations, factions, institutions, NPCs, and the balance of the world.

## Occurrence Status
- **Status**: planned / ongoing / concluded.
- **Outcome** (if concluded): [summary].
- **Date / period**: [world year].

## Protagonists & Witnesses
NPCs, PCs, factions, or peoples involved or present (with links to sheets).

## Links & DM Hooks
Cross-links and hooks reserved for the DM.

## Mechanical Effects *(optional)*
Any game mechanics. Fill in only where applicable.
```

---

## 7. Creation Procedure (Guided Interview)

Ask the DM the following questions (using the environment's interactive question tool such as `vscode_askQuestions` or `AskUserQuestion` if available, otherwise in chat):

1. **Type**: *Is this a custom, a recurring festival/occurrence, or a one-off event?* (Options describing the distinction by nature in §2).
2. **Name & Context**: *Entry name and, if known, the context (faction, location, period)?* (Free text).
3. **Typological Fields**: gather fields for the selected template (for festivals: fixed/variable periodicity, trigger, time windows; for events: historical or ongoing).
4. **Writing**: create the file with sequential numerical prefix inside the correct subfolder, fill in known sections, and mark gaps with `[TO_BE_DEFINED_BY_DM: ...]`.
5. **Badge**: set `> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*`.
6. **Propagation**: update connecting `README.md` files, propose updating `10_timeline/`, and if the entry enters the canonical lore, propose `sync-bible-structure` (`update-bible`, `update-structure-json`).

---

## 8. Managing Occurrences (Already Registered Events)

When a session stages a recurrence of an already registered festival/occurrence (e.g. an annual tournament):

1. **Minutes**: document the occurrence in the session minutes (`session-minutes`).
2. **Timeline**: record the occurrence in `10_timeline/` (occurrence register + Markwhen sources) with status and outcome.
3. **Canonical Sheet**: **ask the DM** whether to amend the sheet.
   - Particulars unique to that single occurrence (figures, participants, outcomes, hiccups) **remain in the timeline and minutes**.
   - The sheet is updated **only** if those particulars **fundamentally alter the nature** of the entry (e.g. changing rules, role, or meaning of the rite). In that case, update the sheet and its "Known Occurrences" row.

---

## 9. Updating `10_timeline/`

For every new entry, occurrence, or status transition (planned → ongoing → concluded):

1. **Historical Chronology** (`10_timeline/historical_chronology/`, per epoch/period): for past events, using category tags (e.g. `#event #historical`).
2. **Occurrence Register** (`10_timeline/occurrence_register/`, per epoch/period): for instances of festivals/recurring events and evolving entries.
3. **Markwhen** (`10_timeline/markwhen/`): update or create `.mw` sources via the dedicated `timeline-markwhen` skill (`create-mw` / `update-mw`) per [markwhen-conventions](./references/markwhen-conventions.md).
4. **Calendar** (`10_timeline/calendar/`): if the entry introduces or relies on fixed periodicity, align the world calendar definition.

Entries inside historical chronology and occurrence register use the same tag taxonomy as Markwhen so both representations remain synchronised.

---

## 10. Badges, Indices & Synchronisation

- **Badge**: always use the standard `> 🛡️ *Verified: ... | Modified: ...*` badge with the usual temporal rules (new text → `Verified: UNVERIFIED`; post-validation edit → advance `Modified` only; audit → align both dates).
- **Indices**: update `README.md` of the subfolder, parent `customs_festivals_and_events/`, and `03_society_and_politics/` if applicable.
- **Canon Codes** (Bible/JSON): customs `3.5.x`, festivals/occurrences `3.6.x`, events `3.7.x`; Tome `10_timeline` coded as Tome `10` (`10.1.x` historical chronology, `10.2.x` occurrence register, `10.3.x` calendar). `.mw` sources and exports are excluded from the Bible and indexed solely in JSON.
- **Zero Hallucinations**: as with every other module, never add details unapproved by the DM.
