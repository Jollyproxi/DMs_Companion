---
name: bibel-struktur-synchronisieren
description: "Use when: die Weltenbibel (Bibel-generieren, Bibel-aktualisieren) und weltstruktur.json (Struktur-JSON-generieren, Struktur-JSON-aktualisieren) erzeugen oder aktualisieren sowie Lore-Änderungen zwischen den Modulen der zehn Bände und den Masterdokumenten synchronisieren."
argument-hint: "Gib den Vorgang an: Bibel-generieren, Struktur-JSON-generieren, Bibel-aktualisieren oder Struktur-JSON-aktualisieren"
user-invocable: true
disable-model-invocation: false
---

# Skill: Synchronisation des Master-Kanons (`bibel-struktur-synchronisieren`)

Dieser Skill steuert den Lebenszyklus der beiden Master-Artefakte der D&D-Welt:
1. **Die Weltenbibel** (`WELTENBIBEL.md` oder eine bereits vorhandene monolithische Masterdatei): der zusammenhängende Fließtext zum narrativen Nachschlagen des gesamten Kanons.
2. **Das Strukturschema** (`weltstruktur.json`): die maschinenlesbare ontologische und taxonomische Karte der zehn Bände, Module, Regionen/Unterordner und Schlüsselkonzepte.

Der Skill handhabt die vollständige Generierung sowie den bidirektionalen inkrementellen Abgleich zwischen den modularen Einzeldateien der zehn Bände und den Masterdokumenten — streng kanontreu ohne vom Spielleiter nicht genehmigte Änderungen.

Siehe die begleitenden Referenzdokumente:
- [struktur-json-format](./references/struktur-json-format.md): Standard des JSON-Schemas, Pflichtfelder und Konzeptextraktion.
- [bibel-konventionen](./references/bibel-konventionen.md): Regeln für Überschriften-Ebenen, Kompilierungsreihenfolge und Tabellenformatierung.

---

## Matrix der unterstützten Operationen

| Argument / Befehl | Ziel-Artefakt | Modus | Hauptzweck |
| :--- | :--- | :--- | :--- |
| **`Bibel-generieren`** | `WELTENBIBEL.md` | Monolithisch / Vollständig | Kompiliert alle Dateien der 10 Bände in ein einziges narratives Masterdokument. |
| **`Struktur-JSON-generieren`** | `weltstruktur.json` | Vollständiger Scan | Scannt die Ordnerstruktur der Bände und erzeugt das taxonomische JSON von Grund auf neu. |
| **`Bibel-aktualisieren`** | `WELTENBIBEL.md` | Inkrementell / Delta | Aktualisiert in der Bibel ausschließlich die Abschnitte geänderter Module. |
| **`Struktur-JSON-aktualisieren`** | `weltstruktur.json` | Inkrementell / Delta | Synchronisiert das JSON mit hinzugefügten, umbenannten oder geänderten Modulen. |

> **📌 Regel: Eigennamen als Verknüpfungen**: Jeder Eigenname einer Weltentität (SCs, NSCs, Fraktionen, Häuser, Städte, Orte, magische Gegenstände, Bräuche, Feste, Ereignisse …), der im erzeugten Text vorkommt, muss eine **Markdown-Verknüpfung** zur kanonischen `.md`-Datei der Entität sein (z. B. `[Name](relativer/pfad/datei.md)`), niemals bloßer Klartext. Ausnahmen: Überschriften, Dateinamen, Frontmatter, Codeblöcke, Mermaid-Knoten und `.mw`-Quellen. Entität ohne Bogen: niemals erfinden — `[VOM_SL_ZU_DEFINIEREN: Bogen fehlt für <Name>]` verwenden und die Lücke melden. Prüfung und Umwandlung: Skill `eigennamen-verlinken`.

---

## 1. Verfahren: `Bibel-generieren` (Master-Kompilierung)

Nutze dieses Verfahren, um `WELTENBIBEL.md` aus den Einzelmodulen komplett neu zu generieren oder erstmals zu erstellen.

### Arbeitsschritte:
1. **Zieldatei ermitteln**:
   - Suche im Wurzelverzeichnis nach einer bestehenden Masterdatei (z. B. `WELTENBIBEL.md` oder einer gleichwertigen im Repository benannten Datei).
   - Existiert noch keine Masterdatei, erstelle `WELTENBIBEL.md`.
2. **Reihenfolge der Bände bestimmen**:
   - Lies `weltstruktur.json`, sofern vorhanden, um die offizielle Reihenfolge von Bänden und Modulen zu übernehmen.
   - Sortiere andernfalls die nummerierten Verzeichnisse: `01_kosmologie`, `02_geografie` (inklusive numerisch sortiertem `regionen/`), `03_gesellschaft_und_politik` (inklusive `braeuche_feste_und_ereignisse/`: `braeuche/` = 3.5.x, `feste_und_vorkommnisse/` = 3.6.x, `ereignisse/` = 3.7.x), `04_recht_und_erbfolge`, `05_charaktere` (`Nichtspielercharaktere/`), `06_orte`, `07_fraktionen`, `08_besondere_magische_gegenstaende`, `09_chroniken`, `10_zeitlinie` (`historische_chronologie/` = 10.1.x, `vorkommnisregister/` = 10.2.x, `kalender/` = 10.3.x; `.mw`-Quellen unter `markwhen/` und `exporte/` sind von der Bibel ausgenommen).
3. **Monolithischen Text zusammenstellen**:
   - Füge den kanonischen Kopfbereich mit Metadaten und Status-Badge ein:
     ```markdown
     ### WELTENBIBEL: [WELTNAME]
     
     > 📜 **Monolithisches Masterdokument des Kanons**
     > *Kanon-Version:* [VERSION] | *Letzte Kompilierung:* [HEUTIGES_DATUM]
     > 🛡️ *Geprüft: [DATUM_G] | Geändert: [HEUTIGES_DATUM]*
     ```
   - Setze für jeden Band eine H5-Überschrift (z. B. `##### 1. Kosmologie & Metaphysische Architektur`).
   - Passe für jede Moduldatei die Überschriftenhierarchie gemäß [bibel-konventionen](./references/bibel-konventionen.md) an:
     - Die H1-Überschrift des Moduls wird zu `###### *X.Y Modultitel*` (oder `### X.Y Modultitel`).
     - Übernimm Markdown-Tabellen, Mermaid-Diagramme und Kästen `**HINWEIS FÜR DEN SPIELLEITER:**` originalgetreu.
     - Bewahre alle `[VOM_SL_ZU_DEFINIEREN]`-Platzhalter.
4. **Speichern & Berichten**:
   - Speichere die kompilierte Masterdatei.
   - Gib dem SL eine Zusammenfassung: Anzahl verarbeiteter Bände, enthaltener Dateien und Gesamtumfang des Dokuments.

---

## 2. Verfahren: `Struktur-JSON-generieren` (Vollständige taxonomische Kartierung)

Nutze dieses Verfahren, um alle Workspace-Dateien zu scannen und eine vollständige maschinenlesbare Karte im JSON-Format zu erstellen.

### Arbeitsschritte:
1. **Allgemeine Angaben erfassen**:
   - Lies die Wurzel-`README.md` oder den Bibel-Kopfbereich, um `weltname`, `beschreibung` und `quelldokument` zu bestimmen.
   - Setze die Startversion auf `"1.0.0"` (oder behalte die aktuelle Version bei, falls bereits vorhanden).
2. **Systematischer Scan der 10 Bände**:
   - Iteriere über die Ordner `01_` bis `10_`:
     - Extrahiere `id`, `code`, `titel` und `beschreibung` aus der `README.md` des jeweiligen Bandes.
     - Sammle alle modularen `.md`-Dateien im Ordner (ohne `README.md`).
     - Für jedes `.md`-Modul:
       - `id`: snake_case-Slug aus dem Dateinamen ohne Nummernpräfix.
       - `code`: hierarchische Nummerierung (z. B. `"1.1"` für `01_kosmologie/01_ebenenstruktur.md`).
       - `titel`: aus der ersten `#`-Überschrift der Datei.
       - `datei`: normalisierter relativer Pfad mit `/`.
       - `schluesselkonzepte`: 3 bis 7 knappe Kernpunkte aus Unterüberschriften und fettgedruckten Definitionen.
       - `tabellen`: Titel vorhandener Markdown-Tabellen.
       - `sl_hinweise`: Inhalt etwaiger Hinweise nur für den SL.
   - Verarbeite kanonische Unterordner (`02_geografie/regionen/`, `03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/`, `05_charaktere/Nichtspielercharaktere/`, `09_chroniken/kampagnen/`, `10_zeitlinie/` samt `markwhen/`-Quellen) und befülle die speziellen Felder gemäß [struktur-json-format](./references/struktur-json-format.md).
3. **Syntaxprüfung & Ausgabe**:
   - Erzeuge `weltstruktur.json` mit 2 Leerzeichen Einrückung.
   - Stelle sicher, dass das JSON streng valide und frei von doppelten Schlüsseln oder fehlerhaften Zeichen ist.
   - Teile dem SL die Gesamtzahl der indizierten Module und Unterstrukturen mit.

---

## 3. Verfahren: `Bibel-aktualisieren` (Inkrementelle Synchronisation)

Nutze dieses Verfahren, wenn ein oder mehrere atomare Module bearbeitet oder hinzugefügt wurden, um die monolithische Bibel abzugleichen, ohne die gesamte Datei neu zu generieren.

### Arbeitsschritte:
1. **Geänderte Dateien identifizieren**:
   - Ermittle vom SL benannte Zielmodule oder Dateien mit `Geändert > Geprüft` anhand der Badges bzw. `PRUEFUNGSSTATUS.md`.
2. **Abschnitt in der Masterdatei lokalisieren**:
   - Öffne die Master-Bibeldatei.
   - Finde für jedes geänderte Modul den Abschnittsanker über den Hierarchiecode (`X.Y`) oder den Modultitel.
3. **Gezielte Abschnittsaktualisierung**:
   - Existiert der Abschnitt: ersetze den veralteten Text durch die neue Modulversion (mit angepassten Überschriftenebenen nach [bibel-konventionen](./references/bibel-konventionen.md)).
   - Ist das Modul neu: füge den neuen Abschnitt an der passenden Ordnungsposition innerhalb seines Bandes ein.
   - Lasse alle übrigen Abschnitte strikt unverändert.
4. **Master-Metadaten aktualisieren**:
   - Aktualisiere die Metadatenzeile im Kopfbereich:
     `> 🛡️ *Geprüft: [DATUM_G] | Geändert: [HEUTIGES_DATUM]*`
5. **Abgleichbericht**:
   - Liste dem SL die in der Bibel aktualisierten Abschnitte auf.

---

## 4. Verfahren: `Struktur-JSON-aktualisieren` (JSON-Delta-Synchronisation)

Nutze dieses Verfahren, um `weltstruktur.json` beim Hinzufügen neuer Dateien, Umbenennen von Modulen oder Erweitern von Inhalten aktuell zu halten.

### Arbeitsschritte:
1. **Aktuellen Stand laden**:
   - Lies die bestehende `weltstruktur.json`.
2. **Delta ermitteln**:
   - Vergleiche die physischen Dateien auf der Festplatte in den Ordnern der 10 Bände mit den Einträgen im Array `struktur`.
   - Identifiziere:
     - ➕ **Hinzugefügte Module**: `.md`-Dateien auf Disk, die im JSON fehlen.
     - 🔄 **Geänderte Module**: Dateien mit verändertem Titel, Tabellen oder Schlüsselkonzepten.
     - ➖ **Entfernte oder umbenannte Module**: Pfade im JSON, die nicht mehr auf Disk existieren.
3. **Änderungen auf das JSON anwenden**:
   - Für neue Module: erstelle das neue Objekt (`id`, `code`, `titel`, `datei`, `schluesselkonzepte`, `tabellen`, `sl_hinweise`) und sortiere es passend ein.
   - Für geänderte Module: aktualisiere `titel`, `schluesselkonzepte` und `tabellen` unter Wahrung vorhandener individueller Anmerkungen.
   - Für entfernte/verschobene Module: aktualisiere den Pfad `datei` oder entferne den veralteten Eintrag (vor dem Löschen vom SL bestätigen lassen).
4. **Versionsnummer erhöhen**:
   - Erhöhe die Version gemäß SemVer (z. B. `"1.0.0"` → `"1.0.1"` für Inhaltsänderungen, `"1.1.0"` für neue Module/Regionen).
5. **Speichern & Diff**:
   - Schreibe die formatierte `weltstruktur.json` neu.
   - Zeige dem SL eine präzise Zusammenfassung aller hinzugefügten, aktualisierten oder entfernten Entitäten.

---

## Strukturierte Interaktion

Wird der Skill ohne klare Vorgabe aufgerufen oder treten Konflikte bei einer Aktualisierung auf, frage den SL (über das strukturierte Fragewerkzeug der Umgebung wie `vscode_askQuestions` / `AskUserQuestion`, falls verfügbar; sonst im Chat), welche Operation ausgeführt werden soll:
- `Bibel-generieren` — Kompiliert alle Module der 10 Bände in das monolithische Masterdokument
- `Struktur-JSON-generieren` — Erzeugt `weltstruktur.json` durch vollständigen Archivscan neu
- `Bibel-aktualisieren` — Synchronisiert nur kürzlich geänderte oder neue Module in die Bibel
- `Struktur-JSON-aktualisieren` — Aktualisiert `weltstruktur.json` inkrementell anhand der Dateiänderungen

---

## Qualitätskriterien & Abschlussprüfung

Nach Abschluss jeder Operation:
1. **JSON-Syntaxprüfung**: Bei jeder Änderung an `weltstruktur.json` strikte JSON-Validität sicherstellen.
2. **Link- & Pfadkontrolle**: `datei`-Pfade im JSON und Querverweise in der Bibel müssen auf existierende Dateien verweisen.
3. **Keine Halluzinationen**: Niemals Konzepte, NSCs oder Fraktionen einfügen, die nicht in Quelldateien belegt oder vom SL freigegeben sind.
4. **Zusammenspiel mit anderen Skills**:
   - Nach größeren Strukturänderungen `struktur-validieren` empfehlen.
   - Nach Bibel- oder Modulaktualisierungen an die Aktualisierung des Dashboards über `pruefungsstatus` erinnern.
