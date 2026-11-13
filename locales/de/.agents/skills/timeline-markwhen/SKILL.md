---
name: timeline-markwhen
description: "Use when: grafische Markwhen-Zeitliniendateien (.mw) unter 10_zeitlinie/markwhen/ (allgemeine_zeitlinie.mw, epochen/<epoche>.mw, kampagnen/<kampagne>.mw) erstellen, generieren, aktualisieren, validieren oder exportieren, Daten, Status und Tags mit historische_chronologie/, vorkommnisregister/, Sitzungsprotokollen und weltstruktur.json synchronisieren oder grafische Renderings unter 10_zeitlinie/exporte/ erzeugen."
argument-hint: "Gib den Vorgang an: mw-erstellen, mw-aktualisieren, mw-validieren oder mw-exportieren (z. B. 'mw-erstellen epoche: Erstes Zeitalter', 'mw-aktualisieren kampagne: Chroniken des Nordens')"
user-invocable: true
disable-model-invocation: false
---

# Skill: Verwaltung der grafischen Markwhen-Zeitlinie (`timeline-markwhen`)

Dieser Skill regelt den gesamten Lebenszyklus der **Markwhen-Quellen (`.mw`)** unter `10_zeitlinie/markwhen/` und der zugehörigen Exporte unter `10_zeitlinie/exporte/`. Er hält die grafische Zeitdarstellung der Welt synchron mit der historischen Chronologie (`10_zeitlinie/historische_chronologie/`), dem Vorkommnisregister (`10_zeitlinie/vorkommnisregister/`), dem Kalender (`10_zeitlinie/kalender/`), den Bögen für Bräuche, Feste und Ereignisse (`03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/`) sowie den Kampagnenprotokollen (`09_chroniken/kampagnen/`).

Siehe die beigefügten technischen Referenzen:
- [mw-syntax-und-vorlagen](./references/mw-syntax-und-vorlagen.md): kanonische Markwhen-Syntax, YAML-Header, Tag-Taxonomie und Vorlagen für `allgemeine_zeitlinie.mw`, `epochen/<epoche>.mw` und `kampagnen/<kampagne>.mw`.
- [synchronisation-und-export](./references/synchronisation-und-export.md): Regeln für den bidirektionalen Abgleich mit Band 10, Indizierung in `weltstruktur.json`, Validierungs-Checkliste und Export-Pipeline für `10_zeitlinie/exporte/`.

> **📌 Regel: Eigennamen als Verknüpfungen**: Jeder Eigenname einer Weltentität (SCs, NSCs, Fraktionen, Häuser, Städte, Orte, magische Gegenstände, Bräuche, Feste, Ereignisse …), der im erzeugten Text vorkommt, muss eine **Markdown-Verknüpfung** zur kanonischen `.md`-Datei der Entität sein (z. B. `[Name](relativer/pfad/datei.md)`), niemals bloßer Klartext. Ausnahmen: Überschriften, Dateinamen, Frontmatter, Codeblöcke, Mermaid-Knoten und `.mw`-Quellen. Entität ohne Bogen: niemals erfinden — `[VOM_SL_ZU_DEFINIEREN: Bogen fehlt für <Name>]` verwenden und die Lücke melden. Prüfung und Umwandlung: Skill `eigennamen-verlinken`.

---

## 1. Goldene Regel: Notarielle Treue (Keine Halluzinationen)

- **Erfindungsverbot**: Erfinde niemals eigenmächtig Daten, Weltjahre, Epochennamen, Zeitspannen, Beteiligte oder Ausgänge, die nicht ausdrücklich vom SL geliefert oder bereits in kanonischen Dateien belegt sind.
- **Umgang mit fehlenden Daten oder Details**:
  - **Pflichtabfrage vor dem Schreiben**: In Markwhen verlangt jedes sichtbare Ereignis ein Datum vor dem `:`. Besitzt ein Ereignis in den kanonischen Dateien noch kein Datum bzw. Weltjahr, **halte inne und frage stets zuerst den SL** (über das strukturierte Fragewerkzeug der Umgebung wie `vscode_askQuestions` oder `AskUserQuestion`, falls verfügbar; sonst direkt im Chat) nach einem kanonischen Datum oder einem **vorläufigen Jahr**, bevor du den Eintrag in die `.mw`-Datei schreibst.
  - Nennt der SL ein vorläufiges Jahr, trage das Ereignis mit diesem Jahr ein, ergänze den Tag `#vorlaeufiges_datum` und vermerke in den Unterpunkten `- [VOM_SL_ZU_DEFINIEREN: endgültiges Datum bestätigen]`, damit das Ereignis sofort sichtbar ist, aber als zu konsolidieren markiert bleibt.

---

## 2. Architektur von `10_zeitlinie/markwhen/`

```text
10_zeitlinie/
├── markwhen/
│   ├── README.md                     # Index der .mw-Quellen und Konventionsübersicht
│   ├── allgemeine_zeitlinie.mw       # Allgemeiner Index/Legende (KEIN Aggregat der Quellen)
│   ├── epochen/
│   │   └── <epochen_slug>.mw         # Eine .mw-Quelle pro historischer Epoche/Zeitspanne
│   └── kampagnen/
│       └── <kampagnen_slug>.mw       # Alles Kampagnenrelevante (vergangen, laufend, geplant)
└── exporte/
    ├── README.md                     # Verzeichnis abgeleiteter grafischer Renderings
    └── <dateiname>.(html|svg|png|pdf)
```

- **Rolle von `allgemeine_zeitlinie.mw`**: enthält den Konfigurations-Header samt Tag-/Farblegende, die Zusammenfassung des Weltkalenders sowie das kommentierte Verzeichnis der Quellen in `epochen/` und `kampagnen/`. Einzelne Ereignisse der Fachdateien werden hier nicht dupliziert.
- **Ausschluss aus der Bibel**: `.mw`-Dateien und Inhalte von `exporte/` sind **von der Weltenbibel ausgeschlossen** und werden ausschließlich in `weltstruktur.json` (`markwhen_dateien` in Band `10`) geführt.

---

## 3. Matrix der Unteroperationen

| Befehl / Argument | Hauptziel | Modus | Zweck |
| :--- | :--- | :--- | :--- |
| **`mw-erstellen`** *(oder `mw-generieren`)* | `allgemeine_zeitlinie.mw`, `epochen/*.mw`, `kampagnen/*.mw` | Initialisierung / Neuaufbau | Legt die `markwhen/`-Struktur an, erzeugt `allgemeine_zeitlinie.mw` oder eine neue `.mw`-Datei für eine Epoche oder Kampagne aus kanonischen Modulen. |
| **`mw-aktualisieren`** | Bestehende `.mw`-Dateien + `markwhen/README.md` | Inkrementell / Delta | Fügt neue Ereignisse/Vorkommnisse ein, aktualisiert Status-Tags (`#geplant` → `#laufend` → `#historisch`), ergänzt Sitzungen und pflegt die Legende. |
| **`mw-validieren`** | `10_zeitlinie/markwhen/**/*.mw` | Diagnose / Technisches Audit | Prüft Markwhen-Syntax, Pflicht-Tags, relative Links zu Bögen/Protokollen und den Abgleich mit Band 10 sowie `weltstruktur.json`. |
| **`mw-exportieren`** | `10_zeitlinie/exporte/` | Rendering / Ableitung | Exportiert `.mw`-Quellen in abgeleitete Ansichten (HTML/SVG/PNG/PDF über optionale `mw`-CLI oder manuellen IDE-/Web-Export) und aktualisiert `exporte/README.md`. |

---

## 4. Verfahren 1: `mw-erstellen` (Initialisierung & Generierung von `.mw`-Quellen)

Nutze dieses Verfahren, um `10_zeitlinie/markwhen/` einzurichten oder eine neue `.mw`-Datei für eine Epoche oder Kampagne zu erstellen.

### Arbeitsschritte:
1. **Kontext & Quellen erkennen**:
   - Lies `10_zeitlinie/README.md`, `10_zeitlinie/kalender/` und `10_zeitlinie/markwhen/README.md`.
   - Prüfe je nach gewünschtem Ziel (`allgemein`, `epoche`, `kampagne` oder `alle`) die relevanten Quellen:
     - Für eine **Epoche**: `10_zeitlinie/historische_chronologie/`, `10_zeitlinie/vorkommnisregister/` und Bögen unter `03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/`.
     - Für eine **Kampagne**: `09_chroniken/kampagnen/<kampagnenname>/README.md`, Protokolle in `sitzungen/`, SC-Dossiers (`05_charaktere/Spielercharaktere/<kampagnenname>/`) sowie verknüpfte historische/laufende Ereignisse.
2. **Vorab-Interview**:
   - Fehlen wesentliche Eckdaten (z. B. Epochenname/-slug, Start-/Endjahr, aktuelles Kampagnenjahr), frage vor dem Erzeugen beim SL nach (über das strukturierte Fragewerkzeug falls verfügbar, sonst im Chat).
3. **Dateien aus Vorlagen erzeugen**:
   - Wende die Vorlagen aus [mw-syntax-und-vorlagen](./references/mw-syntax-und-vorlagen.md) an:
     - Erstelle bei Bedarf die Unterordner `10_zeitlinie/markwhen/epochen/` und `10_zeitlinie/markwhen/kampagnen/`.
     - Erzeuge `allgemeine_zeitlinie.mw` mit Header, Tag-/Farbdefinitionen, Kalenderhinweisen und `.mw`-Dateiübersicht.
     - Erzeuge `epochen/<epochen_slug>.mw` oder `kampagnen/<kampagnen_slug>.mw`, sortiere Ereignisse chronologisch nach Weltjahr (`JJJJ`, `JJJJ-MM`, `JJJJ-MM-TT` oder Spannen `start/ende`) und gruppiere sie in thematische oder phasenbezogene `section`-Blöcke.
     - Füge unter jedem Ereignis den relativen Markdown-Link zum kanonischen Bogen oder Sitzungsprotokoll ein.
4. **Indizes & JSON fortschreiben**:
   - Aktualisiere `10_zeitlinie/markwhen/README.md` mit den neuen `.mw`-Dateien und setze `Geändert` im `🛡️`-Badge auf heute.
   - Schlage die Aktualisierung von `markwhen_dateien` in `weltstruktur.json` (`Struktur-JSON-aktualisieren`) vor.

---

## 5. Verfahren 2: `mw-aktualisieren` (Inkrementelle Aktualisierung)

Nutze dieses Verfahren nach einem Sitzungsprotokoll (`sitzungsprotokoll`), nach Anlage/Änderung eines Bogens unter `braeuche_feste_und_ereignisse/` (`brauch-fest-ereignis`) oder auf direkte Anforderung des SL.

### Arbeitsschritte:
1. **Zeitliches Delta bestimmen**:
   - Ermittle, was sich geändert hat:
     - **Neues Ereignis / neues Vorkommnis**: Datum/Weltjahr, Titel, Typ (`#brauch`, `#fest`, `#ereignis`, `#vorkommnis`), Status (`#geplant`, `#laufend`, `#historisch`) und thematische Tags (`#fraktion_<slug>`, `#ort_<slug>`, `#SC_<slug>`, `#NSC_<slug>`, `#kampagne_<slug>`).
     - **Statusübergang**: Wechsel eines bestehenden Eintrags von `#geplant` auf `#laufend` oder `#historisch` (samt knapper Ergebniszusammenfassung).
     - **Neue Kampagnensitzung**: datierte Ereignisse aus `09_chroniken/kampagnen/<name>/sitzungen/XX_titel.md`.
2. **`.mw`-Quellen aktualisieren**:
   - Öffne die zuständige Epochen-`.mw`-Datei in `10_zeitlinie/markwhen/epochen/` und füge die Ereigniszeile chronologisch korrekt ein oder aktualisiere sie.
   - Betrifft das Ereignis eine Kampagne, aktualisiere ebenso `10_zeitlinie/markwhen/kampagnen/<kampagnen_slug>.mw` samt relativem Link zum Protokoll oder Bogen.
   - Wurden neue Tags (z. B. neue Fraktion oder Kampagne) oder feste Kalenderturnusse ergänzt, aktualisiere Header und Legende in `10_zeitlinie/markwhen/allgemeine_zeitlinie.mw`.
3. **Abgleich mit Band 10**:
   - Prüfe, ob derselbe Eintrag samt Tags auch in `10_zeitlinie/historische_chronologie/` (bei `#historisch`) bzw. `10_zeitlinie/vorkommnisregister/` (bei `#vorkommnis`, `#laufend` oder `#geplant`) steht, und schlage bei Bedarf den Abgleich vor.

---

## 6. Verfahren 3: `mw-validieren` (Diagnose & Konsistenzprüfung)

Nutze dieses Verfahren, um die formale und strukturelle Korrektheit der `.mw`-Quellen anhand der Checkliste in [synchronisation-und-export](./references/synchronisation-und-export.md) zu prüfen.

### Durchgeführte Prüfungen:
1. **Markwhen-Syntax**: Gültigkeit des YAML-Headers (`---`, keine `#Kategorie`-Schlüssel ohne `:`, kein `dateFormat`), korrektes Schließen aller `section` / `endSection`- (bzw. `group` / `endGroup`-)Blöcke und gültige Datumsformate (`JJJJ`, `JJJJ-MM`, `JJJJ-MM-TT`, `datum1/datum2`) vor Doppelpunkten `:`.
2. **Tag-Taxonomie**: Jedes Ereignis muss mindestens einen **Typ**-Tag (`#brauch`, `#fest`, `#ereignis`, `#vorkommnis`) und einen **Status**-Tag (`#historisch`, `#laufend`, `#geplant`) besitzen.
3. **Integrität relativer Links**: Prüfe, ob alle Markdown-Links `[Text](../../...)` in Ereignisbeschreibungen auf existierende Workspace-Dateien verweisen.
4. **Bidirektionale Konsistenz mit Band 10 & JSON**:
   - Vergleiche Ereignisse in `.mw`-Dateien mit `historische_chronologie/` und `vorkommnisregister/` und melde Abweichungen bei Daten oder Status-Tags.
   - Prüfe, ob alle `.mw`-Dateien auf der Festplatte in `markwhen_dateien` innerhalb von `weltstruktur.json` eingetragen sind.
5. **Diagnosebericht**: Gib eine Ergebnistabelle (`OK` / `WARN` / `FEHLER`) aus und frage den SL (über das strukturierte Werkzeug falls verfügbar, sonst im Chat), ob automatische Korrekturen angewendet werden sollen.

---

## 7. Verfahren 4: `mw-exportieren` (Grafische Exporte in `10_zeitlinie/exporte/`)

Nutze dieses Verfahren, wenn der SL gerenderte Ansichten der Zeitlinie erzeugen oder aktualisieren möchte.

### Arbeitsschritte:
1. **Optionale Werkzeuge prüfen (`mw`-CLI / Erweiterung / Web-App)**:
   - Prüfe, ob die Markwhen-CLI (`@markwhen/mw`) in der Umgebung verfügbar ist, oder führe den SL über die Editor-Erweiterung bzw. `markwhen.com` gemäß [synchronisation-und-export](./references/synchronisation-und-export.md).
2. **Erzeugen & Exportieren**:
   - Exportiere die gewünschten `.mw`-Quellen nach `10_zeitlinie/exporte/` unter dem Standardschema (`zeitlinie_<slug>_<format>.<endung>`).
3. **Exportindex aktualisieren**:
   - Aktualisiere `10_zeitlinie/exporte/README.md` mit der Tabelle erzeugter Renderings (Datei, `.mw`-Quelle, Erstellungsdatum) und setze `Geändert` im `🛡️`-Badge fort.

---

## 8. Strukturierte Interaktion

Wird der Skill ohne spezifische Argumente oder mit Teilparametern aufgerufen, frage den SL (über das strukturierte Fragewerkzeug der Umgebung wie `vscode_askQuestions` / `AskUserQuestion`, falls verfügbar; sonst im Chat), welcher Vorgang ausgeführt werden soll:
- `mw-erstellen` — Initialisiert `allgemeine_zeitlinie.mw` oder legt eine neue `.mw`-Datei pro Epoche oder Kampagne an
- `mw-aktualisieren` — Ergänzt neue Ereignisse/Vorkommnisse oder aktualisiert Status und Tags in bestehenden `.mw`-Dateien
- `mw-validieren` — Prüft `.mw`-Syntax, Tags, relative Links sowie Synchronisation mit Band 10 und JSON
- `mw-exportieren` — Exportiert `.mw`-Quellen als abgeleitete Renderings nach `10_zeitlinie/exporte/`
