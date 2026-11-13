---
name: magic-item
description: "Use when: registering or formatting unique magic items, relics, and artefacts of the setting according to the canonical four-section standard (technical sheet, craftsmanship, mechanics, legal status)."
argument-hint: "Name of the magic item and details to record or update"
user-invocable: true
disable-model-invocation: false
---

# Skill: Unique Magic Items Management (`magic-item`)

This skill governs the formal cataloguing of artefacts, relics, and arcane focuses inside Tome `08_unique_magic_items/`, adhering to the structural template defined in [item-template](./references/item-template.md).

> **📌 Linked Proper Names Rule**: every proper name of a setting entity (PCs, NPCs, factions, houses, cities, locations, magic items, customs, festivals, events…) appearing in produced text must be a **Markdown link** to the entity's canonical `.md` file (e.g. `[Name](relative/path/file.md)`), never plain text. Exceptions: headings, file names, frontmatter, code blocks, Mermaid nodes, and `.mw` sources. Entity without a sheet: never invent it — use `[TO_BE_DEFINED_BY_DM: missing sheet for <Name>]` and flag the gap. Checking and conversion: `link-proper-names` skill.

---

## 1. Registration Principles

- **World Framing**: Record the item's origin, rarity, and legal or commercial status according to the setting's rules (freely traded goods, guild licence, state/noble monopoly, or prohibited contraband).
- **Zero Invention**: If the DM supplies only mechanical properties or appearance, never invent fictional provenance or bearers: ask for missing details or insert `[TO_BE_DEFINED_BY_DM: ...]`.
- **Badge Tracking**: Every sheet includes the badge:
  `> 🛡️ *Verified: YYYY-MM-DD | Modified: YYYY-MM-DD*`

---

## 2. Operational Procedure

1. **Gather Information**:
   If the details provided by the DM are incomplete, present a structured prompt (using the environment's interactive question tool such as `vscode_askQuestions` or `AskUserQuestion` if available, otherwise in chat):
   - **`category`**: Options (*Magic Weapon*, *Musical Instrument / Focus*, *Ancient Relic / Artefact*, *Magical Contraption / Device*, *Rare Consumable*).
   - **`bearer`**: Current bearer (options based on registered PCs or free text for an NPC/location).
   - **`legal_status`**: Options (*Lawful Free Possession*, *Subject to Licence or Monopoly*, *Contraband / Prohibited Relic*, *Other*).
   - **`mechanical_powers`**: D&D 5e mechanical properties and sensory resonances (free text).

2. **Create the File**:
   Save the sheet to `08_unique_magic_items/<Item_Name>.md` using the standard template.

3. **Update the Tome Index**:
   Add the entry with its category, resonance, and bearer to the table or list in `08_unique_magic_items/README.md`.

4. **Cross-Link with Bearer**:
   If the item belongs to a PC, update the `04_equipment_and_abilities.md` module of that PC's dossier by linking to the new item sheet.
