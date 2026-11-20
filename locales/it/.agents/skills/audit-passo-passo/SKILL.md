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
   - Presenta un solo concetto o sezione per volta. Includi il testo esatto e la domanda nel modulo interattivo.
   - In Codex usa `request_user_input` quando disponibile e consentito, altrimenti `request_user_input_async` alle stesse condizioni. Negli altri ambienti usa lo strumento equivalente. Come subagente, inoltra domanda e opzioni al coordinatore se il modulo si apre soltanto nella conversazione principale.
   - Con `request_user_input` usa queste tre opzioni e indica nella domanda che il campo libero serve a dettare una rettifica:
     - `Conferma (Consigliato)`: il testo va bene e puoi procedere con il badge.
     - `File modificato`: il Master ha modificato il file di origine. Rileggi il punto prima di aggiornare il badge.
     - `Rimanda`: sospendi la convalida di questo punto.
   - Eccezione per `request_user_input_async` e per i moduli equivalenti: se lo strumento accetta quattro opzioni, aggiungi `Modifica / Rettifica` come scelta esplicita. Se il Master sceglie questa voce senza dettare la rettifica, chiedigliela prima di procedere. Se lo strumento accetta solo tre opzioni, usa le tre voci sopra e il campo libero.
   - Usa la chat solo se il modulo non è utilizzabile, anche tramite il coordinatore, e indica il motivo concreto:
     > **Passo [N/Totale] - [Titolo Sezione o Concetto]**
     > [Testo esatto estratto dal file]
     > **Domanda**: confermi il testo, hai aggiornato il file, vuoi dettare una rettifica o preferisci rimandare?
   - Attendi la risposta prima di applicare modifiche o badge. Con il modulo asincrono mantieni aperto il turno e riprendi dal punto pendente quando arriva la risposta.

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
