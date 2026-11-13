---
name: init-mondo
description: "Use when: inizializzare una nuova repository di ambientazione o campagna D&D, guidare il Master nella definizione delle coordinate del mondo e generare l'architettura modulare a dieci tomi."
argument-hint: "Inizia l'intervista per configurare e generare l'alberatura del mondo"
user-invocable: true
disable-model-invocation: false
---

# Skill: Inizializzazione di un Mondo (Init-Mondo)

Questa skill guida il Dungeon Master nella configurazione interattiva e nella generazione dell'impalcatura a cartelle di un'ambientazione fantasy secondo l'architettura standard a dieci tomi descritta in [architettura-mondo](./references/architettura-mondo.md).

> **📌 Regola Nomi Propri Collegati**: ogni nome proprio di entità dell'ambientazione (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico dell'entità (es. `[Nome](percorso/relativo/file.md)`), mai semplice testo nudo. Eccezioni: intestazioni, nomi di file, frontmatter, blocchi di codice, nodi Mermaid e sorgenti `.mw`. Entità priva di scheda: non inventarla — usa `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna. Verifica e conversione: skill `collega-nomi-propri`.

---

## 1. Procedura Guidata (Intervista Iniziale)

Prima di creare file o cartelle, poni al Master le seguenti domande (usando lo strumento di domande strutturate dell'ambiente, come `vscode_askQuestions` o `AskUserQuestion`, se disponibile; altrimenti direttamente in chat):

1. **`nome_premessa`**: *Qual è il nome dell'ambientazione e la sua tematica fondamentale?*
   - Opzioni suggerite o inserimento libero (es. *High Fantasy Classico*, *Dark Fantasy Gotico*, *Intrigo Politico & Arcano*, *Altro — specificare*).
2. **`peculiarita_piani`**: *Quali peculiarità cosmologiche o piani speciali caratterizzano il mondo?*
   - Opzioni a selezione multipla: *Sottosuolo / Abissi sotterranei*, *Piani liminali / Nebbie*, *Reami fatati o astrali*, *Sfere celesti / Piani elementali*, *Altro (specificare)*.
3. **`fazioni_chiave`**: *Quali sono le 2-3 fazioni, casate o regni dominanti all'avvio?* (Campo libero).
4. **`campagna_iniziale`**: *Vuoi inizializzare subito una prima campagna con relativo gruppo di PG?*
   - Opzioni: *Sì (specifica nome campagna)*, *No (solo ambientazione per ora)*.
5. **`usi_costumi_eventi`**: *Esistono già usanze della vita quotidiana, festival ricorrenti o eventi storici da censire subito?*
   - Opzioni a selezione multipla: *Usanze (es. rituali di saluto/commiato)*, *Festival/eventi ricorrenti*, *Eventi una tantum (storici o in svolgimento)*, *Nessuno per ora (solo struttura)*.
   - Le voci raccolte vengono schedate con la skill `usanza-festa-evento` in `03_societa_e_politica/usi_costumi_ed_eventi/` e registrate nella `10_timeline/`.

---

## 2. Generazione dell'Alberatura

Una volta ricevute le risposte del Master, genera la struttura modulare utilizzando gli strumenti di scrittura o il terminale:

1. **File Radice**:
   - `README.md`: Indice generale del mondo e sommario di navigazione.
   - `struttura_ambientazione.json`: Schema gerarchico con metadati, tomi e cartelle.
   - `BIBBIA DELL'AMBIENTAZIONE.md`: Documento master sorgente con la premessa concordata.

2. **I Dieci Tomi Fondativi**:
   - `01_cosmologia/README.md`
   - `02_geografia/README.md` (con eventuale sottocartella `regioni/` o denominazione scelta per le macro-aree)
   - `03_societa_e_politica/README.md` (con sottocartella `usi_costumi_ed_eventi/` contenente `usanze/`, `festival_ed_occorrenze/`, `eventi/`, ciascuna con `README.md`)
   - `04_diritto_e_leggi/README.md` (con sottocartelle `01_ordinamento_e_fonti/`, `02_diritti_civili_e_status/`, `03_diritto_dinastico_e_successione/`, `04_contratti_e_patti/`, `05_trattati_e_diplomazia/`, `06_diritto_penale_e_reati/`, `07_tribunali_e_procedura/`, `08_diritto_arcano_e_religioso/`, `09_proprieta_commercio_e_fisco/`, `10_diritto_bellico_e_avventurieri/`, ciascuna con `README.md`)
   - `05_personaggi/README.md` (con sottocartelle `Giocanti/` e `Non-Giocanti/`, ciascuna con `README.md`)
   - `06_luoghi/README.md`
   - `07_fazioni/README.md`
   - `08_oggetti_magici_peculiari/README.md`
   - `09_cronache/README.md` (con sottocartelle `campagne/<nome_campagna>/sessioni/`, ciascuna con `README.md`)
   - `10_timeline/README.md` (con sottocartelle `cronologia_storica/`, `registro_occorrenze/`, `markwhen/` — con `README.md`, `timeline_generale.mw`, `epoche/`, `campagne/` —, `calendario/`, `esportazioni/README.md`)

3. **Inizializzazione dei File README**:
   Ogni cartella riceve un `README.md` con l'indice tematico iniziale e il badge di stato:
   `> 🛡️ *Verificato: [DATA_ODIERNA] | Modificato: [DATA_ODIERNA]*`

4. **Validazione Finale**:
   Al termine della creazione, invoca la skill `valida-struttura` per certificare che l'alberatura sia completa e priva di collegamenti rotti.
