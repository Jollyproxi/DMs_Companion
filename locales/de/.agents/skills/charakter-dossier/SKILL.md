---
name: charakter-dossier
description: "Use when: sechsteilige Spielercharakter-(SC-)Dossiers oder Nichtspielercharakter-(NSC-)Bögen gemäß den kanonischen Kampagnenstandards erstellen, aktualisieren oder modularisieren."
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

## 2. Erstellung eines SC-Dossiers (6 Module)

Wenn der SL einen neuen Spielercharakter einführt oder dokumentiert:

1. **Geführte Erfassung (bei Bedarf)**: Bestätige mit dem SL den genauen Namen, die Klasse, Stufe und zugehörige Kampagne/Gruppe.
2. **Ordneranlage**:
   `05_charaktere/<Spielercharaktere>/<Kampagne_oder_Gruppe>/<SC_Name>/` *(Standard: `05_charaktere/Spielercharaktere/<Kampagne>/<SC_Name>/`, unter Wahrung benutzerdefinierter Ordnernamen im Workspace)*
3. **Erzeugung der modularen Dateien**:
   - `README.md`: Charakter-Hub mit Rolle, moralischen Zügen und Index der 6 Dateien.
   - `01_stammdaten_und_merkmale.md`: Stammdaten, Klasse, Stufe, Merkmale und Erscheinungsbild.
   - `02_integrierter_hintergrund.md`: Vergangenheit, Wendepunkte und Verwurzelung in der Welt.
   - `03_beziehungen_und_dynamiken.md`: Bindungen zu Gefährten, Fraktionen und NSCs.
   - `04_ausruestung_und_faehigkeiten.md`: Charakteristische Gegenstände, Waffen, Fokusse und besondere Fähigkeiten.
   - `05_geruechte_und_ueberzeugungen.md` — Gerüchte und Überzeugungen.
   - `06_sl_aufhaenger_und_geheimnisse.md`: Dem SL vorbehaltene Aufhänger, Rätsel und Enthüllungen.
4. **Aufbau**:
   - Kopfbereich mit Rolle, Fraktion (Link zu Band VII `07_fraktionen/`), Wohnort (Link zu Band VI `06_orte/`), Gesinnung und Lebensstatus.
   - Abschnitte zu Erscheinung & Wesen, Narrativer Rolle und Geheimnissen & SL-Aufhängern.
   - **Aktualisierung von Kampagnen- und Gruppen-Hub**:
   Füge den neuen SC der `README.md` in `05_charaktere/<Spielercharaktere>/<Kampagne_oder_Gruppe>/README.md` sowie dem Gesamtindex `05_charaktere/README.md` hinzu.

---

## 3. Erstellung oder Aktualisierung eines NSC-Bogens

## Ablagekonvention für NSC

Wende die NSC-Ablagekonvention des Projekts an. Lies die Projektanweisungen und den Index des Charakterbands. Bei bestehenden Projekten ohne ausdrückliche Regel folge der vorhandenen Ablage und ihren Indizes und melde der SL Widersprüche oder Unklarheiten.

Suche den vorhandenen Bogen in Indizes und Dateien sowie anhand etwaiger Aliasnamen. Führe eine kanonische Datei je Identität und verlinke sie aus Kampagnen, Fraktionen und anderen Orten. Verwende für geografische oder erzählerische Ebenen die belegte dauerhafte Bindung und halte ihre Grundlage fest. Erstbegegnung (Ort und Protokoll) und aktueller Aufenthaltsort sind getrennte Felder.

Markiere ungeklärte Angaben und erhalte bestätigte Ebenen. Verwende einen vorläufigen Ablageort, sofern das Projekt ihn vorsieht, und frage andernfalls die SL nach der hierarchischen Zuordnung. Nutze Kategorien für reisende oder bereichsübergreifende NSC nur, wenn Projekt und Kanon sie stützen. Erfasse diese Angaben bei flacher Ablage wie vereinbart im Bogen oder Index.

Ordne vor einer genehmigten Verschiebung jedem Quellpfad einen Zielpfad zu und prüfe, ob das Ziel frei ist. Aktualisiere alte und neue Indizes, alle eingehenden Verweise und ausgehende relative Links. Erhalte die Historie der Erstbegegnung, aktualisiere die vorgesehenen abgeleiteten Dokumente und prüfe kanonische Linkziele sowie die Eindeutigkeit des Bogens.

Dante behält `<Cornice>/<Luogo_riferimento>/<Nome_PNG>.md` unter seinem NSC-Stammordner.

Nutze die [Vorlage](./references/dossier-vorlage.md) und aktualisiere die vorgesehenen Indizes.

---

## 4. Querverknüpfte Aktualisierungen nach einer Sitzung

Bringt eine Sitzung Neuigkeiten für einen SC (z. B. neu entdeckter Aufhänger, veränderte Bindung, Wunde oder erhaltener Gegenstand):
1. Ermittle das konkret betroffene Modul (z. B. `03_beziehungen_und_dynamiken.md` für einen Pakt, `06_sl_aufhaenger_und_geheimnisse.md` für eine aufgedeckte Spur).
2. Nimm die Ergänzung vor und bewahre bisherige Informationen.
3. Setze `Geändert: [HEUTIGES_DATUM]` weiter, während `Geprüft` unverändert bleibt.

Erhalte bei bestehenden Dossiers den Inhalt der Aufhänger, benenne das bisherige Modul 05 in 06 um, lege das neue Modul 05 an und aktualisiere Index und eingehende Links einschließlich Sprungmarken. Existiert 06 bereits, vergleiche vor dem Verschieben die Inhalte. Prüfe die Links auch bei wiederholter Ausführung.

## Klatsch und Gerüchte

Fasse für jede belegte Rolle die Version in einem Stichpunkt mit relativem Link zusammen. Ergänze die Haltung, soweit dokumentiert.
