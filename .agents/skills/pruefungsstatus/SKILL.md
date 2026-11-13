---
name: pruefungsstatus
description: "Use when: das Lore-Prüfstatus-Dashboard (PRUEFUNGSSTATUS.md) erstellen oder aktualisieren, Prüfquoten berechnen, abgeschlossene Dateien verfolgen und nach dem letzten Audit geänderte Absätze erkennen."
argument-hint: "Erstellt oder aktualisiert das Prüfstatus-Dashboard des Workspace"
user-invocable: true
disable-model-invocation: false
---

# Skill: Lore-Prüfstatus-Dashboard (`pruefungsstatus`)

Dieser Skill erstellt, aktualisiert und pflegt die Kontroll- und Übersichtsdatei `PRUEFUNGSSTATUS.md` im Wurzelverzeichnis des Workspace und bietet dem Spielleiter auf einen Blick den Stand der Faktenprüfung sowie Abschnitte mit erneuten Prüfbedarf.

> **📌 Regel: Eigennamen als Verknüpfungen**: Jeder Eigenname einer Weltentität (SCs, NSCs, Fraktionen, Häuser, Städte, Orte, magische Gegenstände, Bräuche, Feste, Ereignisse …), der im erzeugten Text vorkommt, muss eine **Markdown-Verknüpfung** zur kanonischen `.md`-Datei der Entität sein (z. B. `[Name](relativer/pfad/datei.md)`), niemals bloßer Klartext. Ausnahmen: Überschriften, Dateinamen, Frontmatter, Codeblöcke, Mermaid-Knoten und `.mw`-Quellen. Entität ohne Bogen: niemals erfinden — `[VOM_SL_ZU_DEFINIEREN: Bogen fehlt für <Name>]` verwenden und die Lücke melden. Prüfung und Umwandlung: Skill `eigennamen-verlinken`.

---

## 1. Kriterien zur Statusklassifizierung

Der Skill untersucht die Markdown-Dateien der kanonischen Weltordner (`01_kosmologie`, `02_geografie`, `03_gesellschaft_und_politik` einschließlich optionalem `voelker/` und der Unterserie `braeuche_feste_und_ereignisse/`, `04_recht_und_gesetze`, `05_charaktere`, `06_orte`, `07_fraktionen`, `08_besondere_magische_gegenstaende` oder angepasster Bandname, `09_chroniken`, `10_zeitlinie` — rekursiv auch in optionalen oder benutzerdefinierten Unterordnern) und wertet die Badges aus:

```markdown
> 🛡️ *Geprüft: [DATUM_G] | Geändert: [DATUM_A]*
```

### Konformitätsstufen:
* 🟢 **Vollständig geprüft**: Alle Abschnitte des Dokuments tragen Badges mit `DATUM_G >= DATUM_A` und enthalten keine `[VOM_SL_ZU_DEFINIEREN]`-Platzhalter.
* 🟡 **Teilweise geprüft / Unvollständig**: Einige Abschnitte tragen Badges, andere fehlen oder enthalten `[VOM_SL_ZU_DEFINIEREN]`-Markierungen.
* 🟠 **Nach Audit geändert (Nachprüfung nötig)**: Mindestens ein Abschnitt zeigt `DATUM_A > DATUM_G`, was auf Änderungen nach einer Sitzung oder außerhalb des letzten formellen Audits hinweist.
* ⚪ **Nicht geprüft**: Kein Prüf-Badge in der Datei vorhanden.

---

## 2. Struktur der Datei `PRUEFUNGSSTATUS.md`

Speichere `PRUEFUNGSSTATUS.md` im Wurzelverzeichnis des Workspace nach diesem Schema:

```markdown
# Kanon-Prüfregister & Statusübersicht

Dieses Register dokumentiert den Fortschritt der formellen Lore-Prüfung und erfasst sowohl vom Spielleiter bestätigte als auch im Spielverlauf veränderte Abschnitte.

* **Letztes allgemeines Audit:** [DATUM]
* **Gesamtabdeckung des Kanons:** [PROZENTSATZ]%

---

## 1. Sektor-Übersichtstabelle

| Abschnitt / Band | Dateien gesamt | Geprüft 🟢 | Nach Audit 🟠 | Teilweise 🟡 | Ungeprüft ⚪ | Status |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **01 Kosmologie** | X | A | B | C | D | [Symbol] |
| **02 Geografie** | X | A | B | C | D | [Symbol] |
| **03 Gesellschaft & Politik** | X | A | B | C | D | [Symbol] |
| **03· Bräuche, Feste & Ereignisse** | X | A | B | C | D | [Symbol] |
| **04 Recht & Gesetze** | X | A | B | C | D | [Symbol] |
| **05 Charaktere (SC & NSC)** | X | A | B | C | D | [Symbol] |
| **06 Orte** | X | A | B | C | D | [Symbol] |
| **07 Fraktionen** | X | A | B | C | D | [Symbol] |
| **08 Besondere Magische Gegenstände** | X | A | B | C | D | [Symbol] |
| **09 Kampagnenchroniken** | X | A | B | C | D | [Symbol] |
| **10 Zeitlinie & Vorkommnisse** | X | A | B | C | D | [Symbol] |

---

## 2. Prioritäre Einträge zur Überprüfung

### Dateien mit Änderungen nach Audit (🟠)
* [pfad/datei.md](pfad/datei.md) — *Geändert am [DATUM] (Geprüft am [DATUM])*

### Dateien mit expliziten Lücken (🟡 `[VOM_SL_ZU_DEFINIEREN]`)
* [pfad/datei.md](pfad/datei.md) — *Abschnitt [Name]: [Beschreibung der Unklarheit]*

---

## 3. Historie der Audit-Sitzungen
* **JJJJ-MM-TT**: [Vollständiges / Teilweises] Audit auf [Ordner oder Datei] über `[schritt-fuer-schritt-audit / vollstaendiges-datei-audit]`.
```

---

## 3. Operatives Verfahren

1. **Scan**: Durchsuche rekursiv alle relevanten `.md`-Dateien im Workspace unter Ausschluss technischer Verzeichnisse (z. B. `.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Auslesen der Flags**: Ermittle in jeder Datei `🛡️`-Badges, `Geprüft`- und `Geändert`-Daten sowie `[VOM_SL_ZU_DEFINIEREN]`-Markierungen.
3. **Statistikberechnung**: Berechne Zählwerte und Quoten für jeden der zehn kanonischen Bände (mit gesonderter Ausweisung für die Unterserie `braeuche_feste_und_ereignisse/`).
4. **Schreiben / Aktualisieren**: Erstelle oder aktualisiere `PRUEFUNGSSTATUS.md` im Wurzelverzeichnis des Workspace.
