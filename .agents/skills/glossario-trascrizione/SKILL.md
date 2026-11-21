---
name: glossario-trascrizione
description: "Use when: generare l'elenco testuale compatto dei nomi propri già noti (sola grafia esatta, senza spoiler né fatti) da caricare in NotebookLM o altro LLM insieme al prompt di trascrizione sessione per ridurre i `[?]`."
argument-hint: "Specifica campagna/sessione (es. 'campagna: Cronache del Nord'), cartella/area o 'archivio intero', eventuali nomi extra pronunciati e se salvare anche un file .txt"
user-invocable: true
disable-model-invocation: false
---

# Skill: Glossario Nomi Propri per Trascrizione (`glossario-trascrizione`)

Questa skill estrae dal repository un **elenco testuale compatto di sola grafia dei nomi propri canonici** (PG, PNG, luoghi, fazioni, oggetti, usanze, feste, eventi, divinità e termini chiave) da fornire come fonte ausiliaria a **NotebookLM** o a un altro LLM insieme a [prompt-trascrizione-sessione](../verbale-sessione/references/prompt-trascrizione-sessione.md), così da ridurre al minimo i marcatori `[?]` e gli errori fonetici nella trascrizione delle sessioni.

> **📌 Eccezione alla Regola Nomi Propri Collegati**: il blocco testuale esportato per NotebookLM/LLM (e l'eventuale file `.txt` salvato su disco) è destinato a uno strumento esterno e deve restare **puro testo privo di link Markdown** (`[Nome](...)`). Ogni spiegazione in chat fuori dal blocco e ogni file canonico `.md` restano invece soggetti alla regola della skill `collega-nomi-propri`.

---

## 1. Regola Aurea: Sola Grafia, Zero Fatti e Zero Allucinazioni

- **Esclusivamente Ortografia**: riporta **solo** la grafia canonica esatta di ogni nome proprio, le eventuali varianti ortografiche o alias/diminutivi esplicitamente documentati nelle schede (es. `Nome Canonico (alias: Soprannome)`) e, facoltativamente per i soli PG attivi, l'abbinamento `Giocatore → PG` se già documentato o fornito dal Master.
- **Divieto Assoluto di Fatti e Spoiler**: NON includere **mai** descrizioni, ruoli narrativi, fazioni di appartenenza, relazioni tra personaggi, stato vitale (vivo/morto/traditore), posizione attuale, statistiche, segreti del DM o estratti di lore. Tutto ciò che supera la semplice grafia aumenta il rischio che il modello di trascrizione deduca o importi nel resoconto fatti mai pronunciati durante la sessione.
- **Clausola Anti-Intrusione in Testata**: ogni glossario generato si apre con una riga fissa che istruisce l'LLM trascrittore a usare l'elenco **esclusivamente per l'ortografia** dei nomi uditi, senza importare nomi non pronunciati né dedurre fatti o legami.
- **Nomi Extra della Sessione Appena Giocata**: se il Master fornisce a voce o in chat nomi nuovi pronunciati in sessione ma non ancora censiti in archivio, includili in una sezione dedicata del glossario per agevolare la trascrizione, senza creare schede né alterare il canone.
- **Zero Invenzioni**: se in archivio mancano grafie o l'identità risulta incompleta, non indovinare né normalizzare arbitrariamente; segnalalo fuori dal blocco con `[DA_DEFINIRE_MASTER: ...]` oppure chiedilo al Master prima di esportare.

---

## 2. Ambiti di Selezione (Controllo del Rumore)

Per evitare di sovraccaricare il contesto di trascrizione con decine di nomi irrilevanti che generano falsi positivi fonetici, proponi o applica uno di questi tre ambiti:

- **Modalità A — Mirata alla Campagna / Sessione *(Default consigliato)***:
  - PG attivi della campagna (`05_personaggi/<Giocanti>/<Campagna_o_Party>/`, default `Giocanti/<Campagna>/`).
  - Nomi propri già citati nel `README.md` della campagna e negli ultimi **N verbali di sessione** (default: ultimi **5** verbali in `09_cronache/<campagne>/<nome_campagna>/<sessioni>/`).
  - Entità canoniche del teatro geografico o regione corrente, se specificati dal Master o ricavabili dall'intestazione dell'ultimo verbale.
  - Eventuali nomi nuovi o estemporanei segnalati dal Master per la sessione appena registrata.
- **Modalità B — Area, Cartella o Fazione Specifica**:
  - PG attivi della campagna (se applicabile) + tutte le entità censite nelle cartelle, regioni, fazioni o tomi indicati dal Master (es. `06_luoghi/<regione>/`, `07_fazioni/<casata>/`, `04_diritto_e_leggi/`).
- **Modalità C — Archivio Completo**:
  - Tutti i nomi propri canonici presenti nei Dieci Tomi.
  - **Soglia Anti-Rumore**: se l'elenco supera indicativamente le **250–300 voci**, avvisa esplicitamente il Master che un glossario troppo ampio può aumentare i falsi abbinamenti fonetici in NotebookLM/LLM e proponi di restringere l'ambito alla Modalità A o B.

---

## 3. Fonti e Regole di Estrazione

1. **Indice Privilegiato**: se `struttura_ambientazione.json` esiste nella radice del workspace, leggilo per individuare rapidamente tomi, moduli e percorsi canonici senza leggere prosa superflua.
2. **Ricognizione Diretta / Integrazione nei Dieci Tomi**: scansiona (o integra da) le cartelle dell'ambientazione rispettando la struttura effettiva del repository — inclusi nomi custom o legacy (`06_location/`, `07_factions/`, `08_oggetti magici peculiari/`, `cornici/`, `spedizioni/`, `diari/`) e la convenzione dell'archivio PNG documentata nelle istruzioni del progetto e nell'indice di `05_personaggi/`:
   - `05_personaggi/` (dossier PG modulari e schede PNG)
   - `06_luoghi/` (città, nodi d'avventura, roccaforti, pericoli d'area) e `02_geografia/` (regioni/macro-aree)
   - `07_fazioni/` (casate, congreghe, gilde, ordini, istituzioni)
   - `<08_oggetti_magici_peculiari>/` (artefatti, reliquie, oggetti unici)
   - `03_societa_e_politica/` (`popoli/`, `usi_costumi_ed_eventi/`), `01_cosmologia/` (piani, divinità/pantheon), `04_diritto_e_leggi/` (leggi, trattati, corti) e `10_timeline/cronologia_storica/` (epoche, eventi storici)
   - `09_cronache/` (per la Modalità A: indice campagna e ultimi verbali)
3. **Esclusioni**:
   - Ignora cartelle tecniche (`.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`) e file di servizio/master (`README.md`, `AGENTS.md`, `CLAUDE.md`, `BIBBIA DELL'AMBIENTAZIONE.md`, `STATO_REVISIONE.md`, `GUIDA-UTILIZZO.md`, `struttura_ambientazione.json`, file `.mw` o esportazioni).
   - Scarta intestazioni strutturali generiche (es. *Quadro generale*, *Indice*, *Sinossi*, *Sessione 01*, *Stato dell'occorrenza*) e segnaposto `[DA_DEFINIRE_MASTER: ...]`.
4. **Normalizzazione e Deduplicazione**:
   - Per ogni scheda estrai il nome proprio canonico dal titolo H1 (rimuovendo prefissi numerici come `01_`, etichette come `Scheda PNG:` / `Dossier PG:` / `Oggetto Magico:`, badge `🛡️` o sottotitoli descrittivi dopo `—` o `|`), oppure dal nome del file ripulito se manca un H1 nominale.
   - Nei dossier PG a 5 moduli, estrai **una sola volta** l'identità dalla cartella o dal modulo anagrafico (`01_anagrafica...`), evitando di ripetere i nomi dei file di modulo.
   - Raccogli gli alias o diminutivi solo se esplicitamente annotati nella scheda canonica (`Alias`, `Soprannomi`, `Varianti`); non riportare descrizioni tra parentesi.
   - Deduplica le grafie identiche e ordina alfabeticamente le voci all'interno di ogni categoria.

---

## 4. Procedura Operativa e Interazione Strutturata

1. **Raccolta Parametri (se non già specificati dal Master)**:
   Chiedi tramite lo strumento interattivo di domande strutturate dell'ambiente (`vscode_askQuestions`, `AskUserQuestion`, `ask_question`, `request_user_input` se disponibili, altrimenti direttamente in chat):
   - **`ambito`**: *Quale ambito vuoi coprire nel glossario?*
     - Opzioni: *Campagna / Sessione corrente — consigliata* (elencando le campagne rilevate in `09_cronache/`), *Area, cartella o fazione specifica*, *Archivio completo (tutti i Dieci Tomi)*.
   - **`nomi_extra`**: *Ci sono nuovi nomi pronunciati nell'ultima sessione (PG ospiti, PNG, luoghi o termini non ancora in archivio) da includere solo per la trascrizione?* (Campo libero opzionale o *Nessuno*).
   - **`destinazione`**: *Dove vuoi ricevere il glossario?*
     - Opzioni: *Solo in chat (pronto per copia-incolla su NotebookLM) — consigliata*, *In chat + salva come file `.txt` nel repository*.
2. **Estrazione e Controllo Anti-Spoiler**:
   - Applica le regole della §3 sull'ambito scelto.
   - Verifica che nessuna riga contenga descrizioni, parentele, allineamenti, status o anticipazioni di trama.
   - Ometti le categorie vuote. Se il totale supera ~250–300 voci, avvisa il Master e offri una versione ristretta alla sola campagna o scena corrente.
3. **Consegna del Glossario**:
   - Mostra **sempre** il risultato completo in chat dentro un blocco di codice `text`, pronto per essere incollato in NotebookLM (*Aggiungi fonte → Testo copiato*) o in un altro LLM.
   - Subito fuori dal blocco, riporta un breve riepilogo con: ambito applicato, conteggio voci per categoria e totale, fonti consultate ed eventuali grafie dubbie rilevate nel repository.
   - Se è stato richiesto anche il salvataggio su file, scrivi un file **`.txt` UTF-8** nella cartella della campagna — `09_cronache/<campagne>/<nome_campagna>/glossario_trascrizione.txt` *(default: `09_cronache/campagne/<nome_campagna>/glossario_trascrizione.txt`; oppure nella radice o cartella indicata se non esiste ancora una campagna)* — evitando l'estensione `.md` così da non interferire con i controlli di `valida-struttura`, `collega-nomi-propri`, `stato-revisione` e `sincronizza-bibbia-struttura`.

---

## 5. Modello Canonico di Output

Produce esclusivamente un blocco compatto in questo formato (omettendo eventuali sezioni prive di voci):

````text
# GLOSSARIO NOMI PROPRI (SOLA GRAFIA — NON IMPORTARE FATTI NON DETTI IN SESSIONE)
Campagna / Ambito: <Nome campagna o ambito>

## Personaggi Giocanti (PG)
- <Nome PG> (<Giocatore → PG> solo se documentato/fornito, opzionale)
- <Nome PG> (alias: <Soprannome documentato>)

## Personaggi Non Giocanti (PNG) e Creature Note
- <Nome PNG>
- <Nome PNG> (alias: <Diminutivo / Variante grafia documentata>)

## Luoghi, Città e Regioni
- <Luogo / Regione>

## Fazioni, Casate e Istituzioni
- <Fazione / Casata>

## Oggetti, Artefatti e Reliquie
- <Oggetto>

## Usanze, Feste, Eventi, Divinità e Termini Chiave
- <Usanza / Festa / Evento / Divinità / Legge>

## Nomi Extra della Sessione (non ancora censiti)
- <Nome pronunciato fornito dal Master>
````

---

## 6. Integrazione con le Altre Skill

- **`verbale-sessione` e `prompt-trascrizione-sessione`**: questa skill genera esattamente la fonte opzionale descritta al punto 2 di [prompt-trascrizione-sessione](../verbale-sessione/references/prompt-trascrizione-sessione.md); riduce i `Nome[?]` prima di importare il resoconto tramite il Canale C di `verbale-sessione`.
- **`collega-nomi-propri`**: condivide la logica di ricognizione delle entità canoniche nei Dieci Tomi; il glossario generato è esente da link Markdown perché è testo di riferimento esterno per NotebookLM/LLM.
- **`sincronizza-bibbia-struttura`**: se presente, `struttura_ambientazione.json` funge da indice veloce per raccogliere i titoli canonici senza dover aprire documenti lunghi come `BIBBIA DELL'AMBIENTAZIONE.md`.
- **`valida-struttura`**: il salvataggio opzionale usa l'estensione `.txt` dentro la cartella di campagna per restare innocuo rispetto a controlli di link rotti, badge `🛡️` e file `.md` orfani.
