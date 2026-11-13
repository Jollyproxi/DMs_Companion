---
name: welt-initialisieren
description: "Use when: ein neues D&D-Welt- oder Kampagnen-Repository initialisieren, den Spielleiter durch die Festlegung der Weltkoordinaten führen und die modulare Zehn-Bände-Architektur erzeugen."
argument-hint: "Startet das Interview zur Konfiguration und Erstellung des Welt-Verzeichnisbaums"
user-invocable: true
disable-model-invocation: false
---

# Skill: Initialisierung einer Spielwelt (`welt-initialisieren`)

Dieser Skill begleitet den Spielleiter bei der interaktiven Konfiguration und Erstellung der Ordnerstruktur einer Fantasy-Spielwelt gemäß der standardisierten Zehn-Bände-Architektur aus [weltarchitektur](./references/weltarchitektur.md).

> **📌 Regel: Eigennamen als Verknüpfungen**: Jeder Eigenname einer Weltentität (SCs, NSCs, Fraktionen, Häuser, Städte, Orte, magische Gegenstände, Bräuche, Feste, Ereignisse …), der im erzeugten Text vorkommt, muss eine **Markdown-Verknüpfung** zur kanonischen `.md`-Datei der Entität sein (z. B. `[Name](relativer/pfad/datei.md)`), niemals bloßer Klartext. Ausnahmen: Überschriften, Dateinamen, Frontmatter, Codeblöcke, Mermaid-Knoten und `.mw`-Quellen. Entität ohne Bogen: niemals erfinden — `[VOM_SL_ZU_DEFINIEREN: Bogen fehlt für <Name>]` verwenden und die Lücke melden. Prüfung und Umwandlung: Skill `eigennamen-verlinken`.

---

## 1. Geführtes Verfahren (Erstinterview)

Stelle dem SL vor dem Anlegen von Dateien oder Ordnern folgende Fragen (mit dem strukturierten Fragewerkzeug der Umgebung wie `vscode_askQuestions` oder `AskUserQuestion`, falls verfügbar; sonst direkt im Chat):

1. **`name_praemisse`**: *Wie heißt die Spielwelt und was ist ihr zentrales Leitmotiv?*
   - Vorgeschlagene Optionen oder Freitext (z. B. *Klassische High Fantasy*, *Gotische Dark Fantasy*, *Politische & Arkane Intrigen*, *Sonstiges — angeben*).
2. **`ebenen_besonderheiten`**: *Welche kosmologischen Besonderheiten oder speziellen Ebenen prägen die Welt?*
   - Mehrfachauswahl: *Unterreich / Tiefe Abgründe*, *Liminal-Ebenen / Nebelreiche*, *Feen- oder Astralreiche*, *Himmelssphären / Elementarebenen*, *Sonstiges (angeben)*.
3. **`schluesselfraktionen`**: *Welches sind zu Beginn die 2–3 prägenden Fraktionen, Adelshäuser oder Reiche?* (Freitext).
4. **`erste_kampagne`**: *Möchtest du direkt eine erste Kampagne samt SC-Gruppe anlegen?*
   - Optionen: *Ja (Kampagnennamen angeben)*, *Nein (vorerst nur die Spielwelt)*.
5. **`braeuche_feste_ereignisse`**: *Gibt es bereits Alltagsbräuche, wiederkehrende Feste oder historische Ereignisse, die direkt erfasst werden sollen?*
   - Mehrfachauswahl: *Bräuche (z. B. Gruß-/Abschiedsrituale)*, *Wiederkehrende Feste/Ereignisse*, *Einmalige Ereignisse (historisch oder laufend)*, *Vorerst keine (nur Struktur)*.
   - Erfasste Einträge werden mit dem Skill `brauch-fest-ereignis` unter `03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/` katalogisiert und in `10_zeitlinie/` eingetragen.
6. **`ordner_grossgebiete`**: *Wie soll der Unterordner für Regionen/Großgebiete in `02_geografie/` heißen?*
   - Vorgeschlagene Optionen oder eigener Name (z. B. *`regionen/`* Standard, *`provinzen/`*, *`kontinente/`*, *`domaenen/`*, *`marken/`*, *Sonstiges — Ordnername angeben*).
7. **`unterordner_voelker`**: *Möchtest du unter `03_gesellschaft_und_politik/` den optionalen Unterordner für Völker/Spezies anlegen?*
   - Optionen: *Ja, Standard `voelker/` verwenden*, *Ja, mit eigenem Namen (z. B. `spezies/`, `rassen/`, `abstammungen/`, `kulturen/`)*, *Nein (nur bei späterem Bedarf)*.
8. **`erweiterte_anpassung`**: *Möchtest du für die übrigen Bände die Standardnamen nutzen oder Ordner anpassen bzw. optionale Unterordner aktivieren?*
   - Optionen: *Standardnamen und -struktur verwenden* (empfohlen), *Auf Wunsch anpassen* — falls gewählt, frage den SL nach den gewünschten Anpassungen (aus: `<ebenen>/` und `<pantheon>/` in `01_kosmologie/`; zusätzliche Rechtsgebiete `11_+` oder Gerichtsbarkeiten in `04_recht_und_gesetze/`; Namen `Spielercharaktere/`/`Nichtspielercharaktere/`, SC-Gruppierung nach Kampagne oder Gruppe und `<nsc_gruppen>/` in `05_charaktere/`; `<ortsgruppen>/` in `06_orte/`; `<fraktionsgruppen>/` in `07_fraktionen/`; Band-VIII-Name `08_...` und `<kategorien>/`; `<kampagnen>/` und `<sitzungen>/` in `09_chroniken/`).

---

## 2. Erstellung des Verzeichnisbaums

Erzeuge nach Erhalt der Antworten des SL die modulare Struktur mithilfe der Schreibwerkzeuge oder des Terminals:

1. **Wurzeldateien**:
   - `README.md`: Allgemeines Weltverzeichnis und Navigationsübersicht.
   - `weltstruktur.json`: Hierarchisches Schema mit Metadaten, Bänden und Ordnern.
   - `WELTENBIBEL.md`: Master-Quelldokument mit der vereinbarten Prämisse.

2. **Die zehn Gründungsbände**:
   - `01_kosmologie/README.md` (mit optionalen Unterordnern `<ebenen>/`, `<pantheon>/` falls gewählt, jeweils mit `README.md`)
   - `02_geografie/README.md` (mit Unterordner für Großgebiete: `regionen/` oder dem vom SL gewählten benutzerdefinierten Namen, jeweils mit `README.md`)
   - `03_gesellschaft_und_politik/README.md` (mit optionalem Unterordner `voelker/` oder eigenem Namen falls gewählt, sowie Unterordner `braeuche_feste_und_ereignisse/` samt `braeuche/`, `feste_und_vorkommnisse/`, `ereignisse/`, jeweils mit `README.md`)
   - `04_recht_und_gesetze/README.md` (mit Unterordnern `01_rechtsordnung_und_quellen/`, `02_buergerrechte_und_status/`, `03_dynastisches_recht_und_erbfolge/`, `04_vertraege_und_pakte/`, `05_abkommen_und_diplomatie/`, `06_strafrecht_und_delikte/`, `07_gerichte_und_verfahren/`, `08_arkanes_und_religioeses_recht/`, `09_eigentum_handel_und_steuern/`, `10_kriegsrecht_und_abenteurer/`, plus etwaige Zusatzgebiete `11_+` oder Gerichtsbarkeits-Unterordner, jeweils mit `README.md`)
   - `05_charaktere/README.md` (mit `<Spielercharaktere>/` [Standard `Spielercharaktere/`] und `<Nichtspielercharaktere>/` [Standard `Nichtspielercharaktere/`] sowie optional `<nsc_gruppen>/`, jeweils mit `README.md`)
   - `06_orte/README.md` (mit optionalen Unterordnern `<ortsgruppen>/` falls gewählt, jeweils mit `README.md`)
   - `07_fraktionen/README.md` (mit optionalen Unterordnern `<fraktionsgruppen>/` falls gewählt, jeweils mit `README.md`)
   - `<08_besondere_magische_gegenstaende>/README.md` (Standard `08_besondere_magische_gegenstaende/` oder eigener Name, mit optionalen Unterordnern `<kategorien>/` falls gewählt, jeweils mit `README.md`)
   - `09_chroniken/README.md` (mit `<kampagnen>/<kampagnenname>/<sitzungen>/` — Standard `kampagnen/` und `sitzungen/` — jeweils mit `README.md`)
   - `10_zeitlinie/README.md` (mit Unterordnern `historische_chronologie/`, `vorkommnisregister/`, `markwhen/` — samt `README.md`, `allgemeine_zeitlinie.mw`, `epochen/`, `kampagnen/` —, `kalender/`, `exporte/README.md`)

3. **Initialisierung der README-Dateien**:
   Jeder Ordner erhält eine `README.md` mit thematischem Eingangsindex und Status-Badge:
   `> 🛡️ *Geprüft: [HEUTIGES_DATUM] | Geändert: [HEUTIGES_DATUM]*`

4. **Abschließende Validierung**:
   Rufe nach Abschluss der Erstellung den Skill `struktur-validieren` auf, um sicherzustellen, dass der Verzeichnisbaum vollständig und frei von defekten Links ist.
