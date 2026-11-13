---
name: brauch-fest-ereignis
description: "Use when: Alltagsbräuche und Besonderheiten, wiederkehrende Feste und Ereignisse (Vorkommnisse) sowie einmalige Ereignisse der Spielwelt erfassen; Bögen unter 03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/ erstellen oder aktualisieren und 10_zeitlinie/ (historische Chronologie, Vorkommnisregister und grafische Markwhen-Zeitlinie) pflegen."
argument-hint: "Gib Typ und Eintrag an (z. B. 'brauch: Abschiedszeremonie', 'fest: Sonnenwendfest', 'ereignis: Belagerung der Zitadelle')"
user-invocable: true
disable-model-invocation: false
---

# Skill: Bräuche, Feste & Ereignisse (`brauch-fest-ereignis`)

Dieser Skill verwaltet die Unterserie `03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/` und deren Verzahnung mit Band `10_zeitlinie/`: er katalogisiert Besonderheiten des Alltagslebens, wiederkehrende Feste und Vorkommnisse sowie einmalige Ereignisse nach demselben notariellen Maßstab wie das übrige Archiv.

> **📌 Regel: Eigennamen als Verknüpfungen**: Jeder Eigenname einer Weltentität (SCs, NSCs, Fraktionen, Häuser, Städte, Orte, magische Gegenstände, Bräuche, Feste, Ereignisse …), der im erzeugten Text vorkommt, muss eine **Markdown-Verknüpfung** zur kanonischen `.md`-Datei der Entität sein (z. B. `[Name](relativer/pfad/datei.md)`), niemals bloßer Klartext. Ausnahmen: Überschriften, Dateinamen, Frontmatter, Codeblöcke, Mermaid-Knoten und `.mw`-Quellen. Entität ohne Bogen: niemals erfinden — `[VOM_SL_ZU_DEFINIEREN: Bogen fehlt für <Name>]` verwenden und die Lücke melden. Prüfung und Umwandlung: Skill `eigennamen-verlinken`.

---

## 1. Goldene Regel (Keine Halluzinationen)

- Erfinde niemals Bräuche, Daten, Rituale, Teilnehmer oder Ergebnisse, die nicht vom SL genannt oder bereits in kanonischen Dateien belegt sind.
- Fehlendes Detail: frage im interaktiven Modus beim SL nach (über das strukturierte Fragewerkzeug der Umgebung wie `vscode_askQuestions` oder `AskUserQuestion`, falls verfügbar; sonst direkt im Chat); füge im direkten Schreibmodus `[VOM_SL_ZU_DEFINIEREN: Beschreibung]` ein.

---

## 2. Typologische Taxonomie

Die Einordnung richtet sich nach dem **Wesen** des Eintrags, nicht bloß nach seiner Häufigkeit:

| Typ | Unterordner | Wesen | Beispiele |
| :--- | :--- | :--- | :--- |
| **Brauch** | `braeuche/` | Besonderheiten des Alltagslebens: soziale Verhaltensweisen, Rituale, kodifizierte Formen und Umgangsweisen (Aufbau und Vollzug des Ritus). | Gruß- oder offizielle Abschiedszeremonien; Gastfreundschaftsrituale; Tischsitten; Anredeformen. |
| **Fest / Vorkommnis** | `feste_und_vorkommnisse/` | **Wiederkehrende institutionelle oder rituelle** Ereignisse mit **fester** (Kalender) oder **auslösergebundener variabler** Periodizität (Bedingungen für das Einsetzen, vorziehbare Termine). | Wintersonnenwendfest; Ausleseturnier der Garde (bei Rückkehr von Feldzügen); Wahlen (feste Fristen, aber bei Sonderlagen vorziehbar). |
| **Einmaliges Ereignis** | `ereignisse/` | Von Natur aus **einzigartig oder nicht wiederholbar**: historische Umbrüche, Aufstände, Kataklysmen, Wendepunkte. Kann **historisch (vergangen)** oder **bevorstehend/laufend** sein (Ausgang in Sitzungen entschieden). Auch wenn sich Ähnliches wiederholen könnte, bleibt es wesensgemäß hier. | Belagerung einer Zitadelle; Bergarbeiteraufstand; gebrochener Pakt; Naturkatastrophe. |

Wirkt ein Eintrag hybrid (z. B. ein institutioneller Ritus, der in einen Umsturz umschlug), ordne ihn nach seinem vorherrschenden Wesen ein und setze einen Querverweis zum verknüpften Bogen.

---

## 3. Ordnerstruktur & Dateinamen

```text
03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/
├── README.md                       # Index der Unterserie (ein Abschnitt pro Typ)
├── braeuche/
│   ├── README.md
│   └── 01_<eintrag_slug>.md        # Fortlaufendes Nummernpräfix je Unterordner
├── feste_und_vorkommnisse/
│   ├── README.md
│   └── 01_<eintrag_slug>.md
└── ereignisse/
    ├── README.md
    └── 01_<eintrag_slug>.md
```

- Dateinamen: `NN_slug_in_snake_case.md`, fortlaufende Nummerierung je Unterordner (z. B. `01_abschiedszeremonie.md`, `02_...`).
- Jeder Unterordner sowie der übergeordnete Ordner erhalten eine Index-`README.md`, die bei jedem neuen Bogen aktualisiert wird.

---

## 4. Bogenvorlage — Brauch

```markdown
# [Name des Brauchs]

> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*

## Einordnung
Was es ist, wo und wann es gepflegt wird, wer zur Einhaltung verpflichtet ist.

## Formalismus & Formen
Schrittweiser Ablauf des Ritus/Verhaltens: Gesten, Formeln, Reihenfolge der Handlungen, Zeitpunkte, Tonfall.

## Varianten & Abstufungen
Unterschiede nach sozialem Rang, Fraktion, Region oder Rahmen (Hof, Marktplatz, öffentliche Zeremonie...).

## Bedeutung & Sanktionen
Symbolischer und historischer Wert des Brauchs; Folgen von Verstößen (sozial, rechtlich, rituell).

## Verknüpfungen & SL-Aufhänger
Verweise auf NSCs, Fraktionen, Orte oder andere Bögen (relative Links). Dem SL vorbehaltene Aufhänger.

## Regelauswirkungen *(optional)*
Eventuelle Spieleffekte (Modifikatoren, Vorteil, Inspiration). Nur ausfüllen, wo sinnvoll.
```

---

## 5. Bogenvorlage — Fest / Vorkommnis

```markdown
# [Name des Festes / Wiederkehrenden Ereignisses]

> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*

## Einordnung
Was es ist, wer es feiert/leitet, Bedeutung und Stellung in der Kultur der Welt.

## Periodizität & Auslöser
- **Periodizität**: fest (Kalender) / variabel mit Auslöser / gemischt.
- **Auslöser (Trigger)**: Bedingungen, die das Ereignis einleiten (z. B. „Rückkehr eines Feldzugs“, „Tod des Amtsträgers“, „Ratsbeschluss“).

## Zeitfenster
Geplante Fristen, Vorlaufzeiten, Möglichkeiten und Gründe für Vorverlegung oder Aufschub (z. B. vorgezogene Wahlen aus besonderem Anlass).

## Ablauf
Rituale, Phasen, Zeremonien, Dauer, Abfolge der Handlungen.

## Teilnehmer & Rollen
Wer den Vorsitz führt, wer teilnimmt, Zugangsvoraussetzungen, Ausgeschlossene, beteiligte Amtsrollen.

## Bekannte Vorkommnisse
| Ausgabe / Datum | Status | Ausgang | Zeitlinie |
| :--- | :--- | :--- | :--- |
| [Weltjahr oder Datum] | geplant / laufend / abgeschlossen | [Ergebnis] | [Link zu 10_zeitlinie] |

## Verknüpfungen & SL-Aufhänger
Verbindungen zu NSCs, Fraktionen, Orten, Bräuchen oder verwandten Ereignissen. Dem SL vorbehaltene Aufhänger.

## Regelauswirkungen *(optional)*
Eventuelle Spieleffekte. Nur ausfüllen, wo sinnvoll.
```

---

## 6. Bogenvorlage — Einmaliges Ereignis

```markdown
# [Name des Ereignisses]

> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*

## Einordnung
Was geschehen ist (oder geschehen wird): Wesen des Umbruchs und historische Verortung. Angeben, ob **historisch** oder **laufend**.

## Ursachen & Voraussetzungen
Kontext, Spannungen, Entscheidungen oder Zufälle, die das Ereignis vorbereitet haben.

## Ablauf
Phasen des Ereignisses in chronologischer Folge.

## Folgen & Auswirkungen
Auswirkungen auf Orte, Fraktionen, Institutionen, NSCs und das Gleichgewicht der Welt.

## Status des Vorkommnisses
- **Status**: geplant / laufend / abgeschlossen.
- **Ausgang** (falls abgeschlossen): [Zusammenfassung].
- **Datum / Zeitraum**: [Weltjahr].

## Beteiligte & Zeugen
Beteiligte oder anwesende NSCs, SCs, Fraktionen oder Völker (mit Links zu den Bögen).

## Verknüpfungen & SL-Aufhänger
Querverweise und dem SL vorbehaltene Aufhänger.

## Regelauswirkungen *(optional)*
Eventuelle Spieleffekte. Nur ausfüllen, wo sinnvoll.
```

---

## 7. Erstellungsverfahren (Geführtes Interview)

Stelle dem SL folgende Fragen (über das interaktive Fragewerkzeug der Umgebung wie `vscode_askQuestions` oder `AskUserQuestion`, falls verfügbar; sonst im Chat):

1. **Typologie**: *Handelt es sich um einen Brauch, ein wiederkehrendes Fest/Vorkommnis oder ein einmaliges Ereignis?* (Optionen mit Erklärung der Wesensunterscheidung aus §2).
2. **Name & Kontext**: *Name des Eintrags und, falls bekannt, Kontext (Fraktion, Ort, Zeitraum)?* (Freitext).
3. **Typologische Felder**: erfasse die Felder der gewählten Vorlage (bei Festen: feste/variable Periodizität, Auslöser, Zeitfenster; bei Ereignissen: historisch oder laufend).
4. **Erstellung**: lege die Datei mit fortlaufendem Nummernpräfix im passenden Unterordner an, fülle bekannte Abschnitte aus und kennzeichne Lücken mit `[VOM_SL_ZU_DEFINIEREN: ...]`.
5. **Badge**: setze `> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*`.
6. **Fortschreibung**: aktualisiere die verknüpften `README.md`-Dateien, schlage die Aktualisierung von `10_zeitlinie/` vor und empfiehl bei Aufnahme in den Dokumentenkanon `bibel-struktur-synchronisieren` (`Bibel-aktualisieren`, `Struktur-JSON-aktualisieren`).

---

## 8. Verwaltung von Vorkommnissen (Bereits erfasste Ereignisse)

Findet in einer Sitzung eine Wiederkehr eines bereits erfassten Festes oder Vorkommnisses statt (z. B. ein jährliches Turnier):

1. **Protokoll**: dokumentiere das Vorkommnis im Sitzungsprotokoll (`sitzungsprotokoll`).
2. **Zeitlinie**: erfasse das Vorkommnis in `10_zeitlinie/` (Vorkommnisregister + Markwhen-Quellen) samt Status und Ausgang.
3. **Kanonischer Bogen**: **frage den SL**, ob der Bogen geändert werden soll.
   - Besonderheiten jenes einzelnen Vorkommnisses (Zahlen, Teilnehmer, Ausgänge, Zwischenfälle) **verbleiben in Zeitlinie und Protokollen**.
   - Der Bogen wird **nur dann** aktualisiert, wenn jene Besonderheiten **das Wesen des Eintrags verändern** (z. B. neue Regeln, veränderte Rolle oder Bedeutung des Ritus). Aktualisiere dann auch die Tabelle „Bekannte Vorkommnisse“.

---

## 9. Aktualisierung von `10_zeitlinie/`

Für jeden neuen Eintrag, jedes Vorkommnis und jeden Statuswechsel (geplant → laufend → abgeschlossen):

1. **Historische Chronologie** (`10_zeitlinie/historische_chronologie/`, nach Epoche/Zeitraum): für vergangene Ereignisse, mit Kategorie-Tags (z. B. `#ereignis #historisch`).
2. **Vorkommnisregister** (`10_zeitlinie/vorkommnisregister/`, nach Epoche/Zeitraum): für Instanzen wiederkehrender Feste/Ereignisse und laufende Einträge.
3. **Markwhen** (`10_zeitlinie/markwhen/`): aktualisiere oder erstelle `.mw`-Quellen über den eigenen Skill `timeline-markwhen` (`mw-erstellen` / `mw-aktualisieren`) nach [markwhen-konventionen](./references/markwhen-konventionen.md).
4. **Kalender** (`10_zeitlinie/kalender/`): führt der Eintrag eine feste Periodizität ein oder nutzt sie, gleiche die Weltkalender-Definition ab.

Einträge in historischer Chronologie und Vorkommnisregister verwenden dieselbe Tag-Taxonomie wie Markwhen, damit beide Darstellungen synchron bleiben.

---

## 10. Badges, Indizes & Synchronisation

- **Badge**: nutze stets das Standard-Badge `> 🛡️ *Geprüft: ... | Geändert: ...*` nach den üblichen Zeitregeln (neuer Text → `Geprüft: NICHT_GEPRUEFT`; Bearbeitung nach Bestätigung → nur `Geändert` vorrücken; Audit → beide Daten angleichen).
- **Indizes**: aktualisiere `README.md` des Unterordners, des Elternordners `braeuche_feste_und_ereignisse/` und ggf. `03_gesellschaft_und_politik/`.
- **Kanoncodes** (Bibel/JSON): Bräuche `3.5.x`, Feste/Vorkommnisse `3.6.x`, Ereignisse `3.7.x`; Band `10_zeitlinie` als Band `10` (`10.1.x` historische Chronologie, `10.2.x` Vorkommnisregister, `10.3.x` Kalender). `.mw`-Quellen und Exporte sind von der Bibel ausgenommen und werden nur im JSON indiziert.
- **Keine Halluzinationen**: wie in jedem Modul keinerlei vom SL nicht freigegebene Details.
