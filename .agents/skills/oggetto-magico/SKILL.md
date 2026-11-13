---
name: oggetto-magico
description: "Use when: registrare o formattare oggetti magici peculiari, reliquie e artefatti dell'ambientazione secondo lo standard canonico a quattro sezioni (scheda tecnica, manifattura, meccaniche, statuto giuridico)."
argument-hint: "Nome dell'oggetto magico e dettagli da inserire o aggiornare"
user-invocable: true
disable-model-invocation: false
---

# Skill: Gestione Oggetti Magici Peculiari (Oggetto-Magico)

Questa skill governa la catalogazione formale di artefatti, reliquie e focus arcani all'interno del Tomo VIII (`08_oggetti_magici_peculiari/`, oppure `08_oggetti magici peculiari/` o altro nome custom del tomo nel workspace), rispettando il modello strutturale definito in [template-oggetto](./references/template-oggetto.md).

> **📌 Regola Nomi Propri Collegati**: ogni nome proprio di entità dell'ambientazione (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico dell'entità (es. `[Nome](percorso/relativo/file.md)`), mai semplice testo nudo. Eccezioni: intestazioni, nomi di file, frontmatter, blocchi di codice, nodi Mermaid e sorgenti `.mw`. Entità priva di scheda: non inventarla — usa `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna. Verifica e conversione: skill `collega-nomi-propri`.

---

## 1. Principi di Registrazione

- **Inquadramento nel Mondo**: Registra origine, rarità e statuto legale o commerciale dell'oggetto secondo le regole dell'ambientazione (bene di libero scambio, licenza di gilda, monopolio statale/nobile o contrabbando proibito).
- **Zero Invenzioni**: Se il Master fornisce solo le proprietà meccaniche o l'aspetto, non inventare retroscena o custodi fittizi: richiedi i dettagli mancanti o inserisci `[DA_DEFINIRE_MASTER: ...]`.
- **Tracciamento Badge**: Ogni scheda include il badge:
  `> 🛡️ *Verificato: AAAA-MM-GG | Modificato: AAAA-MM-GG*`

---

## 2. Procedura Operativa

1. **Raccolta Informazioni**:
   Se i dettagli forniti dal Master sono incompleti, poni un prompt strutturato (usando lo strumento interattivo dell'ambiente come `vscode_askQuestions` o `AskUserQuestion` se disponibile, altrimenti in chat):
   - **`categoria`**: Opzioni (*Arma Magica*, *Strumento Musicale / Focus*, *Reliquia / Artefatto Antico*, *Congegno / Dispositivo Magico*, *Consumabile Raro*).
   - **`custode`**: Custode attuale (opzioni basate sui PG censiti o campo libero per PNG/luogo).
   - **`statuto_giuridico`**: Opzioni (*Libero Possesso / Lecito*, *Soggetto a Licenza o Monopolio*, *Contrabbando / Reliquia Proibita*, *Altro*).
   - **`poteri_meccaniche`**: Proprietà meccaniche D&D 5e e risonanze sensoriali (campo libero).

2. **Creazione del File**:
   Salva la scheda in `<08_oggetti_magici_peculiari>/[<categoria>/]<Nome_Oggetto>.md` (rispettando l'eventuale nome custom del tomo VIII e le sottocartelle opzionali di categoria) utilizzando il template standard.

3. **Aggiornamento Indice del Tomo**:
   Aggiungi la voce con categoria, risonanza e custode nella tabella o lista del file `<08_oggetti_magici_peculiari>/README.md` (e dell'eventuale `README.md` di categoria).

4. **Collegamento Incrociato con il Custode**:
   Se l'oggetto appartiene a un PG, aggiorna il modulo `04_equipaggiamento_e_capacita.md` del dossier PG collegandolo alla nuova scheda dell'oggetto.
