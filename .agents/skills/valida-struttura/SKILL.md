---
name: valida-struttura
description: "Use when: verificare l'integrità strutturale della repository di un mondo D&D, rilevare cartelle mancanti, indici README assenti, collegamenti Markdown rotti, nomi propri non collegati e file fuori posto."
argument-hint: "Esegue il controllo di conformità strutturale dell'archivio"
user-invocable: true
disable-model-invocation: false
---

# Skill: Validazione della Struttura del Mondo (Valida-Struttura)

Questa skill esegue un audit diagnostico approfondito dell'alberatura dei file della repository, assicurando che rispetti la conformità dell'architettura standard D&D e identificando tempestivamente anomalie tecniche.

> **📌 Regola Nomi Propri Collegati**: ogni nome proprio di entità dell'ambientazione (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico dell'entità (es. `[Nome](percorso/relativo/file.md)`), mai semplice testo nudo. Eccezioni: intestazioni, nomi di file, frontmatter, blocchi di codice, nodi Mermaid e sorgenti `.mw`. Entità priva di scheda: non inventarla — usa `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna. Verifica e conversione: skill `collega-nomi-propri`.

---

## 1. Criteri di Verifica Diagnostica

La skill controlla i cinque pilastri dell'integrità strutturale:

### A. Conformità dei Dieci Tomi
Verifica la presenza delle directory canoniche (accettando eventuali varianti già in uso nel repository come `06_location`, `07_factions`, `08_oggetti magici peculiari` o `cornici/`):
1. `01_cosmologia`
2. `02_geografia`
3. `03_societa_e_politica` (con sottocartella `usi_costumi_ed_eventi/` contenente `usanze/`, `festival_ed_occorrenze/`, `eventi/`)
4. `04_diritto_e_successione`
5. `05_personaggi` (con sottocartelle `Giocanti/` e `Non-Giocanti/`)
6. `06_luoghi` *(o variante `06_location`)*
7. `07_fazioni` *(o variante `07_factions`)*
8. `08_oggetti_magici_peculiari` *(o variante `08_oggetti magici peculiari`)*
9. `09_cronache` (con sottocartella `campagne/`)
10. `10_timeline` (con sottocartelle `cronologia_storica/`, `registro_occorrenze/`, `markwhen/`, `calendario/`, `esportazioni/`)

### B. Presenza e Validità degli Indici (`README.md`)
Verifica che ciascuna cartella e sottocartella principale contenga un file `README.md` operativo che funge da hub e indice di sezione.

### C. Rilevamento dei Link Markdown Rotti
Scansiona i collegamenti relativi nei file `.md` (es. `[Nome](../../05_personaggi/...)`) per verificare che i file target esistano effettivamente sul disco, segnalando eventuali percorsi errati o ridenominazioni non sincronizzate.

### D. File Orfani o Fuori Posto
Individua file `.md` salvati nella radice del progetto o in percorsi non canonici che dovrebbero essere collocati all'interno di uno dei dieci tomi specifici (escludendo i file master radice canonici come `README.md`, `AGENTS.md`, `CLAUDE.md`, `BIBBIA DELL'AMBIENTAZIONE.md`, `STATO_REVISIONE.md`). Per la validazione sintattica e incrociata dei sorgenti `.mw` in `10_timeline/markwhen/`, si integra con la skill `timeline-markwhen` (`valida-mw`).

### E. Copertura dei Nomi Propri Collegati
Verifica che ogni nome proprio di entità censita (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) compaia nel testo come **collegamento Markdown** al file `.md` canonico dell'entità e non come semplice testo nudo (regola dei nomi-propri-collegati, con le eccezioni previste). La scansione analitica e la conversione dei nomi sono demandate alla skill `collega-nomi-propri`, di cui questo pilastro costituisce il controllo diagnostico di superficie.

---

## 2. Procedura Operativa

1. **Scansione del File System**:
   - Esegui una ricognizione delle cartelle e dei file `.md` presenti nel workspace escludendo directory tecniche (`.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Esecuzione dei Test A-B-C-D-E**:
   - Valida le cartelle dei 10 tomi (incluse le sottocartelle `usi_costumi_ed_eventi/` e `10_timeline/`).
   - Controlla i `README.md` mancanti.
   - Analizza le stringhe di link `[Testo](percorso)` e verifica l'esistenza del file tramite path relativo.
   - Ispeziona la radice per rilevare file orfani.
   - Controlla che i nomi propri di entità censite compaiano come collegamenti e non come testo nudo (per l'analisi approfondita delega a `collega-nomi-propri`).
3. **Produzione del Report Diagnostico**:
   - Mostra al Master un riepilogo sintetico:
     - 🟢 **Conformità Alberatura**: [OK / Segnalazioni Tomi Mancanti]
     - 🟢 **Copertura Indici README**: [OK / Elenco cartelle sprovviste]
     - 🔗 **Integrità Collegamenti**: [OK / Elenco link rotti con riga e file]
     - 🏷️ **Nomi Propri Collegati**: [OK / Elenco nomi non collegati con file e riga]
     - 📂 **Posizionamento File**: [OK / File orfani suggeriti per lo spostamento]
4. **Proposta di Riparazione Automatica**:
   - Se vengono rilevate anomalie, chiedi al Master (usando lo strumento di domande strutturate dell'ambiente come `vscode_askQuestions` / `AskUserQuestion` se disponibile, altrimenti in chat) come procedere:
     - `Ripara automaticamente le anomalie (genera README mancanti e correggi percorsi)`
     - `Mostra solo il report senza modificare file`
