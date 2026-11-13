---
name: audit-file-intero
description: "Use when: revisionare ed eseguire l'audit di un intero documento, dossier o cartella di D&D in un unico passaggio, individuare incongruenze, proporre modifiche e applicare i badge visibili di verifica."
argument-hint: "Percorso del file o cartella da verificare (es. 05_personaggi/ o singolo .md)"
user-invocable: true
disable-model-invocation: false
---

# Skill: Audit di Documento o Cartella Intera

Questa skill consente una revisione rapida, organica e globale di un intero file o di un gruppo di file (cartella tematica) di D&D, ideale quando il Master non desidera l'interrogatorio atomico concetto per concetto, ma un quadro d'insieme con validazione a blocchi.

> **📌 Regola Nomi Propri Collegati**: ogni nome proprio di entità dell'ambientazione (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico dell'entità (es. `[Nome](percorso/relativo/file.md)`), mai semplice testo nudo. Eccezioni: intestazioni, nomi di file, frontmatter, blocchi di codice, nodi Mermaid e sorgenti `.mw`. Entità priva di scheda: non inventarla — usa `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna. Verifica e conversione: skill `collega-nomi-propri`.

---

## 1. Regole di Revisione

- **Rilevamento Discrepanze**: Confronta le affermazioni del documento con la cosmologia e le cronache del workspace (es. date, nomi di casate, gerarchie di fazione) per segnalare eventuali conflitti al Master.
- **Divieto di Riscrivere Senza Approvazione**: Mostra sempre il resoconto e le correzioni prima di modificare il file.
- **Riconoscimento della Struttura**: Rispetta la modularità del workspace (cosmologia, geografia, politica, diritto, personaggi, luoghi, fazioni, oggetti, cronache, usi-costumi-ed-eventi, timeline).

---

## 2. Sintassi del Flag di Verifica (Badge Visibile)

Ogni sezione principale o scheda validata riceve il badge Markdown standard:

```markdown
> 🛡️ *Verificato: AAAA-MM-GG | Modificato: AAAA-MM-GG*
```

Se il file è strutturato in sezioni tematiche (`## Titolo`), il badge viene posizionato subito sotto il titolo di ogni sezione convalidata.

---

## 3. Procedura Operativa

1. **Scansione del Documento o della Cartella**:
   - Leggi il file (o elenca i file della cartella indicata).
   - Estrai la mappa concettuale: entità coinvolte, fatti narrativi, legami con altre parti del mondo.

2. **Presentazione del Sommario di Audit**:
   - Presenta al Master una sinossi strutturata:
     - **File in Esame**: Percorso del file.
     - **Punti di Forza / Canone Riconosciuto**: Elenco dei fatti coerenti.
     - **Eventuali Discrepanze o Dubbi**: Segnala discrepanze o campi `[DA_DEFINIRE_MASTER]`.
     - **Bozza delle Modifiche Proposte**: Mostra le eventuali rettifiche suggerite.

3. **Convalida da parte del Master**:
   - Chiedi conferma al Master (usando lo strumento di domande strutturate dell'ambiente come `vscode_askQuestions` o `AskUserQuestion` se disponibile, altrimenti direttamente in chat) con opzioni chiare:
     - `Approva tutto e applica badge 🛡️` (consigliata se non vi sono discrepanze)
     - `Richiedi rettifiche specifiche` (permette di digitare le correzioni nel campo libero)
     - `Annulla audit / Nessuna modifica`

4. **Applicazione dei Flag**:
   - Una volta ricevuta la conferma, applica le modifiche e apponi i badge `> 🛡️ *Verificato: [DATA_ODIERNA] | Modificato: [DATA_ODIERNA]*` su ciascuna sezione convalidata.

5. **Aggiornamento Dashboard**:
   - Invoca la skill `stato-revisione` per aggiornare il riepilogo generale in `STATO_REVISIONE.md`.
