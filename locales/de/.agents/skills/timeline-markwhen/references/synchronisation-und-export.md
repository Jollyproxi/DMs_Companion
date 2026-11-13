# Markwhen-Synchronisation, Validierung & Export

Abgleichregeln zwischen `10_zeitlinie/markwhen/`, den übrigen Weltmodulen, `weltstruktur.json` und dem Ordner `10_zeitlinie/exporte/`.

---

## 1. Bidirektionale Zuordnung zwischen Modulen & `.mw`-Dateien

Jedes Ereignis in `.mw`-Dateien entspricht einer kanonischen Dokumentationsquelle:

| Kanonische Quelle | Ziel in `markwhen/` | Erforderliche Tags |
| :--- | :--- | :--- |
| `10_zeitlinie/historische_chronologie/*.md` | `epochen/<epoche>.mw` (und `kampagnen/<kampagne>.mw`, falls relevant) | `#ereignis` (oder `#fest`/`#brauch`) + `#historisch` |
| `10_zeitlinie/vorkommnisregister/*.md` | `epochen/<epoche>.mw` + ggf. `kampagnen/<kampagne>.mw` | `#fest #vorkommnis` oder `#ereignis` + `#historisch` / `#laufend` / `#geplant` |
| `03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/feste_und_vorkommnisse/*.md` (Tabelle *Bekannte Vorkommnisse*) | `epochen/<epoche>.mw` + `allgemeine_zeitlinie.mw` (bei festem Kalenderturnus) | `#fest #vorkommnis` + passender Status |
| `03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/ereignisse/*.md` | `epochen/<epoche>.mw` + ggf. `kampagnen/<kampagne>.mw` | `#ereignis` + passender Status (`abgeschlossen` → `#historisch`) |
| `09_chroniken/kampagnen/<name>/sitzungen/*.md` | `kampagnen/<kampagnen_slug>.mw` (und `epochen/<epoche>.mw`, falls historisch bedeutsam) | `#ereignis` oder `#vorkommnis` + `#kampagne_<slug>` + Status |
| `10_zeitlinie/kalender/*.md` | `allgemeine_zeitlinie.mw` (kommentierte Kalenderlegende) | — |

### Umwandlungsregel Bogenstatus → Markwhen-Tag

- Bogen / Register mit Status `abgeschlossen` oder vergangenes Ereignis → `#historisch`
- Bogen / Register mit Status `laufend` → `#laufend`
- Bogen / Register mit Status `geplant` → `#geplant`

---

## 2. Synchronisation mit `weltstruktur.json`

`.mw`-Quellen und Renderings in `exporte/`:

1. **Dürfen NIEMALS in die Weltenbibel aufgenommen werden** (`WELTENBIBEL.md`).
2. **Müssen in `weltstruktur.json` erfasst werden** innerhalb des Objekts von Band `10` (`id: "zeitlinie"`) im Array `markwhen_dateien`:

```json
"ordner_markwhen": "10_zeitlinie/markwhen",
"markwhen_dateien": [
  "10_zeitlinie/markwhen/allgemeine_zeitlinie.mw",
  "10_zeitlinie/markwhen/epochen/01_erstes_zeitalter.mw",
  "10_zeitlinie/markwhen/kampagnen/chroniken_des_nordens.mw"
],
"ordner_exporte": "10_zeitlinie/exporte"
```

Fügt `mw-erstellen` eine `.mw`-Datei hinzu oder entfernt sie, aktualisiere `10_zeitlinie/markwhen/README.md` und schlage die Aktualisierung von `markwhen_dateien` in `weltstruktur.json` vor (oder führe sie nach Freigabe aus).

---

## 3. Validierungs-Checkliste (`mw-validieren`)

Prüfe bei Ausführung von `mw-validieren` folgende Punkte der Reihe nach:

1. **Ordnerstruktur & Index**:
   - Vorhandensein von `10_zeitlinie/markwhen/README.md` und `10_zeitlinie/markwhen/allgemeine_zeitlinie.mw`.
   - Jede `.mw`-Datei in `epochen/` und `kampagnen/` muss sowohl in `10_zeitlinie/markwhen/README.md` als auch im kommentierten Index von `allgemeine_zeitlinie.mw` stehen.
2. **Markwhen-Syntax**:
   - YAML-Header sauber zwischen zwei `---`-Zeilen eingeschlossen, ohne `#Kategorie`-Schlüssel ohne `:` und ohne `dateFormat: yyyy-MM-dd` (ISO-Format ist nativ; stattdessen `timezone: UTC` angeben).
   - Ausgeglichene `section` / `endSection`- (und `group` / `endGroup`-)Blöcke.
   - Gültiges Datumsformat vor `:` in Ereigniszeilen (keine erfundenen Daten oder unkommentierter Freitext anstelle des Datums).
3. **Tag-Abdeckung**:
   - Jede Ereigniszeile trägt mindestens 1 Typ-Tag (`#brauch`, `#fest`, `#ereignis`, `#vorkommnis`) und 1 Status-Tag (`#historisch`, `#laufend`, `#geplant`).
   - Alle in `epochen/*.mw` und `kampagnen/*.mw` genutzten Tags sind in der Legende von `allgemeine_zeitlinie.mw` verzeichnet.
4. **Markdown-Links**:
   - Relative Pfade in Ereignis-Unterpunkten (z. B. `../../../03_gesellschaft_und_politik/...`) verweisen auf real existierende Dateien und kodieren Leerzeichen als `%20`.
5. **Abgleich mit Band 10 & `weltstruktur.json`**:
   - Jeder Eintrag in `historische_chronologie/` und `vorkommnisregister/` hat sein Gegenstück in der Epochen-`.mw`-Datei.
   - Das Array `markwhen_dateien` von Band 10 in `weltstruktur.json` entspricht exakt den `.mw`-Dateien auf dem Datenträger.

---

## 4. Export-Pipeline (`mw-exportieren`) *(Optional)*

Der Ordner `10_zeitlinie/exporte/` enthält abgeleitete Renderings (aus der Bibel ausgeschlossen).

### Modus A — Über Markwhen-CLI (`@markwhen/mw`)

Falls Node.js / `npx` oder der Befehl `mw` in der Umgebung verfügbar sind:

- **Interaktive HTML-Zeitlinie**:
  `npx @markwhen/mw <dateipfad.mw> -o 10_zeitlinie/exporte/<dateiname>.html`
- Prüfe vorab stets die Verfügbarkeit (`command -v mw` unter macOS/Linux bzw. `Get-Command mw` in PowerShell, oder `npx --version`).

### Modus B — Über IDE-Erweiterung (`Markwhen`) oder Web-App

Falls der SL lieber über die Editor-Erweiterung von Markwhen oder `markwhen.com` nach PNG/SVG/PDF exportiert:

1. Bereite die `.mw`-Quelldatei vor, validiere sie und achte auf `title` sowie vollständige Tag-Farben im YAML-Header.
2. Gib den kanonischen Speicherdateinamen unter `10_zeitlinie/exporte/` an:
   - `zeitlinie_epoche_<slug>.(html|svg|png|pdf)`
   - `zeitlinie_kampagne_<slug>.(html|svg|png|pdf)`
3. Aktualisiere `10_zeitlinie/exporte/README.md` mit einer Übersichtstabelle:

```markdown
## Exportierte Dateien

| Exportiertes Rendering | `.mw`-Quelle | Format | Letzte Aktualisierung |
| :--- | :--- | :--- | :--- |
| [zeitlinie_kampagne_...](zeitlinie_kampagne_....html) | [kampagnen/....mw](../markwhen/kampagnen/....mw) | HTML | JJJJ-MM-TT |
```
