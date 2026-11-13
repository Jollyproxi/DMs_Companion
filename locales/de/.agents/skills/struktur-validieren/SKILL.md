---
name: struktur-validieren
description: "Use when: die strukturelle Integrität eines D&D-Welt-Repositories prüfen, fehlende Ordner, abwesende README-Indizes, defekte Markdown-Links, nicht verknüpfte Eigennamen und fehlplatzierte Dateien erkennen."
argument-hint: "Führt die strukturelle Konformitätsprüfung des Archivs aus"
user-invocable: true
disable-model-invocation: false
---

# Skill: Validierung der Weltstruktur (`struktur-validieren`)

Dieser Skill führt ein gründliches Diagnose-Audit des Verzeichnisbaums im Repository durch, stellt die Konformität mit der standardisierten D&D-Architektur sicher und deckt technische Abweichungen frühzeitig auf.

> **📌 Regel: Eigennamen als Verknüpfungen**: Jeder Eigenname einer Weltentität (SCs, NSCs, Fraktionen, Häuser, Städte, Orte, magische Gegenstände, Bräuche, Feste, Ereignisse …), der im erzeugten Text vorkommt, muss eine **Markdown-Verknüpfung** zur kanonischen `.md`-Datei der Entität sein (z. B. `[Name](relativer/pfad/datei.md)`), niemals bloßer Klartext. Ausnahmen: Überschriften, Dateinamen, Frontmatter, Codeblöcke, Mermaid-Knoten und `.mw`-Quellen. Entität ohne Bogen: niemals erfinden — `[VOM_SL_ZU_DEFINIEREN: Bogen fehlt für <Name>]` verwenden und die Lücke melden. Prüfung und Umwandlung: Skill `eigennamen-verlinken`.

---

## 1. Diagnose- und Prüfkriterien

Der Skill überprüft die fünf Säulen der strukturellen Integrität:

### A. Konformität der zehn Bände
Prüft das Vorhandensein der kanonischen Verzeichnisse (wobei gleichwertige etablierte oder vom SL angepasste Benennungen im Repository akzeptiert werden):
1. `01_kosmologie` *(mit optionalen benutzerdefinierten Unterordnern für Ebenen/Sphären und Pantheon/Gottheiten)*
2. `02_geografie` *(mit optionalem Unterordner `regionen/` oder benutzerdefiniertem Namen für Großgebiete, z. B. `provinzen/`, `kontinente/`, `domaenen/`)*
3. `03_gesellschaft_und_politik` *(mit optionalem Unterordner `voelker/` oder eigenem Namen sowie dem Pflicht-Unterordner `braeuche_feste_und_ereignisse/` samt `braeuche/`, `feste_und_vorkommnisse/`, `ereignisse/`)*
4. `04_recht_und_gesetze` *(mit Unterordnern `01_rechtsordnung_und_quellen/` … `10_kriegsrecht_und_abenteurer/`, plus etwaigen Zusatzgebieten `11_+` oder Unterordnern nach Gerichtsbarkeit)*
5. `05_charaktere` *(mit `<Spielercharaktere>/` [Standard `Spielercharaktere/`, z. B. `SCs/`, `Helden/`], gruppiert nach `<Kampagne_oder_Gruppe>/`, und `<Nichtspielercharaktere>/` [Standard `Nichtspielercharaktere/`, z. B. `NSCs/`] samt optionalen Gruppierungs-Unterordnern)*
6. `06_orte` *(mit optionalen benutzerdefinierten Unterordnern `<ortsgruppen>/` nach Typ oder Großgebiet)*
7. `07_fraktionen` *(mit optionalen benutzerdefinierten Unterordnern `<fraktionsgruppen>/` nach Typ)*
8. `08_besondere_magische_gegenstaende` *(oder eigenem Namen für Band VIII, z. B. `08_magische_gegenstaende/`, `08_artefakte_und_relikte/`, mit optionalen Unterordnern `<kategorien>/`)*
9. `09_chroniken` *(mit `<kampagnen>/` [Standard `kampagnen/`, z. B. `expeditionen/`, `abenteuer/`, `one_shots/`] und `<sitzungen>/` [Standard `sitzungen/`, z. B. `tagebuecher/`, `kapitel/`])*
10. `10_zeitlinie` (mit Unterordnern `historische_chronologie/`, `vorkommnisregister/`, `markwhen/`, `kalender/`, `exporte/`)

### B. Vorhandensein & Gültigkeit der Indizes (`README.md`)
Prüft, ob jeder Haupt- und Unterordner eine funktionierende `README.md` besitzt, die als Hub und Abschnittsindex dient.

### C. Erkennung defekter Markdown-Links
Durchsucht relative Links in `.md`-Dateien (z. B. `[Name](../../05_charaktere/...)`), um zu verifizieren, dass die Zieldateien tatsächlich auf der Festplatte existieren, und meldet fehlerhafte Pfade oder unsynchronisierte Umbenennungen.

### D. Verwaiste oder fehlplatzierte Dateien
Erkennt `.md`-Dateien im Wurzelverzeichnis oder an nicht-kanonischen Pfaden, die in einen der zehn Bände gehören (ausgenommen kanonische Masterdateien im Wurzelverzeichnis wie `README.md`, `AGENTS.md`, `CLAUDE.md`, `WELTENBIBEL.md`, `PRUEFUNGSSTATUS.md`). Für die syntaktische und übergreifende Validierung von `.mw`-Quellen unter `10_zeitlinie/markwhen/` arbeitet der Skill mit `timeline-markwhen` (`mw-validieren`) zusammen.

### E. Abdeckung verknüpfter Eigennamen
Prüft, ob jeder Eigenname einer erfassten Entität (SCs, NSCs, Fraktionen, Häuser, Städte, Orte, magische Gegenstände, Bräuche, Feste, Ereignisse …) im Text als **Markdown-Link** auf die kanonische `.md`-Datei der Entität erscheint und nicht als bloßer Klartext (Regel der verknüpften Eigennamen, vorbehaltlich der festgelegten Ausnahmen). Die eingehende Analyse und Umwandlung werden der Skill `eigennamen-verlinken` übertragen, deren oberflächliche Diagnosekontrolle dieser Pfeiler darstellt.

---

## 2. Operatives Verfahren

1. **Dateisystem-Scan**:
   - Untersuche Ordner und `.md`-Dateien im Workspace unter Ausschluss technischer Verzeichnisse (`.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Durchführung der Tests A–E**:
   - Prüfe die Verzeichnisse der 10 Bände und deren kanonische, optionale oder angepasste Unterordner (`<ebenen>/`, `<pantheon>/`, `<regionen>/`, `voelker/`, `braeuche_feste_und_ereignisse/`, `04_recht_und_gesetze/`, `05_charaktere/`, `<ortsgruppen>/`, `<fraktionsgruppen>/`, `<kategorien>/`, `<kampagnen>/<sitzungen>/` und `10_zeitlinie/`).
   - Prüfe auf fehlende `README.md`-Dateien.
   - Analysiere `[Text](pfad)`-Links und verifiziere die Existenz der Zieldatei über den relativen Pfad.
   - Prüfe das Wurzelverzeichnis auf verwaiste Dateien.
   - Prüfe, ob Eigennamen erfasster Entitäten als Links und nicht als Klartext erscheinen (eingehende Analyse an `eigennamen-verlinken` delegieren).
3. **Erstellung des Diagnoseberichts**:
   - Zeige dem SL eine übersichtliche Zusammenfassung:
     - 🟢 **Verzeichnisbaum-Konformität**: [OK / Hinweise auf fehlende Bände]
     - 🟢 **README-Index-Abdeckung**: [OK / Liste der Ordner ohne README]
     - 🔗 **Link-Integrität**: [OK / Liste defekter Links mit Datei und Zeile]
     - 🏷️ **Verknüpfte Eigennamen**: [OK / Liste nicht verknüpfter Namen mit Datei und Zeile]
     - 📂 **Dateiplatzierung**: [OK / Verwaiste Dateien mit Verschiebungsvorschlag]
4. **Vorschlag zur automatischen Reparatur**:
   - Werden Abweichungen entdeckt, frage den SL (über das strukturierte Fragewerkzeug der Umgebung wie `vscode_askQuestions` / `AskUserQuestion`, falls verfügbar; sonst im Chat), wie verfahren werden soll:
     - `Abweichungen automatisch beheben (fehlende READMEs erzeugen und Pfade korrigieren)`
     - `Nur Bericht anzeigen, keine Dateien ändern`
