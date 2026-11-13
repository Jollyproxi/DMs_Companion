---
name: full-file-audit
description: "Use when: reviewing and auditing an entire D&D document, dossier, or folder in a single pass, spotting inconsistencies, proposing amendments, and applying visible verification badges."
argument-hint: "Path of the file or folder to verify (e.g. 05_characters/ or single .md)"
user-invocable: true
disable-model-invocation: false
---

# Skill: Full Document or Folder Audit (`full-file-audit`)

This skill enables a fast, holistic, and organic review of an entire D&D file or group of files (thematic folder), ideal when the DM prefers a comprehensive overview with block-level validation rather than concept-by-concept questioning.

---

## 1. Review Rules

- **Inconsistency Detection**: Cross-check the document's claims against the workspace's cosmology and chronicles (e.g. dates, house names, faction hierarchies) to flag potential conflicts to the DM.
- **No Rewriting Without Approval**: Always present the findings and proposed corrections before editing the file.
- **Structure Awareness**: Respect the workspace's modularity (cosmology, geography, politics, law, characters, locations, factions, items, chronicles, customs-festivals-events, timeline).

---

## 2. Verification Flag Syntax (Visible Badge)

Each validated main section or sheet receives the standard Markdown badge:

```markdown
> 🛡️ *Verified: YYYY-MM-DD | Modified: YYYY-MM-DD*
```

If the file is organised into thematic sections (`## Title`), place the badge immediately beneath each validated section heading.

---

## 3. Operational Procedure

1. **Scan the Document or Folder**:
   - Read the file (or list the files in the specified directory).
   - Extract the conceptual map: entities involved, narrative facts, and links to other parts of the world.

2. **Present the Audit Summary**:
   - Provide the DM with a structured synopsis:
     - **File Under Review**: File path.
     - **Strengths / Recognised Canon**: List of consistent facts.
     - **Potential Discrepancies or Doubts**: Flag conflicts or `[TO_BE_DEFINED_BY_DM]` fields.
     - **Draft Proposed Amendments**: Show suggested corrections, if any.

3. **DM Confirmation**:
   - Request confirmation from the DM (using the environment's structured question tool such as `vscode_askQuestions` or `AskUserQuestion` if available, otherwise directly in chat) with clear options:
     - `Approve all and apply 🛡️ badges` (recommended if there are no discrepancies)
     - `Request specific amendments` (allows entering corrections as free text)
     - `Cancel audit / No changes`

4. **Apply Flags**:
   - Once confirmed, apply the edits and place `> 🛡️ *Verified: [TODAY_DATE] | Modified: [TODAY_DATE]*` badges on each validated section.

5. **Update Dashboard**:
   - Invoke the `review-status` skill to update the general overview in `REVIEW_STATUS.md`.
