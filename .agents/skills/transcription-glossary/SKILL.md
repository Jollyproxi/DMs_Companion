---
name: transcription-glossary
description: "Use when: generating a compact, spelling-only list of already-known proper names (zero facts or spoilers) to upload into NotebookLM or another LLM alongside the session transcription prompt to reduce `[?]` flags."
argument-hint: "Specify campaign/session (e.g. 'campaign: Chronicles of the North'), folder/area or 'full archive', any extra spoken names, and whether to also save a .txt file"
user-invocable: true
disable-model-invocation: false
---

# Skill: Transcription Proper-Name Glossary (`transcription-glossary`)

This skill extracts a **compact, spelling-only plain-text list of canonical proper names** (PCs, NPCs, locations, factions, items, customs, festivals, events, deities, and key terms) from the repository to upload as a helper source in **NotebookLM** or another LLM alongside [session-transcription-prompt](../session-minutes/references/session-transcription-prompt.md), minimising `[?]` uncertainty flags and phonetic misspellings in session transcripts.

> **📌 Linked Proper Names Rule Exception**: the exported text block for NotebookLM/LLM (and any optional `.txt` file saved to disk) is meant for an external tool and must remain **plain text with no Markdown links** (`[Name](...)`). Any explanation in chat outside the block and all canonical `.md` repository files remain governed by `link-proper-names`.

---

## 1. Golden Rule: Spelling Only, Zero Facts & Zero Hallucinations

- **Orthography Only**: include **only** the exact canonical spelling of each proper name, any variant spellings or aliases/diminutives explicitly documented in its canonical sheet (e.g. `Canonical Name (alias: Nickname)`), and optionally `Player → PC` mapping for active PCs only if already documented or supplied by the DM.
- **Strict Ban on Facts and Spoilers**: NEVER include descriptions, narrative roles, faction affiliations, relationships, vital status (alive/dead/traitor), current whereabouts, stats, DM secrets, or lore snippets. Anything beyond spelling increases the risk that the transcription model will bleed archive lore into the transcript report as if spoken at the table.
- **Top Anti-Intrusion Guard**: every generated glossary opens with a fixed one-line instruction telling the transcription LLM to use the list **solely for spelling** spoken names, without importing unspoken entries or deducing facts or relationships.
- **Extra Names Spoken in the Latest Session**: if the DM supplies uncatalogued names spoken during the session just played, include them in a dedicated section purely to aid transcription, without creating sheets or modifying repository canon.
- **Zero Invention**: if the archive itself lacks a confirmed spelling or shows ambiguity, never guess or silently normalise; flag it outside the block with `[TO_BE_DEFINED_BY_DM: ...]` or ask the DM before exporting.

---

## 2. Selection Scopes (Noise Control)

To avoid flooding the transcription context with dozens of distant names that trigger false phonetic matches, offer or apply one of three scopes:

- **Mode A — Campaign / Session-Focused *(Recommended default)***:
  - Active campaign PCs (`05_characters/<Player_Characters>/<Campaign_or_Party>/`, default `Player_Characters/<Campaign>/`).
  - Proper names already referenced in the campaign hub `README.md` and the last **N session minutes** (default: last **5** minutes under `09_chronicles/<campaigns>/<campaign_name>/<sessions>/`).
  - Canonical entities belonging to the current geographical theatre or region, if specified by the DM or stated in the latest minute header.
  - Any extra spoken names supplied by the DM for the newly recorded session.
- **Mode B — Targeted Area, Folder, or Faction**:
  - Active campaign PCs (where relevant) + all canonical entities inside folders, regions, factions, or tomes specified by the DM (e.g. `06_locations/<region>/`, `07_factions/<house>/`, `04_law_and_statutes/`).
- **Mode C — Full Archive**:
  - Every canonical proper name across the Ten Tomes.
  - **Anti-Noise Threshold**: if the resulting list exceeds roughly **250–300 entries**, warn the DM explicitly that an overly broad glossary can increase false phonetic matches in NotebookLM/LLM and offer narrowing to Mode A or Mode B.

---

## 3. Sources & Extraction Rules

1. **Preferred Index**: if `setting_structure.json` exists at the workspace root, read it first to catalogue tomes, modules, and canonical paths quickly without reading prose.
2. **Direct Sweep / Supplement Across the Ten Tomes**: scan (or supplement from) the setting folders, adapting automatically to the repository's actual layout — including custom or legacy folder names (`06_location/`, `07_factions/`, `08_oggetti magici peculiari/`, `cornici/`, `expeditions/`, `logs/`) and the project's NPC archive convention documented in project instructions and the `05_characters/` index:
   - `05_characters/` (modular PC dossiers and NPC sheets)
   - `06_locations/` (cities, adventure hubs, strongholds, area hazards) and `02_geography/` (regions/macro-areas)
   - `07_factions/` (noble houses, covens, guilds, orders, institutions)
   - `<08_unique_magic_items>/` (artefacts, relics, unique items)
   - `03_society_and_politics/` (`peoples/`, `customs_festivals_and_events/`), `01_cosmology/` (planes, pantheon/deities), `04_law_and_statutes/` (statutes, treaties, courts), and `10_timeline/historical_chronology/` (epochs, historical events)
   - `09_chronicles/` (for Mode A: campaign index and recent minutes)
3. **Exclusions**:
   - Exclude technical directories (`.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`) and meta/master files (`README.md`, `AGENTS.md`, `CLAUDE.md`, `SETTING_BIBLE.md`, `REVIEW_STATUS.md`, `USAGE.md`, `setting_structure.json`, `.mw` sources, or rendered exports).
   - Discard generic structural headings (e.g. *General Framework*, *Index*, *Synopsis*, *Session 01*, *Occurrence Status*) and `[TO_BE_DEFINED_BY_DM: ...]` placeholders.
4. **Normalisation & Deduplication**:
   - For each canonical sheet, extract the proper name from the H1 heading (stripping numeric prefixes like `01_`, type prefixes such as `NPC Sheet:` / `PC Dossier:` / `Magic Item:`, `🛡️` status badges, or descriptive subtitles after `—` or `|`), or from the cleaned file name if no H1 proper name is present.
   - For 5-module PC dossiers, extract the character identity **once** from the PC folder name or profile module (`01_profile...`) rather than repeating the 5 module file names.
   - Collect aliases or diminutives only where explicitly documented in the sheet (`Aliases`, `Nicknames`, `Variants`); never include parenthetical lore explanations.
   - Deduplicate identical spellings and sort entries alphabetically within each category.

---

## 4. Operational Procedure & Structured Interaction

1. **Gather Parameters (if not already specified by the DM)**:
   Use the environment's interactive question tool (`vscode_askQuestions`, `AskUserQuestion`, `ask_question`, `request_user_input` when available, otherwise ask in chat):
   - **`scope`**: *Which scope should the glossary cover?*
     - Options: *Campaign / Current session — recommended* (listing campaigns detected under `09_chronicles/`), *Targeted area, folder, or faction*, *Full archive (all Ten Tomes)*.
   - **`extra_names`**: *Are there any newly spoken names from the latest session (guest PCs, new NPCs, places, or terms not yet in the archive) to include for transcription only?* (Optional free text or *None*).
   - **`delivery`**: *How should the glossary be delivered?*
     - Options: *Chat only (ready to copy-paste into NotebookLM) — recommended*, *Chat + save as a `.txt` file in the repository*.
2. **Extract & Run Anti-Spoiler Check**:
   - Apply the §3 rules across the chosen scope.
   - Verify that no entry contains descriptions, relationships, allegiances, vital status, or plot hints.
   - Omit empty categories. If total entries exceed ~250–300, warn the DM and offer a tighter campaign/scene subset.
3. **Deliver the Glossary**:
   - Always output the complete glossary directly in chat inside a fenced `text` code block, ready to paste into NotebookLM (*Add source → Copied text*) or another LLM.
   - Outside the block, print a short summary: chosen scope, entry count per category and total, sources consulted, and any doubtful spellings noticed in the archive.
   - If the DM also requested saving a file, write a **UTF-8 `.txt` file** inside the campaign folder — `09_chronicles/<campaigns>/<campaign_name>/transcription_glossary.txt` *(default: `09_chronicles/campaigns/<campaign_name>/transcription_glossary.txt`; or workspace root / requested path if no campaign folder exists)* — avoiding `.md` so it never interferes with `validate-structure`, `link-proper-names`, `review-status`, or `sync-bible-structure`.

---

## 5. Canonical Output Template

Output only a compact plain-text block in this format (omitting any empty categories):

````text
# PROPER-NAME GLOSSARY (SPELLING ONLY — DO NOT IMPORT FACTS NOT SPOKEN IN SESSION)
Campaign / Scope: <Campaign name or scope>

## Player Characters (PCs)
- <PC Name> (<Player → PC> only if documented/provided, optional)
- <PC Name> (alias: <Documented nickname>)

## Non-Player Characters (NPCs) & Notable Creatures
- <NPC Name>
- <NPC Name> (alias: <Documented diminutive / variant spelling>)

## Locations, Cities & Regions
- <Location / Region>

## Factions, Houses & Institutions
- <Faction / House>

## Items, Artefacts & Relics
- <Item>

## Customs, Festivals, Events, Deities & Key Terms
- <Custom / Festival / Event / Deity / Statute>

## Extra Session Names (not yet catalogued)
- <Spoken name provided by the DM>
````

---

## 6. Integration with Other Skills

- **`session-minutes` & `session-transcription-prompt`**: this skill generates the optional helper source described in step 2 of [session-transcription-prompt](../session-minutes/references/session-transcription-prompt.md), reducing `Name[?]` flags before Channel C import in `session-minutes`.
- **`link-proper-names`**: shares entity discovery logic across the Ten Tomes and JSON index; explains why the external NotebookLM text block / `.txt` export is exempt from Markdown linking.
- **`sync-bible-structure`**: reads `setting_structure.json` when available as a fast index of canonical names without loading full narrative prose from `SETTING_BIBLE.md`.
- **`validate-structure`**: optional `.txt` export stays cleanly outside `.md` broken-link, `🛡️` badge, and orphan-file checks.
