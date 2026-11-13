# Setting Bible Compilation Conventions

The Setting Bible (`SETTING_BIBLE.md` or extended title adopted in the workspace) is the world's monolithic narrative master document. It compiles the entire body of knowledge spread across the ten tomes into a continuous, fluid, searchable sequence.

---

## 1. Title Page & Metadata

The canonical header is placed at the top of the file:

```markdown
### SETTING BIBLE: [SETTING_NAME]

> 📜 **Monolithic Master Canon Document**  
> *Canon Version:* [VERSION] | *Last Compiled:* [TODAY_DATE]  
> 🛡️ *Verified: [DATE_V] | Modified: [DATE_M]*

---
```

---

## 2. Heading Hierarchy (Level Mapping)

Because the document brings together many tomes and nested modules, individual `.md` file headings are transposed according to the following canonical scale:

| Level in Atomic Module | Level in Master Bible | Example Format |
| :--- | :--- | :--- |
| **Tome Title (from README)** | Level 5 (`#####`) | `##### 1. Cosmology & Metaphysical Architecture` |
| **Module Title (`# Title`)** | Level 6 Italic (`###### *...*`) or `### X.Y` | `###### *1.1 Planar and Cosmic Structure*` |
| **Internal Section (`## Section`)** | Heading `###` or `####` | `### Elemental Planes and Liminal Realms` |
| **Subsection (`### Sub`)** | Bold bullet or `#####` | `* **Astral Court:** ...` |

> **Continuity Note**: If the workspace already contains a master Bible file, match the exact heading style and tags already in use in that file.

---

## 3. Sequential Tome Compilation Order

Compilation follows the strict canonical numerical sequence:

1. **##### 1. Cosmology & Metaphysical Architecture** (`01_cosmology/`)
   - `01_planar_structure.md`
   - `02_seasons_and_celestial_mechanics.md`
   - `03_flow_of_magic_and_divine_order.md`
   - `04_moral_or_philosophical_system.md`
2. **##### 2. Physical, Territorial & Environmental Geography** (`02_geography/`)
   - Main geography, map, subterranean, and liminal-plane modules.
   - Individual regions/provinces in `regions/`, ordered by ascending number.
3. **##### 3. Social, Political & Economic Order** (`03_society_and_politics/`)
   - Social models, economy, classes, criminal law.
   - Sub-series `customs_festivals_and_events/`: customs (`3.5.x`), festivals/occurrences (`3.6.x`), one-off events (`3.7.x`), in ascending numerical order per subfolder.
4. **##### 4. Law, Pacts & Rules of Succession** (`04_law_and_succession/`)
   - Contracts, pacts, treaties, succession hierarchy, courts.
5. **##### 5. Character Roster of the World** (`05_characters/`)
   - Notable NPC roster (`Non_Player_Characters/`), grouped by faction or region.
   - Party bonds summary if a canonical campaign is present.
6. **##### 6. Atlas of Locations & Adventure Hubs** (`06_locations/`)
   - Prominent sites, strongholds, cities, and gates.
7. **##### 7. Geopolitical Register of Factions & Houses** (`07_factions/`)
   - Charters, hierarchies, and rivalries of dominant powers.
8. **##### 8. Register of Unique Magic Items & Relics** (`08_unique_magic_items/`)
   - Unique artefacts, history, legal standing, and distinct mechanics.
9. **##### 9. Historical Chronicles & Campaign Compendium** (`09_chronicles/`)
   - Compendium of active campaigns and progressive session minutes.
10. **##### 10. Timeline & World Chronology** (`10_timeline/`)
    - Historical chronology (`10.1.x`, files per epoch/period), occurrence register (`10.2.x`, files per epoch/period), and calendar (`10.3.x`).
    - Markwhen sources (`markwhen/*.mw`) and graphical exports (`exports/`) are **excluded** from the Bible: they remain indexed solely in `setting_structure.json`.
    - Internal entries use the Markwhen tag taxonomy (e.g. `#custom #festival #event #occurrence`) to stay synchronised with the graphical timeline.

---

## 4. Handling Tables, Diagrams & DM Notes

1. **Markdown Tables**: Reproduced verbatim, ensuring pipe-delimited column formatting `| :--- | :--- |` remains intact with no broken rows.
2. **Mermaid Diagrams**: Retained within their respective ```` ```mermaid ```` blocks, ensuring valid node syntax.
3. **DM Notes**: Boxes marked `**NOTE FOR THE DUNGEON MASTER:**` or `> ⚠️ **DM Note:**` are preserved as highlighted blockquotes (`> ...`) to retain operational context for running sessions.
4. **Incomplete Placeholders**: Any `[TO_BE_DEFINED_BY_DM: ...]` markers are preserved faithfully without inventing content.

---

## 5. Incremental Update Rules (`update-bible`)

When incremental mode is invoked:
1. Do not rewrite the entire master document.
2. Locate the exact heading of the modified module (via `X.Y` code or title).
3. Replace the block between that module's heading and the next module's heading.
4. If the module is newly added, insert it at the end of its tome while respecting numerical order.
5. Update the header metadata line, setting `Modified: [TODAY_DATE]`.
