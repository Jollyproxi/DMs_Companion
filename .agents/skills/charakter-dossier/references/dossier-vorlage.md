# Referenzvorlagen für Charakter-Dossiers

## 1. Modulares Spielercharakter-(SC-)Dossier

Jeder SC besitzt einen eigenen Ordner unter `05_charaktere/<Spielercharaktere>/<Kampagne_oder_Gruppe>/<SC_Name>/` (Standard: `05_charaktere/Spielercharaktere/<Kampagne>/<SC_Name>/`) mit einer verbindenden `README.md` und fünf thematischen Modulen:

### `README.md` (Charakter-Hub)
```markdown
# [Charaktername]

> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*

* **Kampagne:** [Kampagnenname]
* **Rolle in der Gruppe:** [Kurzbeschreibung der kämpferischen/arkanen/sozialen Rolle]
* **Gesinnung / Moralkodex:** [Gesinnung oder ethische Grundsätze]

## Modulverzeichnis
1. [01. Stammdaten & Kernmerkmale](01_stammdaten_und_merkmale.md)
2. [02. Integrierter Hintergrund](02_integrierter_hintergrund.md)
3. [03. Beziehungen & Gruppendynamik](03_beziehungen_und_dynamiken.md)
4. [04. Ausrüstung & Besondere Fähigkeiten](04_ausruestung_und_faehigkeiten.md)
5. [05. Erzählaufhänger & SL-Geheimnisse](05_sl_aufhaenger_und_geheimnisse.md)
```

### `01_stammdaten_und_merkmale.md`
```markdown
# 01. Stammdaten & Kernmerkmale

> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*

* **Name:** [Vollständiger Name]
* **Spezies / Abstammung:** [D&D-5e-Spezies / Herkunftslinie der Welt]
* **Klasse & Stufe:** [Klasse, Unterklasse, Stufe]
* **Gesinnung / Moralkodex:** [Gesinnung oder Leitprinzipien]
* **Äußeres Erscheinungsbild:** [Visuelle Beschreibung, Erkennungszeichen, Narben, Kleidung]
* **Persönlichkeitsmerkmale, Ideale, Bindungen, Makel:** [Knappe Listen]
```

### `02_integrierter_hintergrund.md`
```markdown
# 02. In den Kanon integrierter Hintergrund

> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*

## Ursprünge & Wurzeln
[Beschreibung der geografischen und sozialen Herkunft mit relativen Links zu Orten der Welt.]

## Der Wendepunkt
[Das prägende Ereignis oder Trauma, das den Charakter auf den Weg des Abenteuers führte.]

## Jüngste Entwicklungen vor Kampagnenbeginn
[Was in der Zeit unmittelbar vor dem Start der Kampagne geschah.]
```

### `03_beziehungen_und_dynamiken.md`
```markdown
# 03. Beziehungen & Dynamiken

> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*

## Bindungen zu Gefährten der Gruppe
* **[Name Gefährte 1]:** [Beziehungsdynamik, Vertrauen, Reibungspunkte]
* **[Name Gefährte 2]:** [...]

## Bindungen zu NSCs & Fraktionen
* **[Name NSC / Fraktion]:** [Art der Beziehung, Ehrenschulden, Rivalitäten]
```

### `04_ausruestung_und_faehigkeiten.md`
```markdown
# 04. Ausrüstung & Besondere Fähigkeiten

> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*

## Hauptausrüstung & Fokusse
* [Magischer Gegenstand / Fokus mit optionalem Link zu 08_besondere_magische_gegenstaende/]

## Besondere Fähigkeiten & Merkmale
* **[Fähigkeitsname]:** [Narrative und regeltechnische Beschreibung]
```

### `05_sl_aufhaenger_und_geheimnisse.md`
```markdown
# 05. Erzählaufhänger & SL-Geheimnisse

> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*

> ⚠️ *Vertraulicher Abschnitt ausschließlich zur Verwendung durch den Spielleiter.*

## Offene Ermittlungsspuren
* **[Spur 1]:** [Details, Aufhänger, mögliche Entwicklungen]

## Verborgene Wahrheiten & Künftige Enthüllungen
* **[Geheimnis 1]:** [Wahrheit über die Vergangenheit des SC, die dem Charakter selbst unbekannt ist]
```

---

## 2. Nichtspielercharakter-(NSC-)Bogen

Jeder NSC liegt als einzelne Datei unter `05_charaktere/<Nichtspielercharaktere>/[<nsc_gruppe>/][NSC_Name].md` (Standard: `05_charaktere/Nichtspielercharaktere/[NSC_Name].md`):

```markdown
# [NSC Name] — [Titel oder Rolle]

> 🛡️ *Geprüft: NICHT_GEPRUEFT | Geändert: [HEUTIGES_DATUM]*

* **Fraktion / Haus:** [Fraktionsname mit relativem Link zu 07_fraktionen/]
* **Wohnort / Wirkungsstätte:** [Ort mit Link zu 06_orte/]
* **Gesinnung / Moral:** [Gesinnung oder moralische Grundsätze]
* **Aktueller Status:** [Lebend, Flüchtig, Verstorben, Vermisst]

---

## Erscheinung & Wesen
[Körperbeschreibung, Haltung, Sprechweise, Temperament.]

---

## Narrative Rolle & Verhältnis zur Gruppe
[Wer der NSC in der Welt ist und wie er mit den SCs interagiert.]

---

## Geheimnisse & Aufhänger für den SL
* **[Geheimnis / Verborgenes Motiv]:** [Was der NSC wirklich verfolgt]
* **[Abenteueraufhänger]:** [Wie er in künftigen Sitzungen eingebunden werden kann]
```
