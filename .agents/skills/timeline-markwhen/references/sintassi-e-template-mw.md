# Sintassi e Template Markwhen (`.mw`)

Riferimento operativo per la scrittura e l'aggiornamento dei file `.mw` in `10_timeline/markwhen/`.

---

## 1. Sintassi Canonica Markwhen

### Header YAML (`---`)

Ogni file `.mw` inizia con un blocco YAML tra `---` che definisce `title`, `description`, `timezone: UTC` (raccomandato per evitare offset storici LMT su anni antichi) e palette colori per i tag standard (eventuali intestazioni descrittive vanno scritte come commenti `//`, mai come `#NomeCategoria` senza `:`, per non invalidare il parser YAML; il formato ISO `AAAA-MM-GG` è nativo e non richiede `dateFormat`):

```yaml
---
title: "Titolo della Timeline"
description: "Descrizione sintetica del file .mw"
timezone: UTC

// Tipologia
#usanza: #8b5cf6
#festival: #f59e0b
#evento: #ef4444
#occorrenza: #ec4899

// Stato
#storico: #64748b
#in_svolgimento: #10b981
#pianificato: #3b82f6
#data_provvisoria: #eab308
---
```

### Formati delle Date (Anni del Mondo)

Le date usano gli **anni del mondo** espressi in formato ISO (`AAAA`, `AAAA-MM`, `AAAA-MM-GG`), con anni a 4 cifre (eventualmente preceduti da zeri per anni `< 1000`, es. `0512-03-01` o `512-03-01` in modo uniforme dentro lo stesso file):

- **Giorno singolo**: `512-03-01: Festa del Solstizio #festival #storico`
- **Mese approssimato**: `512-03: Convocazione del Consiglio #evento #storico`
- **Anno singolo**: `514: Torneo della Guardia #festival #occorrenza #in_svolgimento`
- **Intervallo di date**: `512-03-01/512-03-07: Fiera d'Autunno #festival #storico` oppure `512/513: Assedio della Cittadella #evento #storico`
- **Data non ancora definita**: non inventare numeri né omettere l'evento; **chiedi sempre prima al Master** (usando lo strumento di domande strutturate se disponibile o in chat) una data o un **anno provvisorio** e, se provvisorio, usa il tag `#data_provvisoria` con nota `- [DA_DEFINIRE_MASTER: data definitiva da confermare]`.

### Descrizioni, Sottopunti e Link Relativi

Sotto la riga dell'evento (indentati o su righe immediatamente successive prima della riga vuota) si inseriscono:

- Breve sintesi notarile o esito (se `#storico` / `#in_svolgimento`).
- Link Markdown relativi (senza backtick) alle schede canoniche o ai verbali, ribasati rispetto alla posizione del file `.mw`:
  - Da `10_timeline/markwhen/timeline_generale.mw`: `../../03_societa_e_politica/...`
  - Da `10_timeline/markwhen/epoche/<epoca>.mw` o `campagne/<campagna>.mw`: `../../../03_societa_e_politica/...` e `../../../09_cronache/campagne/...`

Esempio completo di voce:

```text
514-06-12: Torneo della Guardia — Edizione 514 #festival #occorrenza #in_svolgimento #luogo_cittadella_alta
- Stato: in svolgimento.
- Scheda canonica: [Il Torneo della Guardia](../../../03_societa_e_politica/usi_costumi_ed_eventi/festival_ed_occorrenze/01_torneo_guardia.md)
- Verbale correlato: [Sessione 02](../../../09_cronache/campagne/Cronache%20del%20Nord/sessioni/02_sessione.md)
```

### Raggruppamenti (`section` / `endSection`)

Usa `section Nome Sezione` ... `endSection` per raggruppare logicamente gli eventi (es. per sotto-periodo storico nei file di epoca, o per arco narrativo / atto nei file di campagna).

---

## 2. Tassonomia Obbligatoria dei Tag

Ogni evento in un file `.mw` deve avere **almeno 1 tag di Tipologia** e **1 tag di Stato**, più eventuali tag tematici e di campagna:

| Categoria | Tag ammessi | Regola d'uso |
| :--- | :--- | :--- |
| **Tipologia** *(obbligatorio)* | `#usanza` `#festival` `#evento` `#occorrenza` | `#occorrenza` si affianca a `#festival` o `#evento` quando si registra una verifica puntuale datata. |
| **Stato** *(obbligatorio)* | `#storico` `#in_svolgimento` `#pianificato` | Allineato con il campo stato del registro occorrenze e delle schede. |
| **Tematici** *(opzionali)* | `#fazione_<slug>` `#luogo_<slug>` `#PG_<slug>` `#PNG_<slug>` | Usa `snake_case` coerente con gli `id` di `struttura_ambientazione.json`. |
| **Campagna** *(opzionale/obbl. in campagne/)* | `#campagna_<slug>` | Obbligatorio per gli eventi che impattano una specifica campagna. |

---

## 3. Template 1: `10_timeline/markwhen/timeline_generale.mw`

`timeline_generale.mw` è l'**indice/legenda generale** (non duplica gli eventi dei singoli file):

```text
---
title: "Timeline Generale — Legenda e Indice Cronologico"
description: "Indice generale, legenda dei tag e convenzioni del calendario del mondo. I singoli eventi risiedono in epoche/ e campagne/."
timezone: UTC

// Tipologia
#usanza: #8b5cf6
#festival: #f59e0b
#evento: #ef4444
#occorrenza: #ec4899

// Stato
#storico: #64748b
#in_svolgimento: #10b981
#pianificato: #3b82f6
#data_provvisoria: #eab308
---

// ============================================================================
// LEGENDA E CONVENZIONI DEL CALENDARIO
// - Date espresse in Anni del Mondo (formato AAAA, AAAA-MM, AAAA-MM-GG).
// - Mapping del calendario: [Calendario del Mondo](../calendario/README.md)
// - Ricorrenze fisse: [DA_DEFINIRE_MASTER: elenco ricorrenze fisse annuali]
// ============================================================================

// ============================================================================
// INDICE DEI SORGENTI PER EPOCA (10_timeline/markwhen/epoche/)
// - [Epoca 01](epoche/01_<slug_epoca>.mw) — [Cronologia Storica](../cronologia_storica/01_<slug_epoca>.md)
// ============================================================================

// ============================================================================
// INDICE DEI SORGENTI PER CAMPAGNA (10_timeline/markwhen/campagne/)
// - [Campagna](campagne/<slug_campagna>.mw) — [Hub Campagna](../../09_cronache/campagne/<Nome_Campagna>/README.md)
// ============================================================================

section Quadro delle Epoche
// Riporta solo le macro-fasce temporali delle epoche (senza duplicare i singoli eventi)
// [DA_DEFINIRE_MASTER: intervallo anni Epoca 1]: Prima Epoca #storico
endSection
```

---

## 4. Template 2: `10_timeline/markwhen/epoche/<NN_slug_epoca>.mw`

```text
---
title: "Epoca: [Nome dell'Epoca]"
description: "Cronologia Markwhen dell'epoca [Nome dell'Epoca] — sincronizzata con cronologia_storica e registro_occorrenze."
timezone: UTC

#usanza: #8b5cf6
#festival: #f59e0b
#evento: #ef4444
#occorrenza: #ec4899
#storico: #64748b
#in_svolgimento: #10b981
#pianificato: #3b82f6
#data_provvisoria: #eab308
---

// Fonti canoniche sincronizzate:
// - Cronologia storica: [../../cronologia_storica/NN_<slug_epoca>.md](../../cronologia_storica/NN_<slug_epoca>.md)
// - Registro occorrenze: [../../registro_occorrenze/NN_<slug_epoca>.md](../../registro_occorrenze/NN_<slug_epoca>.md)

section Eventi Storici e Fondativi
// Esempio:
// 512/513: Assedio della Cittadella #evento #storico #fazione_guardia_del_nord
// - Esito: [sintesi canonica]
// - Scheda: [L'Assedio della Cittadella](../../../03_societa_e_politica/usi_costumi_ed_eventi/eventi/01_assedio_cittadella.md)
endSection

section Occorrenze e Voci in Divenire
// Esempio:
// 514: Torneo della Guardia #festival #occorrenza #in_svolgimento
// - Scheda: [Il Torneo della Guardia](../../../03_societa_e_politica/usi_costumi_ed_eventi/festival_ed_occorrenze/01_torneo_guardia.md)
endSection
```

---

## 5. Template 3: `10_timeline/markwhen/campagne/<slug_campagna>.mw`

```text
---
title: "Campagna: [Nome Campagna]"
description: "Timeline completa della campagna [Nome Campagna]: antefatti dei PG, sessioni giocate ed eventi futuri/pianificati."
timezone: UTC

#usanza: #8b5cf6
#festival: #f59e0b
#evento: #ef4444
#occorrenza: #ec4899
#storico: #64748b
#in_svolgimento: #10b981
#pianificato: #3b82f6
#data_provvisoria: #eab308
#campagna_<slug_campagna>: #f43f5e
---

// Hub della campagna: [../../../09_cronache/campagne/<Nome_Campagna>/README.md](../../../09_cronache/campagne/<Nome_Campagna>/README.md)

section Antefatti e Backstory PG
// Eventi pregressi rilevanti per i PG della campagna (#storico #campagna_<slug_campagna>)
endSection

section Cronaca delle Sessioni
// Eventi accaduti nelle sessioni verbalizzate (#storico o #in_svolgimento)
// Con link a ../../../09_cronache/campagne/<Nome_Campagna>/sessioni/XX_titolo.md
endSection

section Eventi in Svolgimento e Pianificati
// Finestre temporali, scadenze e occorrenze future (#in_svolgimento / #pianificato)
endSection
```
