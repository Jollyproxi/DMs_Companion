# Kampagnen-Archivar — Nutzungsanleitung

Alles, was Sie brauchen, um den **Kampagnen-Archivar** an Ihrem Spieltisch arbeiten zu lassen: Installation, erste Schritte, vollständige Referenz aller **11 Fähigkeiten**, typische Arbeitsabläufe, Fehlerbehebung und FAQ.

* Lokalisierte Fassungen dieser Anleitung: [Italiano](https://github.com/<owner>/DMs_Companion/blob/main/locales/it/GUIDA-UTILIZZO.md) · [British English](https://github.com/<owner>/DMs_Companion/blob/main/locales/en-gb/USAGE.md) · [Français](https://github.com/<owner>/DMs_Companion/blob/main/locales/fr/GUIDE-UTILISATION.md) — siehe auch das projekteigene [USAGE.md](https://github.com/<owner>/DMs_Companion/blob/main/USAGE.md) auf dem `main`-Branch.

---

## 1. Installation

**Voraussetzungen**: ein KI-Programmierassistent (siehe die Harness-Tabelle unten) und, empfohlen aber nicht zwingend, ein Git-Repository für Ihre Kampagne/Welt.

### Option 1 — Diesen Branch in Ihre Kampagne kopieren (empfohlen)

Sie lesen das Sprachpaket `de` (geklont mit `git clone --depth 1 -b de …` oder als ZIP heruntergeladen). Kopieren Sie den Inhalt in das Wurzelverzeichnis **Ihres eigenen Kampagnen-Repositories** (oder in das nutzerspezifische KI-Konfigurationsverzeichnis, um die Werkzeugsammlung in jedem Projekt verfügbar zu machen):

* `AGENTS.md`, `CLAUDE.md`
* `.github/agents/`
* `.agents/skills/`
* `NUTZUNGSANLEITUNG.md` (diese Anleitung)

### Option 2 — Fähigkeiten über die Agent Skills CLI installieren (`npx skills`)

```bash
# Alle Fähigkeiten aus diesem Sprach-Branch
npx skills add https://github.com/<owner>/DMs_Companion/tree/de

# Oder direkt aus dem Sprachordner auf main
npx skills add https://github.com/<owner>/DMs_Companion/tree/main/locales/de/.agents/skills
```

*(Kopieren Sie auch `AGENTS.md` und/oder `.github/agents/*.agent.md`, wenn Sie die vollständige Archivar-Persona und die Arbeitsablauf-Orchestrierung wünschen.)*

### Was die installierten Dateien tun

| Datei / Ordner | Zweck |
| :--- | :--- |
| `AGENTS.md` | Universelle Regeln und Abläufe, von jedem Harness gelesen. |
| `CLAUDE.md` | Einstiegspunkt für Claude Code; importiert `AGENTS.md`. |
| `.github/agents/kampagnen-archivar.agent.md` | Die Persona *Kampagnen-Archivar* (Eintrag im Agenten-Auswahlmenü von VS Code). |
| `.agents/skills/<faehigkeit>/SKILL.md` | Die 11 modularen Fähigkeiten (plus Vorlagen unter `references/`). |
| `NUTZUNGSANLEITUNG.md` | Diese Anleitung. |

### Hinweise je Harness

| Harness | Was passiert |
| :--- | :--- |
| **VS Code / GitHub Copilot** | Der Agent erscheint im Agenten-Auswahlmenü des Chats; die Fähigkeiten stehen als `/slash`-Befehle bereit; Rückfragen kommen als strukturierte Dialoge (`vscode_askQuestions`). |
| **Claude Code** | `CLAUDE.md` wird automatisch geladen. Werden die Fähigkeiten nicht erkannt, kopieren Sie `.agents/skills/*` nach `.claude/skills/` oder erstellen Sie einen Symlink. |
| **OpenAI Codex CLI / Cursor / OpenCode / Gemini CLI / Antigravity** | `AGENTS.md` und `.agents/skills/` werden automatisch erkannt; fragen Sie einfach in natürlicher Sprache. |
| **Optionale Erweiterungen** | Graphify MCP (Querverlinkungs-Graph) und die Markwhen-CLI/-Erweiterung (`@markwhen/mw`) für den Timeline-Render. Alles funktioniert auch ohne sie. |

---

## 2. Die ersten fünf Minuten

1. **Öffnen Sie Ihr Kampagnen-Repository** in Ihrem KI-Assistenten.
2. **Wählen Sie den Agenten *Kampagnen-Archivar*** im Agenten-Auswahlmenü (VS Code) oder erwähnen Sie ihn im Chat (andere Harnesses).
3. **Erklären Sie ihm, wo Sie stehen**:
   * *Neue Welt* → starten Sie `/welt-initialisieren` und beantworten Sie das geführte Interview: Es generiert den Zehn-Bände-Verzeichnisbaum, den Wurzelindex und die Anfangsdateien der Masterdokumente.
   * *Bestehende Welt* → starten Sie zuerst `/struktur-validieren`. Der Archivar passt sich an die vorhandenen Ordner an, einschließlich alter Namen (`06_location/`, `07_factions/`, `08_oggetti magici peculiari/`, `cornici/`, …).
4. **Prüfen Sie das Ergebnis**: Die Masterdateien (`WELTENBIBEL.md`, `PRUEFUNGSSTATUS.md`, `weltstruktur.json`) liegen im Wurzelverzeichnis der Welt; die Lore lebt in den zehn Bänden.
5. **Probieren Sie eine echte Aufgabe**: Fügen Sie die Rohnotizen Ihrer letzten Sitzung ein und lassen Sie den Archivar das Protokoll erstellen.

---

## 3. Wie die Werkzeugsammlung denkt

### Die goldene Regel: Notarielle Treue (Null Halluzinationen)

Der Archivar ordnet **nur** das, was Sie liefern oder bereits kanonisiert haben. Er erfindet niemals Charaktere, Orte, Daten, Wendungen oder Zahlen.

* **Fehlende Information** → er fragt Sie direkt (interaktiver Modus) oder fügt einen gut sichtbaren Platzhalter `[VOM_SL_ZU_DEFINIEREN: Beschreibung des fehlenden Details]` ein, den Sie später durchsuchen können.
* **Kreativität nur auf Anforderung** → er brainstormt (Namen, Optionen, Ideen) **nur**, wenn Sie es ausdrücklich verlangen (z. B. *„Gib mir 3 Optionen für …“*, *„Erfinde einen passenden Namen“*).

### Die Zehn-Bände-Architektur

| Band | Inhalt |
| :--- | :--- |
| `01_kosmologie/` | Ebenen, Himmelsmechanik, Magiefluss, kosmische Ethik. |
| `02_geografie/` | Kartografie, Gebiete, unterirdische Regionen, Regions-Dossiers (`regionen/`). |
| `03_gesellschaft_und_politik/` | Zivile Ordnung, Wirtschaft, Gesellschaftsschichten, Justiz; Unterreihe `braeuche_feste_und_ereignisse/` (`braeuche/`, `feste_und_vorkommnisse/`, `ereignisse/`). |
| `04_recht_und_erbfolge/` | Grundgesetze, Erbfolgerecht, Pakte, Abkommen, Gerichte. |
| `05_charaktere/` | Modulare SC-Dossiers (`Spielercharaktere/<Kampagne>/<SC_Name>/`) und NSC-Bögen (`Nichtspielercharaktere/`). |
| `06_orte/` | Abenteuerknoten, Städte, Festungen, Gebietsgefahren. |
| `07_fraktionen/` | Adelshäuser, Zirkel, Gilden, Orden, Machthierarchien. |
| `08_besondere_magische_gegenstaende/` | Einzigartige Artefakte, Relikte, Rechtsregister, Eigenschaften. |
| `09_chroniken/` | Kampagnen-Hub: Übersichtstabelle + fortlaufende Sitzungsprotokolle (`kampagnen/<name>/sitzungen/`). |
| `10_zeitlinie/` | Querschnitts-Chronologie: `historische_chronologie/`, `vorkommnisregister/`, `markwhen/` (`allgemeine_zeitlinie.mw`, `epochen/`, `kampagnen/`), `kalender/`, `exporte/`. |

### Prüf-Badges

Jeder validierte Abschnitt trägt das Standard-Badge:

```markdown
> 🛡️ *Geprüft: JJJJ-MM-TT | Geändert: JJJJ-MM-TT*
```

* **Neuer Text** → `Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]`, bis Sie ihn prüfen.
* **Änderungen nach einer Sitzung** berühren nur `Geändert`: Ist es neuer als `Geprüft`, muss der Abschnitt erneut geprüft werden.
* **Während eines Audits** werden beide Daten auf das heutige Datum gesetzt.

---

## 4. Referenz der Fähigkeiten

Rufen Sie die Fähigkeiten über ihren Slash-Befehl auf, wo verfügbar (VS Code, Claude Code), oder erwähnen Sie einfach den Namen im Chat — der Archivar leitet die Anfrage für Sie weiter.

| # | Fähigkeit | Wofür sie dient |
| :-: | :--- | :--- |
| 1 | `welt-initialisieren` | Geführte Einrichtung und Gerüst einer neuen Welt. |
| 2 | `struktur-validieren` | Strukturelle Gesundheitsprüfung des Archivs. |
| 3 | `sitzungsprotokoll` | Sitzungsprotokolle aus Rohnotizen oder Interview. |
| 4 | `charakter-dossier` | SC-Dossiers mit 5 Modulen und NSC-Bögen. |
| 5 | `magischer-gegenstand` | 4-Abschnitt-Register für magische Gegenstände. |
| 6 | `schritt-fuer-schritt-audit` | Interaktive Faktenprüfung, Aussage für Aussage. |
| 7 | `vollstaendiges-datei-audit` | Audit einer ganzen Datei oder eines Ordners. |
| 8 | `pruefungsstatus` | Prüfstatus-Dashboard aus den `🛡️`-Badges. |
| 9 | `bibel-struktur-synchronisieren` | Master-Weltenbibel + maschinenlesbares JSON. |
| 10 | `brauch-fest-ereignis` | Bräuche, Feste/Vorkommnisse, Einmal-Ereignisse. |
| 11 | `timeline-markwhen` | Grafische Markwhen-Zeitlinien (`.mw`). |

### 4.1 `welt-initialisieren` — Weltgerüst

* **Wann**: Sie starten eine brandneue Welt oder ein neues Kampagnen-Repository.
* **Wie**: `/welt-initialisieren` — *„Startet das Interview zur Konfiguration und Erstellung des Welt-Verzeichnisbaums.“*
* **Ergebnis**: der Zehn-Bände-Verzeichnisbaum mit `README.md`-Indizes, die Anfangsdateien der Masterdokumente (`WELTENBIBEL.md`, `weltstruktur.json`, …) und die dokumentierte Weltprämisse.

### 4.2 `struktur-validieren` — Strukturdiagnose

* **Wann**: vor/nach großen Umstrukturierungen oder wenn etwas falsch platziert wirkt.
* **Wie**: `/struktur-validieren` — *„Führt die strukturelle Konformitätsprüfung des Archivs aus.“*
* **Ergebnis**: ein Bericht über fehlende Ordner, fehlende `README.md`-Indize, tote Markdown-Links und verirrte `.md`-Dateien, die in einen der zehn Bände gehören.

### 4.3 `sitzungsprotokoll` — Chroniken & Sitzungsprotokolle

* **Wann**: direkt nach einer Spielsitzung.
* **Wie**: Fügen Sie Ihre Rohnotizen ein oder schreiben Sie *„Interview starten“* (`/sitzungsprotokoll`), um Frage für Frage geführt zu werden.
* **Ergebnis**: eine formelle Protokolldatei unter `09_chroniken/kampagnen/<name>/sitzungen/NN_titel.md` — notarielle Synopsis, Mermaid-Diagramm der SC-Aufhänger, prägende Phasen, optionales Regelwerk-Register — plus die aktualisierte Kampagnen-Übersichtstabelle.

### 4.4 `charakter-dossier` — SC-Dossiers & NSC-Bögen

* **Wann**: ein neuer Spielercharakter stößt dazu, ein NSC wird ausgearbeitet oder ein Dossiermodul muss aktualisiert werden.
* **Wie**: `/charakter-dossier` — *„Gib Typ (SC oder NSC), Charakternamen und Vorgang (erstellen, modul aktualisieren, bogen) an.“*
* **Ergebnis**: ein SC-Dossier mit 5 Modulen (`01_stammdaten_und_merkmale`, `02_integrierter_hintergrund`, `03_beziehungen_und_dynamiken`, `04_ausruestung_und_faehigkeiten`, `05_sl_aufhaenger_und_geheimnisse`) unter `05_charaktere/Spielercharaktere/<Kampagne>/<SC_Name>/`, oder ein NSC-Bogen unter `05_charaktere/Nichtspielercharaktere/`, beide in den Indizes eingetragen.

### 4.5 `magischer-gegenstand` — Besondere magische Gegenstände

* **Wann**: ein einzigartiges Artefakt, eine Relikt oder ein arkaner Fokus tritt in den Kanon ein.
* **Wie**: `/magischer-gegenstand` — *„Name des magischen Gegenstands und einzutragende oder zu aktualisierende Details.“*
* **Ergebnis**: ein Register mit 4 Abschnitten unter `08_besondere_magische_gegenstaende/`: technischer Bogen, Manufaktur, Mechaniken und Rechtsstatus.

### 4.6 `schritt-fuer-schritt-audit` — Atomare Faktenprüfung

* **Wann**: Sie wollen die Lore Aussage für Aussage prüfen, wobei der Assistent Sie jeden Punkt fragt.
* **Wie**: `/schritt-fuer-schritt-audit` — *„Gib die zu prüfende Datei oder das Thema sowie die Granularität (atomar oder abschnitt) an.“*
* **Ergebnis**: eine interaktive Prüfung ohne erfundene Korrekturen; geprüfte Abschnitte erhalten ihr aktualisiertes Badge.

### 4.7 `vollstaendiges-datei-audit` — Audit ganzer Dateien

* **Wann**: ein ganzes Dokument oder ein Ordner braucht eine organische Durchsicht.
* **Wie**: `/vollstaendiges-datei-audit` — *„Pfad der zu prüfenden Datei oder des Ordners (z. B. `05_charaktere/` oder einzelne .md).“*
* **Ergebnis**: ein strukturiertes Audit des gesamten Ziels, markierte Inkonsistenzen, zu Ihrer Freigabe vorgeschlagene Korrekturen.

### 4.8 `pruefungsstatus` — Prüfstatus-Dashboard

* **Wann**: Sie wollen einen Überblick, was geprüft und was veraltet ist.
* **Wie**: `/pruefungsstatus` — *„Erstellt oder aktualisiert das Prüfstatus-Dashboard des Workspace.“*
* **Ergebnis**: `PRUEFUNGSSTATUS.md` im Wurzelverzeichnis der Welt, mit Prozentsätzen je Datei und markierten Absätzen, die nach dem Audit geändert wurden.

### 4.9 `bibel-struktur-synchronisieren` — Master-Kanon-Synchronisation

* **Wann**: nach Kanon-Änderungen oder wenn Sie ein einzelnes narratives Masterdokument / eine maschinenlesbare Karte wollen.
* **Wie**: `/bibel-struktur-synchronisieren` mit einem Vorgang — `Bibel-generieren`, `Struktur-JSON-generieren`, `Bibel-aktualisieren` oder `Struktur-JSON-aktualisieren`.
* **Ergebnis**: `WELTENBIBEL.md` (monolithische narrative Kompilation der zehn Bände) und `weltstruktur.json` (hierarchische Taxonomie mit Metadaten).

### 4.10 `brauch-fest-ereignis` — Bräuche, Feste & Ereignisse

* **Wann**: eine Sitzung führt einen Brauch, ein wiederkehrendes Fest/Vorkommnis oder ein Einmal-Ereignis (Aufstand, Katastrophe, historische Erschütterung) ein.
* **Wie**: `/brauch-fest-ereignis` — *„Gib Typ und Eintrag an (z. B. 'brauch: Abschiedszeremonie', 'fest: Sonnenwendfest', 'ereignis: Belagerung der Zitadelle').“*
* **Ergebnis**: ein typologischer Bogen unter `03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/`, abgestimmt auf `10_zeitlinie/` (Chronologie und Vorkommnisregister).

### 4.11 `timeline-markwhen` — Grafische Zeitlinien

* **Wann**: Sie die Markwhen-Zeitlinienquellen erstellen, aktualisieren, validieren oder rendern wollen.
* **Wie**: `/timeline-markwhen` mit einem Vorgang — `mw-erstellen`, `mw-aktualisieren`, `mw-validieren` oder `mw-exportieren` (z. B. *„mw-erstellen epoche: Erstes Zeitalter“*, *„mw-aktualisieren kampagne: Chroniken des Nordens“*).
* **Ergebnis**: `.mw`-Quellen unter `10_zeitlinie/markwhen/` (`allgemeine_zeitlinie.mw`, `epochen/`, `kampagnen/`), synchron gehalten mit Chronologie, Vorkommnisregister und Protokollen; gerenderte Exporte unter `10_zeitlinie/exporte/`.

---

## 5. Typische Arbeitsabläufe

### A. Eine neue Welt einrichten

`welt-initialisieren` (geführtes Interview) → `struktur-validieren` (Konsistenzprüfung) → erste Lore-Bögen hinzufügen → `bibel-struktur-synchronisieren` (`Bibel-generieren`, `Struktur-JSON-generieren`), wann immer Sie die Masterdokumente wollen.

### B. Nach einer Spielsitzung (die Hauptschleife)

1. `sitzungsprotokoll` — Notizen einfügen (oder „Interview starten“); das Protokoll wird gespeichert und der Kampagnenindex aktualisiert.
2. Der Archivar listet jede betroffene Datei und bereitet die Queraktualisierungen vor (Dossiers, NSC-Bögen, Indize): Sie genehmigen sie eine nach der anderen.
3. Neuer Brauch/Fest/Ereignis erwähnt? → `brauch-fest-ereignis` schlägt den Bogen vor; Wiederholungen bekannter Ereignisse werden in `10_zeitlinie/` eingetragen.
4. `timeline-markwhen` (`mw-aktualisieren`, oder `mw-erstellen` für neue Kampagnen/Epochen) hält die `.mw`-Quellen synchron.
5. Hat die Sitzung den Kanon geändert? → `bibel-struktur-synchronisieren` (`Bibel-aktualisieren`, `Struktur-JSON-aktualisieren`).
6. Die Badges zeigen bereits, was sich geändert hat (`Geändert` > `Geprüft`): Ihre nächste Prüfung startet dort.

### C. Inhalte zwischen den Sitzungen hinzufügen

SC/NSC → `charakter-dossier` · Artefakt → `magischer-gegenstand` · Brauch/Fest/Ereignis → `brauch-fest-ereignis` · Große Umstrukturierung → `struktur-validieren`.

### D. Ein Prüf-/Audit-Durchgang

`pruefungsstatus` (sehen, was veraltet ist) → `schritt-fuer-schritt-audit` oder `vollstaendiges-datei-audit` auf die Ziele → `pruefungsstatus` erneut, um das Dashboard zu aktualisieren.

---

## 6. Fehlerbehebung

* **Der Agent oder die Fähigkeiten erscheinen nicht in VS Code** — die Dateien müssen im **Wurzelverzeichnis des Workspace** liegen: `.github/agents/` und `.agents/skills/`. Laden Sie das Fenster neu und öffnen Sie das Agenten-Auswahlmenü erneut.
* **Claude Code erkennt die Fähigkeiten nicht** — kopieren Sie `.agents/skills/*` nach `.claude/skills/` oder erstellen Sie einen Symlink; `CLAUDE.md` importiert bereits `AGENTS.md`.
* **Kein strukturierter Frage-Dialog erscheint** — das ist außerhalb von VS Code normal: Der Archivar weicht auf den Textchat aus und stellt dieselben Fragen als Text.
* **`mw-exportieren` kann nicht rendern** — installieren Sie die Markwhen-CLI (`npx @markwhen/mw`) oder nutzen Sie die Markwhen-VS-Code-Erweiterung / `markwhen.com`; Exporte sind optional und blockieren nie die `.mw`-Quellen.
* **Der Assistent hat Lore erfunden** — das verletzt die goldene Regel: Verweisen Sie ihn auf `AGENTS.md`, löschen Sie den erfundenen Text und starten Sie ein `schritt-fuer-schritt-audit` auf den betroffenen Abschnitt.
* **Die Platzhalter sammeln sich an** — suchen Sie nach `[VOM_SL_ZU_DEFINIEREN:` und lösen Sie sie während eines Audits auf, oder bitten Sie den Archivar, sie alle aufzulisten.
* **Gemischtsprachige Inhalte in einem Repo** — installieren Sie nur ein Sprachpaket pro Welt; löschen Sie die Dateien des anderen Pakets und starten Sie `struktur-validieren` erneut.
* **Alte Ordnernamen** (`06_location/`, `07_factions/`, …) — kein Problem: Der Archivar passt sich an, was existiert. Fest sind nur die *Rollen* der zehn Bände, nicht die Schreibweisen.

---

## 7. FAQ

* **Brauche ich alle 11 Fähigkeiten?** Nein. Installieren Sie sie alle (sie sind eigenständig) und nutzen Sie nur, was Sie brauchen.
* **Kann ich mehrere Kampagnen in einer Welt führen?** Ja — `09_chroniken/kampagnen/<name>/` hält die Protokolle jeder Kampagne getrennt; gemeinsame Lore lebt in den übrigen Bänden.
* **Kann ich es für bezahlte Kampagnen, Streams oder Actual Plays nutzen?** Ja. Die Nicht-Kommerz-Klausel betrifft den Verkauf der Werkzeugsammlung selbst, niemals die Spiele, die Sie damit leiten.
* **Kann ich die Fähigkeiten umverpacken oder verkaufen?** Nein — CC BY-NC-SA 4.0 (siehe `LICENSE` auf dem `main`-Branch).
* **Wie aktualisiere ich auf eine neue Version?** Klonen Sie den Sprach-Branch neu (oder `git pull`) und kopieren Sie die Dateien erneut; führen Sie lokale Anpassungen an `AGENTS.md` wieder zusammen.
* **Wo melde ich Bugs oder Harness-Erkenntnisse?** GitHub Issues — siehe `CONTRIBUTING.md` auf dem `main`-Branch.

---

*DMs_Companion ist frei nutzbar und teilbar unter CC BY-NC-SA 4.0. Wenn es Ihnen Vorbereitungszeit spart, können Sie das Projekt über [GitHub Sponsors](https://github.com/sponsors/Jollyproxi) oder [Buy Me a Coffee](https://buymeacoffee.com/jollyproxi) unterstützen — völlig optional.*
