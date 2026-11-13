# Referenzarchitektur der Spielwelt (Modulare D&D-Taxonomie)

Dieses Dokument definiert die standardisierte Ordner- und Dateistruktur für die enzyklopädische Archivierung einer Spielwelt und ihrer D&D-Kampagnen.

> **Anpassungshinweis**: Enthält der Workspace bereits eine bestehende Spielwelt mit äquivalenten Ordnernamen (z. B. `04_recht_und_erbfolge/`), respektiere und bewahre die vorhandene Struktur, ohne etablierte Dateien zwangsweise umzubenennen.

```text
├── README.md                                               # Allgemeines Weltverzeichnis und Navigationsleitfaden
├── weltstruktur.json                                       # Hierarchische Karte, Metadaten und Welttaxonomie
├── WELTENBIBEL.md                                           # Vollständiges Quelldokument / Master-Lorebuch
│
├── 01_kosmologie/                                          # Band I: Kosmologie, Metaphysik, Ebenen, Magiefluss und Ethik
│   ├── README.md                                           # Kosmologischer Überblick
│   ├── 01_ebenenstruktur.md                                # Ebenen, Himmelssphären, höllische oder abgrundtiefe Reiche
│   ├── 02_jahreszeiten_und_himmelsmechanik.md              # Zeitdynamiken, astronomische Zyklen und Ebenenübergänge
│   ├── 03_magiefluss_und_goettliche_ordnung.md             # Natur des Arkanen, Theurgie, Monopole und Grenzen
│   └── 04_moralisches_oder_philosophisches_system.md       # Werte, Tugenden, Laster oder kosmischer Ethikkodex
│
├── 02_geografie/                                           # Band II: Physische Geografie, Kartografie und Regionen
│   ├── README.md                                           # Allgemeiner geografischer Überblick und Gebietsquerschnitte
│   ├── 01_hauptkarte_und_biome.md                          # Gebiete, Klimazonen und Grenzen
│   ├── 02_unterirdische_regionen_und_abgruende.md          # Unterreich, Verwerfungen und Höhlen
│   ├── 03_besondere_domaenen_und_verbundene_ebenen.md      # Schwebende Reiche, Portale und Schwellenlande
│   └── regionen/                                           # Dossiers pro Region/Reich/Provinz (mit README.md)
│
├── 03_gesellschaft_und_politik/                            # Band III: Gesellschaftliches, wirtschaftliches und kulturelles Modell
│   ├── README.md                                           # Überblick über die Gesellschaftsordnung
│   ├── 01_sozialphilosophie_und_braeuche.md                # Gesellschaftliche Werte, Ethik und Konventionen
│   ├── 02_machtmonopol_und_wirtschaft.md                   # Militär, Handel, Währungen und Abgaben
│   ├── 03_gesellschaftsschichten_und_rollen.md             # Bürgerliche Schichtung, Zünfte und Ästhetik
│   ├── 04_oeffentliche_ordnung_und_sicherheitskraefte.md   # Stadtwachen, Milizen, öffentliche Ordnung und Wahrnehmung (Gesetze und Gerichte in Band IV)
│   └── braeuche_feste_und_ereignisse/                      # Unterserie: Bräuche, wiederkehrende Feste und einmalige Ereignisse
│       ├── README.md                                       # Index der Unterserie nach Typologie
│       ├── braeuche/                                       # Besonderheiten des Alltags (Struktur und Ablauf)
│       │   ├── README.md
│       │   └── 01_<eintrag_slug>.md                        # Brauch-Bogen (fortlaufend nummeriert)
│       ├── feste_und_vorkommnisse/                         # Wiederkehrende institutionelle/rituelle Feste und Ereignisse
│       │   ├── README.md
│       │   └── 01_<eintrag_slug>.md                        # Fest-/Vorkommnis-Bogen (feste oder variable Periodizität)
│       └── ereignisse/                                     # Von Natur aus einmalige besondere Ereignisse
│           ├── README.md
│           └── 01_<eintrag_slug>.md                        # Ereignis-Bogen (historisch oder laufend)
│
├── 04_recht_und_gesetze/                                   # Band IV: Recht, Grundgesetze, Bürgerrechte, Pakte, Straftaten und Gerichtsbarkeiten (jeder Unterordner 01–10 enthält README.md, 01_allgemeiner_rahmen.md, 02_<eintrag_slug>.md…)
│   ├── README.md                                           # Juristisch-institutioneller Überblick und Index der Rechtsgebiete
│   ├── 01_rechtsordnung_und_quellen/                       # Rechtsquellen, herrscherliche Edikte, Satzungen, Gewohnheitsrecht, Gesetzgeber und Normenhierarchie
│   │   ├── README.md                                       # Index des Rechtsgebiets
│   │   ├── 01_allgemeiner_rahmen.md                        # Allgemeine Grundsätze und Rahmenordnung des Rechtsgebiets
│   │   └── 02_<eintrag_slug>.md                            # Einzelne Gesetze, Kodizes, Satzungen oder Edikte (fortlaufend nummeriert)
│   ├── 02_buergerrechte_und_status/                        # Bürgerrecht, Rechte nach Stand oder Spezies, Unfreiheit/Freilassung, Staatenlose, Asyl und Geleitbriefe
│   ├── 03_dynastisches_recht_und_erbfolge/                 # Erbfolgen (Blut, Wahl, Verdienst), Regentschaften, Nachlass, Lehen und Amtsübergabe
│   ├── 04_vertraege_und_pakte/                             # Zivil- und Handelsverträge, Verbindlichkeiten, bindende Schwüre und Blutpakte
│   ├── 05_abkommen_und_diplomatie/                         # Staatsverträge, Bündnisse zwischen Reichen oder Fraktionen, Friedensabkommen und Grenzen
│   ├── 06_strafrecht_und_delikte/                          # Straftatenklassifikation, Hochverrat, Strafen, Wergeld, Kopfgelder, Beschlagnahmen, Verbannung und Begnadigung
│   ├── 07_gerichte_und_verfahren/                          # Gerichtszuständigkeiten, Prozesse, magische Beweise (Zone der Wahrheit), Gottesurteile, Gerichtskämpfe und Berufung
│   ├── 08_arkanes_und_religioeses_recht/                   # Verbotene Schulen und Zauber, Zauberlizenzen, Artefaktstatus, Häresien und geistliche Gerichtsbarkeit
│   ├── 09_eigentum_handel_und_steuern/                     # Grundbesitz und Krongut, Zunftmonopole, Zölle und Steuern, Darlehen, Konkurs und Seerecht
│   └── 10_kriegsrecht_und_abenteurer/                      # Kriegserklärungen, Waffenstillstände, Gefangene und Lösegeld, Söldner, Abenteurergilden und Ruinenschürfrechte
│
├── 05_charaktere/                                          # Band V: Verzeichnis der Spieler- und Nichtspielercharaktere
│   ├── README.md                                           # Allgemeiner Charakterindex und Beziehungsmatrix
│   ├── Spielercharaktere/                                  # SC-Archiv
│   │   ├── README.md                                       # Gesamtübersicht der Gruppen und Synergien
│   │   └── [Kampagnenname]/                                # Ordner der jeweiligen Gruppe/Kampagne
│   │       ├── README.md                                   # Beziehungs-Hub der Gruppe
│   │       └── [SC_Name]/                                  # Modulares SC-Dossier:
│   │           ├── README.md                               # Zusammenfassung und Index des Charakters
│   │           ├── 01_stammdaten_und_merkmale.md           # Werte, Spezies, Klasse, Merkmale
│   │           ├── 02_integrierter_hintergrund.md          # Mit der Weltlore verknüpfte Vorgeschichte
│   │           ├── 03_beziehungen_und_dynamiken.md         # Bindungen zu anderen SCs und NSCs
│   │           ├── 04_ausruestung_und_faehigkeiten.md      # Schlüsselgegenstände, Talente und Fähigkeiten
│   │           └── 05_sl_aufhaenger_und_geheimnisse.md     # Dem SL vorbehaltene Erzählaufhänger
│   └── Nichtspielercharaktere/                             # NSC-Archiv der Spielwelt
│       ├── README.md                                       # Index und Gruppierung nach Fraktion
│       └── [NSC_Name].md                                   # Bogen mit Rolle, Wesen, Geheimnissen und Aufhängern
│
├── 06_orte/                                                # Band VI: Bedeutsame Orte und Abenteuerknoten
│   ├── README.md                                           # Liste relevanter Orte und Verbindungen
│   └── [XX_ortsname].md                                    # Ortsbogen (Atmosphäre, Gefahren, NSCs, Aufhänger)
│
├── 07_fraktionen/                                          # Band VII: Fraktionen, Adelshäuser, Zirkel und Gilden
│   ├── README.md                                           # Geopolitische Machtkarte und Konflikte
│   └── [XX_fraktionsname].md                               # Satzung, Hierarchie, Bündnisse, Ressourcen und Ziele
│
├── 08_besondere_magische_gegenstaende/                     # Band VIII: Artefakte, Relikte und einzigartige Apparaturen
│   ├── README.md                                           # Rechtsregister für Magie und Gegenstandsindex
│   └── [Gegenstandsname].md                                # Technischer Bogen, Herkunft, Kräfte und SL-Aufhänger
│
├── 09_chroniken/                                           # Band IX: Chroniken und Kampagnenprotokolle
│   ├── README.md                                           # Chronologischer Index aller aktiven Kampagnen
│   └── kampagnen/
│       └── [kampagnenname]/                                # Ordner der einzelnen Kampagne
│           ├── README.md                                   # Hub: Gruppenzusammensetzung, Ziel, Sitzungsübersicht
│           └── sitzungen/                                  # Fortlaufend nummerierte Protokolle:
│               ├── README.md                               # Protokollindex
│               ├── 01_sitzungstitel.md                     # Protokoll Sitzung 1
│               └── 02_sitzungstitel.md                     # Protokoll Sitzung 2...
│
└── 10_zeitlinie/                                           # Band X: Querschnitts-Zeitlinie und Weltchronologie
    ├── README.md                                           # Allgemeine Legende: Daten (Weltjahre), Tags, Navigation
    ├── historische_chronologie/                            # Vergangene Ereignisse, Dateien je Epoche/Zeitraum (mit Tags)
    │   └── 01_<epochenname>.md
    ├── vorkommnisregister/                                 # Vorkommnisse von Festen/Ereignissen & laufende Einträge
    │   └── 01_<zeitraumname>.md
    ├── markwhen/                                           # Grafische Zeitlinie (Markwhen-Quellen, von Bibel ausgenommen)
    │   ├── README.md                                       # Index der .mw-Quellen und Konventionsübersicht
    │   ├── allgemeine_zeitlinie.mw                         # Index/Legende (nicht aggregiert)
    │   ├── epochen/
    │   │   └── <epochenname>.mw                            # Quelle pro historischer Epoche/Zeitraum
    │   └── kampagnen/
    │       └── <kampagnenname>.mw                          # Alles Kampagnenrelevante (mit Links zu Protokollen)
    ├── kalender/                                           # Weltkalender: Monate, Jahreszeiten, Schalttage, Zuordnung
    │   └── 01_kalender.md
    └── exporte/                                            # Abgeleitete grafische Renderings (HTML/PNG/SVG/PDF)
        └── README.md                                       # Verzeichnis der abgeleiteten Renderings
```
