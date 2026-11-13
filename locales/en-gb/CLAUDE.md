@AGENTS.md

## Claude Code Specific Notes

- Follow all rules and workflows defined in `AGENTS.md`.
- If skills inside `.agents/skills/` are not automatically discovered by your environment, copy or symlink them to `.claude/skills/`, or read the relevant `SKILL.md` directly when invoked.
- For interactive questions to the DM, use `AskUserQuestion` if available; otherwise ask directly in chat.
