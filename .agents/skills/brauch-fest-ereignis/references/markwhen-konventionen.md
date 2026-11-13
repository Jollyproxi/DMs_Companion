# Konventionen für die grafische Markwhen-Zeitlinie

Erfassungsstandard für die Markwhen-Quellen unter `10_zeitlinie/markwhen/`, der grafischen Zeitlinie der Welt.

---

## 1. Struktur des Ordners `markwhen/`

```text
10_zeitlinie/markwhen/
├── README.md                   # Index der .mw-Quellen und Konventionsübersicht
├── allgemeine_zeitlinie.mw     # Allgemeiner Index/Legende (KEIN Aggregat der Quellen)
├── epochen/
│   └── <epochenname>.mw        # Eine Quelle pro historischer Epoche/Zeitraum
└── kampagnen/
    └── <kampagnenname>.mw      # Eine Quelle pro Kampagne: alles Kampagnenrelevante
```

- `allgemeine_zeitlinie.mw` dient als **Index/Legende**: sie enthält die Tag-Legende, Datumskonventionen und Links zu Epochen- und Kampagnenquellen. Sie dupliziert nicht den Inhalt der anderen Dateien.
- Dateien unter `epochen/` sind die maßgeblichen Chronologiequellen und einzeln betrachtbar.
- Dateien unter `kampagnen/` enthalten **alles Relevante** für die Kampagne (Vergangenheit und Zukunft) mit Links zu den Protokollen unter `09_chroniken/`.

---

## 2. Grundsyntax

Ein Ereignis pro Zeile mit Datum, Titel und Tags:

```text
512-03-01: Sonnenwendfest #fest #historisch
512/513: Belagerung der Zitadelle #ereignis #historisch #fraktion_nordwacht
514: Turnier der Garde #fest #vorkommnis #laufend
```

- **Zeiträume**: `startdatum/enddatum` (z. B. `512-03-01/512-03-07`).
- **Ungefähre Daten**: nur Jahr (z. B. `512`) oder Jahr mit ungefährem Monat (`512-03`).
- **Tags**: `#tag`-Suffixe in derselben Ereigniszeile.
- **Links zu Bögen**: in Beschreibungen/Unterpunkten relative Markdown-Links zu kanonischen Bögen (z. B. `[Turnier der Garde](../../../03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/feste_und_vorkommnisse/01_gardeturnier.md)`), angepasst an den Speicherort der `.mw`-Datei.

---

## 3. Datumskonvention

- Daten verwenden **Weltjahre** im ISO-Format (z. B. `512-03-01`, `512`, `512/513`).
- Die Zuordnung zum realen Weltkalender (Monate, Jahreszeiten, Schalttage) wird unter `10_zeitlinie/kalender/` dokumentiert und in der Legende von `allgemeine_zeitlinie.mw` zusammengefasst.
- Besitzt ein Ereignis eine feste Periodizität, muss sein Datum/Turnus ebenfalls in der Kalenderlegende vermerkt sein.

---

## 4. Tag-Taxonomie

| Kategorie | Tags | Verwendung |
| :--- | :--- | :--- |
| **Typ** | `#brauch` `#fest` `#ereignis` `#vorkommnis` | Wesen des Eintrags; `#vorkommnis` kennzeichnet eine konkret datierte Instanz eines wiederkehrenden Ereignisses. |
| **Status** | `#historisch` `#laufend` `#geplant` | Status des Vorkommnisses passend zum Bogenmodell. |
| **Thematisch** | `#fraktion_<slug>` `#ort_<slug>` `#SC_<slug>` `#NSC_<slug>` | Filter nach Akteur oder Schauplatz (z. B. `#fraktion_handelsbund`, `#ort_hochhafen`). |
| **Kampagne** | `#kampagne_<name>` | Grenzt Ereignisse einer bestimmten Kampagne ein. |

Dieselben Tag-Kategorien müssen auch in `10_zeitlinie/historische_chronologie/` und `10_zeitlinie/vorkommnisregister/` verwendet werden, um beide Darstellungen synchron zu halten.

---

## 5. Aktualisierungsregeln

1. **Neuer Eintrag oder neues Vorkommnis**: Zeile in die passende Epochenquelle unter `epochen/` einfügen; sofern kampagnenrelevant, ebenfalls in `kampagnen/<name>.mw`.
2. **Statuswechsel** (geplant → laufend → abgeschlossen): Status-Tag in der Zeile und Ausgang in den Notizen aktualisieren.
3. **Legende**: bei neuen Tags oder Kalendereinträgen `allgemeine_zeitlinie.mw` aktualisieren.
4. **Kanon-Ausnahmen**: `.mw`-Dateien und Inhalte von `exporte/` sind **von der Weltenbibel ausgeschlossen**; sie werden ausschließlich in `weltstruktur.json` (eigene Unterstruktur in Band `10`) indiziert.
5. **Keine Halluzinationen**: kein Ereignis, Datum oder Ergebnis ohne Zustimmung des SL.
