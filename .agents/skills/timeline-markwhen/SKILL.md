---
name: timeline-markwhen
description: "Use when: creare, generare, aggiornare, validare o esportare i file della timeline grafica Markwhen (.mw) in 10_timeline/markwhen/ (timeline_generale.mw, epoche/<epoca>.mw, campagne/<campagna>.mw), sincronizzare date, stati e tag con cronologia_storica/, registro_occorrenze/, verbali di sessione e struttura_ambientazione.json, o produrre render grafici in 10_timeline/esportazioni/."
argument-hint: "Specifica l'operazione: crea-mw, aggiorna-mw, valida-mw o esporta-mw (es. 'crea-mw epoca: Prima Era', 'aggiorna-mw campagna: Cronache del Nord')"
user-invocable: true
disable-model-invocation: false
---

# Skill: Gestione Timeline Grafica Markwhen (`timeline-markwhen`)

Questa skill governa il ciclo di vita completo dei sorgenti **Markwhen (`.mw`)** in `10_timeline/markwhen/` e delle relative esportazioni in `10_timeline/esportazioni/`. Mantiene la rappresentazione grafica temporale del mondo sincronizzata con la cronologia storica (`10_timeline/cronologia_storica/`), il registro delle occorrenze (`10_timeline/registro_occorrenze/`), il calendario (`10_timeline/calendario/`), le schede di usi, costumi ed eventi (`03_societa_e_politica/usi_costumi_ed_eventi/`) e i verbali di campagna (`09_cronache/campagne/`).

Consulta i riferimenti tecnici allegati:
- [sintassi-e-template-mw](./references/sintassi-e-template-mw.md): sintassi Markwhen canonica, header YAML, tassonomia tag e template per `timeline_generale.mw`, `epoche/<epoca>.mw` e `campagne/<campagna>.mw`.
- [sincronizzazione-ed-esportazione](./references/sincronizzazione-ed-esportazione.md): regole di mappatura bidirezionale col Tomo 10, indicizzazione in `struttura_ambientazione.json`, checklist di validazione e pipeline di esportazione in `10_timeline/esportazioni/`.

> **📌 Regola Nomi Propri Collegati**: ogni nome proprio di entità dell'ambientazione (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico dell'entità (es. `[Nome](percorso/relativo/file.md)`), mai semplice testo nudo. Eccezioni: intestazioni, nomi di file, frontmatter, blocchi di codice, nodi Mermaid e sorgenti `.mw`. Entità priva di scheda: non inventarla — usa `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna. Verifica e conversione: skill `collega-nomi-propri`.

---

## 1. Regola Aurea: Fedeltà Notarile (Zero Allucinazioni)

- **Divieto di invenzione**: Non inventare mai autonomamente date, anni del mondo, nomi di epoche, durate, partecipanti o esiti non espressamente forniti dal Master o già attestati nei file canonici.
- **Gestione delle date o dei dettagli mancanti**:
  - **Richiesta obbligatoria prima della scrittura**: in Markwhen ogni evento visibile richiede una data prima dei `:`. Se un evento non ha ancora una data/anno del mondo nei file canonici, **fermati e chiedi sempre al Master** (usando lo strumento di domande strutturate dell'ambiente come `vscode_askQuestions` o `AskUserQuestion` se disponibile, altrimenti direttamente in chat) una data canonica o un **anno provvisorio** prima di scrivere la voce nel file `.mw`.
  - Se il Master fornisce un anno provvisorio, inserisci l'evento con quell'anno, aggiungi il tag `#data_provvisoria` e annota nei sottopunti `- [DA_DEFINIRE_MASTER: data definitiva da confermare]`, così l'evento compare subito nella timeline grafica ma resta tracciato come da consolidare.

---

## 2. Architettura di `10_timeline/markwhen/`

```text
10_timeline/
├── markwhen/
│   ├── README.md                     # Indice dei sorgenti .mw e sintesi convenzioni
│   ├── timeline_generale.mw          # Indice/legenda generale (NON aggregato dei sorgenti)
│   ├── epoche/
│   │   └── <slug_epoca>.mw           # Un sorgente .mw per epoca/periodo storico
│   └── campagne/
│       └── <slug_campagna>.mw        # Tutto il rilevante per la campagna (passato, presente, pianificato)
└── esportazioni/
    ├── README.md                     # Registro dei render grafici derivati
    └── <nome_file>.(html|svg|png|pdf)
```

- **Ruolo di `timeline_generale.mw`**: contiene l'header di configurazione e legenda dei tag/colori, il riepilogo del calendario del mondo e l'indice commentato dei sorgenti in `epoche/` e `campagne/`. Non duplica i singoli eventi dei file specifici.
- **Esclusione dalla Bibbia**: i file `.mw` e il contenuto di `esportazioni/` sono **esclusi dalla Bibbia dell'Ambientazione** e vengono censiti esclusivamente in `struttura_ambientazione.json` (campo `file_markwhen` del Tomo `10`).

---

## 3. Matrice delle Sotto-Operazioni

| Comando / Argomento | Target Principale | Modalità | Scopo |
| :--- | :--- | :--- | :--- |
| **`crea-mw`** *(o `genera-mw`)* | `timeline_generale.mw`, `epoche/*.mw`, `campagne/*.mw` | Inizializzazione / Ex-novo | Crea la struttura `markwhen/`, genera `timeline_generale.mw` o crea un nuovo file `.mw` di epoca o di campagna estraendo i dati dai moduli canonici. |
| **`aggiorna-mw`** *(o `update-mw`)* | File `.mw` esistenti + `markwhen/README.md` | Incrementale / Delta | Inserisce nuovi eventi/occorrenze, aggiorna i tag di stato (`#pianificato` → `#in_svolgimento` → `#storico`), aggiunge sessioni e aggiorna la legenda. |
| **`valida-mw`** | `10_timeline/markwhen/**/*.mw` | Diagnostica / Audit tecnico | Verifica la sintassi Markwhen, la presenza dei tag obbligatori, i link relativi alle schede/verbali e l'allineamento con Tomo 10 e `struttura_ambientazione.json`. |
| **`esporta-mw`** | `10_timeline/esportazioni/` | Render / Derivazione | Esporta i sorgenti `.mw` in visualizzazioni derivate (HTML/SVG/PNG/PDF tramite CLI `mw` opzionale o esportazione manuale da estensione/web app) e aggiorna `esportazioni/README.md`. |

---

## 4. Procedura 1: `crea-mw` (Inizializzazione e Generazione Sorgenti `.mw`)

Usa questa procedura per inizializzare `10_timeline/markwhen/` o creare un nuovo file `.mw` per un'epoca storica o una campagna.

### Passi Operativi:
1. **Rilevamento Contesto e Fonti**:
   - Leggi `10_timeline/README.md`, `10_timeline/calendario/` e `10_timeline/markwhen/README.md`.
   - In base al target richiesto (`generale`, `epoca`, `campagna`, o `tutto`), ispeziona le fonti pertinenti:
     - Per un'**epoca**: `10_timeline/cronologia_storica/`, `10_timeline/registro_occorrenze/` e le schede in `03_societa_e_politica/usi_costumi_ed_eventi/`.
     - Per una **campagna**: `09_cronache/<campagne>/<nome_campagna>/README.md`, i verbali in `<sessioni>/`, i dossier PG (`05_personaggi/<Giocanti>/<Campagna_o_Party>/`) e gli eventi storici/in svolgimento collegati.
2. **Intervista Preliminare**:
   - Se mancano coordinate essenziali (es. nome/slug dell'epoca, anno di inizio/fine, anno corrente della campagna), chiedile al Master prima di generare il file (usando lo strumento di domande strutturate dell'ambiente se disponibile, altrimenti in chat).
3. **Generazione dei File secondo i Template**:
   - Applica i template di [sintassi-e-template-mw](./references/sintassi-e-template-mw.md):
     - Crea le sottocartelle `10_timeline/markwhen/epoche/` e `10_timeline/markwhen/campagne/` se assenti.
     - Genera `timeline_generale.mw` con header, definizione tag/colori, note di calendario e mappa dei file `.mw`.
     - Genera `epoche/<slug_epoca>.mw` o `campagne/<slug_campagna>.mw` ordinando gli eventi cronologicamente per anno del mondo (`AAAA`, `AAAA-MM`, `AAAA-MM-GG` o intervalli `inizio/fine`) e raggruppandoli in `section` tematiche o di fase.
     - Includi sotto ogni evento il link Markdown relativo alla scheda canonica o al verbale di sessione.
4. **Propagazione Indici e JSON**:
   - Aggiorna `10_timeline/markwhen/README.md` elencando i nuovi file `.mw` creati e aggiornando la data `Modificato` nel badge `🛡️`.
   - Proponi l'aggiornamento di `file_markwhen` in `struttura_ambientazione.json` (`aggiorna-struttura-json`).

---

## 5. Procedura 2: `aggiorna-mw` (Aggiornamento Incrementale)

Usa questa procedura dopo una sessione verbalizzata (`verbale-sessione`), dopo la creazione/modifica di una scheda in `usi_costumi_ed_eventi/` (`usanza-festa-evento`), o su richiesta diretta del Master.

### Passi Operativi:
1. **Identificazione del Delta Temporale**:
   - Determina cosa è cambiato:
     - **Nuovo evento / nuova occorrenza**: data/anno del mondo, titolo, tipologia (`#usanza`, `#festival`, `#evento`, `#occorrenza`), stato (`#pianificato`, `#in_svolgimento`, `#storico`) e tag tematici (`#fazione_<slug>`, `#luogo_<slug>`, `#PG_<slug>`, `#PNG_<slug>`, `#campagna_<slug>`).
     - **Transizione di stato**: passaggio di una voce esistente da `#pianificato` a `#in_svolgimento` o `#storico` (con sintesi dell'esito).
     - **Nuova sessione di campagna**: eventi datati emersi nel verbale `09_cronache/campagne/<nome>/sessioni/XX_titolo.md`.
2. **Aggiornamento dei Sorgenti `.mw`**:
   - Apri il file `.mw` dell'epoca pertinente in `10_timeline/markwhen/epoche/` e inserisci o aggiorna la riga dell'evento mantenendo l'ordine cronologico.
   - Se l'evento riguarda una campagna, aggiorna anche `10_timeline/markwhen/campagne/<slug_campagna>.mw` aggiungendo il link relativo al verbale o alla scheda.
   - Se sono stati introdotti nuovi tag (es. una nuova fazione o campagna) o nuove ricorrenze fisse di calendario, aggiorna l'header e la legenda in `10_timeline/markwhen/timeline_generale.mw`.
3. **Allineamento Incrociato col Tomo 10**:
   - Verifica che la medesima voce/occorrenza e i medesimi tag figurino in `10_timeline/cronologia_storica/` (se `#storico`) o in `10_timeline/registro_occorrenze/` (se `#occorrenza`, `#in_svolgimento` o `#pianificato`), proponendo l'allineamento se mancante.

---

## 6. Procedura 3: `valida-mw` (Diagnostica e Verifica Coerenza)

Usa questa procedura per controllare la correttezza formale e strutturale dei sorgenti `.mw` secondo la checklist in [sincronizzazione-ed-esportazione](./references/sincronizzazione-ed-esportazione.md).

### Controlli Eseguiti:
1. **Sintassi Markwhen**: validità dell'header YAML (`---`, assenza di `#Categoria` senza `:` o `dateFormat`), chiusura corretta dei blocchi `section` / `endSection` (o `group` / `endGroup`) e formato valido delle date (`AAAA`, `AAAA-MM`, `AAAA-MM-GG`, `data1/data2`) prima dei due punti `:`.
2. **Tassonomia Tag**: ogni evento deve possedere almeno un tag di **tipologia** (`#usanza`, `#festival`, `#evento`, `#occorrenza`) e un tag di **stato** (`#storico`, `#in_svolgimento`, `#pianificato`).
3. **Integrità dei Link Relativi**: verifica che tutti i link Markdown `[Testo](../../...)` nelle descrizioni degli eventi puntino a file realmente esistenti nel workspace.
4. **Coerenza Bidirezionale Tomo 10 & JSON**:
   - Confronta gli eventi nei file `.mw` con `cronologia_storica/` e `registro_occorrenze/` segnalando discrepanze di date o tag di stato.
   - Verifica che tutti i file `.mw` su disco siano elencati in `file_markwhen` dentro `struttura_ambientazione.json`.
5. **Report Diagnostico**: restituisce una tabella di esito (`OK` / `WARN` / `ERRORE`) e chiede al Master (tramite strumento strutturato se disponibile o in chat) se applicare le correzioni automatiche.

---

## 7. Procedura 4: `esporta-mw` (Esportazioni Grafiche in `10_timeline/esportazioni/`)

Usa questa procedura quando il Master richiede di generare o aggiornare le viste renderizzate della timeline.

### Passi Operativi:
1. **Verifica Strumenti Opzionali (`mw` CLI / Estensione / Web App)**:
   - Controlla se la CLI Markwhen (`@markwhen/mw`) è disponibile nell'ambiente oppure guida il Master tramite l'estensione Markwhen o `markwhen.com`, seguendo le istruzioni in [sincronizzazione-ed-esportazione](./references/sincronizzazione-ed-esportazione.md).
2. **Generazione ed Esportazione**:
   - Esporta i sorgenti `.mw` richiesti nella cartella `10_timeline/esportazioni/` con naming standard (`timeline_<slug>_<formato>.<estensione>`).
3. **Aggiornamento Indice Esportazioni**:
   - Aggiorna `10_timeline/esportazioni/README.md` con la tabella dei render generati (file, sorgente `.mw` di origine, data di generazione) e aggiorna la data `Modificato` del badge `🛡️`.

---

## 8. Interazione Strutturata

Se la skill viene invocata senza argomenti specifici o con parametri parziali, chiedi al Master (usando lo strumento di domande strutturate dell'ambiente come `vscode_askQuestions` / `AskUserQuestion` se disponibile, altrimenti in chat) quale operazione eseguire:
- `crea-mw` — Inizializza `timeline_generale.mw` o crea un nuovo file `.mw` per epoca o campagna
- `aggiorna-mw` — Aggiunge nuovi eventi/occorrenze o aggiorna stati e tag nei file `.mw` esistenti
- `valida-mw` — Controlla sintassi `.mw`, tag, link relativi e sincronizzazione col Tomo 10 e JSON
- `esporta-mw` — Esporta i sorgenti `.mw` in render derivati dentro `10_timeline/esportazioni/`
