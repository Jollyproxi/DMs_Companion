# Contributing to DMs_Companion

Thank you for considering a contribution! This document explains how to contribute, what the project's non-negotiable principles are, and the terms under which contributions are accepted.

---

## Ways to Contribute

* **Bug reports** — if a skill misbehaves, loops, or breaks in your harness, open an issue describing the harness, the skill, and what happened.
* **Translation fixes** — corrections and improvements to the localisations under [`locales/`](locales).
* **Harness compatibility notes** — if you got the toolkit working (or partly working) in a harness not yet documented, your findings are gold.
* **Skill improvements** — clearer instructions, better templates, new references, workflow refinements.

---

## Project Principles

These are the pillars of the toolkit. Contributions should preserve them:

1. **Notarial fidelity (zero hallucinations)** — skills must organise only what the DM provides or has already canonised. Missing information gets flagged and asked for; it is never invented. Templates must never encourage placeholder lore to be silently filled in by the AI.
2. **Harness agnosticism** — every skill must degrade gracefully across VS Code Copilot, Claude Code, Codex CLI, Cursor, Gemini CLI / Antigravity, OpenCode, etc. Structured question tools are used when available, with plain-chat fallbacks.
3. **Architecture** — skills must respect the standard world tree (`01_` … `10_`) and its cross-references (especially the sync between tomes and `10_timeline/`).
4. **Self-contained skills** — each skill lives in its own folder with `SKILL.md` and, when useful, a `references/` subfolder. No hidden cross-skill dependencies.

---

* Keep translations idiomatic: skill names and file names follow each language's established conventions (see the existing skills in that locale).

## How to Submit

1. Fork the repository and create a branch from `main`.
2. Make your changes in `locales/<lang>/`.
3. Open a pull request against `main` with a short description of the problem and the solution. If the change touches behaviour or conventions, explain the reasoning.

---

## Licence of Contributions

By submitting a contribution (pull request, patch, or translation), you agree that:

1. your contribution is licensed under the [CC BY-NC-SA 4.0 Licence](LICENSE), like the rest of the project; and
2. you grant the project maintainer the right to **relicense** your contribution as part of future versions of DMs_Companion under a different licence (e.g. a dual-licensing model) across the universe.

You retain the copyright of your work. This keeps a future licence change possible without having to track down every past contributor.

---

## A Note on Review Times

This is a solo-maintained project, and **reviews may take a while**: each contribution gets proper attention to preserve the project's principles. Please be patient if responses aren't immediate — a slow "yes, carefully reviewed" is worth more than a fast "merged and broken". Thank you for understanding!
