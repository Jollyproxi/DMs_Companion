---
name: campaign-knowledge
description: "Consult, validate and update who knows a campaign fact in-world."
argument-hint: "Specify a fact, PC, party or sheet to check"
user-invocable: true
disable-model-invocation: false
---

# In-world knowledge

Work in the GM’s archive and use canonical sheets. Common knowledge is implicit, and knowledge lines record exceptions only.

On a Markdown blockquote below the individual fact, leave a blank line before the quote and indent it within the same list item when applicable.

- `> **Knowledge:** GM only` — Use when no PC knows the fact. NPCs may know it.
- `> **Knowledge:** Party — [Party name](party.md) | PCs — [PC name](pc.md)` — Use when all PCs in the named party know it. You can combine multiple parties and individual PCs.
- `> **Knowledge:** Common knowledge except — [PC name](pc.md)` — Use to name PCs excluded from common knowledge. It remains common knowledge for everyone else.

Use relative links to available canonical sheets or indexes. The three forms are mutually exclusive. Read a legacy explicit common knowledge label with no exceptions as common knowledge and remove it when updating the entry.

## Consultation

For ‘Who knows this fact?’, find the canonical entry and report the recorded assignments or implicit common knowledge, including recorded exceptions. For ‘What does this PC or party know?’, show relevant assignments and exceptions to common knowledge. For a party, distinguish group assignments from those of individual members. Resolve membership from the relevant dossiers or indexes. Ask the GM about ambiguous facts, identities or memberships.

## Validation

Report the file and fact for malformed or duplicate labels, missing required recipients, broken links or incompatible categories. Facts without a line are valid. Validation makes no edits.

## Update

Apply what the GM confirms or what the confirmed session record states explicitly. For discoveries, preserve existing assignments and replace GM only once a PC learns the fact. Edit the knowledge line and update the modification badge according to project conventions. Remove the line when the fact is common knowledge with no exceptions.

The **Party** and **PCs** sections can each appear on their own. When a PC learns a fact they were excluded from, remove that PC from the exceptions.
