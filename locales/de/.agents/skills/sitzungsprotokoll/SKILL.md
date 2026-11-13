---
name: sitzungsprotokoll
description: "Use when: ein D&D-Sitzungsprotokoll verfassen, das Nachgespräch mit dem Spielleiter führen, das formelle Protokoll samt Mermaid-Diagramm der SC-Aufhänger erstellen und den Kampagnenindex aktualisieren."
argument-hint: "Sitzungsnotizen einfügen oder 'Interview starten' schreiben, um das geführte Verfahren zu beginnen"
user-invocable: true
disable-model-invocation: false
---

# Skill: Sitzungsprotokoll (`sitzungsprotokoll`)

Dieser Skill leitet die Erfassung, Strukturierung und Formatierung von Spielsitzungsprotokollen für beliebige D&D-Kampagnen und stellt die Einhaltung des Standardmodells aus [protokoll-vorlage](./references/protokoll-vorlage.md) sicher.

> **📌 Regel: Eigennamen als Verknüpfungen**: Jeder Eigenname einer Weltentität (SCs, NSCs, Fraktionen, Häuser, Städte, Orte, magische Gegenstände, Bräuche, Feste, Ereignisse …), der im erzeugten Text vorkommt, muss eine **Markdown-Verknüpfung** zur kanonischen `.md`-Datei der Entität sein (z. B. `[Name](relativer/pfad/datei.md)`), niemals bloßer Klartext. Ausnahmen: Überschriften, Dateinamen, Frontmatter, Codeblöcke, Mermaid-Knoten und `.mw`-Quellen. Entität ohne Bogen: niemals erfinden — `[VOM_SL_ZU_DEFINIEREN: Bogen fehlt für <Name>]` verwenden und die Lücke melden. Prüfung und Umwandlung: Skill `eigennamen-verlinken`.

---

## 1. Goldene Regel (Keine Halluzinationen)

- **Absolute Treue**: Erfinde niemals NSCs, Dialoge, Orte oder Hintergründe, die nicht vom SL beschrieben wurden.
- **Lücken**: Fehlen wesentliche Angaben (z. B. der Name eines NSC oder der Ausgang eines Kampfes), erfrage sie während des Interviews oder markiere sie mit `[VOM_SL_ZU_DEFINIEREN: Beschreibung]`.

---

## 2. Datenerfassungsmodi

### Kanal A: Geführtes Nachgespräch
Aktivierbar mit *„Interview starten“* oder direkt nach einer Sitzung. Stelle dem SL die Fragen strukturiert (über das interaktive Fragewerkzeug der Umgebung wie `vscode_askQuestions` oder `AskUserQuestion`, falls verfügbar; sonst direkt im Chat):
1. **`sitzungskoordinaten`**: *Sitzungsnummer, Ingame-Datum und geografischer Schauplatz der Ereignisse?* (Freitext mit kurzem Hinweis).
2. **`anwesende_scs`**: *Welche Spielercharaktere waren anwesend?*
   - Mehrfachauswahl basierend auf den in `05_charaktere/<Spielercharaktere>/<Kampagne_oder_Gruppe>/` erfassten Dossiers (mit Freitextmöglichkeit für neue SCs oder bedeutende NSCs).
3. **`ereignischronologie`**: *Was ist der Reihe nach geschehen (Auftakt, zentrale Wendepunkte, Kämpfe/Verhandlungen, Ausklang)?* (Freitext).
4. **`aufhaenger_enthuellungen`**: *Welche Entdeckungen, Hinweise oder Wendepunkte haben gezielt einzelne SCs betroffen?* (Freitext zur Erstellung des Mermaid-Diagramms).
5. **`regeldaten`**: *Gibt es regeltechnische Ressourcen oder Ereignisse festzuhalten?*
   - Optionen: *Keine (nur Erzählung)*, *Münzen & Ausgaben*, *Magische Gegenstände / Beute*, *Bleibende Verletzungen, Zustände oder Schulden* (bei Auswahl mit Detailangabe).

### Kanal B: Aufbereitung von Rohnotizen
Fügt der SL ungeordnete Notizen ein, extrahiere die Chronologie, isoliere gesicherte Fakten und erstelle direkt einen Entwurf. Fehlen kritische Details, bitte den SL (über das strukturierte Fragewerkzeug falls verfügbar, sonst im Chat), vor dem Speichern lediglich diese Lücken zu schließen.

---

## 3. Verfassen des Protokolls

Das Protokoll wird in den kanonischen Abschnitten erstellt:
1. **Kopfzeile**: Technische Daten und relative Markdown-Links zu SC- und Ortsdossiers.
2. **Ereigniszusammenfassung**: Formelles, distanziertes Notariatsregister in der dritten Person, flüssig und chronologisch geordnet.
3. **Die Aufhänger der Protagonisten**:
   - Mermaid-Diagramm `flowchart TD`, das das Schlüsselereignis oder die Bedrohung mit den einzelnen SCs verbindet.
   - Unterabschnitte pro SC mit erkanntem/erhaltenem Element und narrativer Wirkung.
4. **Schlüsselphasen**: Nummerierte Kurzliste zur schnellen Orientierung am Spieltisch.
5. **Regelprotokoll (Optional)**: Nur auf ausdrücklichen Wunsch enthalten.

---

## 4. Archivierung & Fortschreibung

1. **Datei speichern**:
   Speichere unter `09_chroniken/<kampagnen>/<kampagnenname>/<sitzungen>/XX_sitzungstitel.md` *(Standard: `09_chroniken/kampagnen/<kampagnenname>/sitzungen/...`, unter Wahrung benutzerdefinierter Ordnernamen wie `expeditionen/`, `abenteuer/`, `tagebuecher/`)*.
2. **Kampagnenindex aktualisieren**:
   Füge die neue Zeile in die Übersichtstabelle unter `09_chroniken/<kampagnen>/<kampagnenname>/README.md` ein:
   `| **XX** | [Titel] | [Datum] | [Ort] | [Hauptfokus] | [Protokoll](<sitzungen>/XX_titel.md) |`
3. **Vorschläge für Querverknüpfte Aktualisierungen (A + B)**:
   - Liste am Ende der Antwort alle betroffenen Repository-Dateien auf (neue NSCs, gefundene magische Gegenstände, in SC-Dossiers per `charakter-dossier` nachzutragende Aufhänger).
   - **Bräuche, Feste und Ereignisse**: Führt die Sitzung einen neuen Brauch, ein neues Fest/Vorkommnis oder ein neues Ereignis ein bzw. erwähnt es, **schlage stets die Anlage des zugehörigen Bogens** in `03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/` über `brauch-fest-ereignis` vor.
   - **Vorkommnisse bereits erfasster Ereignisse & Markwhen-Zeitlinie**: Spielt in der Sitzung eine bekannte Wiederkehr (z. B. ein jährliches Turnier oder ein saisonales Fest) oder treten datierte Ereignisse auf, dokumentiere sie im Protokoll und trage sie in `10_zeitlinie/` ein (Vorkommnisregister und `.mw`-Quellen über `timeline-markwhen`); **frage anschließend den SL**, ob der kanonische Bogen angepasst werden soll: Besonderheiten des einzelnen Vorkommnisses bleiben in Zeitlinie und Protokoll, der Bogen wird nur bei einer Wesensänderung angepasst.
   - Zeige die Änderungen an und biete an, sie nach Bestätigung anzuwenden.
