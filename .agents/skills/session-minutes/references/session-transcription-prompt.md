# Session Transcription Prompt (NotebookLM / LLM)

Use this prompt in **NotebookLM** (or another LLM able to process audio recordings or long transcripts) to extract a notarial report before handing the output to the **Campaign Archivist** (`session-minutes`):

1. Upload the session audio recording or raw transcript into the notebook (split across multiple files if needed).
2. *(Optional)* Upload a short plain-text list with the exact spelling of already-known proper names (PCs, NPCs, recurring places) to reduce `[?]` flags — you can generate it directly from your archive with the `transcription-glossary` skill.
3. Copy and paste the block below into the chat. If the session is long and the model ends with `[CONTINUE FROM: Section X / HH:MM:SS]`, instruct it to continue from that point until **Section 12 (Coverage)** is complete.
4. Paste or save the full report and run `/session-minutes` (Channel C) to draft the canonical minutes and cross-updates.

---

````markdown
# TASK
You receive the transcript (or audio recording) of a tabletop RPG session.
Produce a structured, faithful report of what was said and done.
You do NOT know the setting, the characters, the campaign rules, or who is speaking:
everything you know is contained in the source. If a glossary or proper-name list
provided by the DM is also among the sources, use it solely for spelling proper names,
without importing facts or backstory that did not emerge during the session.
Your output will be reviewed and reorganised by someone else: you must not interpret,
you must report faithfully.

# RULES
1. Only what is in the source. Never present a deduction as a fact: `(inference)` is
   permitted only for obvious technical bridging (e.g. an unmistakable speaker or
   pronoun), never for unstated motives, causes, or backstory.
2. Do not correct, translate, or arbitrarily "normalise" proper names: report them as
   pronounced (unless a spelling is given in the DM's glossary). Doubtful spelling →
   `Name[?]`. Incomprehensible word or passage → `[inaudible 00:12:34]`.
3. Attribute every action to whoever performed it, using the character's name if
   spoken, otherwise the player's name. In `NARRATION`, distinguish objective DM
   descriptions from in-character statements by NPCs or PCs (e.g. `"<NPC> claims
   that …"`), never turning a character's words into objective world facts.
4. Always separate three registers and never mix them:
   - `NARRATION` = fiction, what happens in the world (always included in Chronology)
   - `TABLE` = rules, rolls, initiative, mechanics discussions (included in Chronology
     only if it determines a significant mechanical outcome or a rules/campaign ruling)
   - `OUT OF CHARACTER` = jokes, breaks, logistics, personal chat (excluded from
     Chronology; mention only in Coverage, or in Overview if relevant to attendance
     or logistics)
5. Dialogue: do not rewrite it. Quote verbatim in quotation marks with timestamp,
   assigning sequential IDs (`[C1]`–`[C20]`, maximum 20 quotes) in this priority order:
   pacts/oaths/threats → revelations/clues → decisions → names/numbers. Write each
   verbatim quote only once in Section 4 under the primary entity involved, and refer
   to it by ID (`[C#]`) under any other entities involved.
6. Do not invent titles, themes, causes, or motives. What is unsaid remains unsaid.
   Do not fill gaps with narrative logic.
7. Multi-source and timestamps: when multiple session files exist in the notebook,
   prefix each timestamp with the source name (e.g. `[Part1 00:12:34]`). If the
   source contains no timestamps, never invent them: write `[no timestamp]` (or the
   segment label present, e.g. `[part 2]`).
8. Anti-truncation: if the transcript is long and you approach the response limit, do
   not summarise or omit events; stop cleanly at the end of a completed section or
   table row with `[CONTINUE FROM: Section X / HH:MM:SS]`.
9. British English, valid Markdown. Use the exact headings shown below, in the same
   order. No introduction, no closing remarks, no commentary.

# OUTPUT

## 1. Overview
Bullet list: campaign name and session number (if stated); participants and their
roles (with `Player → PC` mapping if declared); real and/or in-game time reference
for the session (if stated); starting point; ending point; scene or time jumps
detected; any declared game data or logistics (level, experience, resources,
absences) — only if explicit.

## 2. Cast & Participants
| Name (as pronounced) | Player / Voice (player name / DM / uncertain) | Type (PC / NPC / creature / group / other / unclear) | In scene (yes / no / mentioned only) | One-line note |

## 3. Chronology
| # | Timestamp | Where | Who | What happens (3–5 factual sentences) | Immediate consequence | Register |
Mark time or scene discontinuities with a valid Markdown table row:
`| — | <timestamp> | JUMP | — | From <place/moment A> to <place/moment B> | — | NARRATION |`
Below the table: **Terse list** — one line per event, maximum 20 words each.

## 4. Facts by Entity
One block for every proper name mentioned, ordered from most to least present:

### <Name>
- Type: PC / NPC / creature / location / faction-institution / item-artefact / custom-festival / event / law-statute / concept / unclear
- Variants / aliases heard: list of phonetic spellings or alternative nicknames (include this line only if present; if uncertain whether variants refer to distinct entities, keep them separate and flag in `Open Questions`)
- Facts: bullet list. One verifiable fact per bullet, with timestamp (distinguishing DM narration from NPC/PC statements).
- Relations: `<Name> → <other name>: what` (one line per relation)
- First mention: timestamp
- Quotes: only if included under Rule 5 (`[C#] "..." (timestamp)` or cross-reference `[C#]`)

If an entity is only named with no details, write:
"named only, no details".

## 5. State Changes & Clues
| Who | Category (item / condition-injury / resource / clue-revelation / location) | Declared fact | Timestamp |
Only explicit facts (items gained/lost, persistent injuries or conditions, resource
changes, clues/revelations aimed at a PC, notable movements). If none: "None".

## 6. Commitments
| Who | Towards whom | What | Condition | Witnesses | Timestamp |
Promises, threats, pacts, debts, agreements, oaths. If none: "None".

## 7. Figures
| Item | Value | Context | Timestamp |
Every spoken figure: coin, prices, damage, hit points, distances, quantities, ages,
dates, percentages, durations.

## 8. Time References
| Expression (verbatim) | Context / associated event | Timestamp |
Every temporal reference: "yesterday", "three days", "last year", seasons,
anniversaries, deadlines, "long ago".

## 9. Open Questions
Numbered list. Phrasing: "Not stated whether / who / when / why ..." + timestamp of
the point where the information would be expected (include any doubts about whether
phonetic variants refer to the same entity or different entities).

## 10. Contradictions
Internal inconsistencies within the source only: `A states X (timestamp)` /
`B states Y (timestamp)`. No corrections, reporting only. If none: "None".

## 11. Data Block
A single valid YAML block, without comments. Include only keys with real content.
Keep descriptive fields (`what`, `fact`, `facts`) concise (one line per entry).

```yaml
session:
  campaign: ""
  number: ""
  reference: ""
  start: ""
  end: ""
cast:
  - name: ""
    player_voice: ""
    type: ""
    in_scene: ""
    notes: ""
events:
  - order: 1
    timestamp: ""
    where: ""
    actors: []
    what: ""
    consequence: ""
    register: ""
entities:
  - name: ""
    type: ""
    variants: []
    facts: []
    relations: []
    first_mention: ""
    quotes: []
state_changes_clues:
  - who: ""
    category: ""
    fact: ""
    timestamp: ""
commitments:
  - who: ""
    towards: ""
    what: ""
    condition: ""
    witnesses: []
    timestamp: ""
figures:
  - item: ""
    value: ""
    context: ""
    timestamp: ""
time_references:
  - expression: ""
    context: ""
    timestamp: ""
open_questions:
  - question: ""
    timestamp: ""
contradictions:
  - statement_a: ""
    timestamp_a: ""
    statement_b: ""
    timestamp_b: ""
```

## 12. Coverage
| Interval | Content | Quality (clear / garbled / inaudible) |
````
