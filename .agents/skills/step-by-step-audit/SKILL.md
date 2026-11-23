---
name: step-by-step-audit
description: "Use when: conducting a step-by-step review of D&D lore or sheets with the Dungeon Master, validating individual statements (micro-atomic) or logical sections upon request, and applying the visible verification and modification badge."
argument-hint: "Specify the file or topic to review and granularity (atomic or section)"
user-invocable: true
disable-model-invocation: false
---

# Skill: Step-by-Step Lore Audit (`step-by-step-audit`)

> **In-world knowledge** — For the fact under review, use **Consultation** from `campaign-knowledge`. When the GM confirms who knows it, use **Update**. If installed but undiscovered, read its `SKILL.md` directly. If absent, continue the regular workflow.

This skill guides an interactive, systematic, hallucination-free review of D&D setting files, sheets, dossiers, or tomes by questioning the Dungeon Master (DM) concept by concept.

> **📌 Linked Proper Names Rule**: every proper name of a setting entity (PCs, NPCs, factions, houses, cities, locations, magic items, customs, festivals, events…) appearing in produced text must be a **Markdown link** to the entity's canonical `.md` file (e.g. `[Name](relative/path/file.md)`), never plain text. Exceptions: headings, file names, frontmatter, code blocks, Mermaid nodes, and `.mw` sources. Entity without a sheet: never invent it — use `[TO_BE_DEFINED_BY_DM: missing sheet for <Name>]` and flag the gap. Checking and conversion: `link-proper-names` skill.

---

## 1. Core Fact-Checking Rule

- **Absolute Source of Truth**: The Dungeon Master is the sole canonical authority.
- **No Invention**: Never alter, supplement, or deduce lore details not explicitly confirmed by the DM during the audit.
- **Placeholder for Uncertainty**: If the DM is unsure about an item under review, retain or insert `[TO_BE_DEFINED_BY_DM: description]` without inventing answers.

---

## 2. Review Granularity

Before starting (or per the DM's instructions), establish the step-by-step granularity:

1. **Level 1: Micro-Atomic (Single Statement / Bullet Point)**
   - Used for character statistics, critical hooks, dates, DM secrets, and item lists.
   - Each individual line or key concept is presented in isolation.
2. **Level 2: Logical Section (Thematic Block)**
   - Used for descriptive paragraphs, social customs, geographical chapters, or narrative sections (e.g. `## Appearance & Craftsmanship`, `## 1. Synopsis of Events`).
   - The entire coherent section is presented for validation.

---

## 3. Verification Flag Syntax (Visible Badge)

Upon validating each block or element, the official Markdown badge is applied:

```markdown
> 🛡️ *Verified: YYYY-MM-DD | Modified: YYYY-MM-DD*
```

* **Temporal Rules**:
  - When the block is validated with no edits: both dates match today's date.
  - If the block receives an agreed modification: both dates are set to today's date.
  - If an agent or the DM later edits the text outside an audit: the `Modified` date advances while leaving the `Verified` date intact. If `Modified > Verified`, the block is flagged as modified post-audit.

---

## 4. Step-by-Step Operational Procedure

1. **Load the File**:
   - Use the file-reading tool to inspect the file indicated by the DM.
   - Partition the document according to the agreed granularity (atomic or logical sections).

2. **Atomic Questioning**:
   - Present one concept or section at a time. Include the exact passage and the question in the structured form.
   - In Codex, use `request_user_input` when available and permitted, otherwise use `request_user_input_async` under the same conditions. In other environments, use the native equivalent. As a subagent, forward the question and options to the coordinator if only the main conversation can open the form.
   - With `request_user_input`, offer these three options and tell the DM to use the free-text field to dictate a correction:
     - `Confirm (Recommended)`: approve the passage as written.
     - `File edited`: re-read the passage the DM edited before updating the badge.
     - `Defer`: postpone validation of this passage.
   - Exception for `request_user_input_async` and equivalent forms: if the tool supports four options, add `Amend`. If the DM selects it without a correction, ask for the correction before continuing. With a three-option limit, use the choices above and the free-text field.
   - Use chat only if the form is unavailable or disallowed, including through the coordinator. Explain the specific reason and include the exact passage and the question.
   - Wait for the answer before applying edits or badges. With the asynchronous form, keep the turn open and resume at the pending passage when the reply arrives.

3. **Apply the Answer**:
   - **If approved without changes**: Add or update the badge:
     `> 🛡️ *Verified: [TODAY_DATE] | Modified: [TODAY_DATE]*`
   - **If the DM dictates edits**: Rewrite the text incorporating solely the DM's words or directives, then set the badge to today's date.
   - **If the DM already edited the file**: Add or update the badge to today's date.
   - **If deferred**: Add `[TO_BE_DEFINED_BY_DM: element to clarify]` and set `Verified: UNVERIFIED`.

4. **Persistence & Wrap-Up**:
   - Apply changes directly to the file with editing tools.
   - Continue to the next step until the file is complete.
   - At the end of the file, invoke the `review-status` skill to update the summary dashboard `REVIEW_STATUS.md`.
