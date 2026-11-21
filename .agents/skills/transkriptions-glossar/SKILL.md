---
name: transkriptions-glossar
description: "Use when: eine kompakte reine Rechtschreibliste bereits bekannter Eigennamen (ohne Fakten oder Spoiler) erzeugen, um sie zusammen mit dem Sitzungstranskriptions-Prompt in NotebookLM oder ein anderes LLM hochzuladen und `[?]`-Markierungen zu verringern."
argument-hint: "Kampagne/Sitzung angeben (z. B. 'kampagne: Chroniken des Nordens'), Ordner/Gebiet oder 'ganzes Archiv', etwaige zusätzlich gesprochene Namen und ob eine .txt-Datei gespeichert werden soll"
user-invocable: true
disable-model-invocation: false
---

# Skill: Transkriptions-Glossar für Eigennamen (`transkriptions-glossar`)

Dieser Skill extrahiert aus dem Repository eine **kompakte reine Textliste mit der genauen Schreibweise kanonischer Eigennamen** (SCs, NSCs, Orte, Fraktionen, Gegenstände, Bräuche, Feste, Ereignisse, Gottheiten und Schlüsselbegriffe) als Hilfsquelle für **NotebookLM** oder ein anderes LLM zusammen mit [sitzungstranskription-prompt](../sitzungsprotokoll/references/sitzungstranskription-prompt.md), um `[?]`-Markierungen und Hörfehler in Sitzungsberichten zu minimieren.

> **📌 Ausnahme von der Regel verknüpfter Eigennamen**: der für NotebookLM/LLM exportierte Textblock (sowie eine optional gespeicherte `.txt`-Datei) ist für ein externes Werkzeug gedacht und muss **reiner Klartext ohne Markdown-Links** (`[Name](...)`) bleiben. Erläuterungen im Chat außerhalb des Blocks und alle kanonischen `.md`-Dateien unterliegen weiterhin dem Skill `eigennamen-verlinken`.

---

## 1. Goldene Regel: Nur Schreibweise, Keine Fakten & Keine Halluzinationen

- **Ausschließlich Rechtschreibung**: nimm **nur** die exakte kanonische Schreibweise jedes Eigennamens auf, ausdrücklich dokumentierte Schreibvarianten oder Aliase/Spitznamen aus dem Bogen (z. B. `Kanonischer Name (Alias: Spitzname)`) sowie optional bei aktiven SCs die Zuordnung `Spieler → SC`, sofern bereits dokumentiert oder vom SL angegeben.
- **Striktes Fakten- und Spoilerverbot**: füge **niemals** Beschreibungen, narrative Rollen, Fraktionszugehörigkeiten, Beziehungen, Lebensstatus (lebendig/tot/Verräter), aktuellen Aufenthaltsort, Spielwerte, SL-Geheimnisse oder Lore-Auszüge hinzu. Alles über die bloße Schreibweise hinaus birgt das Risiko, dass das Transkriptionsmodell Archiv-Lore als angeblich am Spieltisch gesagt einfließen lässt.
- **Schutzklausel im Kopfbereich**: jedes erzeugte Glossar beginnt mit einer festen Hinweiszeile für das Transkriptions-LLM, die Liste **ausschließlich für die Schreibweise** gehörter Namen zu nutzen und weder ungenannte Namen zu übernehmen noch Fakten oder Beziehungen abzuleiten.
- **Zusätzliche Namen aus der gerade gespielten Sitzung**: nennt der SL neue, noch nicht archivierte Namen aus der Sitzung, nimm sie ausschließlich zur Transkriptionshilfe in den dafür vorgesehenen Abschnitt auf, ohne Bögen anzulegen oder den Kanon zu ändern.
- **Keine Erfindungen**: fehlt im Archiv eine gesicherte Schreibweise oder besteht Unklarheit, rate niemals und vereinheitliche nicht eigenmächtig; melde dies außerhalb des Blocks mit `[VOM_SL_ZU_DEFINIEREN: ...]` oder frage den SL vor dem Export.

---

## 2. Auswahlbereiche (Rauschkontrolle)

Um den Transkriptionskontext nicht mit Dutzenden fernen Namen zu überfrachten, die phonetische Fehlzuordnungen begünstigen, biete einen von drei Bereichen an:

- **Modus A — Kampagnen- / Sitzungsfokus *(Empfohlener Standard)***:
  - Aktive SCs der Kampagne (`05_charaktere/<Spielercharaktere>/<Kampagne_oder_Gruppe>/`, Standard `Spielercharaktere/<Kampagne>/`).
  - Eigennamen, die in der `README.md` der Kampagne und in den letzten **N Sitzungsprotokollen** vorkommen (Standard: die letzten **5** Protokolle unter `09_chroniken/<kampagnen>/<kampagnenname>/<sitzungen>/`).
  - Kanonische Entitäten des aktuellen geografischen Schauplatzes bzw. der Region, sofern vom SL genannt oder in der Kopfzeile des letzten Protokolls vermerkt.
  - Etwaige neue oder spontane Namen, die der SL für die aufgezeichnete Sitzung zusätzlich nennt.
- **Modus B — Gezieltes Gebiet, Ordner oder Fraktion**:
  - Aktive SCs der Kampagne (sofern relevant) + alle kanonischen Entitäten in den vom SL genannten Ordnern, Regionen, Fraktionen oder Bänden (z. B. `06_orte/<region>/`, `07_fraktionen/<haus>/`, `04_recht_und_gesetze/`).
- **Modus C — Gesamtes Archiv**:
  - Alle kanonischen Eigennamen über die Zehn Bände hinweg.
  - **Anti-Rausch-Schwelle**: überschreitet die Liste etwa **250–300 Einträge**, weise den SL ausdrücklich darauf hin, dass ein zu großes Glossar phonetische Verwechslungen in NotebookLM/LLM fördern kann, und biete die Eingrenzung auf Modus A oder B an.

---

## 3. Quellen & Extraktionsregeln

1. **Bevorzugter Index**: liegt `weltstruktur.json` im Wurzelverzeichnis des Workspaces, lies ihn zuerst, um Bände, Module und kanonische Pfade schnell zu erfassen, ohne unnötige Prosa zu laden.
2. **Direkte Durchsicht / Ergänzung in den Zehn Bänden**: durchsuche (oder ergänze aus) die Ordner der Spielwelt gemäß der realen Repository-Struktur — einschließlich benutzerdefinierter oder älterer Ordnernamen (`06_location/`, `07_factions/`, `08_oggetti magici peculiari/`, `cornici/`, `expeditionen/`, `tagebuecher/`) und unter Beachtung der NSC-Ablagekonvention aus den Projektanweisungen und dem Index von `05_charaktere/`:
   - `05_charaktere/` (modulare SC-Dossiers und NSC-Bögen)
   - `06_orte/` (Städte, Abenteuerknoten, Festungen, Gebietsgefahren) und `02_geografie/` (Regionen/Großgebiete)
   - `07_fraktionen/` (Adelshäuser, Zirkel, Gilden, Orden, Institutionen)
   - `<08_besondere_magische_gegenstaende>/` (Artefakte, Relikte, einzigartige Gegenstände)
   - `03_gesellschaft_und_politik/` (`voelker/`, `braeuche_feste_und_ereignisse/`), `01_kosmologie/` (Ebenen, Pantheon/Gottheiten), `04_recht_und_gesetze/` (Gesetze, Abkommen, Gerichte) und `10_zeitlinie/historische_chronologie/` (Epochen, historische Ereignisse)
   - `09_chroniken/` (für Modus A: Kampagnenindex und aktuelle Protokolle)
3. **Ausschlüsse**:
   - Schließe technische Verzeichnisse (`.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`) sowie Meta- und Masterdateien (`README.md`, `AGENTS.md`, `CLAUDE.md`, `WELTENBIBEL.md`, `PRUEFUNGSSTATUS.md`, `NUTZUNGSANLEITUNG.md`, `weltstruktur.json`, `.mw`-Quellen oder Exporte) aus.
   - Verwende keine generischen Strukturüberschriften (z. B. *Allgemeiner Rahmen*, *Index*, *Synopsis*, *Sitzung 01*, *Status des Vorkommnisses*) und keine Platzhalter `[VOM_SL_ZU_DEFINIEREN: ...]`.
4. **Normalisierung und Deduplizierung**:
   - Extrahiere für jeden kanonischen Bogen den Eigennamen aus der H1-Überschrift (ohne Zahlenpräfixe wie `01_`, Typbezeichnungen wie `NSC-Bogen:` / `SC-Dossier:` / `Magischer Gegenstand:`, `🛡️`-Badges oder beschreibende Untertitel nach `—` oder `|`) bzw. ersatzweise aus dem bereinigten Dateinamen.
   - Extrahiere bei 5-teiligen SC-Dossiers die Identität **genau einmal** aus dem SC-Ordnernamen oder Stammdaten-Modul (`01_stammdaten...`), ohne die 5 Moduldateinamen zu wiederholen.
   - Übernimm Aliase oder Spitznamen nur, wenn sie ausdrücklich im kanonischen Bogen dokumentiert sind (`Aliase`, `Spitznamen`, `Varianten`); füge niemals erklärende Zusätze in Klammern hinzu.
   - Entferne doppelte Schreibweisen und sortiere innerhalb jeder Kategorie alphabetisch.

---

## 4. Operatives Verfahren & Strukturierte Interaktion

1. **Parameter klären (falls vom SL nicht bereits angegeben)**:
   Frage über das interaktive Fragewerkzeug der Umgebung (`vscode_askQuestions`, `AskUserQuestion`, `ask_question`, `request_user_input`, falls verfügbar; sonst direkt im Chat):
   - **`bereich`**: *Welchen Bereich soll das Glossar abdecken?*
     - Optionen: *Kampagne / Aktuelle Sitzung — empfohlen* (unter Auflistung der in `09_chroniken/` erkannten Kampagnen), *Gezieltes Gebiet, Ordner oder Fraktion*, *Gesamtes Archiv (alle Zehn Bände)*.
   - **`zusatz_namen`**: *Gibt es neu gesprochene Namen aus der letzten Sitzung (Gast-SCs, neue NSCs, Orte oder Begriffe, noch nicht im Archiv), die nur für die Transkription aufgenommen werden sollen?* (Optionaler Freitext oder *Keine*).
   - **`ausgabeziel`**: *Wie soll das Glossar bereitgestellt werden?*
     - Optionen: *Nur im Chat (fertig zum Kopieren in NotebookLM) — empfohlen*, *Im Chat + zusätzlich als `.txt`-Datei im Repository speichern*.
2. **Extraktion und Anti-Spoiler-Prüfung**:
   - Wende die Regeln aus §3 auf den gewählten Bereich an.
   - Prüfe, dass kein Eintrag Beschreibungen, Verwandtschaften, Zugehörigkeiten, Status oder Handlungsdetails enthält.
   - Lasse leere Kategorien weg. Überschreitet die Gesamtzahl ~250–300 Einträge, warne den SL und biete eine engere Kampagnen- oder Szenenauswahl an.
3. **Bereitstellung des Glossars**:
   - Gib das vollständige Glossar **immer** direkt im Chat in einem `text`-Codeblock aus, fertig zum Einfügen in NotebookLM (*Quelle hinzufügen → Kopierter Text*) oder ein anderes LLM.
   - Gib direkt außerhalb des Blocks eine knappe Übersicht aus: gewählter Bereich, Anzahl pro Kategorie und gesamt, geprüfte Quellen sowie etwaige unklare Schreibweisen im Archiv.
   - Falls auch Dateispeicherung gewünscht wurde, schreibe eine **UTF-8-`.txt`-Datei** im Kampagnenordner — `09_chroniken/<kampagnen>/<kampagnenname>/transkriptions_glossar.txt` *(Standard: `09_chroniken/kampagnen/<kampagnenname>/transkriptions_glossar.txt`; bzw. Wurzelverzeichnis oder Zielpfad, falls noch kein Kampagnenordner existiert)* — ohne `.md`-Endung, damit Prüfungen von `struktur-validieren`, `eigennamen-verlinken`, `pruefungsstatus` und `bibel-struktur-synchronisieren` unberührt bleiben.

---

## 5. Kanonische Ausgabevorlage

Gib ausschließlich einen kompakten Textblock in diesem Format aus (leere Kategorien weglassen):

````text
# EIGENNAMEN-GLOSSAR (NUR SCHREIBWEISE — KEINE NICHT GENANNTEN FAKTEN AUS DER SITZUNG IMPORTIEREN)
Kampagne / Bereich: <Kampagnenname oder Bereich>

## Spielercharaktere (SCs)
- <SC-Name> (<Spieler → SC> nur falls dokumentiert/genannt, optional)
- <SC-Name> (Alias: <Dokumentierter Spitzname>)

## Nichtspielercharaktere (NSCs) & Bedeutende Kreaturen
- <NSC-Name>
- <NSC-Name> (Alias: <Dokumentierter Spitzname / Schreibvariante>)

## Orte, Städte & Regionen
- <Ort / Region>

## Fraktionen, Häuser & Institutionen
- <Fraktion / Haus>

## Gegenstände, Artefakte & Relikte
- <Gegenstand>

## Bräuche, Feste, Ereignisse, Gottheiten & Schlüsselbegriffe
- <Brauch / Fest / Ereignis / Gottheit / Gesetz>

## Zusätzliche Sitzungsnamen (noch nicht archiviert)
- <Vom SL genannter gesprochener Name>
````

---

## 6. Integration mit den anderen Skills

- **`sitzungsprotokoll` und `sitzungstranskription-prompt`**: dieser Skill erzeugt genau die optionale Hilfsquelle aus Schritt 2 von [sitzungstranskription-prompt](../sitzungsprotokoll/references/sitzungstranskription-prompt.md) und verringert `Name[?]`-Markierungen vor dem Import über Kanal C von `sitzungsprotokoll`.
- **`eigennamen-verlinken`**: teilt die Erfassungslogik kanonischer Entitäten über die Zehn Bände und den JSON-Index; das erzeugte Glossar ist von Markdown-Links befreit, da es als reiner Text für NotebookLM/LLM dient.
- **`bibel-struktur-synchronisieren`**: nutzt, sofern vorhanden, `weltstruktur.json` als schnellen Namensindex, ohne die Langprosa der `WELTENBIBEL.md` vollständig einlesen zu müssen.
- **`struktur-validieren`**: der optionale Export nutzt `.txt` im Kampagnenordner, um Prüfungen auf defekte Links, `🛡️`-Badges und verwaiste `.md`-Dateien nicht zu stören.
