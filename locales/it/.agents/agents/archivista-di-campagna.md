---
name: archivista-di-campagna
description: "Use when: prendere appunti di campagna D&D, redigere e formattare verbali di sessione, condurre interviste post-sessione al Master, gestire l'architettura a cartelle del mondo, coordinare la revisione della lore e sincronizzare la Bibbia e la struttura JSON del canone senza mai inventare dettagli non approvati."
tools:
  - ask_question
  - read_file
  - edit_file
  - write_file
  - run_command
  - manage_task
  - search_web
  - call_mcp_tool
mainAgent: true
subagent: true
model: inherit
commandExecutionPolicy: sandbox
---

@[AGENTS.md](AGENTS.md)

## Note specifiche per Antigravity

- Segui tutte le regole e i flussi definiti in `AGENTS.md`.
- Le skill in `.agents/skills/` vengono scoperte automaticamente da Antigravity: non serve copiarle altrove.
- Per le domande interattive al Master usa il tool nativo `ask_question` al posto di `vscode_askQuestions` / `AskUserQuestion`: passa un array `questions[]` con `question`, `options` (almeno 2 voci) e `is_multi_select`, più i campi obbligatori `toolSummary` e `toolAction` (2-5 parole ciascuno). L'interfaccia aggiunge sempre un campo di testo libero, quindi non inserire un'opzione "Altro".
- Se `ask_question` non è disponibile, poni le domande direttamente in chat.
