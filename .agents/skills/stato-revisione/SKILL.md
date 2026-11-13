---
name: stato-revisione
description: "Use when: generare o aggiornare la dashboard dello stato di revisione della lore (STATO_REVISIONE.md), calcolare percentuali di verifica, tracciare file completati e individuare paragrafi modificati dopo l'ultimo audit."
argument-hint: "Genera o aggiorna la dashboard di revisione del workspace"
user-invocable: true
disable-model-invocation: false
---

# Skill: Dashboard e Stato di Revisione della Lore

Questa skill genera, aggiorna e mantiene il file di controllo e monitoraggio `STATO_REVISIONE.md` nella radice del workspace, offrendo al Dungeon Master una vista immediata della copertura del fact-checking e delle sezioni che necessitano di nuova verifica.

> **📌 Regola Nomi Propri Collegati**: ogni nome proprio di entità dell'ambientazione (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico dell'entità (es. `[Nome](percorso/relativo/file.md)`), mai semplice testo nudo. Eccezioni: intestazioni, nomi di file, frontmatter, blocchi di codice, nodi Mermaid e sorgenti `.mw`. Entità priva di scheda: non inventarla — usa `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna. Verifica e conversione: skill `collega-nomi-propri`.

---

## 1. Criteri di Classificazione dello Stato

La skill analizza i file markdown delle cartelle canoniche del mondo (`01_cosmologia`, `02_geografia`, `03_societa_e_politica` inclusa la sottoserie `usi_costumi_ed_eventi/`, `04_diritto_e_successione`, `05_personaggi`, `06_luoghi` o `06_location`, `07_fazioni` o `07_factions`, `08_oggetti_magici_peculiari` o `08_oggetti magici peculiari`, `09_cronache`, `10_timeline`) e individua i badge:

```markdown
> 🛡️ *Verificato: [DATA_V] | Modificato: [DATA_M]*
```

### Stati di Conformità:
* 🟢 **Verificato Completo**: Tutte le sezioni del documento hanno badge con `DATA_V >= DATA_M` e non contengono `[DA_DEFINIRE_MASTER]`.
* 🟡 **Verificato Parziale / Incompleto**: Alcune sezioni possiedono il badge, ma altre ne sono prive oppure contengono marcatori `[DA_DEFINIRE_MASTER]`.
* 🟠 **Modificato Post-Audit (Richiede Ricontrollo)**: Una o più sezioni presentano `DATA_M > DATA_V`, indicando che sono state modificate a seguito di una sessione o di un editing successivo all'ultimo audit formale.
* ⚪ **Non Verificato**: Nessun badge di verifica presente nel file.

---

## 2. Struttura del File `STATO_REVISIONE.md`

Il file `STATO_REVISIONE.md` deve essere salvato nella radice del workspace con questa struttura:

```markdown
# Registro e Stato di Revisione del Canone

Questo registro monitora l'avanzamento dell'audit formale della lore, tracciando le sezioni convalidate dal Dungeon Master e quelle modificate nel corso delle sessioni.

* **Ultimo Audit Generale:** [DATA]
* **Copertura Globale Canone:** [PERCENTUALE]%

---

## 1. Quadro Sinottico per Settore

| Sezione / Tomo | File Totali | Verificati 🟢 | Post-Audit 🟠 | Parziali 🟡 | Non Verificati ⚪ | Stato |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **01 Cosmologia** | X | A | B | C | D | [Icona] |
| **02 Geografia** | X | A | B | C | D | [Icona] |
| **03 Società e Politica** | X | A | B | C | D | [Icona] |
| **03· Usi, Costumi ed Eventi** | X | A | B | C | D | [Icona] |
| **04 Diritto e Successione** | X | A | B | C | D | [Icona] |
| **05 Personaggi (PG & PNG)** | X | A | B | C | D | [Icona] |
| **06 Luoghi** | X | A | B | C | D | [Icona] |
| **07 Fazioni** | X | A | B | C | D | [Icona] |
| **08 Oggetti Magici** | X | A | B | C | D | [Icona] |
| **09 Cronache di Campagna** | X | A | B | C | D | [Icona] |
| **10 Timeline & Occorrenze** | X | A | B | C | D | [Icona] |

---

## 2. Elementi Prioritari in Attesa di Controllo

### File con Modifiche Post-Audit (🟠)
* [percorso/file.md](percorso/file.md) — *Modificato il [DATA] (Verificato il [DATA])*

### File con Lacune Esplicite (🟡 `[DA_DEFINIRE_MASTER]`)
* [percorso/file.md](percorso/file.md) — *Sezione [Nome]: [descrizione del dubbio]*

---

## 3. Storico delle Sessioni di Audit
* **AAAA-MM-GG**: Audit [completo / parziale] eseguito su [cartella o file] tramite skill `[audit-passo-passo / audit-file-intero]`.
```

---

## 3. Procedura Operativa

1. **Scansione**: Cerca ricorsivamente tutti i file `.md` rilevanti nel workspace escludendo cartelle tecniche (es. `.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Parsing dei Flag**: Estrai da ciascun file la presenza dei badge `🛡️`, le date `Verificato` e `Modificato`, e la presenza di `[DA_DEFINIRE_MASTER]`.
3. **Calcolo Statistiche**: Calcola i conteggi e le percentuali per ciascuno dei dieci tomi canonici (con rilievo separato per la sottoserie `usi_costumi_ed_eventi/`).
4. **Scrittura/Aggiornamento**: Compila o aggiorna `STATO_REVISIONE.md` nella radice del workspace.
