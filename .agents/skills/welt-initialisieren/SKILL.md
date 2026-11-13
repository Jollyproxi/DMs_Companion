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

---

## 2. Erstellung des Verzeichnisbaums

Erzeuge nach Erhalt der Antworten des SL die modulare Struktur mithilfe der Schreibwerkzeuge oder des Terminals:

1. **Wurzeldateien**:
   - `README.md`: Allgemeines Weltverzeichnis und Navigationsübersicht.
   - `weltstruktur.json`: Hierarchisches Schema mit Metadaten, Bänden und Ordnern.
   - `WELTENBIBEL.md`: Master-Quelldokument mit der vereinbarten Prämisse.

2. **Die zehn Gründungsbände**:
   - `01_kosmologie/README.md`
   - `02_geografie/README.md` (mit optionalem Unterordner `regionen/` oder der gewählten Bezeichnung für Großgebiete)
   - `03_gesellschaft_und_politik/README.md` (mit Unterordner `braeuche_feste_und_ereignisse/` samt `braeuche/`, `feste_und_vorkommnisse/`, `ereignisse/`, jeweils mit `README.md`)
   - `04_recht_und_gesetze/README.md` (mit Unterordnern `01_rechtsordnung_und_quellen/`, `02_buergerrechte_und_status/`, `03_dynastisches_recht_und_erbfolge/`, `04_vertraege_und_pakte/`, `05_abkommen_und_diplomatie/`, `06_strafrecht_und_delikte/`, `07_gerichte_und_verfahren/`, `08_arkanes_und_religioeses_recht/`, `09_eigentum_handel_und_steuern/`, `10_kriegsrecht_und_abenteurer/`, jeweils mit `README.md`)
   - `05_charaktere/README.md` (mit Unterordnern `Spielercharaktere/` und `Nichtspielercharaktere/`, jeweils mit `README.md`)
   - `06_orte/README.md`
   - `07_fraktionen/README.md`
   - `08_besondere_magische_gegenstaende/README.md`
   - `09_chroniken/README.md` (mit Unterordnern `kampagnen/<kampagnenname>/sitzungen/`, jeweils mit `README.md`)
   - `10_zeitlinie/README.md` (mit Unterordnern `historische_chronologie/`, `vorkommnisregister/`, `markwhen/` — samt `README.md`, `allgemeine_zeitlinie.mw`, `epochen/`, `kampagnen/` —, `kalender/`, `exporte/README.md`)

3. **Initialisierung der README-Dateien**:
   Jeder Ordner erhält eine `README.md` mit thematischem Eingangsindex und Status-Badge:
   `> 🛡️ *Geprüft: [HEUTIGES_DATUM] | Geändert: [HEUTIGES_DATUM]*`

4. **Abschließende Validierung**:
   Rufe nach Abschluss der Erstellung den Skill `struktur-validieren` auf, um sicherzustellen, dass der Verzeichnisbaum vollständig und frei von defekten Links ist.
