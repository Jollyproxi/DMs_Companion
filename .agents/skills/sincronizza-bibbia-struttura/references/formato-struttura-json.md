# Specifica e Formato di `struttura_ambientazione.json`

Il file `struttura_ambientazione.json` rappresenta la mappa ontologica e tassonomica machine-readable dell'intera ambientazione. Funge da indice strutturato per agenti AI, strumenti di visualizzazione, script di validazione e interrogazioni rapide.

---

## 1. Schema Radice del Documento

```json
{
  "nome_ambientazione": "Nome dell'Ambientazione",
  "versione": "1.0.0",
  "documento_sorgente": "BIBBIA DELL'AMBIENTAZIONE.md",
  "descrizione": "Sintesi concisa dei pilastri dell'ambientazione in 2-3 frasi.",
  "struttura": [
    /* Array dei 10 tomi canonici */
  ]
}
```

### Campi Radice
* `nome_ambientazione` *(string)*: Titolo ufficiale dell'ambientazione.
* `versione` *(string, SemVer)*: Versione corrente del canone (es. `"1.0.0"`). Viene incrementata (`patch` per correzioni/aggiornamenti a moduli esistenti, `minor` per aggiunta di nuovi moduli/regioni/fazioni).
* `documento_sorgente` *(string)*: Percorso relativo del file master monolitico della Bibbia.
* `descrizione` *(string)*: Descrizione ad alto livello dell'architettura e della tematica (cosmologia, società, conflitti centrali).
* `struttura` *(array)*: Elenco ordinato degli oggetti capitolo/tomo (da 01 a 10).

---

## 2. Oggetto Tomo / Capitolo

Ciascun elemento dell'array `struttura` rappresenta uno dei dieci tomi dell'architettura:

```json
{
  "id": "cosmologia",
  "codice": "01",
  "titolo": "Cosmologia & Architettura Metafisica",
  "cartella": "01_cosmologia",
  "indice": "01_cosmologia/README.md",
  "descrizione": "Sintesi dei contenuti trattati nel tomo.",
  "moduli": [
    /* Array dei singoli file modulari */
  ]
}
```

### Campi del Tomo
* `id` *(string)*: Identificatore univoco snake_case senza prefisso numerico (es. `"cosmologia"`, `"geografia"`, `"diritto_successione"`).
* `codice` *(string)*: Numero del tomo a due cifre (`"01"` - `"10"`).
* `titolo` *(string)*: Titolo formale del tomo, desunto dal rispettivo `README.md`.
* `cartella` *(string)*: Nome della directory relativa alla radice (es. `"01_cosmologia"`).
* `indice` *(string)*: Percorso relativo del file `README.md` hub del tomo.
* `descrizione` *(string)*: Descrizione dell'argomento trattato nel tomo.
* `moduli` *(array)*: Elenco dei singoli moduli appartenenti al tomo.

---

## 3. Oggetto Modulo

Ciascun elemento dell'array `moduli` descrive un file `.md` atomico:

```json
{
  "id": "struttura_verticale",
  "codice": "1.1",
  "titolo": "La Struttura Planare e Cosmica",
  "file": "01_cosmologia/01_struttura_verticale.md",
  "concetti_chiave": [
    "Piano Materiale e confini planari",
    "Sfere celesti e reami esterni",
    "Sottosuolo e faglie profonde",
    "Piani elementali e varchi liminali"
  ],
  "tabelle": [
    "Tabella Sinottica dei Piani"
  ],
  "note_dm": "Dettaglio di rilevanza per il Master (opzionale)"
}
```

### Campi del Modulo
* `id` *(string)*: Identificativo univoco snake_case ricavato dal nome del file (senza prefisso numerico né estensione).
* `codice` *(string)*: Codice gerarchico decimale (es. `"1.1"`, `"2.3"`, `"7.8"`).
* `titolo` *(string)*: Titolo esatto del modulo (corrispondente all'intestazione H1 del file `.md`).
* `file` *(string)*: Percorso relativo del file markdown dalla radice del workspace.
* `concetti_chiave` *(array di stringhe)*: Da 3 a 7 punti elenco concisi che riassumono le regole, la lore e le istituzioni fondamentali introdotte nel modulo.
* `tabelle` *(array di stringhe, opzionale)*: Nomi delle tabelle markdown presenti nel documento. Omettere o lasciare vuoto se assenti.
* `note_dm` *(string, opzionale)*: Sintesi di eventuali box `NOTA PER IL DUNGEON MASTER` o ganci narrativi speciali.

---

## 4. Sottostrutture Speciali (Regioni, Schede PNG, Campagne, Eventi, Timeline)

Per tomi che contengono sottocartelle canoniche:

### A. Tomo 02 (Geografia - Sottocartella `regioni/` o `cornici/`)
Se presente una sottodirectory regionale:
```json
"cartella_regioni": "02_geografia/regioni",
"indice_regioni": "02_geografia/regioni/README.md",
"moduli_regioni": [
  {
    "numero": 1,
    "titolo": "1ª Regione — Marca Settentrionale",
    "tratto_distintivo": "Clima rigido / Frontiera mineraria",
    "file": "02_geografia/regioni/01_marca_settentrionale.md"
  }
]
```
*(In ambientazioni esistenti con cartelle `cornici/`, è ammesso mantenere i nomi chiave `cartella_cornici` / `moduli_cornici`.)*

### B. Tomo 05 (Personaggi - Sottocartelle `Giocanti/` e `Non-Giocanti/`)
```json
"sottocartelle": {
  "giocanti": "05_personaggi/Giocanti",
  "non_giocanti": "05_personaggi/Non-Giocanti"
}
```

### C. Tomo 09 (Cronache - Sottocartella `campagne/`)
```json
"cartella_campagne": "09_cronache/campagne",
"campagne_attive": [
  {
    "id": "nome_campagna",
    "indice": "09_cronache/campagne/nome_campagna/README.md",
    "sessioni_totali": 12
  }
]
```

### D. Tomo 03 (Società e Politica - Sottoserie `usi_costumi_ed_eventi/`)
```json
"cartella_usi_costumi_ed_eventi": "03_societa_e_politica/usi_costumi_ed_eventi",
"indice_usi_costumi_ed_eventi": "03_societa_e_politica/usi_costumi_ed_eventi/README.md",
"moduli_usanze": [
  {
    "id": "cerimonia_commiato",
    "codice": "3.5.1",
    "titolo": "La Cerimonia del Commiato",
    "file": "03_societa_e_politica/usi_costumi_ed_eventi/usanze/01_cerimonia_commiato.md"
  }
],
"moduli_festival_occorrenze": [
  {
    "id": "torneo_guardia",
    "codice": "3.6.1",
    "titolo": "Il Torneo della Guardia",
    "file": "03_societa_e_politica/usi_costumi_ed_eventi/festival_ed_occorrenze/01_torneo_guardia.md",
    "periodicita": "variabile",
    "scaturiggine": "Ritorno di spedizioni militari o ricambio dei ranghi"
  }
],
"moduli_eventi": [
  {
    "id": "assedio_cittadella",
    "codice": "3.7.1",
    "titolo": "L'Assedio della Cittadella",
    "file": "03_societa_e_politica/usi_costumi_ed_eventi/eventi/01_assedio_cittadella.md",
    "stato_occorrenza": "concluso"
  }
]
```
* `periodicita` *(string, opzionale)* per i festival: `"fissa"`, `"variabile"` o `"mista"`.
* `scaturiggine` *(string, opzionale)*: condizioni di innesto dell'evento ricorrente.
* `stato_occorrenza` *(string, opzionale)* per gli eventi: `"pianificato"`, `"in_svolgimento"` o `"concluso"`.

### E. Tomo 10 (Timeline)
```json
{
  "id": "timeline",
  "codice": "10",
  "titolo": "Timeline e Cronologia del Mondo",
  "cartella": "10_timeline",
  "indice": "10_timeline/README.md",
  "descrizione": "Cronologia storica, registro occorrenze, calendario e timeline grafica Markwhen.",
  "moduli": [],
  "cartella_cronologia_storica": "10_timeline/cronologia_storica",
  "moduli_cronologia_storica": [
    {
      "id": "nome_epoca",
      "codice": "10.1.1",
      "titolo": "Titolo dell'epoca o periodo storico",
      "file": "10_timeline/cronologia_storica/01_nome_epoca.md"
    }
  ],
  "cartella_registro_occorrenze": "10_timeline/registro_occorrenze",
  "moduli_registro_occorrenze": [
    {
      "id": "nome_periodo",
      "codice": "10.2.1",
      "titolo": "Titolo del periodo di registro",
      "file": "10_timeline/registro_occorrenze/01_nome_periodo.md"
    }
  ],
  "cartella_calendario": "10_timeline/calendario",
  "moduli_calendario": [
    {
      "id": "calendario",
      "codice": "10.3.1",
      "titolo": "Il Calendario del Mondo",
      "file": "10_timeline/calendario/01_calendario.md"
    }
  ],
  "cartella_markwhen": "10_timeline/markwhen",
  "file_markwhen": [
    "10_timeline/markwhen/timeline_generale.mw",
    "10_timeline/markwhen/epoche/<nome_epoca>.mw",
    "10_timeline/markwhen/campagne/<nome_campagna>.mw"
  ],
  "cartella_esportazioni": "10_timeline/esportazioni"
}
```
* I file `.mw` e le esportazioni **non** vengono trasposti nella Bibbia: compaiono solo in `file_markwhen` e nelle proprietà di cartella.
* L'array `moduli` del tomo resta vuoto: i file `.md` del tomo 10 vivono negli array dedicati (`moduli_cronologia_storica`, `moduli_registro_occorrenze`, `moduli_calendario`), come i `moduli_regioni` del tomo 02 e le sottoserie del tomo 03.

---

## 5. Regole di Parsing ed Estrazione Automatica

Quando si esegue `genera-struttura-json` o `aggiorna-struttura-json`:
1. **Titolo Modulo**: Estratto dal primo `# Titolo` del file markdown.
2. **Concetti Chiave**:
   - Individuati da elenchi puntati (`* Concetto: spiegazione`), sottotitoli `##` e `###`, o termini in grassetto `**Termine**`.
   - Normalizzati come frasi concise e autoesplicative.
3. **Tabelle**: Rilevate tramite righe con separatori di colonna `| :--- | :--- |` precedute da un titolo `## Tabella...` o didascalia.
4. **Note DM**: Rilevate tramite marcatori `**NOTA PER IL DUNGEON MASTER:**` o `> ⚠️ **Nota DM:**`.
5. **Codice Numerico**: Se il file si chiama `03_flusso_della_magia.md` dentro `01_cosmologia`, il codice è `"1.3"`.
6. **Codici Sottoserie**: Le schede di `usi_costumi_ed_eventi/` usano codici di terzo livello per sottocartella (`3.5.x` usanze, `3.6.x` festival/occorrenze, `3.7.x` eventi; numerazione progressiva per sottocartella). I file della `10_timeline/` usano `10.1.x` (cronologia storica), `10.2.x` (registro occorrenze), `10.3.x` (calendario).
7. **Campi Tipologici**: Per i festival/occorrenze estrarre `periodicita` e `scaturiggine` dalle rispettive sezioni del template; per gli eventi una tantum estrarre `stato_occorrenza`.
