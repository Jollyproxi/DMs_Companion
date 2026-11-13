---
name: vollstaendiges-datei-audit
description: "Use when: ein komplettes D&D-Dokument, Dossier oder einen Ordner in einem Durchgang prüfen und auditieren, Unstimmigkeiten aufspüren, Anpassungen vorschlagen und sichtbare Prüf-Badges anbringen."
argument-hint: "Pfad der zu prüfenden Datei oder des Ordners (z. B. 05_charaktere/ oder einzelne .md)"
user-invocable: true
disable-model-invocation: false
---

# Skill: Vollständiges Dokument- oder Ordner-Audit (`vollstaendiges-datei-audit`)

Dieser Skill ermöglicht eine zügige, ganzheitliche und stimmige Prüfung einer gesamten Datei oder Dateigruppe (Themenordner) zu D&D — ideal, wenn der Spielleiter anstelle der atomaren Einzelbefragung einen Gesamtüberblick mit Blockvalidierung wünscht.

---

## 1. Prüfregeln

- **Erkennung von Unstimmigkeiten**: Gleiche Aussagen des Dokuments mit der Kosmologie und den Chroniken des Workspace ab (z. B. Daten, Hausnamen, Fraktionshierarchien), um dem SL mögliche Konflikte aufzuzeigen.
- **Kein Umschreiben ohne Freigabe**: Zeige vor jeder Dateiänderung stets den Prüfbericht und die vorgeschlagenen Korrekturen.
- **Strukturbewusstsein**: Respektiere die Modularität des Workspace (Kosmologie, Geografie, Politik, Recht, Charaktere, Orte, Fraktionen, Gegenstände, Chroniken, Bräuche-Feste-Ereignisse, Zeitlinie).

---

## 2. Syntax der Prüfmarkierung (Sichtbares Badge)

Jeder validierte Hauptabschnitt oder Bogen erhält das standardisierte Markdown-Badge:

```markdown
> 🛡️ *Geprüft: JJJJ-MM-TT | Geändert: JJJJ-MM-TT*
```

Ist die Datei in Themenabschnitte (`## Titel`) gegliedert, wird das Badge unmittelbar unter der Überschrift jedes validierten Abschnitts platziert.

---

## 3. Operatives Verfahren

1. **Scan des Dokuments oder Ordners**:
   - Lies die Datei (oder liste die Dateien des angegebenen Ordners auf).
   - Extrahiere die Konzeptkarte: beteiligte Entitäten, narrative Fakten und Verknüpfungen mit anderen Teilen der Welt.

2. **Vorlage der Audit-Zusammenfassung**:
   - Präsentiere dem SL eine strukturierte Übersicht:
     - **Geprüfte Datei**: Dateipfad.
     - **Stärken / Bestätigter Kanon**: Liste konsistenter Fakten.
     - **Mögliche Unstimmigkeiten oder Unklarheiten**: Markiere Widersprüche oder `[VOM_SL_ZU_DEFINIEREN]`-Stellen.
     - **Entwurf vorgeschlagener Änderungen**: Zeige ggf. empfohlene Korrekturen.

3. **Bestätigung durch den SL**:
   - Bitte den SL (über das strukturierte Fragewerkzeug der Umgebung wie `vscode_askQuestions` oder `AskUserQuestion`, falls verfügbar; sonst direkt im Chat) um Freigabe mit klaren Optionen:
     - `Alles freigeben und 🛡️-Badges setzen` (empfohlen, wenn keine Unstimmigkeiten vorliegen)
     - `Gezielte Korrekturen anfordern` (ermöglicht Freitexteingabe der Änderungen)
     - `Audit abbrechen / Keine Änderungen`

4. **Setzen der Badges**:
   - Wende nach der Bestätigung die Änderungen an und setze die Badges `> 🛡️ *Geprüft: [HEUTIGES_DATUM] | Geändert: [HEUTIGES_DATUM]*` in jeden validierten Abschnitt.

5. **Dashboard aktualisieren**:
   - Rufe den Skill `pruefungsstatus` auf, um die Gesamtübersicht in `PRUEFUNGSSTATUS.md` zu aktualisieren.
