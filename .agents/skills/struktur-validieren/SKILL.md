---
name: struktur-validieren
description: "Use when: die strukturelle Integrität eines D&D-Welt-Repositories prüfen, fehlende Ordner, abwesende README-Indizes, defekte Markdown-Links und fehlplatzierte Dateien erkennen."
argument-hint: "Führt die strukturelle Konformitätsprüfung des Archivs aus"
user-invocable: true
disable-model-invocation: false
---

# Skill: Validierung der Weltstruktur (`struktur-validieren`)

Dieser Skill führt ein gründliches Diagnose-Audit des Verzeichnisbaums im Repository durch, stellt die Konformität mit der standardisierten D&D-Architektur sicher und deckt technische Abweichungen frühzeitig auf.

---

## 1. Diagnose- und Prüfkriterien

Der Skill überprüft die vier Säulen der strukturellen Integrität:

### A. Konformität der zehn Bände
Prüft das Vorhandensein der kanonischen Verzeichnisse (wobei gleichwertige bereits etablierte Benennungen in bestehenden Repositories akzeptiert werden):
1. `01_kosmologie`
2. `02_geografie`
3. `03_gesellschaft_und_politik` (mit Unterordner `braeuche_feste_und_ereignisse/` samt `braeuche/`, `feste_und_vorkommnisse/`, `ereignisse/`)
4. `04_recht_und_erbfolge`
5. `05_charaktere` (mit Unterordnern `Spielercharaktere/` und `Nichtspielercharaktere/`)
6. `06_orte`
7. `07_fraktionen`
8. `08_besondere_magische_gegenstaende`
9. `09_chroniken` (mit Unterordner `kampagnen/`)
10. `10_zeitlinie` (mit Unterordnern `historische_chronologie/`, `vorkommnisregister/`, `markwhen/`, `kalender/`, `exporte/`)

### B. Vorhandensein & Gültigkeit der Indizes (`README.md`)
Prüft, ob jeder Haupt- und Unterordner eine funktionierende `README.md` besitzt, die als Hub und Abschnittsindex dient.

### C. Erkennung defekter Markdown-Links
Durchsucht relative Links in `.md`-Dateien (z. B. `[Name](../../05_charaktere/...)`), um zu verifizieren, dass die Zieldateien tatsächlich auf der Festplatte existieren, und meldet fehlerhafte Pfade oder unsynchronisierte Umbenennungen.

### D. Verwaiste oder fehlplatzierte Dateien
Erkennt `.md`-Dateien im Wurzelverzeichnis oder an nicht-kanonischen Pfaden, die in einen der zehn Bände gehören (ausgenommen kanonische Masterdateien im Wurzelverzeichnis wie `README.md`, `AGENTS.md`, `CLAUDE.md`, `WELTENBIBEL.md`, `PRUEFUNGSSTATUS.md`). Für die syntaktische und übergreifende Validierung von `.mw`-Quellen unter `10_zeitlinie/markwhen/` arbeitet der Skill mit `timeline-markwhen` (`mw-validieren`) zusammen.

---

## 2. Operatives Verfahren

1. **Dateisystem-Scan**:
   - Untersuche Ordner und `.md`-Dateien im Workspace unter Ausschluss technischer Verzeichnisse (`.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Durchführung der Tests A–D**:
   - Prüfe die Verzeichnisse der 10 Bände (inklusive der Unterordner in `braeuche_feste_und_ereignisse/` und `10_zeitlinie/`).
   - Prüfe auf fehlende `README.md`-Dateien.
   - Analysiere `[Text](pfad)`-Links und verifiziere die Existenz der Zieldatei über den relativen Pfad.
   - Prüfe das Wurzelverzeichnis auf verwaiste Dateien.
3. **Erstellung des Diagnoseberichts**:
   - Zeige dem SL eine übersichtliche Zusammenfassung:
     - 🟢 **Verzeichnisbaum-Konformität**: [OK / Hinweise auf fehlende Bände]
     - 🟢 **README-Index-Abdeckung**: [OK / Liste der Ordner ohne README]
     - 🔗 **Link-Integrität**: [OK / Liste defekter Links mit Datei und Zeile]
     - 📂 **Dateiplatzierung**: [OK / Verwaiste Dateien mit Verschiebungsvorschlag]
4. **Vorschlag zur automatischen Reparatur**:
   - Werden Abweichungen entdeckt, frage den SL (über das strukturierte Fragewerkzeug der Umgebung wie `vscode_askQuestions` / `AskUserQuestion`, falls verfügbar; sonst im Chat), wie verfahren werden soll:
     - `Abweichungen automatisch beheben (fehlende READMEs erzeugen und Pfade korrigieren)`
     - `Nur Bericht anzeigen, keine Dateien ändern`
