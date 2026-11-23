# Gossip and rumours

`03_society_and_politics/gossip_and_rumours/` · `region/place/topic`

Before the first entry, including a draft, complete any missing parts of the tome 03 structure: the collection folder, its README and the link from the tome index.

Collect GM ideas, reported claims, community beliefs, lies and half-truths. Mark each record **draft** or **in circulation**. Index drafts even without a location. Queries about what is circulating include only circulating records. Change status when circulation is documented.

When the GM asks what to tell players, briefly give the circulating account and the context the PCs can perceive. Reserve notes and hidden details for the GM.

Before creating a record, search by title, subject, alias and tag. Reuse the file for the same account across places or circles. Give each distinct telling that changes the claim its own file. Link related versions to each other using relative links and give the family a stable shared tag. Use a neutral title on the sheet and in indexes. For each version, add one row per documented place–circle pair, linking each row to the same file. If only the place is known, leave the circle blank. When splitting older multi-version records, preserve attributions and notes and redirect incoming fragment links.

File by place of circulation. For a regionally shared account use the regional folder and list known locations. File worldwide accounts at the root. For the same version in exactly two specific locations, even in one region, keep one record and link to the relevant version from the other location’s index. Update indexes and links if the scope changes.

Record title, status, topic and the attributed claim. Record where it circulates, local details, its origin and instigator when known. Distinguish its setting from the place it describes. Use relative links to participants and all related sheets, including events, customs and recurring occasions. An optional free-text **GM note** at the end can clarify true, false and undecided elements later. Confirmed accounts stay in the collection.

End each related sheet with a bulleted **Rumours** section. Use module 05 for PCs. For PCs, NPCs and factions group entries by role. Each bullet summarises the relevant version in one line and links to the version’s file using a relative Markdown link. Repeat the link for each documented role. Record separately what the subject has heard, believes or knows (including knowing a claim is false) and what they spread. Neither local circulation nor being mentioned establishes awareness. Keep personal PC beliefs in their own section of module 05, even without a corresponding rumour.

- Rumours heard
- Rumours believed
- Rumours spread
- Rumours about this subject

## Record template

```markdown
# [Title of the account]

* **Status** — [draft or in circulation]
* **Topic** — […]
* **Family tag** — `#<slug>`
* **Aliases** — […]
* **Location and documented circle** — […]

## Reported version

[Attributed version, circulation and local details]

## Related versions

- [Other version](../version-b.md)

## Participants and related sheets

- [Subject](../subject.md) — role in this version, documented stance, if known.
- [Related sheet](../context.md) — relationship.

## GM note (optional)
```
