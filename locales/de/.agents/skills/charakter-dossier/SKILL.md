---
name: charakter-dossier
description: "Use when: fünfteilige Spielercharakter-(SC-)Dossiers oder Nichtspielercharakter-(NSC-)Bögen gemäß den kanonischen Kampagnenstandards erstellen, aktualisieren oder modularisieren."
argument-hint: "Gib Typ (SC oder NSC), Charakternamen und Vorgang (erstellen, modul aktualisieren, bogen) an"
user-invocable: true
disable-model-invocation: false
---

# Skill: Verwaltung von Charakter-Dossiers (SC & NSC)

Dieser Skill regelt die Erstellung, Modularisierung und systematische Pflege der Dossiers für Spielercharaktere (SC) und der Bögen für Nichtspielercharaktere (NSC) unter Wahrung formaler Strenge, Querverlinkung und Kanontreue — ohne jemals vom Spielleiter nicht autorisierte Details zu erfinden.

Die vollständigen Vorlagen sind in [dossier-vorlage](./references/dossier-vorlage.md) verfügbar.

> **📌 Regel: Eigennamen als Verknüpfungen**: Jeder Eigenname einer Weltentität (SCs, NSCs, Fraktionen, Häuser, Städte, Orte, magische Gegenstände, Bräuche, Feste, Ereignisse …), der im erzeugten Text vorkommt, muss eine **Markdown-Verknüpfung** zur kanonischen `.md`-Datei der Entität sein (z. B. `[Name](relativer/pfad/datei.md)`), niemals bloßer Klartext. Ausnahmen: Überschriften, Dateinamen, Frontmatter, Codeblöcke, Mermaid-Knoten und `.mw`-Quellen. Entität ohne Bogen: niemals erfinden — `[VOM_SL_ZU_DEFINIEREN: Bogen fehlt für <Name>]` verwenden und die Lücke melden. Prüfung und Umwandlung: Skill `eigennamen-verlinken`.

---

## 1. Ausfüllregeln (Keine Halluzinationen)

- **Nur gesicherte Daten**: Fülle ausschließlich Felder aus, die vom SL vorgegeben oder bereits in Sitzungsprotokollen dokumentiert sind.
- **Fehlende Felder**: Füge `[VOM_SL_ZU_DEFINIEREN: fehlendes Element]` ein (z. B. noch nicht gewählte Unterklasse, Schutzgottheit oder unenthülltes SL-Geheimnis).
- **Strukturierte Interaktion**: Gibt der SL zu einem neuen Charakter nur Teilangaben an, erfrage die Kerndaten (Typ: SC oder NSC; Zielkampagne; Rolle im Kampf/Arkanen/Sozialen; Gesinnung oder Moralkodex) über das strukturierte Fragewerkzeug der Umgebung (`vscode_askQuestions`, `AskUserQuestion`), falls verfügbar; sonst direkt im Chat.
- **Zeitnachverfolgung**: Jede erstellte oder geänderte Datei bzw. jedes Modul enthält das Status-Badge:
  `> 🛡️ *Geprüft: JJJJ-MM-TT | Geändert: JJJJ-MM-TT*`
  Wird die Datei infolge einer Sitzung geändert, aktualisiere nur das Datum unter `Geändert`.

---

## 2. Erstellung eines SC-Dossiers (5 Module)

Wenn der SL einen neuen Spielercharakter einführt oder dokumentiert:

1. **Geführte Erfassung (bei Bedarf)**: Bestätige mit dem SL den genauen Namen, die Klasse, Stufe und zugehörige Kampagne.
2. **Ordneranlage**:
   `05_charaktere/Spielercharaktere/<Kampagne>/<SC_Name>/`
3. **Erzeugung der modularen Dateien**:
   - `README.md`: Charakter-Hub mit Rolle, moralischen Zügen und Index der 5 Dateien.
   - `01_stammdaten_und_merkmale.md`: Stammdaten, Klasse, Stufe, Merkmale und Erscheinungsbild.
   - `02_integrierter_hintergrund.md`: Vergangenheit, Wendepunkte und Verwurzelung in der Welt.
   - `03_beziehungen_und_dynamiken.md`: Bindungen zu Gefährten, Fraktionen und NSCs.
   - `04_ausruestung_und_faehigkeiten.md`: Charakteristische Gegenstände, Waffen, Fokusse und besondere Fähigkeiten.
   - `05_sl_aufhaenger_und_geheimnisse.md`: Dem SL vorbehaltene Aufhänger, Rätsel und Enthüllungen.
4. **Aktualisierung von Kampagnen- und Gruppen-Hub**:
   Füge den neuen SC der `README.md` in `05_charaktere/Spielercharaktere/<Kampagne>/README.md` sowie dem Gesamtindex `05_charaktere/README.md` hinzu.

---

## 3. Erstellung oder Aktualisierung eines NSC-Bogens

Wenn der SL einen bedeutsamen Nichtspielercharakter einführt:

1. **Geführte Erfassung**: Fehlen zentrale Angaben, kläre mit dem SL Fraktionszugehörigkeit, Lebensstatus und Aufenthaltsort.
2. **Pfad**:
   `05_charaktere/Nichtspielercharaktere/<NSC_Name>.md`
3. **Aufbau**:
   - Kopfbereich mit Rolle, Fraktion (Link zu `07_fraktionen/`), Wohnort (Link zu `06_orte/`), Gesinnung und Lebensstatus.
   - Abschnitte zu Erscheinung & Wesen, Narrativer Rolle und Geheimnissen & SL-Aufhängern.
4. **Aktualisierung des NSC-Index**:
   Füge den Eintrag in die Beziehungstabelle unter `05_charaktere/Nichtspielercharaktere/README.md` ein.

---

## 4. Querverknüpfte Aktualisierungen nach einer Sitzung

Bringt eine Sitzung Neuigkeiten für einen SC (z. B. neu entdeckter Aufhänger, veränderte Bindung, Wunde oder erhaltener Gegenstand):
1. Ermittle das konkret betroffene Modul (z. B. `03_beziehungen_und_dynamiken.md` für einen Pakt, `05_sl_aufhaenger_und_geheimnisse.md` für eine aufgedeckte Spur).
2. Nimm die Ergänzung vor und bewahre bisherige Informationen.
3. Setze `Geändert: [HEUTIGES_DATUM]` weiter, während `Geprüft` unverändert bleibt.
