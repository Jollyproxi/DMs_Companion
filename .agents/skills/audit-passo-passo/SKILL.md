---
name: audit-passo-passo
description: "Use when: condurre una revisione passo-passo della lore o delle schede di D&D con il Dungeon Master, validare singole affermazioni (micro-atomica) o sezioni logiche a richiesta, e apporre il badge visibile di verifica e modifica."
argument-hint: "Specifica il file o l'argomento da revisionare e la granularità (atomica o sezione)"
user-invocable: true
disable-model-invocation: false
---

# Skill: Audit della Lore Passo-Passo

Questa skill guida una revisione interattiva, sistematica e priva di allucinazioni di file, schede, dossier o tomi dell'ambientazione di D&D, interrogando il Dungeon Master (DM) concetto per concetto.

> **📌 Regola Nomi Propri Collegati**: ogni nome proprio di entità dell'ambientazione (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico dell'entità (es. `[Nome](percorso/relativo/file.md)`), mai semplice testo nudo. Eccezioni: intestazioni, nomi di file, frontmatter, blocchi di codice, nodi Mermaid e sorgenti `.mw`. Entità priva di scheda: non inventarla — usa `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna. Verifica e conversione: skill `collega-nomi-propri`.

---

## 1. Regola Fondamentale di Fact-Checking

- **Fonte di Verità Assoluta**: Il Dungeon Master è l'unica autorità canonica.
- **Divieto di Invenzione**: Non alterare, integrare o dedurre dettagli di lore non confermati esplicitamente dal Master durante l'audit.
- **Segnaposto per Dubbi**: Se il Master è incerto su un elemento da revisionare, mantieni o inserisci `[DA_DEFINIRE_MASTER: descrizione]` senza inventare risposte.

---

## 2. Granularità della Revisione

Prima di iniziare (o in base all'istruzione del Master), stabilisci la granularità del passo-passo:

1. **Livello 1: Micro-Atomico (Singola Affermazione / Punto Elenco)**
   - Utilizzato per statistiche di personaggi, ganci critici, date, segreti del DM, elenchi di oggetti.
   - Ogni singola riga o concetto chiave viene presentato isolato.
2. **Livello 2: Sezione Logica (Blocco Tematico)**
   - Utilizzato per paragrafi descrittivi, costumi sociali, capitoli geografici o sezioni narrative (es. `## Aspetto & Fabbricazione`, `## 1. Sinossi degli Eventi`).
   - L'intera sezione coerente viene presentata per la validazione.

---

## 3. Sintassi del Flag di Verifica (Badge Visibile)

Al termine della validazione di ciascun blocco o elemento, viene apposto il badge Markdown ufficiale:

```markdown
> 🛡️ *Verificato: AAAA-MM-GG | Modificato: AAAA-MM-GG*
```

* **Regole Temporali**:
  - Quando il blocco viene validato e non subisce modifiche: entrambe le date coincidono con la data corrente.
  - Se il blocco subisce una modifica concordata: entrambe le date vengono impostate alla data corrente.
  - Se in futuro un agente o il Master modifica il testo al di fuori dell'audit: la data `Modificato` viene avanzata, lasciando intatta la data `Verificato`. Se `Modificato > Verificato`, il blocco è segnalato come modificato post-audit.

---

## 4. Procedura Operativa Passo-Passo

1. **Caricamento del File**:
   - Usa lo strumento di lettura per esaminare il file indicato dal Master.
   - Seziona il documento secondo la granularità concordata (atomica o per sezioni logiche).

2. **Interrogatorio Atomico**:
   - Mostra al Master un concetto/sezione per volta in chat.
   - Se l'ambiente dispone di uno strumento interattivo di domande strutturate (es. `vscode_askQuestions`, `AskUserQuestion`), utilizzalo per presentare la domanda con opzioni rapide:
     - `Conferma senza modifiche` (consigliata)
     - `Modifiche effettuate sul file di origine da parte del Master` (il Master ha già aggiornato il file, quindi il badge va aggiornato)
     - `Modifica / Rettifica` (apre campo libero per digitare la correzione)
     - `Rimanda a dopo [DA_DEFINIRE_MASTER]`
   - Altrimenti, poni la domanda direttamente in chat:
     > **Passo [N/Totale] — [Titolo Sezione o Concetto]**
     > ```markdown
     > [Testo esatto estratto dal file]
     > ```
     > **Domanda**: *«Confermi che questo passaggio è corretto ed esattamente conforme al canone, oppure desideri rettificare o aggiungere dettagli?»*

3. **Applicazione della Risposta**:
   - **Se approvato senza modifiche**: Aggiungi o aggiorna il badge:
     `> 🛡️ *Verificato: [DATA_ODIERNA] | Modificato: [DATA_ODIERNA]*`
   - **Se il Master detta modifiche**: Riscrivi il testo incorporando unicamente le parole o direttive del Master, quindi imposta il badge con la data odierna.
   - **Se il Master ha effettuato modifiche**: Aggiungi o aggiorna il badge con la data odierna.
   - **Se rimandato**: Aggiungi `[DA_DEFINIRE_MASTER: elemento da chiarire]` e imposta `Verificato: NON_CONVALIDATO`.

4. **Persistenza & Chiusura**:
   - Applica le modifiche direttamente sul file con gli strumenti di editing.
   - Prosegui con il passo successivo finché il file non è completato.
   - Al termine del file, invoca la skill `stato-revisione` per aggiornare la dashboard riassuntiva `STATO_REVISIONE.md`.
