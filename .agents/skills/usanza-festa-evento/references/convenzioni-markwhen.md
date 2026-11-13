# Convenzioni della Timeline Grafica Markwhen

Standard di compilazione dei sorgenti Markwhen contenuti in `10_timeline/markwhen/`, la timeline grafica del mondo.

---

## 1. Struttura della Cartella `markwhen/`

```text
10_timeline/markwhen/
├── README.md                   # Indice dei sorgenti .mw e sintesi convenzioni
├── timeline_generale.mw        # Indice/legenda generale (NON un aggregato dei sorgenti)
├── epoche/
│   └── <nome_epoca>.mw         # Un sorgente per epoca/periodo storico
└── campagne/
    └── <nome_campagna>.mw      # Un sorgente per campagna: tutto il rilevante per quella campagna
```

- `timeline_generale.mw` è l'**indice/legenda**: contiene la legenda dei tag, le convenzioni delle date e i collegamenti ai sorgenti per epoca e per campagna. Non duplica il contenuto degli altri file.
- I file in `epoche/` sono le fonti effettive della cronologia, consultabili singolarmente.
- I file in `campagne/` contengono **tutto il rilevante** per la campagna (passato e futuro), con link ai verbali di `09_cronache/`.

---

## 2. Sintassi di Base

Un evento per riga, con data, titolo e tag:

```text
512-03-01: Festa del Solstizio #festival #storico
512/513: Assedio della Cittadella #evento #storico #fazione_guardia_del_nord
514: Torneo della Guardia #festival #occorrenza #in_svolgimento
```

- **Intervalli**: `data_inizio/data_fine` (es. `512-03-01/512-03-07`).
- **Date imprecise**: solo l'anno (es. `512`) o l'anno con mese approssimato (`512-03`).
- **Tag**: suffissi `#tag` sulla stessa riga dell'evento.
- **Collegamenti alle schede**: nei commenti/descrizioni dell'evento, link Markdown relativi alle schede canoniche (es. `[Torneo della Guardia](../../../03_societa_e_politica/usi_costumi_ed_eventi/festival_ed_occorrenze/01_torneo_guardia.md)`), adattando il percorso alla posizione del file `.mw`.

---

## 3. Convenzione delle Date

- Le date usano gli **anni del mondo** trattandoli come date (es. `512-03-01`, `512`, `512/513`).
- Il mapping con il calendario reale del mondo (mesi, stagioni, giorni intercalari) è documentato in `10_timeline/calendario/` e riassunto nella legenda di `timeline_generale.mw`.
- Se un evento ha periodicità fissa, la data/ricorrenza va comunque esplicitata nella legenda del calendario.

---

## 4. Tassonomia dei Tag

| Categoria | Tag | Uso |
| :--- | :--- | :--- |
| **Tipologia** | `#usanza` `#festival` `#evento` `#occorrenza` | Natura della voce; `#occorrenza` marca la verifica singola di un evento ricorrente. |
| **Stato** | `#storico` `#in_svolgimento` `#pianificato` | Stato dell'occorrenza secondo il modello delle schede. |
| **Tematici** | `#fazione_<slug>` `#luogo_<slug>` `#PG_<slug>` `#PNG_<slug>` | Filtri per attore o ambientazione (es. `#fazione_lega_mercanti`, `#luogo_porto_alto`). |
| **Campagna** | `#campagna_<nome>` | Isola ciò che riguarda una specifica campagna. |

Le stesse categorie di tag vanno usate nelle voci di `10_timeline/cronologia_storica/` e `10_timeline/registro_occorrenze/`, così le due rappresentazioni restano sincronizzate.

---

## 5. Regole di Aggiornamento

1. **Nuova voce o occorrenza**: aggiungere la riga al sorgente dell'epoca corretta in `epoche/`; se rilevante per una campagna, aggiungerla anche al sorgente in `campagne/<nome>.mw`.
2. **Cambio di stato** (pianificato → in svolgimento → concluso): aggiornare il tag di stato nella riga dell'evento e l'esito nelle note.
3. **Legenda**: se si introducono nuovi tag o voci di calendario, aggiornare `timeline_generale.mw`.
4. **Esclusioni canone**: i file `.mw` e il contenuto di `esportazioni/` sono **esclusi dalla Bibbia** dell'Ambientazione; vengono indicizzati solo in `struttura_ambientazione.json` (sottostruttura dedicata del tomo `10`).
5. **Zero allucinazioni**: nessun evento, data o esito non approvato dal Master.
