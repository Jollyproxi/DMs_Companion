---
name: schritt-fuer-schritt-audit
description: "Use when: eine schrittweise Prüfung der Lore oder von D&D-Bögen mit dem Spielleiter durchführen, Einzelaussagen (mikro-atomar) oder logische Abschnitte auf Wunsch validieren und das sichtbare Prüf- und Änderungs-Badge anbringen."
argument-hint: "Gib die zu prüfende Datei oder das Thema sowie die Granularität (atomar oder abschnitt) an"
user-invocable: true
disable-model-invocation: false
---

# Skill: Schritt-für-Schritt-Audit der Lore (`schritt-fuer-schritt-audit`)

Dieser Skill leitet eine interaktive, systematische und halluzinationsfreie Prüfung von D&D-Weltdateien, Bögen, Dossiers oder Bänden, indem der Spielleiter (SL) Konzept für Konzept befragt wird.

> **📌 Regel: Eigennamen als Verknüpfungen**: Jeder Eigenname einer Weltentität (SCs, NSCs, Fraktionen, Häuser, Städte, Orte, magische Gegenstände, Bräuche, Feste, Ereignisse …), der im erzeugten Text vorkommt, muss eine **Markdown-Verknüpfung** zur kanonischen `.md`-Datei der Entität sein (z. B. `[Name](relativer/pfad/datei.md)`), niemals bloßer Klartext. Ausnahmen: Überschriften, Dateinamen, Frontmatter, Codeblöcke, Mermaid-Knoten und `.mw`-Quellen. Entität ohne Bogen: niemals erfinden — `[VOM_SL_ZU_DEFINIEREN: Bogen fehlt für <Name>]` verwenden und die Lücke melden. Prüfung und Umwandlung: Skill `eigennamen-verlinken`.

---

## 1. Grundregel der Faktenprüfung

- **Absolute Wahrheitsquelle**: Allein der Spielleiter ist kanonische Autorität.
- **Erfindungsverbot**: Verändere, ergänze oder folgere niemals Lore-Details, die während des Audits nicht ausdrücklich vom SL bestätigt wurden.
- **Platzhalter bei Unklarheit**: Ist der SL bei einem geprüften Punkt unsicher, belasse oder ergänze `[VOM_SL_ZU_DEFINIEREN: Beschreibung]`, ohne Antworten zu erfinden.

---

## 2. Granularität der Prüfung

Lege vor Beginn (oder nach Anweisung des SL) die Granularität des Audits fest:

1. **Stufe 1: Mikro-Atomar (Einzelaussage / Aufzählungspunkt)**
   - Für Charakterwerte, kritische Aufhänger, Daten, SL-Geheimnisse und Gegenstandslisten.
   - Jede einzelne Zeile oder Kernaussage wird isoliert vorgelegt.
2. **Stufe 2: Logischer Abschnitt (Themenblock)**
   - Für beschreibende Absätze, gesellschaftliche Bräuche, geografische Kapitel oder Erzählabschnitte (z. B. `## Aussehen & Herstellung`, `## 1. Zusammenfassung der Ereignisse`).
   - Der gesamte zusammenhängende Abschnitt wird zur Validierung vorgelegt.

---

## 3. Syntax der Prüfmarkierung (Sichtbares Badge)

Nach der Validierung jedes Blocks oder Elements wird das offizielle Markdown-Badge angebracht:

```markdown
> 🛡️ *Geprüft: JJJJ-MM-TT | Geändert: JJJJ-MM-TT*
```

* **Zeitregeln**:
  - Wird der Block ohne Änderungen bestätigt: beide Daten entsprechen dem heutigen Datum.
  - Wird der Block einvernehmlich geändert: beide Daten werden auf das heutige Datum gesetzt.
  - Bearbeitet ein Agent oder der SL den Text später außerhalb eines Audits: das Datum `Geändert` rückt vor, während `Geprüft` unverändert bleibt. Ist `Geändert > Geprüft`, wird der Block als nach dem Audit geändert markiert.

---

## 4. Schritt-für-Schritt-Verfahren

1. **Datei laden**:
   - Lese die vom SL benannte Datei mit dem Lesewerkzeug.
   - Unterteile das Dokument gemäß der vereinbarten Granularität (atomar oder nach logischen Abschnitten).

2. **Atomare Befragung**:
   - Lege jeweils einen Begriff oder Abschnitt vor. Füge den genauen Wortlaut und die Frage in das Formular ein.
   - Verwende in Codex `request_user_input`, sofern verfügbar und zulässig, sonst unter denselben Bedingungen `request_user_input_async`. Nutze in anderen Umgebungen das entsprechende Werkzeug. Leite als Subagent die Frage und die Optionen an die Hauptunterhaltung weiter, wenn nur diese das Formular öffnen kann.
   - Biete mit `request_user_input` diese drei Optionen an und weise darauf hin, dass Korrekturen im Freitextfeld eingegeben werden können:
     - `Bestätigen (empfohlen)`: den Abschnitt unverändert freigeben.
     - `Datei bearbeitet`: den von der Spielleitung geänderten Abschnitt vor der Aktualisierung des Prüfvermerks erneut lesen.
     - `Zurückstellen`: die Prüfung dieses Abschnitts verschieben.
   - Ausnahme für `request_user_input_async` und vergleichbare Formulare: Unterstützt das Werkzeug vier Optionen, ergänze `Korrigieren`. Wählt die Spielleitung diese Option ohne Korrekturtext, frage nach der Korrektur, bevor du fortfährst. Bei höchstens drei Optionen verwende die obigen Optionen und das Freitextfeld.
   - Frage nur im Chat, wenn das Formular auch über die Hauptunterhaltung nicht verfügbar oder nicht zulässig ist. Nenne den konkreten Grund und füge den genauen Wortlaut und die Frage bei.
   - Warte auf die Antwort, bevor du Änderungen oder Prüfvermerke anbringst. Halte beim asynchronen Formular den Gesprächsschritt offen und setze die Prüfung nach der Antwort am offenen Punkt fort.

3. **Antwort anwenden**:
   - **Ohne Änderungen genehmigt**: Badge hinzufügen oder aktualisieren:
     `> 🛡️ *Geprüft: [HEUTIGES_DATUM] | Geändert: [HEUTIGES_DATUM]*`
   - **SL diktiert Änderungen**: Formuliere den Text ausschließlich anhand der Worte oder Vorgaben des SL neu und setze das Badge auf das heutige Datum.
   - **SL hat die Datei bereits bearbeitet**: Badge hinzufügen oder auf das heutige Datum setzen.
   - **Zurückgestellt**: `[VOM_SL_ZU_DEFINIEREN: zu klärender Punkt]` ergänzen und `Geprüft: NICHT_GEPRUEFT` setzen.

4. **Speicherung & Abschluss**:
   - Wende die Änderungen mit den Bearbeitungswerkzeugen direkt auf die Datei an.
   - Fahre mit dem nächsten Schritt fort, bis die Datei abgeschlossen ist.
   - Rufe am Dateiende den Skill `pruefungsstatus` auf, um das Übersichts-Dashboard `PRUEFUNGSSTATUS.md` zu aktualisieren.
