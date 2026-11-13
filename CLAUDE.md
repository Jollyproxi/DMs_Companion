@AGENTS.md

## Note specifiche per Claude Code

- Segui tutte le regole e i flussi definiti in `AGENTS.md`.
- Se le skill in `.agents/skills/` non vengono caricate automaticamente dal tuo ambiente, copiale o collegale in `.claude/skills/` oppure leggi direttamente il relativo `SKILL.md` al momento dell'invocazione.
- Per le domande interattive al Master usa `AskUserQuestion` se disponibile, altrimenti poni le domande direttamente in chat.
