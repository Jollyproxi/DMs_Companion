---
name: eigennamen-verlinken
description: "Use when: Eigennamen von Personen, Orten, Städten, Gegenständen, Fraktionen, Bräuchen und Ereignissen prüfen oder in Markdown-Links auf ihre kanonischen `.md`-Dateien umwandeln; Dateien, Ordner oder das gesamte Archiv scannen, um unverknüpfte Namen zu erkennen und die Konformität mit der Regel der verknüpften Eigennamen wiederherzustellen."
argument-hint: "Pfad der zu scannenden Datei oder des Ordners (oder 'ganzes Archiv')"
user-invocable: true
disable-model-invocation: false
---

# Skill: Pflichtverknüpfung von Eigennamen (`eigennamen-verlinken`)

Dieser Skill setzt die universelle Regel durch, dass jeder Eigenname einer Weltentität ein Markdown-Link auf die kanonische `.md`-Datei der Entität sein muss: Er durchsucht Dokumente, erkennt Namen, die als bloßer Klartext vorkommen, klassifiziert sie und schlägt ihre Umwandlung in Links vor bzw. wendet sie an, wobei bögenlose Entitäten dem SL gemeldet werden.

---

## 1. Referenzregel

- Jeder **Eigenname** einer Weltentität — Personen (SCs, NSCs), Häuser, Fraktionen, Gilden, Städte, Orte, Regionen, Ebenen, magische Gegenstände, Bräuche, Feste, Ereignisse, Epochen, Gesetze, Institutionen —, der im erzeugten Text vorkommt, muss ein **Markdown-Link** auf die kanonische `.md`-Datei dieser Entität sein, mit dem Eigennamen als Linktext: `[Name](relativer/pfad/datei.md)`.
- Der Pfad ist **relativ zur geschriebenen Datei** und muss auf eine tatsächlich auf der Festplatte existierende Datei verweisen.
- Der Linktext ist der Eigenname der Entität in seiner kanonischen Form (die des H1-Titels bzw. des Dateinamens des Bogens).
- **Ausnahmen** (Namen ohne Link zulässig):
  1. Überschriften und Dateinamen.
  2. YAML-Frontmatter, Codeblöcke, Befehle und Pfade.
  3. Beschriftungen von Mermaid-Diagrammen und Markwhen-`.mw`-Quellen (dort werden Markdown-Links nicht gerendert).
  4. Allgemeine Bezeichnungen ohne Bezug auf erfasste Entitäten.
- **Entität ohne Bogen**: Erfinde niemals den Bogen. Setze den Platzhalter `[VOM_SL_ZU_DEFINIEREN: Bogen fehlt für <Name>]` und melde die Lücke, oder frage — im interaktiven Modus — den SL, ob die Entität mit der passenden Skill zu erfassen ist (`charakter-dossier`, `magischer-gegenstand`, `brauch-fest-ereignis` usw.).

---

## 2. Aufbau des Entitätsindex

Baue vor dem Scan die Zuordnung `Name → Pfad der kanonischen Datei` auf:

1. **Bevorzugte Quelle**: Liegt `weltstruktur.json` im Wurzelverzeichnis des Workspaces, verwende sie als Index (Modulnamen und zugehörige Pfade).
2. **Direkte Durchsicht**: Andernfalls (oder ergänzend) durchsuche die zehn Bände — `05_charaktere/` (SCs und NSCs), `06_orte/`, `07_fraktionen/`, `08_besondere_magische_gegenstaende/`, `03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/`, `02_geografie/` (Regionen), `01_kosmologie/` (Ebenen), `04_recht_und_gesetze/` (oder `04_recht_und_erbfolge/`, Gesetze, Abkommen, Pakte, Gerichte), `10_zeitlinie/historische_chronologie/` (Epochen, historische Ereignisse) — und erfasse H1-Titel und Dateinamen.
3. **Kanonische Namen**: Für jeden Bogen ist der Eigenname der Dokumenttitel (H1) oder der Dateiname ohne Erweiterung; halte auch etwaige, im Bogen ausdrücklich dokumentierte Varianten oder Aliase fest.
4. **Homonyme**: Teilen zwei Entitäten denselben Namen, markiere die Mehrdeutigkeit und frage den SL, welcher Bogen verknüpft werden soll.

---

## 3. Operatives Verfahren

1. **Umfang festlegen**: Einzeldatei, Ordner oder ganzes Archiv (unter Ausschluss technischer Verzeichnisse wie `.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Text scannen**: Analysiere `.md`-Dateien Zeile für Zeile unter Ausschluss der Ausnahmen der §1 (Frontmatter, Codeblöcke, Mermaid-Beschriftungen, `.mw`-Quellen, Überschriften).
3. **Jedes Vorkommen klassifizieren**:
   - ✅ **Bereits verknüpft**: Der Name ist bereits ein gültiger Link (prüfe, ob das Ziel auf der Festplatte existiert).
   - 🔗 **Zu verknüpfen**: Bloßer Name mit vorhandenem Bogen → Umwandlung in einen Link.
   - ⚠️ **Ohne Bogen**: Bloßer Name einer nicht erfassten Entität → Platzhalter `[VOM_SL_ZU_DEFINIEREN: ...]`.
   - ❓ **Mehrdeutig**: Homonym oder unsichere Entsprechung → den SL befragen.
4. **Ergebnis berichten**: Zeige dem SL eine Tabelle (`datei:zeile | name | status | vorgeschlagene Aktion`).
5. **Nach Bestätigung anwenden**: Wandle Namen in korrekte relative Links um (berechne den Pfad anhand des Dateistandsorts neu); bei ⚠️-Fällen setze den Platzhalter und schlage die Erfassung mit der passenden Skill vor; bei ❓-Fällen warte auf die Entscheidung des SL.
6. **Abschlusszusammenfassung**: Liste die geänderten Dateien, die umgewandelten Namen und die offenen Lücken auf.

---

## 4. Integration mit den anderen Skills

- **`struktur-validieren`**: Dieser Skill bildet den **Pfeiler E** der Strukturdiagnose (Abdeckung verknüpfter Eigennamen); führe ihn zusammen mit den Prüfungen A–D für ein vollständiges Audit aus.
- **Audit-Skills (`schritt-fuer-schritt-audit`, `vollstaendiges-datei-audit`)**: Prüfe während des Audits auch, ob Eigennamen verknüpft sind, und stelle die Konformität im Zuge der vom SL genehmigten Korrekturen wieder her.
- **Bogen-Erstellungsskills (`charakter-dossier`, `magischer-gegenstand`, `brauch-fest-ereignis`)**: Jeder neue Bogen macht seinen Namen verknüpfbar; weise bei der Erstellung darauf hin, in welchen bestehenden Dateien der neue Name verknüpft werden soll, und schlage die Aktualisierung der Verweise vor.
- **`bibel-struktur-synchronisieren`**: In der Weltenbibel folgen Eigennamen derselben Konvention und bleiben Links auf ihre Ursprungsmodule.
- **`pruefungsstatus`**: Offene Lücken (Namen ohne Bogen) können im Dashboard `PRUEFUNGSSTATUS.md` als Einträge zur Erfassung nachverfolgt werden.
