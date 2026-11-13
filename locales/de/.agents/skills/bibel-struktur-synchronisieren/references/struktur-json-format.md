# Spezifikation und Format von `weltstruktur.json`

Die Datei `weltstruktur.json` bildet die maschinenlesbare ontologische und taxonomische Karte der gesamten Spielwelt. Sie dient als strukturierter Index für KI-Agenten, Visualisierungstools, Validierungsskripte und schnelle Abfragen.

---

## 1. Wurzelschema des Dokuments

```json
{
  "weltname": "Name der Spielwelt",
  "version": "1.0.0",
  "quelldokument": "WELTENBIBEL.md",
  "beschreibung": "Knappe Zusammenfassung der Grundpfeiler der Spielwelt in 2–3 Sätzen.",
  "struktur": [
    /* Array der 10 kanonischen Bände */
  ]
}
```

### Wurzelfelder
* `weltname` *(string)*: Offizieller Titel der Spielwelt.
* `version` *(string, SemVer)*: Aktuelle Kanon-Version (z. B. `"1.0.0"`). Wird erhöht (`patch` für Korrekturen/Änderungen an bestehenden Modulen, `minor` für neue Module/Regionen/Fraktionen).
* `quelldokument` *(string)*: Relativer Pfad zur monolithischen Weltenbibel-Masterdatei.
* `beschreibung` *(string)*: Überblick über Architektur und Leitmotiv (Kosmologie, Gesellschaft, zentrale Konflikte).
* `struktur` *(array)*: Geordnete Liste der Kapitel-/Bandobjekte (`01` bis `10`).

---

## 2. Band- / Kapitelobjekt

Jedes Element des Arrays `struktur` repräsentiert einen der zehn Architektur-Bände:

```json
{
  "id": "kosmologie",
  "code": "01",
  "titel": "Kosmologie & Metaphysische Architektur",
  "ordner": "01_kosmologie",
  "index": "01_kosmologie/README.md",
  "beschreibung": "Zusammenfassung der in diesem Band behandelten Themen.",
  "module": [
    /* Array der einzelnen Moduldateien */
  ]
}
```

### Bandfelder
* `id` *(string)*: Eindeutige snake_case-Kennung ohne Nummernpräfix (z. B. `"kosmologie"`, `"geografie"`, `"recht_und_gesetze"`).
* `code` *(string)*: Zweistellige Bandnummer (`"01"`–`"10"`).
* `titel` *(string)*: Formeller Bandtitel aus der jeweiligen `README.md`.
* `ordner` *(string)*: Verzeichnisname relativ zum Wurzelverzeichnis (z. B. `"01_kosmologie"`).
* `index` *(string)*: Relativer Pfad zur Hub-`README.md` des Bandes.
* `beschreibung` *(string)*: Beschreibung des im Band behandelten Themenbereichs.
* `module` *(array)*: Liste der zum Band gehörenden Einzelmodule.

---

## 3. Modulobjekt

Jedes Element des Arrays `module` beschreibt eine atomare `.md`-Datei:

```json
{
  "id": "ebenenstruktur",
  "code": "1.1",
  "titel": "Ebenenstruktur und Kosmos",
  "datei": "01_kosmologie/01_ebenenstruktur.md",
  "schluesselkonzepte": [
    "Materielle Ebene und Ebenengrenzen",
    "Himmelssphären und äußere Reiche",
    "Unterirdische Tiefen und Verwerfungen",
    "Elementarebenen und Schwellenportale"
  ],
  "tabellen": [
    "Übersichtstabelle der Ebenen"
  ],
  "sl_hinweise": "Für den SL relevantes Detail (optional)"
}
```

### Modulfelder
* `id` *(string)*: Eindeutige snake_case-Kennung aus dem Dateinamen (ohne Nummernpräfix und Dateiendung).
* `code` *(string)*: Hierarchischer Dezimalcode (z. B. `"1.1"`, `"2.3"`, `"7.8"`).
* `titel` *(string)*: Exakter Modultitel (entsprechend der H1-Überschrift der `.md`-Datei).
* `datei` *(string)*: Relativer Pfad der Markdown-Datei vom Workspace-Wurzelverzeichnis.
* `schluesselkonzepte` *(Array von Strings)*: 3 bis 7 prägnante Stichpunkte zu Regeln, Lore und wichtigen Institutionen des Moduls.
* `tabellen` *(Array von Strings, optional)*: Titel der im Dokument enthaltenen Markdown-Tabellen. Weglassen oder leer lassen, falls keine vorhanden sind.
* `sl_hinweise` *(string, optional)*: Zusammenfassung etwaiger Kästen `HINWEIS FÜR DEN SPIELLEITER` oder besonderer Erzählaufhänger.

---

## 4. Spezielle Unterstrukturen (Regionen, NSCs, Kampagnen, Ereignisse, Zeitlinie)

Für Bände mit kanonischen Unterordnern:

### A. Band 02 (Geografie — Unterordner `regionen/`)
Falls ein regionales Unterverzeichnis existiert:
```json
"ordner_regionen": "02_geografie/regionen",
"index_regionen": "02_geografie/regionen/README.md",
"regionen_module": [
  {
    "nummer": 1,
    "titel": "1. Region — Nordmark",
    "besonderheit": "Raues Klima / Bergbaugrenze",
    "datei": "02_geografie/regionen/01_nordmark.md"
  }
]
```

### B. Band 05 (Charaktere — Unterordner `Spielercharaktere/` und `Nichtspielercharaktere/`)
```json
"unterordner": {
  "spielercharaktere": "05_charaktere/Spielercharaktere",
  "nichtspielercharaktere": "05_charaktere/Nichtspielercharaktere"
}
```

### C. Band 09 (Chroniken — Unterordner `kampagnen/`)
```json
"ordner_kampagnen": "09_chroniken/kampagnen",
"aktive_kampagnen": [
  {
    "id": "kampagnenname",
    "index": "09_chroniken/kampagnen/kampagnenname/README.md",
    "sitzungen_gesamt": 12
  }
]
```

### D. Band 03 (Gesellschaft & Politik — Unterserie `braeuche_feste_und_ereignisse/`)
```json
"ordner_braeuche_feste_ereignisse": "03_gesellschaft_und_politik/braeuche_feste_und_ereignisse",
"index_braeuche_feste_ereignisse": "03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/README.md",
"brauch_module": [
  {
    "id": "abschiedszeremonie",
    "code": "3.5.1",
    "titel": "Die Abschiedszeremonie",
    "datei": "03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/braeuche/01_abschiedszeremonie.md"
  }
],
"fest_vorkommnis_module": [
  {
    "id": "gardeturnier",
    "code": "3.6.1",
    "titel": "Das Turnier der Garde",
    "datei": "03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/feste_und_vorkommnisse/01_gardeturnier.md",
    "periodizitaet": "variabel",
    "ausloeser": "Rückkehr von Feldzügen oder Ablösung der Ränge"
  }
],
"ereignis_module": [
  {
    "id": "belagerung_zitadelle",
    "code": "3.7.1",
    "titel": "Die Belagerung der Zitadelle",
    "datei": "03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/ereignisse/01_belagerung_zitadelle.md",
    "vorkommnis_status": "abgeschlossen"
  }
]
```
* `periodizitaet` *(string, optional)* für Feste: `"fest"`, `"variabel"` oder `"gemischt"`.
* `ausloeser` *(string, optional)*: Bedingungen, die das wiederkehrende Ereignis auslösen.
* `vorkommnis_status` *(string, optional)* für Ereignisse: `"geplant"`, `"laufend"` oder `"abgeschlossen"`.

### D2. Band 04 (Recht & Gesetze — Unterordner `01_` … `10_`)
```json
{
  "id": "recht_und_gesetze",
  "code": "04",
  "titel": "Recht & Gesetze",
  "ordner": "04_recht_und_gesetze",
  "index": "04_recht_und_gesetze/README.md",
  "beschreibung": "Rechtsordnung, Bürgerrechte, Erbfolge, Verträge, Abkommen, Strafrecht, Gerichte, arkanes Recht, Steuern und Kriegsrecht.",
  "module": [],
  "rechtsgebiete": [
    {
      "id": "rechtsordnung_und_quellen",
      "code": "4.1",
      "titel": "Rechtsordnung & Rechtsquellen",
      "ordner": "04_recht_und_gesetze/01_rechtsordnung_und_quellen",
      "index": "04_recht_und_gesetze/01_rechtsordnung_und_quellen/README.md",
      "module": [
        {
          "id": "allgemeiner_rahmen",
          "code": "4.1.1",
          "titel": "Allgemeiner Rahmen der Rechtsordnung",
          "datei": "04_recht_und_gesetze/01_rechtsordnung_und_quellen/01_allgemeiner_rahmen.md"
        }
      ]
    }
  ]
}
```
*(In bestehenden Welten mit flachem Ordner `04_recht_und_erbfolge/` werden die Dateien unter `"module"` indiziert und behalten ggf. `"id": "recht_und_erbfolge"`.)*

### E. Band 10 (Zeitlinie)
```json
{
  "id": "zeitlinie",
  "code": "10",
  "titel": "Zeitlinie & Weltchronologie",
  "ordner": "10_zeitlinie",
  "index": "10_zeitlinie/README.md",
  "beschreibung": "Historische Chronologie, Vorkommnisregister, Kalender und grafische Markwhen-Zeitlinie.",
  "module": [],
  "ordner_historische_chronologie": "10_zeitlinie/historische_chronologie",
  "historische_chronologie_module": [
    {
      "id": "epochenname",
      "code": "10.1.1",
      "titel": "Titel der historischen Epoche oder Zeitspanne",
      "datei": "10_zeitlinie/historische_chronologie/01_epochenname.md"
    }
  ],
  "ordner_vorkommnisregister": "10_zeitlinie/vorkommnisregister",
  "vorkommnisregister_module": [
    {
      "id": "zeitraumname",
      "code": "10.2.1",
      "titel": "Titel des Registerzeitraums",
      "datei": "10_zeitlinie/vorkommnisregister/01_zeitraumname.md"
    }
  ],
  "ordner_kalender": "10_zeitlinie/kalender",
  "kalender_module": [
    {
      "id": "kalender",
      "code": "10.3.1",
      "titel": "Der Weltkalender",
      "datei": "10_zeitlinie/kalender/01_kalender.md"
    }
  ],
  "ordner_markwhen": "10_zeitlinie/markwhen",
  "markwhen_dateien": [
    "10_zeitlinie/markwhen/allgemeine_zeitlinie.mw",
    "10_zeitlinie/markwhen/epochen/<epochenname>.mw",
    "10_zeitlinie/markwhen/kampagnen/<kampagnenname>.mw"
  ],
  "ordner_exporte": "10_zeitlinie/exporte"
}
```
* `.mw`-Dateien und Exporte werden **nicht** in die Bibel übernommen: sie erscheinen ausschließlich in `markwhen_dateien` und den Ordnereigenschaften.
* Das Array `module` des Bandes bleibt leer: die `.md`-Dateien von Band 10 liegen in ihren eigenen Arrays (`historische_chronologie_module`, `vorkommnisregister_module`, `kalender_module`), analog zu `regionen_module` in Band 02 und den Unterserien in Band 03.

---

## 5. Regeln für Parsing & automatische Extraktion

Bei Ausführung von `Struktur-JSON-generieren` oder `Struktur-JSON-aktualisieren`:
1. **Modultitel**: Aus der ersten `# Überschrift` der Markdown-Datei extrahiert.
2. **Schlüsselkonzepte**:
   - Aus Aufzählungslisten (`* Konzept: Erklärung`), `##`- und `###`-Unterüberschriften oder fettgedruckten Begriffen `**Begriff**` gewonnen.
   - Als knappe, selbsterklärende Aussagen normalisiert.
3. **Tabellen**: Erkannt anhand von Spaltentrennzeilen `| :--- | :--- |` nach einer `## Tabelle...`-Überschrift oder Bildunterschrift.
4. **SL-Hinweise**: Erkannt über `**HINWEIS FÜR DEN SPIELLEITER:**` oder `> ⚠️ **SL-Hinweis:**`.
5. **Zahlencode**: Heißt eine Datei `03_magiefluss.md` in `01_kosmologie`, lautet der Code `"1.3"`.
6. **Unterseriencodes**: Bögen unter `braeuche_feste_und_ereignisse/` verwenden dreistufige Codes je Unterordner (`3.5.x` Bräuche, `3.6.x` Feste/Vorkommnisse, `3.7.x` Ereignisse; fortlaufend je Unterordner). Rechtsgebiete unter `04_recht_und_gesetze/` verwenden `4.1.x` … `4.10.x` (`4.Y.1` für `01_allgemeiner_rahmen.md`, `4.Y.2+` für Einzelakte `02_<eintrag_slug>.md`). Dateien unter `10_zeitlinie/` verwenden `10.1.x` (historische Chronologie), `10.2.x` (Vorkommnisregister), `10.3.x` (Kalender).
7. **Typologische Felder**: Für Feste/Vorkommnisse `periodizitaet` und `ausloeser` aus den jeweiligen Vorlagenabschnitten extrahieren; für einmalige Ereignisse `vorkommnis_status`.
