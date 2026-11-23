# Reference Templates for Character Dossiers

## 1. Modular Player Character (PC) Dossier

Each PC has a dedicated folder under `05_characters/<Player_Characters>/<Campaign_or_Party>/<PC_Name>/` (default: `05_characters/Player_Characters/<Campaign>/<PC_Name>/`) with a connecting `README.md` and six thematic modules:

### `README.md` (Character Hub)
```markdown
# [Character Name]

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

* **Campaign:** [Campaign Name]
* **Party Role:** [Summary of martial/arcane/social role]
* **Alignment / Moral Code:** [Alignment or ethical principles]

## Module Index
1. [01. Profile & Core Traits](01_profile_and_traits.md)
2. [02. Integrated Backstory](02_integrated_backstory.md)
3. [03. Relationships & Group Dynamics](03_relationships_and_dynamics.md)
4. [04. Equipment & Signature Abilities](04_equipment_and_abilities.md)
5. [05. Rumours and beliefs](05_rumours_and_beliefs.md)
6. [06. Narrative Hooks & DM Secrets](06_dm_hooks_and_secrets.md)
```

### `01_profile_and_traits.md`
```markdown
# 01. Profile & Core Traits

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

* **Name:** [Full Name]
* **Species / Lineage:** [D&D 5e species / world lineage]
* **Class & Level:** [Class, Subclass, Level]
* **Alignment / Moral Code:** [Alignment or guiding principles]
* **Physical Appearance:** [Visual description, distinguishing marks, scars, attire]
* **Personality Traits, Ideals, Bonds, Flaws:** [Concise lists]
```

### `02_integrated_backstory.md`
```markdown
# 02. Canon-Integrated Backstory

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

## Origins & Roots
[Description of geographical and social background with relative links to world locations.]

## The Turning Point
[The founding event or trauma that set the character upon the path of adventure.]

## Recent Developments Prior to the Campaign
[What occurred in the period immediately preceding the campaign's start.]
```

### `03_relationships_and_dynamics.md`
```markdown
# 03. Relationships & Dynamics

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

## Bonds with Party Companions
* **[Companion Name 1]:** [Relational dynamic, trust, friction]
* **[Companion Name 2]:** [...]

## Bonds with NPCs & Factions
* **[NPC / Faction Name]:** [Nature of relationship, debts of honour, rivalries]
```

### `04_equipment_and_abilities.md`
```markdown
# 04. Equipment & Signature Abilities

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

## Primary Gear & Focuses
* [Magic Item / Focus with optional link to 08_unique_magic_items/]

## Signature Abilities & Traits
* **[Ability Name]:** [Narrative and mechanical description]
```

### `05_rumours_and_beliefs.md`

For each documented role add a bullet summarising the version with a relative link to it. Include the subject’s stance when documented.

```markdown
# 05. Rumours and beliefs

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

## Rumours heard

## Rumours believed

## Rumours spread

## Rumours about this subject

## Personal beliefs
```

### `06_dm_hooks_and_secrets.md`
```markdown
# 06. Narrative Hooks & DM Secrets

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

> ⚠️ *Confidential section for Dungeon Master use only.*

## Open Investigative Leads
* **[Lead 1]:** [Details, hooks, potential developments]

## Hidden Truths & Future Revelations
* **[Secret 1]:** [Truth about the PC's past unknown to the character]
```

---

## 2. Non-Player Character (NPC) Sheet

Follow the project’s NPC archive convention. Read the project instructions and the character volume index. For existing projects without an explicit rule, follow the established layout and indexes and flag conflicts or ambiguities to the GM. Look up the existing sheet through indexes, files and any aliases. Keep one canonical file per identity and link to it from campaigns, factions and other locations. For geographical or narrative levels, use the documented stable connection and record its basis. First encounter (location and session record) and current whereabouts are separate fields. Flag unresolved information and retain confirmed levels. Use a provisional location where the project defines one, otherwise ask the GM to resolve hierarchical placement. Use itinerant or cross-cutting categories only when supported by both the project and canon. In a flat archive, record these details in the sheet or index as specified.

```markdown
# [NPC Name] — [Title or Role]

> 🛡️ *Verified: UNVERIFIED | Modified: [TODAY_DATE]*

* **Stable connection and basis:** [Level values, category or unresolved detail as specified by the convention]
* **Current whereabouts:** [Location link, if known; separate from primary reference]
* **First encounter:** [Links to minutes and location, if documented]
* **Faction / House:** [Faction Name with relative link to 07_factions/]
* **Place of Residence / Operations:** [Location with link to 06_locations/]
* **Alignment / Morals:** [Alignment or moral principles]
* **Current Status:** [Alive, Fugitive, Deceased, Missing]

---

## Appearance & Temperament
[Physical description, bearing, manner of speech, disposition.]

---

## Narrative Role & Party Relations
[Who they are in the world and how they interact with the PCs.]

---

## Secrets & DM Hooks
* **[Secret / Hidden Motive]:** [What they truly pursue]
* **[Adventure Hook]:** [How to involve them in upcoming sessions]

## Rumours

### Rumours believed

### Rumours spread

### Rumours about this subject
```
