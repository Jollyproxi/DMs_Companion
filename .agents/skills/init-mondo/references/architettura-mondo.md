# Architettura di Riferimento del Mondo (Tassonomia Modulare D&D)

Questo documento definisce la struttura a cartelle e file standard per l'archiviazione enciclopedica di un'ambientazione e delle relative campagne di D&D.

> **Nota di adattamento**: Se il workspace ospita già un'ambientazione esistente con nomi di cartelle equivalenti (es. `06_location/`, `07_factions/`, `08_oggetti magici peculiari/`, `cornici/` o `Readme.md`), rispetta e mantieni la struttura già adottata senza rinominare forzatamente i file esistenti.

```text
├── README.md                                               # Indice generale del mondo e linee guida di navigazione
├── struttura_ambientazione.json                           # Mappa gerarchica, metadati e tassonomia del mondo
├── BIBBIA DELL'AMBIENTAZIONE.md                            # Documento sorgente integrale / Master lore book
│
├── 01_cosmologia/                                         # Tomo I: Cosmologia, metafisica, piani, flusso della magia ed etica
│   ├── README.md                                          # Panoramica cosmologica
│   ├── 01_struttura_verticale.md                          # Piani, sfere celesti, infernali o abissali
│   ├── 02_ciclo_stagioni_e_meccaniche_celesti.md          # Dinamiche temporali, cicli astronomici e transiti planari
│   ├── 03_flusso_della_magia_e_ordine_divino.md           # Natura dell'arcano, teurgia, monopoli e limitazioni
│   └── 04_sistema_morale_o_filosofico.md                  # Valori, virtù, vizi o codice etico del cosmo
│
├── 02_geografia/                                          # Tomo II: Geografia fisica, cartografia e regioni
│   ├── README.md                                          # Quadro geografico generale e spaccati territoriali
│   ├── 01_mappa_principale_e_biomi.md                     # Territori, climi e confini
│   ├── 02_regioni_sotterranee_o_abissi.md                 # Sottosuolo, faglie e caverne
│   ├── 03_domini_speciali_o_piani_connessi.md             # Reami sospesi, varchi e terre liminali
│   └── regioni/                                           # Dossier per singola regione/regno/cornice (con README.md)
│
├── 03_societa_e_politica/                                 # Tomo III: Modello sociale, economico e culturale
│   ├── README.md                                          # Panoramica dell'ordinamento sociale
│   ├── 01_filosofia_sociale_e_costumi.md                  # Valori sociali, etica e convenzioni
│   ├── 02_monopolio_del_potere_ed_economia.md             # Esercito, commercio, valute e tributi
│   ├── 03_classi_sociali_e_ruoli.md                       # Stratificazione civica, corporazioni ed estetica
│   ├── 04_diritto_penale_e_giustizia.md                   # Tribunali ordinari, pene e leggi civili
│   └── usi_costumi_ed_eventi/                             # Sottoserie: usanze, festival ricorrenti ed eventi una tantum
│       ├── README.md                                      # Indice della sottoserie per tipologia
│       ├── usanze/                                        # Peculiarità della vita quotidiana (strutture e modi)
│       │   ├── README.md
│       │   └── 01_<slug_voce>.md                          # Scheda usanza (numerazione progressiva)
│       ├── festival_ed_occorrenze/                        # Feste ed eventi istituzionali/rituali ricorrenti
│       │   ├── README.md
│       │   └── 01_<slug_voce>.md                          # Scheda festival/occorrenza (periodicità fissa o variabile)
│       └── eventi/                                        # Eventi peculiari una tantum (per natura)
│           ├── README.md
│           └── 01_<slug_voce>.md                          # Scheda evento (storico o in svolgimento)
│
├── 04_diritto_e_successione/                              # Tomo IV: Leggi fondamentali, diritto dinastico, patti e trattati
│   ├── README.md                                          # Panoramica giuridico-istituzionale
│   ├── 01_contratti_patti_e_trattati.md                   # Norme, alleanze formali e contratti di sangue
│   ├── 02_gerarchia_e_successione.md                      # Ordini di successione, cariche ed eredità
│   └── 03_tribunali_e_contese.md                          # Risoluzione dispute giuridiche, ereditarie e perizie
│
├── 05_personaggi/                                         # Tomo V: Roster Personaggi Giocanti e Non-Giocanti
│   ├── README.md                                          # Indice generale dei personaggi e matrice relazioni
│   ├── Giocanti/                                          # Archivio dei PG
│   │   ├── README.md                                      # Quadro d'insieme dei gruppi/party
│   │   └── [Nome_Campagna]/                               # Cartella del gruppo/party specifico
│   │       ├── README.md                                  # Hub delle relazioni del gruppo
│   │       └── [Nome_PG]/                                 # Dossier modulare del PG:
│   │           ├── README.md                              # Indice e sintesi del personaggio
│   │           ├── 01_anagrafica_e_tratti.md              # Statistiche, razza, classe, tratti
│   │           ├── 02_backstory_integrata.md              # Storia legata alla lore del mondo
│   │           ├── 03_relazioni_e_dinamiche.md            # Legami con gli altri PG e PNG
│   │           ├── 04_equipaggiamento_e_capacita.md       # Oggetti chiave, talenti e capacità
│   │           └── 05_ganci_e_segreti_dm.md               # Spunti narrativi riservati al Master
│   └── Non-Giocanti/                                      # Archivio PNG dell'ambientazione
│       ├── README.md                                      # Indice e raggruppamento per fazione
│       └── [Nome_PNG].md                                  # Scheda con ruolo, indole, segreti e ganci
│
├── 06_luoghi/                                             # Tomo VI: Luoghi rilevanti e snodi d'avventura
│   ├── README.md                                          # Elenco dei luoghi d'interesse e collegamenti
│   └── [XX_nome_luogo].md                                 # Scheda del luogo (atmosfera, pericoli, PNG, agganci)
│
├── 07_fazioni/                                            # Tomo VII: Fazioni, casate, congreghe e gilde
│   ├── README.md                                          # Mappa geopolitica del potere e conflitti
│   └── [XX_nome_fazione].md                               # Statuto, gerarchia, alleanze, risorse e obiettivi
│
├── 08_oggetti_magici_peculiari/                           # Tomo VIII: Artefatti, reliquie e congegni unici
│   ├── README.md                                          # Registro normativo del magico e indice oggetti
│   └── [Nome_Oggetto].md                                  # Scheda tecnica, provenienza, poteri e ganci DM
│
├── 09_cronache/                                           # Tomo IX: Cronache e verbali di campagna
│   ├── README.md                                          # Indice cronologico di tutte le campagne attive
│   └── campagne/
│       └── [nome_campagna]/                               # Cartella della singola campagna
│           ├── README.md                                  # Hub: composizione party, obiettivo, tabella sinottica sessioni
│           └── sessioni/                                  # Verbali progressivi numerati:
│               ├── README.md                              # Indice dei verbali
│               ├── 01_titolo_sessione.md                  # Verbale Sessione 1
│               └── 02_titolo_sessione.md                  # Verbale Sessione 2...
│
└── 10_timeline/                                           # Tomo X: Timeline e cronologia trasversale del mondo
    ├── README.md                                          # Legenda generale: date (anni del mondo), tag, navigazione
    ├── cronologia_storica/                                # Eventi passati, file per epoca/periodo (con tag di categoria)
    │   └── 01_<nome_epoca>.md
    ├── registro_occorrenze/                               # Occorrenze di festival/eventi e voci in divenire, file per epoca/periodo
    │   └── 01_<nome_periodo>.md
    ├── markwhen/                                          # Timeline grafica (sorgenti Markwhen, esclusi dalla Bibbia)
    │   ├── README.md                                      # Indice dei sorgenti .mw e sintesi convenzioni
    │   ├── timeline_generale.mw                           # Indice/legenda (non aggregato)
    │   ├── epoche/
    │   │   └── <nome_epoca>.mw                            # Sorgente per epoca/periodo storico
    │   └── campagne/
    │       └── <nome_campagna>.mw                         # Tutto il rilevante per la campagna (con link ai verbali)
    ├── calendario/                                        # Calendario del mondo: mesi, stagioni, giorni intercalari, mapping date
    │   └── 01_calendario.md
    └── esportazioni/                                      # Render grafici derivati (HTML/PNG/SVG/PDF della timeline)
        └── README.md                                      # Registro dei render grafici derivati
```
