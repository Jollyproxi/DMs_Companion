# Konventionen zur Kompilierung der Weltenbibel

Die Weltenbibel (`WELTENBIBEL.md` oder ein erweiterter im Workspace gewählter Titel) ist das monolithische narrative Masterdokument der Welt. Sie vereint das gesamte über die zehn Bände verteilte Wissen in einer fließenden, durchgehenden und durchsuchbaren Reihenfolge.

---

## 1. Titelblatt & Metadaten

Am Dateianfang steht der kanonische Kopfbereich:

```markdown
### WELTENBIBEL: [WELTNAME]

> 📜 **Monolithisches Masterdokument des Kanons**  
> *Kanon-Version:* [VERSION] | *Letzte Kompilierung:* [HEUTIGES_DATUM]  
> 🛡️ *Geprüft: [DATUM_G] | Geändert: [DATUM_A]*

---
```

---

## 2. Überschriftenhierarchie (Ebenen-Zuordnung)

Da das Dokument viele Bände und verschachtelte Module bündelt, werden die Überschriften einzelner `.md`-Dateien nach folgender kanonischer Skala übertragen:

| Ebene im atomaren Modul | Ebene in der Master-Bibel | Beispielformat |
| :--- | :--- | :--- |
| **Bandtitel (aus README)** | Ebene 5 (`#####`) | `##### 1. Kosmologie & Metaphysische Architektur` |
| **Modultitel (`# Titel`)** | Ebene 6 Kursiv (`###### *...*`) oder `### X.Y` | `###### *1.1 Ebenenstruktur und Kosmos*` |
| **Interner Abschnitt (`## Abschnitt`)** | Überschrift `###` oder `####` | `### Elementarebenen und Schwellenlande` |
| **Unterabschnitt (`### Unter`)** | Fettgedruckter Punkt oder `#####` | `* **Astralhof:** ...` |

> **Kontinuitätshinweis**: Enthält der Workspace bereits eine Master-Bibeldatei, übernimm exakt den dort bereits verwendeten Überschriftenstil.

---

## 3. Sequenzielle Kompilierungsreihenfolge der Bände

Die Kompilierung folgt streng der kanonischen Nummerierung:

1. **##### 1. Kosmologie & Metaphysische Architektur** (`01_kosmologie/`)
   - `01_ebenenstruktur.md`
   - `02_jahreszeiten_und_himmelsmechanik.md`
   - `03_magiefluss_und_goettliche_ordnung.md`
   - `04_moralisches_oder_philosophisches_system.md`
   - Optionale benutzerdefinierte Unterordner (`<ebenen>/`, `<pantheon>/`).
2. **##### 2. Physische, Territoriale & Umweltbezogene Geografie** (`02_geografie/`)
   - Hauptmodule zu Geografie, Karte, Unterreich und Schwellenebenen.
   - Einzelne Regionen oder Großgebiete im zugehörigen Unterordner (`regionen/` oder benutzerdefinierter Ordnername im Workspace) in aufsteigender Reihenfolge.
3. **##### 3. Gesellschafts-, Politik- & Wirtschaftsordnung** (`03_gesellschaft_und_politik/`)
   - Gesellschaftsmodelle, Wirtschaft, Schichten, öffentliche Ordnung und Sicherheitskräfte.
   - Optionaler Unterordner `voelker/` (oder eigener Name für Spezies/Rassen/Abstammungen/Kulturen, Codes `3.8.x`).
   - Unterserie `braeuche_feste_und_ereignisse/`: Bräuche (`3.5.x`), Feste/Vorkommnisse (`3.6.x`), einmalige Ereignisse (`3.7.x`), jeweils aufsteigend nummeriert.
4. **##### 4. Recht & Gesetze** (`04_recht_und_gesetze/`)
   - Rechtsordnung und Quellen (`4.1.x`), Bürgerrechte und Status (`4.2.x`), dynastisches Recht und Erbfolge (`4.3.x`), Verträge und Pakte (`4.4.x`), Abkommen und Diplomatie (`4.5.x`), Strafrecht und Delikte (`4.6.x`), Gerichte und Verfahren (`4.7.x`), arkanes und religiöses Recht (`4.8.x`), Eigentum, Handel und Steuern (`4.9.x`), Kriegsrecht und Abenteurer (`4.10.x`), plus etwaige Zusatzgebiete (`4.11.x+`) oder Unterordner nach Gerichtsbarkeit, jeweils mit allgemeinem Rahmen (`4.Y.1`) und erfassten Rechtsakten (`4.Y.2+`) in aufsteigender Reihenfolge.
5. **##### 5. Charakterverzeichnis der Welt** (`05_charaktere/`)
   - Bedeutsame NSCs (`<Nichtspielercharaktere>/`, mit etwaigen angepassten Gruppierungs-Unterordnern), gruppiert nach Fraktion oder Region.
   - Zusammenfassung der Gruppenbindungen, falls eine kanonische Kampagne/Gruppe existiert.
6. **##### 6. Atlas der Orte & Abenteuerknoten** (`06_orte/`)
   - Bedeutende Orte, Festungen, Städte und Portale (auch gruppiert in optionalen Unterordnern `<ortsgruppen>/`).
7. **##### 7. Geopolitisches Register der Fraktionen & Häuser** (`07_fraktionen/`)
   - Satzungen, Hierarchien und Rivalitäten herrschender Mächte (auch gruppiert in optionalen Unterordnern `<fraktionsgruppen>/`).
8. **##### 8. Register besonderer magischer Gegenstände & Relikte** (`<08_besondere_magische_gegenstaende>/` oder angepasster Bandname)
   - Einzigartige Artefakte, Geschichte, Rechtsstatus und besondere Mechaniken (auch unterteilt in optionale Unterordner `<kategorien>/`).
9. **##### 9. Historische Chroniken & Kampagnen-Kompendium** (`09_chroniken/`)
   - Übersicht aktiver Kampagnen/Expeditionen (`<kampagnen>/`) und fortlaufende Sitzungsprotokolle (`<sitzungen>/`).
10. **##### 10. Zeitlinie & Weltchronologie** (`10_zeitlinie/`)
    - Historische Chronologie (`10.1.x`, Dateien nach Epoche/Zeitraum), Vorkommnisregister (`10.2.x`, Dateien nach Epoche/Zeitraum) und Kalender (`10.3.x`).
    - Markwhen-Quellen (`markwhen/*.mw`) und grafische Exporte (`exporte/`) sind **von der Bibel ausgeschlossen**: sie bleiben ausschließlich in `weltstruktur.json` indiziert.
    - Interne Einträge verwenden dieselbe Markwhen-Tag-Taxonomie (z. B. `#brauch #fest #ereignis #vorkommnis`), um mit der grafischen Zeitlinie synchron zu bleiben.

---

## 4. Behandlung von Tabellen, Diagrammen & SL-Hinweisen

1. **Markdown-Tabellen**: Werden vollständig übernommen, wobei auf intakte Spaltentrennung `| :--- | :--- |` ohne umgebrochene Zeilen zu achten ist.
2. **Mermaid-Diagramme**: Bleiben in ihren jeweiligen ```` ```mermaid ````-Blöcken mit gültiger Knotensyntax erhalten.
3. **SL-Hinweise**: Kästen mit `**HINWEIS FÜR DEN SPIELLEITER:**` oder `> ⚠️ **SL-Hinweis:**` werden als hervorgehobene Zitate (`> ...`) bewahrt, um den Spielleitungskontext zu sichern.
4. **Unvollständige Platzhalter**: Alle `[VOM_SL_ZU_DEFINIEREN: ...]`-Markierungen werden originalgetreu übernommen, ohne Inhalte hinzuzudichten.

---

## 5. Regeln für inkrementelle Aktualisierungen (`Bibel-aktualisieren`)

Im inkrementellen Modus gilt:
1. Nicht das gesamte Masterdokument neu schreiben.
2. Die exakte Überschrift des geänderten Moduls lokalisieren (über Code `X.Y` oder Titel).
3. Den Block zwischen dem Beginn des Modulabschnitts und dem Beginn des nächsten Moduls ersetzen.
4. Handelt es sich um ein neues Modul, es am Ende seines Bandes gemäß der numerischen Reihenfolge einfügen.
5. Die Metadatenzeile im Kopf auf das heutige Datum aktualisieren: `Geändert: [HEUTIGES_DATUM]`.
