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
Verifica la presenza delle directory canoniche (accettando eventuali varianti già in uso o personalizzate dal Master nel repository come `06_location`, `07_factions`, `08_oggetti magici peculiari` o nomi custom):
1. `01_cosmologia` *(con eventuali sottocartelle opzionali custom per piani/sfere e pantheon/divinità)*
2. `02_geografia` *(con eventuale sottocartella `regioni/` o nome custom scelto per le macro-aree, es. `province/`, `continenti/`, `domini/`, `cornici/`)*
3. `03_societa_e_politica` *(con eventuale sottocartella opzionale `popoli/` o nome custom, e sottocartella obbligatoria `usi_costumi_ed_eventi/` contenente `usanze/`, `festival_ed_occorrenze/`, `eventi/`)*
4. `04_diritto_e_leggi` *(con sottocartelle `01_ordinamento_e_fonti/` … `10_diritto_bellico_e_avventurieri/`, più eventuali branche custom `11_+` o sottocartelle per giurisdizione)*
5. `05_personaggi` *(con sottocartelle `<Giocanti>/` [default `Giocanti/`, es. `PG/`, `Eroi/`], organizzate per `<Campagna_o_Party>/`, e `<Non-Giocanti>/` [default `Non-Giocanti/`, es. `PNG/`] con eventuali sottocartelle di raggruppamento opzionali)*
6. `06_luoghi` *(o variante `06_location`; con eventuali sottocartelle opzionali custom per tipologia o macro-area)*
7. `07_fazioni` *(o variante `07_factions`; con eventuali sottocartelle opzionali custom per tipologia)*
8. `08_oggetti_magici_peculiari` *(o variante `08_oggetti magici peculiari` o nome custom es. `08_oggetti_magici/`, `08_artefatti_e_reliquie/`; con eventuali sottocartelle opzionali per categoria)*
9. `09_cronache` *(con sottocartella `<campagne>/` [default `campagne/`, es. `spedizioni/`, `avventure/`, `one_shot/`] e `<sessioni>/` [default `sessioni/`, es. `diari/`, `capitoli/`])*
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
   - Valida le cartelle dei 10 tomi e le rispettive sottocartelle canoniche, opzionali o personalizzate (`<piani>/`, `<pantheon>/`, `<regioni>/`, `popoli/`, `usi_costumi_ed_eventi/`, `04_diritto_e_leggi/`, `05_personaggi/`, `<gruppi_luoghi>/`, `<gruppi_fazioni>/`, `<categorie>/`, `<campagne>/<sessioni>/`, `10_timeline/`).
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
