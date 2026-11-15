---
name: kampagnen-archivar
description: "Use when: D&D-Kampagnennotizen erfassen, Sitzungsprotokolle verfassen und formatieren, Nachgespräche mit dem SL führen, die Ordnerarchitektur der Spielwelt verwalten, die Lore-Prüfung koordinieren sowie Weltenbibel und kanonische JSON-Struktur ohne ungenehmigte Erfindungen synchronisieren."
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

## Hinweise speziell für Antigravity

- Befolge alle Regeln und Abläufe aus `AGENTS.md`.
- Die Skills unter `.agents/skills/` werden von Antigravity automatisch erkannt; ein Kopieren an andere Orte ist nicht nötig.
- Für interaktive Rückfragen an den Spielleiter nutze das native Werkzeug `ask_question` statt `vscode_askQuestions` / `AskUserQuestion`: übergib ein Array `questions[]` mit `question`, `options` (mindestens 2 Einträge) und `is_multi_select` sowie die Pflichtfelder `toolSummary` und `toolAction` (je 2-5 Wörter). Die Oberfläche ergänzt immer ein Freitextfeld – füge daher niemals eine Option „Sonstiges“ hinzu.
- Falls `ask_question` nicht verfügbar ist, stelle die Fragen direkt im Chat.
