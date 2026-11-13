# Markwhen-Syntax und Vorlagen (`.mw`)

Operative Referenz für das Schreiben und Aktualisieren von `.mw`-Dateien unter `10_zeitlinie/markwhen/`.

---

## 1. Kanonische Markwhen-Syntax

### YAML-Header (`---`)

Jede `.mw`-Datei beginnt mit einem YAML-Block zwischen `---`-Zeilen, der `title`, `description`, `timezone: UTC` (empfohlen, um historische LMT-Versätze bei frühen Jahreszahlen zu vermeiden) sowie die Farbpalette für Standard-Tags festlegt (beschreibende Zwischenüberschriften sind stets als `//`-Kommentar zu schreiben, niemals als `#KategorieName` ohne `:`, um den YAML-Parser nicht ungültig zu machen; das ISO-Format `JJJJ-MM-TT` ist nativ und benötigt kein `dateFormat`):

```yaml
---
title: "Titel der Zeitlinie"
description: "Kurze Beschreibung der .mw-Datei"
timezone: UTC

// Typ
#brauch: #8b5cf6
#fest: #f59e0b
#ereignis: #ef4444
#vorkommnis: #ec4899

// Status
#historisch: #64748b
#laufend: #10b981
#geplant: #3b82f6
#vorlaeufiges_datum: #eab308
---
```

### Datumsformate (Weltjahre)

Daten verwenden **Weltjahre** im ISO-Format (`JJJJ`, `JJJJ-MM`, `JJJJ-MM-TT`) mit vierstelligen Jahreszahlen (bei Jahren `< 1000` innerhalb derselben Datei einheitlich z. B. `0512-03-01` oder `512-03-01`):

- **Einzelner Tag**: `512-03-01: Sonnenwendfest #fest #historisch`
- **Ungefährer Monat**: `512-03: Einberufung des Rates #ereignis #historisch`
- **Einzelnes Jahr**: `514: Turnier der Garde #fest #vorkommnis #laufend`
- **Zeitraum**: `512-03-01/512-03-07: Herbstmesse #fest #historisch` oder `512/513: Belagerung der Zitadelle #ereignis #historisch`
- **Noch undefiniertes Datum**: niemals Zahlen erfinden oder das Ereignis weglassen; **frage stets zuerst den SL** (über das strukturierte Fragewerkzeug falls verfügbar, sonst im Chat) nach einem Datum oder einem **vorläufigen Jahr**, nutze bei Vorläufigkeit den Tag `#vorlaeufiges_datum` und notiere `- [VOM_SL_ZU_DEFINIEREN: endgültiges Datum bestätigen]`.

### Beschreibungen, Unterpunkte & relative Links

Unterhalb der Ereigniszeile (eingerückt oder in den unmittelbar folgenden Zeilen vor der Leerzeile) stehen:

- Eine kurze notarielle Zusammenfassung oder der Ausgang (bei `#historisch` / `#laufend`).
- Relative Markdown-Links (ohne Backticks) zu kanonischen Bögen oder Protokollen, bezogen auf den Speicherort der `.mw`-Datei:
  - Aus `10_zeitlinie/markwhen/allgemeine_zeitlinie.mw`: `../../03_gesellschaft_und_politik/...`
  - Aus `10_zeitlinie/markwhen/epochen/<epoche>.mw` oder `kampagnen/<kampagne>.mw`: `../../../03_gesellschaft_und_politik/...` und `../../../09_chroniken/kampagnen/...`

Vollständiges Eintragsbeispiel:

```text
514-06-12: Turnier der Garde — Ausgabe 514 #fest #vorkommnis #laufend #ort_hohe_zitadelle
- Status: laufend.
- Kanonischer Bogen: [Das Turnier der Garde](../../../03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/feste_und_vorkommnisse/01_gardeturnier.md)
- Zugehöriges Protokoll: [Sitzung 02](../../../09_chroniken/kampagnen/Chroniken%20des%20Nordens/sitzungen/02_sitzung.md)
```

### Gruppierungen (`section` / `endSection`)

Nutze `section Abschnittsname` ... `endSection`, um Ereignisse logisch zu bündeln (z. B. nach historischem Teilabschnitt in Epochendateien oder nach Erzählbogen / Akt in Kampagnendateien).

---

## 2. Verpflichtende Tag-Taxonomie

Jedes Ereignis einer `.mw`-Datei muss **mindestens 1 Typ-Tag** und **1 Status-Tag** sowie optionale thematische und Kampagnen-Tags tragen:

| Kategorie | Zulässige Tags | Verwendungsregel |
| :--- | :--- | :--- |
| **Typ** *(Pflicht)* | `#brauch` `#fest` `#ereignis` `#vorkommnis` | `#vorkommnis` begleitet `#fest` oder `#ereignis`, wenn eine konkret datierte einzelne Durchführung eingetragen wird. |
| **Status** *(Pflicht)* | `#historisch` `#laufend` `#geplant` | Abgeglichen mit dem Statusfeld im Vorkommnisregister und in den Bögen. |
| **Thematisch** *(optional)* | `#fraktion_<slug>` `#ort_<slug>` `#SC_<slug>` `#NSC_<slug>` | `snake_case` passend zu den `id`-Werten in `weltstruktur.json`. |
| **Kampagne** *(optional/Pflicht in kampagnen/)* | `#kampagne_<slug>` | Verpflichtend für Ereignisse, die eine konkrete Kampagne betreffen. |

---

## 3. Vorlage 1: `10_zeitlinie/markwhen/allgemeine_zeitlinie.mw`

`allgemeine_zeitlinie.mw` ist der **allgemeine Index bzw. die Legende** (sie dupliziert keine Ereignisse aus Einzeldateien):

```text
---
title: "Allgemeine Zeitlinie — Legende & Chronologisches Verzeichnis"
description: "Allgemeiner Index, Tag-Legende und Weltkalender-Konventionen. Einzelne Ereignisse liegen in epochen/ und kampagnen/."
timezone: UTC

// Typ
#brauch: #8b5cf6
#fest: #f59e0b
#ereignis: #ef4444
#vorkommnis: #ec4899

// Status
#historisch: #64748b
#laufend: #10b981
#geplant: #3b82f6
#vorlaeufiges_datum: #eab308
---

// ============================================================================
// KALENDERLEGENDE & KONVENTIONEN
// - Datumsangaben in Weltjahren (Format JJJJ, JJJJ-MM, JJJJ-MM-TT).
// - Kalenderzuordnung: [Weltkalender](../kalender/README.md)
// - Feste Wiederkehr: [VOM_SL_ZU_DEFINIEREN: Liste fester jährlicher Feiertage]
// ============================================================================

// ============================================================================
// INDEX DER EPOCHENQUELLEN (10_zeitlinie/markwhen/epochen/)
// - [Epoche 01](epochen/01_<epochen_slug>.mw) — [Historische Chronologie](../historische_chronologie/01_<epochen_slug>.md)
// ============================================================================

// ============================================================================
// INDEX DER KAMPAGNENQUELLEN (10_zeitlinie/markwhen/kampagnen/)
// - [Kampagne](kampagnen/<kampagnen_slug>.mw) — [Kampagnen-Hub](../../09_chroniken/kampagnen/<Kampagnenname>/README.md)
// ============================================================================

section Überblick der Epochen
// Nur grobe Zeitspannen der Epochen eintragen (keine Einzelereignisse duplizieren)
// [VOM_SL_ZU_DEFINIEREN: Jahresspanne Epoche 1]: Erstes Zeitalter #historisch
endSection
```

---

## 4. Vorlage 2: `10_zeitlinie/markwhen/epochen/<NN_epochen_slug>.mw`

```text
---
title: "Epoche: [Name der Epoche]"
description: "Markwhen-Chronologie der Epoche [Name der Epoche] — synchronisiert mit historische_chronologie und vorkommnisregister."
timezone: UTC

#brauch: #8b5cf6
#fest: #f59e0b
#ereignis: #ef4444
#vorkommnis: #ec4899
#historisch: #64748b
#laufend: #10b981
#geplant: #3b82f6
#vorlaeufiges_datum: #eab308
---

// Synchronisierte kanonische Quellen:
// - Historische Chronologie: [../../historische_chronologie/NN_<epochen_slug>.md](../../historische_chronologie/NN_<epochen_slug>.md)
// - Vorkommnisregister: [../../vorkommnisregister/NN_<epochen_slug>.md](../../vorkommnisregister/NN_<epochen_slug>.md)

section Historische & Gründungsereignisse
// Beispiel:
// 512/513: Belagerung der Zitadelle #ereignis #historisch #fraktion_nordwacht
// - Ausgang: [kanonische Zusammenfassung]
// - Bogen: [Die Belagerung der Zitadelle](../../../03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/ereignisse/01_belagerung_zitadelle.md)
endSection

section Vorkommnisse & Laufende Einträge
// Beispiel:
// 514: Turnier der Garde #fest #vorkommnis #laufend
// - Bogen: [Das Turnier der Garde](../../../03_gesellschaft_und_politik/braeuche_feste_und_ereignisse/feste_und_vorkommnisse/01_gardeturnier.md)
endSection
```

---

## 5. Vorlage 3: `10_zeitlinie/markwhen/kampagnen/<kampagnen_slug>.mw`

```text
---
title: "Kampagne: [Kampagnenname]"
description: "Vollständige Zeitlinie der Kampagne [Kampagnenname]: SC-Vorgeschichten, gespielte Sitzungen sowie laufende/geplante Ereignisse."
timezone: UTC

#brauch: #8b5cf6
#fest: #f59e0b
#ereignis: #ef4444
#vorkommnis: #ec4899
#historisch: #64748b
#laufend: #10b981
#geplant: #3b82f6
#vorlaeufiges_datum: #eab308
#kampagne_<kampagnen_slug>: #f43f5e
---

// Kampagnen-Hub: [../../../09_chroniken/kampagnen/<Kampagnenname>/README.md](../../../09_chroniken/kampagnen/<Kampagnenname>/README.md)

section Vorgeschichten & SC-Hintergründe
// Frühere Ereignisse mit Relevanz für die SCs der Kampagne (#historisch #kampagne_<kampagnen_slug>)
endSection

section Sitzungschronik
// Ereignisse aus protokollierten Sitzungen (#historisch oder #laufend)
// Verlinkt auf ../../../09_chroniken/kampagnen/<Kampagnenname>/sitzungen/XX_titel.md
endSection

section Laufende & Geplante Ereignisse
// Zeitfenster, Fristen und künftige Vorkommnisse (#laufend / #geplant)
endSection
```
