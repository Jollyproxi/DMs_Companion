---
name: sincronizza-bibbia-struttura
description: "Use when: generare o aggiornare la Bibbia dell'Ambientazione (genera-Bibbia, aggiorna-bibbia) e il file struttura_ambientazione.json (genera-struttura-json, aggiorna-struttura-json), sincronizzare modifiche della lore tra i moduli a dieci tomi e i documenti master."
argument-hint: "Specifica l'operazione: genera-Bibbia, genera-struttura-json, aggiorna-bibbia, o aggiorna-struttura-json"
user-invocable: true
disable-model-invocation: false
---

# Skill: Sincronizzazione Canone Master (Bibbia & Struttura JSON)

Questa skill governa il ciclo vitale dei due artefatti master del mondo D&D:
1. **La Bibbia dell'Ambientazione** (`BIBBIA DELL'AMBIENTAZIONE.md` o eventuale file master monolitico già presente): il testo unico continuo per la consultazione narrativa dell'intero canone.
2. **Lo Schema Strutturale** (`struttura_ambientazione.json`): la mappa ontologica e tassonomica machine-readable dei dieci tomi, dei moduli, delle regioni/sottocartelle e dei concetti chiave.

La skill gestisce la generazione completa e l'allineamento incrementale bidirezionale tra i singoli file modulari dei dieci tomi e i documenti master, garantendo fedeltà al canone senza alterazioni non concordate col Dungeon Master.

Consultare i documenti di supporto:
- [formato-struttura-json](./references/formato-struttura-json.md): standard dello schema JSON, campi obbligatori ed estrazione concetti.
- [convenzioni-bibbia](./references/convenzioni-bibbia.md): regole di trasposizione dei titoli, ordine di compilazione e formattazione tabelle.

---

## Matrice delle Operazioni Supportate

| Argomento / Comando | Artefatto Target | Modalità | Scopo Principale |
| :--- | :--- | :--- | :--- |
| **`genera-Bibbia`** | `BIBBIA DELL'AMBIENTAZIONE.md` | Monolitica / Integrale | Compila tutti i file dei 10 tomi in un unico documento narrativo master. |
| **`genera-struttura-json`** | `struttura_ambientazione.json` | Ricognizione Completa | Scansiona l'alberatura dei tomi e genera il JSON tassonomico da zero. |
| **`aggiorna-bibbia`** | `BIBBIA DELL'AMBIENTAZIONE.md` | Incrementale / Delta | Aggiorna nella Bibbia solo le sezioni corrispondenti ai moduli modificati. |
| **`aggiorna-struttura-json`** | `struttura_ambientazione.json` | Incrementale / Delta | Sincronizza il JSON con i moduli aggiunti, ridenominati o aggiornati. |

> **📌 Regola Nomi Propri Collegati**: ogni nome proprio di entità dell'ambientazione (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico dell'entità (es. `[Nome](percorso/relativo/file.md)`), mai semplice testo nudo. Eccezioni: intestazioni, nomi di file, frontmatter, blocchi di codice, nodi Mermaid e sorgenti `.mw`. Entità priva di scheda: non inventarla — usa `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna. Verifica e conversione: skill `collega-nomi-propri`.

---

## 1. Procedura: `genera-Bibbia` (Compilazione Master)

Usa questa procedura per rigenerare o creare ex-novo la Bibbia dell'Ambientazione assemblando i singoli moduli.

### Passi Operativi:
1. **Rilevamento del File Target**:
   - Cerca nella radice del workspace il file master esistente (es. `BIBBIA DELL'AMBIENTAZIONE.md` o file equivalente già nominato nel repository).
   - Se non esiste alcun file master, crea `BIBBIA DELL'AMBIENTAZIONE.md`.
2. **Determinazione dell'Ordine dei Tomi**:
   - Legge `struttura_ambientazione.json` se disponibile per recuperare l'ordine ufficiale dei tomi e dei moduli.
   - In alternativa, ordina le directory con prefisso numerico: `01_cosmologia`, `02_geografia` (inclusa la sottocartella `regioni/` o `cornici/` ordinata numericamente), `03_societa_e_politica` (inclusa la sottoserie `usi_costumi_ed_eventi/`: `usanze/` = 3.5.x, `festival_ed_occorrenze/` = 3.6.x, `eventi/` = 3.7.x), `04_diritto_e_successione`, `05_personaggi` (`Non-Giocanti/`), `06_luoghi` (o `06_location`), `07_fazioni` (o `07_factions`), `08_oggetti_magici_peculiari` (o `08_oggetti magici peculiari`), `09_cronache`, `10_timeline` (`cronologia_storica/` = 10.1.x, `registro_occorrenze/` = 10.2.x, `calendario/` = 10.3.x; i sorgenti `.mw` di `markwhen/` e `esportazioni/` sono esclusi dalla Bibbia).
3. **Composizione del Testo Monolitico**:
   - Inserisci la testata canonica con metadati e badge di stato:
     ```markdown
     ### BIBBIA DELL'AMBIENTAZIONE: [NOME_AMBIENTAZIONE]
     
     > 📜 **Documento Master Monolitico del Canone**
     > *Versione Canone:* [VERSIONE] | *Ultima Compilazione:* [DATA_ODIERNA]
     > 🛡️ *Verificato: [DATA_V] | Modificato: [DATA_ODIERNA]*
     ```
   - Per ciascun tomo, inserisci l'intestazione H5 (es. `##### 1. Cosmologia & Architettura Metafisica`).
   - Per ciascun file modulare, adatta la gerarchia dei titoli come indicato in [convenzioni-bibbia](./references/convenzioni-bibbia.md):
     - L'intestazione H1 del modulo diventa `###### *X.Y Titolo Modulo*` (o `### X.Y Titolo Modulo`).
     - Preserva fedelmente le tabelle markdown, i diagrammi Mermaid e i box `**NOTA PER IL DUNGEON MASTER:**`.
     - Preserva tutti i marcatori `[DA_DEFINIRE_MASTER]`.
4. **Scrittura e Report**:
   - Salva il file master compilato.
   - Presenta al Master un resoconto: numero di tomi processati, file inclusi e dimensione complessiva del documento.

---

## 2. Procedura: `genera-struttura-json` (Mappatura Tassonomica Completa)

Usa questa procedura per scansionare tutti i file del workspace e produrre una mappa machine-readable completa e aggiornata in formato JSON.

### Passi Operativi:
1. **Acquisizione Informazioni Generali**:
   - Legge il `README.md` radice o la testata della Bibbia per estrarre `nome_ambientazione`, `descrizione` e determinare il `documento_sorgente`.
   - Imposta la versione iniziale su `"1.0.0"` (o mantiene la versione attuale se presente).
2. **Scansione Sistematica dei 10 Tomi**:
   - Itera attraverso le cartelle da `01_` a `10_`:
     - Estrae `id`, `codice`, `titolo` e `descrizione` dal `README.md` del tomo.
     - Raccoglie tutti i file `.md` dei moduli contenuti nella cartella (escludendo `README.md`).
     - Per ciascun modulo `.md`:
       - `id`: slug snake_case ricavato dal nome file senza prefisso numerico.
       - `codice`: numerazione gerarchica (es. `"1.1"` per `01_cosmologia/01_struttura_verticale.md`).
       - `titolo`: estratto dal primo tag `#` del file.
       - `file`: percorso relativo normalizzato con `/`.
       - `concetti_chiave`: estrae da 3 a 7 punti salienti ricavati dai sottotitoli e dalle definizioni in grassetto.
       - `tabelle`: rileva e inserisce i titoli delle tabelle markdown presenti.
       - `note_dm`: estrae il contenuto di eventuali note per il DM.
   - Gestisce le sottocartelle canoniche (`02_geografia/regioni/` o `cornici/`, `03_societa_e_politica/usi_costumi_ed_eventi/`, `05_personaggi/Non-Giocanti/`, `09_cronache/campagne/`, `10_timeline/` con i sorgenti `markwhen/`) popolando le proprietà dedicate definite in [formato-struttura-json](./references/formato-struttura-json.md).
3. **Validazione Sintattica e Scrittura**:
   - Genera il file `struttura_ambientazione.json` con indentazione a 2 spazi.
   - Valida che il JSON sia formalmente valido e privo di chiavi duplicate o caratteri spuri.
   - Notifica il Master con il riepilogo del totale dei moduli e delle sottostrutture indicizzate.

---

## 3. Procedura: `aggiorna-bibbia` (Sincronizzazione Incrementale)

Usa questa procedura quando uno o più moduli atomici sono stati modificati o aggiunti, per allineare la Bibbia monolitica senza rigenerare l'intero file.

### Passi Operativi:
1. **Identificazione dei File Modificati**:
   - Rileva i moduli target specificati dal Master o individua i file con `Modificato > Verificato` analizzando i badge o la dashboard `STATO_REVISIONE.md`.
2. **Localizzazione della Sezione nel File Master**:
   - Apri il file master della Bibbia.
   - Per ciascun modulo modificato, individua l'ancora della sezione tramite il codice gerarchico (`X.Y`) o il titolo del modulo.
3. **Aggiornamento Mirato della Sezione**:
   - Se la sezione esiste: sostituisci il testo obsoleto con la nuova versione modulare (adattando i livelli di intestazione secondo [convenzioni-bibbia](./references/convenzioni-bibbia.md)).
   - Se il modulo è nuovo: inserisci la nuova sezione nella corretta posizione ordinale all'interno del tomo di pertinenza.
   - Lascia rigorosamente inalterate tutte le altre sezioni del documento.
4. **Aggiornamento Metadati Master**:
   - Aggiorna la riga di metadati in testata:
     `> 🛡️ *Verificato: [DATA_V] | Modificato: [DATA_ODIERNA]*`
5. **Report di Allineamento**:
   - Elenca al Master i paragrafi aggiornati nella Bibbia.

---

## 4. Procedura: `aggiorna-struttura-json` (Sincronizzazione Delta JSON)

Usa questa procedura per mantenere `struttura_ambientazione.json` sincronizzato quando vengono aggiunti nuovi file, ridenominati moduli o arricchiti i contenuti.

### Passi Operativi:
1. **Caricamento dello Stato Attuale**:
   - Legge il file `struttura_ambientazione.json` esistente.
2. **Rilevamento del Delta**:
   - Confronta i file fisici presenti sul disco nelle cartelle dei 10 tomi con l'elenco presente nell'array `struttura`.
   - Identifica:
     - ➕ **Moduli Aggiunti**: file `.md` presenti sul disco ma assenti nel JSON.
     - 🔄 **Moduli Modificati**: file con titoli, tabelle o concetti chiave modificati.
     - ➖ **Moduli Rimossi o Ridenominati**: percorsi nel JSON non più esistenti su disco.
3. **Applicazione delle Modifiche al JSON**:
   - Per i moduli aggiunti: crea il nuovo oggetto con `id`, `codice`, `titolo`, `file`, `concetti_chiave`, `tabelle`, `note_dm` e ordinalo correttamente.
   - Per i moduli modificati: aggiorna i campi `titolo`, `concetti_chiave` e `tabelle`, preservando eventuali annotazioni custom preesistenti.
   - Per i moduli rimossi/spostati: aggiorna il percorso `file` o rimuovi l'elemento obsoleto (chiedendo conferma al Master prima di cancellare).
4. **Incremento di Versione**:
   - Incrementa la versione secondo SemVer (es. da `"1.0.0"` a `"1.0.1"` per modifiche di contenuto, oppure `"1.1.0"` per nuovi moduli/regioni).
5. **Salvataggio e Diff**:
   - Riscrivi `struttura_ambientazione.json` formattato.
   - Mostra al Master un riepilogo puntuale delle entità aggiunte, aggiornate o rimosse.

---

## Interazione Strutturata

Se l'utente invoca la skill senza specificare chiaramente l'operazione desiderata o se emergono conflitti durante l'aggiornamento, chiedi quale operazione eseguire (usando lo strumento di domande strutturate dell'ambiente come `vscode_askQuestions` / `AskUserQuestion` se disponibile, altrimenti in chat) presentando queste opzioni:
- `genera-Bibbia` — Compila tutti i moduli dei 10 tomi nel documento master monolitico
- `genera-struttura-json` — Rigenera integralmente `struttura_ambientazione.json` scansionando l'archivio
- `aggiorna-bibbia` — Sincronizza nella Bibbia solo i moduli modificati o aggiunti di recente
- `aggiorna-struttura-json` — Aggiorna incrementalmente `struttura_ambientazione.json` con il delta dei file

---

## Criteri di Qualità e Validazione Finale

Al termine di ciascuna operazione:
1. **Verifica Sintattica JSON**: In caso di operazioni su `struttura_ambientazione.json`, accertarsi che il file sia un JSON rigorosamente valido.
2. **Controllo dei Link e dei Percorsi**: I percorsi `file` nel JSON e i riferimenti incrociati nella Bibbia devono puntare a file esistenti.
3. **Zero Allucinazioni**: Non inserire mai concetti, PNG o fazioni non documentati nei file sorgente o non approvati dal Master.
4. **Integrazione con Altre Skill**:
   - Dopo modifiche strutturali rilevanti, suggerire l'esecuzione di `valida-struttura`.
   - Dopo l'aggiornamento della Bibbia o dei moduli, ricordare l'aggiornamento della dashboard con `stato-revisione`.
