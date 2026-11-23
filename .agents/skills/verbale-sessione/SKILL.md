---
name: verbale-sessione
description: "Use when: verbalizzare una sessione di D&D, importare una trascrizione strutturata da NotebookLM o altro LLM, condurre l'intervista post-sessione al Master, redigere il verbale formale con diagramma Mermaid dei ganci PG e aggiornare l'indice della campagna."
argument-hint: "Incolla gli appunti, un resoconto da trascrizione NotebookLM/LLM oppure scrivi 'inizia intervista' per avviare la procedura guidata"
user-invocable: true
disable-model-invocation: false
---

# Skill: Verbalizzazione di Sessione (Verbale-Sessione)

> **Conoscenze nella fiction** — Se il resoconto confermato indica chi ha appreso un fatto, usa **Aggiornamento** di `conoscenze-campagna` sulla scheda canonica. Una presenza in sessione da sola non dimostra che il PG abbia appreso il fatto. Se la skill è installata ma il client non la rileva, leggi direttamente il suo `SKILL.md`. Se manca, prosegui con il flusso ordinario.

Questa skill guida la raccolta, strutturazione e formattazione dei verbali di sessione di gioco per qualsiasi campagna D&D, garantendo conformità al modello standard documentato in [template-verbale](./references/template-verbale.md). Per estrarre prima un resoconto notarile da registrazioni audio o trascrizioni lunghe tramite **NotebookLM** o un altro LLM, usa il prompt dedicato in [prompt-trascrizione-sessione](./references/prompt-trascrizione-sessione.md). Prima di avviare NotebookLM o un altro LLM, puoi anche generare dal repository l'elenco compatto di sola grafia dei nomi propri già noti con la skill `glossario-trascrizione` per ridurre i `[?]`.

> **📌 Regola Nomi Propri Collegati**: ogni nome proprio di entità dell'ambientazione (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico dell'entità (es. `[Nome](percorso/relativo/file.md)`), mai semplice testo nudo. Eccezioni: intestazioni, nomi di file, frontmatter, blocchi di codice, nodi Mermaid e sorgenti `.mw`. Entità priva di scheda: non inventarla — usa `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna. Verifica e conversione: skill `collega-nomi-propri`.

---

## 1. Regola Aurea (Zero Allucinazioni)

- **Fedeltà Assoluta**: Non inventare PNG, dialoghi, luoghi o retroscena non descritti dal Master.
- **Lacune**: Se mancano dettagli essenziali (es. nome di un PNG o esito di uno scontro), chiedili durante l'intervista o segnalali con `[DA_DEFINIRE_MASTER: descrizione]`.

---

## 2. Modalità di Raccolta Dati

### Canale A: Intervista Guidata Post-Sessione
Attivabile con *"inizia intervista"* o a sessione appena conclusa. Poni al Master le domande in modo strutturato (usando lo strumento interattivo dell'ambiente come `vscode_askQuestions` o `AskUserQuestion` se disponibile, altrimenti direttamente in chat):
1. **`coordinate_sessione`**: *Numero della sessione, data in-game e teatro geografico degli eventi?* (Campo libero con prompt sintetico).
2. **`pg_presenti`**: *Quali Personaggi Giocanti erano presenti?*
   - Opzioni a selezione multipla ricavate dai dossier censiti in `05_personaggi/<Giocanti>/<Campagna_o_Party>/` (con possibilità di aggiungere nomi liberi per PG nuovi o PNG di spicco).
3. **`cronologia_eventi`**: *Cosa è accaduto in sequenza (inizio, snodi centrali, scontri/trattative, epilogo)?* (Campo libero).
4. **`ganci_rivelazioni`**: *Quali scoperte, indizi o svolte hanno toccato specificamente i singoli PG?* (Campo libero per generare il diagramma Mermaid).
5. **`dati_meccanici`**: *Ci sono risorse meccaniche da registrare?*
   - Opzioni: *Nessuna (solo narrazione)*, *Monete & Spese*, *Oggetti magici / Bottino*, *Danni permanenti, condizioni o debiti* (con inserimento dettagli se selezionato).

### Canale B: Rielaborazione Appunti Grezzi
Se il Master incolla note disordinate, estrai la cronologia, isola i dati certi e compila direttamente la bozza. Se mancano dettagli critici, chiedi al Master di colmare unicamente le lacune (tramite lo strumento di domande strutturate se disponibile o in chat) prima di salvare il file.

### Canale C: Importazione da Trascrizione Strutturata (NotebookLM / LLM)
Se il Master fornisce un resoconto generato con [prompt-trascrizione-sessione](./references/prompt-trascrizione-sessione.md) (da audio o trascrizione lunga):
1. **Mappatura sul Verbale**:
   - `Scheda` + `Chi c'è` + `Cronologia` → *Intestazione*, *Sinossi degli Eventi* e *Fasi Salienti* (risolvendo ogni nome proprio esistente in link Markdown secondo la Regola Nomi Propri Collegati).
   - `Cambi di stato e indizi` (+ `Numeri` e `Impegni` pertinenti) → *I Ganci dei Protagonisti* (diagramma Mermaid `flowchart TD` e sottosezioni per PG) ed eventuale *Registro Meccanico* se richiesto.
   - `Fatti per elemento` (tassonomia Dieci Tomi), `Impegni`, `Numeri`, `Tempo` e `Blocco dati` YAML → lista dei file impattati e proposte di aggiornamento incrociato (nuovi PNG, oggetti magici, usi/costumi/eventi, `10_timeline/`).
2. **Controllo Notarile Prima di Canonizzare**:
   - Confronta nomi, varianti e fatti con i file canonici già presenti nel repository.
   - Prima di salvare o creare schede derivate, **chiedi conferma al Master** (tramite lo strumento di domande strutturate se disponibile, altrimenti in chat) per risolvere eventuali `Nome[?]`, `(inferenza)`, `Varianti / alias uditi`, voci in `Domande aperte`, `Contraddizioni` o lacune `[incomprensibile ...]` non già chiarite dal canone: non normalizzare né indovinare mai in autonomia.
3. **Resoconto Incompleto**: se il resoconto termina con `[CONTINUA DA: ...]`, segnala al Master la porzione mancante prima di procedere con l'archiviazione definitiva.

---

## 3. Redazione del Verbale

Il verbale viene compilato secondo le sezioni canoniche:
1. **Intestazione**: Dati tecnici e collegamenti Markdown relativi ai dossier di PG e luoghi.
2. **Sinossi degli Eventi**: Registro notarile formale in terza persona, fluido e ordinato.
3. **I Ganci dei Protagonisti**:
   - Diagramma Mermaid `flowchart TD` che connette la minaccia o l'evento cardine ai singoli PG.
   - Sottosezioni per ciascun PG con l'elemento riconosciuto/ottenuto e l'impatto narrativo.
4. **Fasi Salienti**: Elenco numerato di sintesi per consultazione rapida a sessione in corso.
5. **Registro Meccanico (Opzionale)**: Presente solo se espressamente richiesto.

---

## 4. Archiviazione e Propagazione

1. **Salvataggio File**:
   Salva in `09_cronache/<campagne>/<nome_campagna>/<sessioni>/XX_titolo_sessione.md` *(default: `09_cronache/campagne/<nome_campagna>/sessioni/...`, rispettando eventuali nomi custom configurati come `spedizioni/`, `avventure/`, `diari/`)*.
2. **Aggiornamento Indice Campagna**:
   Inserisci la nuova riga nella tabella sinottica di `09_cronache/<campagne>/<nome_campagna>/README.md`:
   `| **XX** | [Titolo] | [Data] | [Luogo] | [Focus Principale] | [Verbale](<sessioni>/XX_titolo.md) |`
3. **Proposta Aggiornamenti Incrociati (A + B + C)**:
   - Elenca a fine risposta quali file della repository risultano impattati (nuovi PNG, oggetti magici trovati, ganci da aggiornare nei dossier PG con la skill `dossier-personaggio`).
   - **Usi, costumi ed eventi**: se la sessione introduce o menziona una nuova usanza, un nuovo festival/occorrenza o un nuovo evento, **proponi sempre** la creazione della scheda relativa in `03_societa_e_politica/usi_costumi_ed_eventi/` con la skill `usanza-festa-evento`.
   - **Occorrenze di eventi già censiti e Timeline Markwhen**: se la sessione fa svolgere una ricorrenza nota (es. un torneo annuale o una festa stagionale) o introduce eventi datati, documentali nel verbale e registrali nella `10_timeline/` (registro occorrenze e sorgenti `.mw` tramite la skill `timeline-markwhen`), poi **chiedi al Master** se modificare la scheda canonica: le peculiarità proprie dell'occorrenza restano nella timeline e nei verbali, e la scheda si aggiorna solo se ne stravolgono la natura.
   - Mostra le modifiche e offriti di applicarle previa conferma.

## Pettegolezzi e dicerie

Registra chi ha sentito o diffuso quale versione solo se attestato dal verbale confermato. Conserva stato, attribuzione e link alla variante. Riporta il contenuto della voce solo come tale. Registra in cronologia un evento solo quando attestato indipendentemente.
