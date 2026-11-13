---
name: collega-nomi-propri
description: "Use when: verificare o convertire i nomi propri di persone, luoghi, città, oggetti, fazioni, usanze ed eventi in collegamenti Markdown ai rispettivi file .md canonici; scansionare file, cartelle o l'intero archivio per individuare nomi non collegati e ripristinare la conformità della regola dei nomi-propri-collegati."
argument-hint: "Percorso del file o della cartella da scansionare (oppure 'intero archivio')"
user-invocable: true
disable-model-invocation: false
---

# Skill: Collegamento Obbligatorio dei Nomi Propri (Collega-Nomi-Propri)

Questa skill fa rispettare la regola universale secondo cui ogni nome proprio di entità dell'ambientazione deve essere un collegamento Markdown al file `.md` canonico dell'entità: scansiona i documenti, individua i nomi comparsi come semplice testo, li classifica e ne propone o applica la conversione in link, segnalando al Master le entità prive di scheda.

---

## 1. Regola di Riferimento

- Ogni **nome proprio** di entità dell'ambientazione — persone (PG, PNG), casate, fazioni, gilde, città, luoghi, regioni, piani, oggetti magici, usanze, festival, eventi, epoche, leggi, istituzioni — che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico di quell'entità, con il nome proprio come testo del link: `[Nome](percorso/relativo/file.md)`.
- Il percorso è **relativo al file in cui si scrive** e deve puntare a un file realmente esistente su disco.
- Il testo del link è il nome proprio dell'entità nella sua forma canonica (quella del titolo H1 o del nome del file della scheda).
- **Eccezioni** (nomi ammessi senza link):
  1. Intestazioni (heading) e nomi di file.
  2. Frontmatter YAML, blocchi di codice, comandi e percorsi.
  3. Etichette dei diagrammi Mermaid e dei sorgenti Markwhen `.mw` (dove i link Markdown non sono renderizzabili).
  4. Designazioni generiche non riferite a entità censite.
- **Entità Priva di Scheda**: non inventare mai la scheda. Lascia il segnaposto `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna, oppure — in modalità interattiva — chiedi al Master se censire l'entità con la skill pertinente (`dossier-personaggio`, `oggetto-magico`, `usanza-festa-evento`, ecc.).

---

## 2. Costruzione dell'Indice delle Entità

Prima di scansionare, costruisci la mappa `nome → percorso del file canonico`:

1. **Fonte privilegiata**: se `struttura_ambientazione.json` è presente nella radice del workspace, usalo come indice (nomi dei moduli e percorsi associati).
2. **Ricognizione diretta**: altrimenti (o per integrazione) scansiona i dieci tomi — `05_personaggi/` (PG e PNG), `06_luoghi/` (o `06_location/`), `07_fazioni/` (o `07_factions/`), `08_oggetti_magici_peculiari/` (o variante legacy), `03_societa_e_politica/usi_costumi_ed_eventi/`, `02_geografia/` (regioni), `01_cosmologia/` (piani), `04_diritto_e_successione/` (leggi, trattati), `10_timeline/cronologia_storica/` (epoche, eventi storici) — raccogliendo titoli H1 e nomi di file.
3. **Nomi canonici**: per ogni scheda il nome proprio è il titolo del documento (H1) o il nome del file senza estensione; registra anche le eventuali varianti o alias esplicitamente documentate nella scheda.
4. **Omonimie**: se due entità condividono lo stesso nome, marca l'ambiguità e chiedi al Master a quale scheda collegare.

---

## 3. Procedura Operativa

1. **Determina lo Scope**: singolo file, cartella o intero archivio (escludendo directory tecniche come `.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Scansiona il Testo**: analizza i file `.md` riga per riga escludendo le eccezioni della §1 (frontmatter, blocchi di codice, etichette Mermaid, sorgenti `.mw`, intestazioni).
3. **Classifica Ogni Occorrenza**:
   - ✅ **Già Collegato**: il nome è già un link valido (verifica che il target esista su disco).
   - 🔗 **Da Collegare**: nome nudo con scheda esistente → conversione in link.
   - ⚠️ **Senza Scheda**: nome nudo di entità non censita → segnaposto `[DA_DEFINIRE_MASTER: ...]`.
   - ❓ **Ambiguo**: omonimia o corrispondenza incerta → interpellare il Master.
4. **Riporta il Risultato** al Master in tabella (`file:riga | nome | stato | azione proposta`).
5. **Applica su Conferma**: converti i nomi in link relativi corretti (ricalcola il percorso in base alla posizione del file); per i casi ⚠️ lascia il segnaposto e proponi il censimento con la skill pertinente; per i casi ❓ attendi la decisione del Master.
6. **Riepilogo Finale**: elenca i file modificati, i nomi convertiti e le lacune ancora aperte.

---

## 4. Integrazione con le Altre Skill

- **`valida-struttura`**: questa skill costituisce il **pilastro E** della diagnostica strutturale (copertura dei nomi propri collegati); eseguila insieme ai controlli A-D per un audit completo.
- **Skill di audit (`audit-passo-passo`, `audit-file-intero`)**: durante l'audit verifica anche che i nomi propri siano collegati e ripristina la conformità contestualmente alle correzioni approvate dal Master.
- **Skill di creazione schede (`dossier-personaggio`, `oggetto-magico`, `usanza-festa-evento`)**: ogni nuova scheda rende il relativo nome collegabile; alla creazione segnala in quali file esistenti il nuovo nome andrà collegato e proponi l'aggiornamento dei riferimenti.
- **`sincronizza-bibbia-struttura`**: nella Bibbia dell'Ambientazione i nomi propri mantengono la stessa convenzione, restando collegamenti ai moduli di provenienza.
- **`stato-revisione`**: le lacune aperte (nomi senza scheda) possono essere tracciate nella dashboard `STATO_REVISIONE.md` come voci da censire.
