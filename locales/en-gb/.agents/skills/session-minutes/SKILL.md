---
name: session-minutes
description: "Use when: taking D&D session minutes, conducting the post-session interview with the DM, drafting formal minutes with a Mermaid diagram of PC hooks, and updating the campaign index."
argument-hint: "Paste session notes or write 'start interview' to launch the guided procedure"
user-invocable: true
disable-model-invocation: false
---

# Skill: Session Minutes (`session-minutes`)

This skill guides the collection, structuring, and formatting of session minutes for any D&D campaign, ensuring compliance with the standard model documented in [minutes-template](./references/minutes-template.md).

> **📌 Linked Proper Names Rule**: every proper name of a setting entity (PCs, NPCs, factions, houses, cities, locations, magic items, customs, festivals, events…) appearing in produced text must be a **Markdown link** to the entity's canonical `.md` file (e.g. `[Name](relative/path/file.md)`), never plain text. Exceptions: headings, file names, frontmatter, code blocks, Mermaid nodes, and `.mw` sources. Entity without a sheet: never invent it — use `[TO_BE_DEFINED_BY_DM: missing sheet for <Name>]` and flag the gap. Checking and conversion: `link-proper-names` skill.

---

## 1. Golden Rule (Zero Hallucinations)

- **Absolute Fidelity**: Never invent NPCs, dialogue, locations, or backstory not described by the DM.
- **Gaps**: If essential details are missing (e.g. an NPC's name or the outcome of an encounter), ask during the interview or flag them with `[TO_BE_DEFINED_BY_DM: description]`.

---

## 2. Data Collection Modes

### Channel A: Guided Post-Session Interview
Triggered with *"start interview"* or right after a session ends. Ask the DM the following questions in a structured way (using the environment's interactive question tool such as `vscode_askQuestions` or `AskUserQuestion` if available, otherwise directly in chat):
1. **`session_coordinates`**: *Session number, in-game date, and geographical theatre of events?* (Free text with brief prompt).
2. **`present_pcs`**: *Which Player Characters were present?*
   - Multi-select options derived from dossiers registered in `05_characters/<Player_Characters>/<Campaign_or_Party>/` (with free-text option for new PCs or prominent NPCs).
3. **`event_chronology`**: *What happened in sequence (opening, central turning points, clashes/negotiations, epilogue)?* (Free text).
4. **`hooks_revelations`**: *Which discoveries, clues, or turning points specifically affected individual PCs?* (Free text used to generate the Mermaid diagram).
5. **`mechanical_data`**: *Are there mechanical resources to log?*
   - Options: *None (narrative only)*, *Coin & Expenses*, *Magic Items / Loot*, *Permanent injuries, conditions, or debts* (with details entered if selected).

### Channel B: Structuring Rough Notes
If the DM pastes disorderly notes, extract the chronology, isolate verified facts, and compile a draft directly. If critical details are missing, ask the DM to fill only those gaps (via the structured question tool if available, or in chat) before saving the file.

---

## 3. Drafting the Minutes

The minutes are compiled across the canonical sections:
1. **Header**: Technical data and relative Markdown links to PC and location dossiers.
2. **Synopsis of Events**: Formal, third-person notarial register, fluid and chronological.
3. **Protagonist Hooks**:
   - Mermaid `flowchart TD` diagram connecting the central threat or event to individual PCs.
   - Subsections per PC detailing the clue/element uncovered and its narrative impact.
4. **Key Phases**: Numbered summary list for quick reference during play.
5. **Mechanical Log (Optional)**: Included only if expressly requested.

---

## 4. Archiving & Propagation

1. **Save File**:
   Save to `09_chronicles/<campaigns>/<campaign_name>/<sessions>/XX_session_title.md` *(default: `09_chronicles/campaigns/<campaign_name>/sessions/...`, respecting any custom folder names such as `expeditions/`, `adventures/`, `logs/`)*.
2. **Update Campaign Index**:
   Insert the new row in the summary table of `09_chronicles/<campaigns>/<campaign_name>/README.md`:
   `| **XX** | [Title] | [Date] | [Location] | [Main Focus] | [Minutes](<sessions>/XX_title.md) |`
3. **Cross-Update Proposals (A + B)**:
   - List at the end of your response which repository files are affected (new NPCs, magic items found, hooks to update in PC dossiers via `character-dossier`).
   - **Customs, festivals, and events**: if the session introduces or mentions a new custom, recurring festival/occurrence, or one-off event, **always propose** creating the corresponding sheet in `03_society_and_politics/customs_festivals_and_events/` via `custom-festival-event`.
   - **Occurrences of registered events & Markwhen Timeline**: if the session stages a known recurrence (e.g. an annual tournament or seasonal feast) or introduces dated events, document them in the minutes and record them in `10_timeline/` (occurrence register and `.mw` sources via `timeline-markwhen`), then **ask the DM** whether to amend the canonical sheet: particulars specific to that occurrence stay in the timeline and minutes, and the sheet is updated only if they alter its nature.
   - Show the proposed edits and offer to apply them upon confirmation.
