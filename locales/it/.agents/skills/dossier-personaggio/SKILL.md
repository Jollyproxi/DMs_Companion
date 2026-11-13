---
name: dossier-personaggio
description: "Use when: creare, aggiornare o modularizzare i dossier dei Personaggi Giocanti (PG) a cinque moduli o le schede dei Personaggi Non Giocanti (PNG) secondo gli standard canonici della campagna."
argument-hint: "Specifica il tipo (PG o PNG), il nome del personaggio e l'operazione (crea, aggiorna modulo, scheda)"
user-invocable: true
disable-model-invocation: false
---

# Skill: Gestione Dossier Personaggi (PG & PNG)

Questa skill governa la creazione, la modularizzazione e l'aggiornamento sistematico dei dossier dei Personaggi Giocanti (PG) e delle schede dei Personaggi Non Giocanti (PNG), garantendo rigore formale, cross-linking e aderenza al canone senza mai inventare dettagli non autorizzati dal Dungeon Master.

I template completi sono consultabili in [template-dossier](./references/template-dossier.md).

> **📌 Regola Nomi Propri Collegati**: ogni nome proprio di entità dell'ambientazione (PG, PNG, fazioni, casate, città, luoghi, oggetti magici, usanze, festival, eventi…) che compare nel testo prodotto deve essere un **collegamento Markdown** al file `.md` canonico dell'entità (es. `[Nome](percorso/relativo/file.md)`), mai semplice testo nudo. Eccezioni: intestazioni, nomi di file, frontmatter, blocchi di codice, nodi Mermaid e sorgenti `.mw`. Entità priva di scheda: non inventarla — usa `[DA_DEFINIRE_MASTER: scheda mancante per <Nome>]` e segnala la lacuna. Verifica e conversione: skill `collega-nomi-propri`.

---

## 1. Regole di Compilazione (Zero Allucinazioni)

- **Dati Certi**: Compila unicamente i campi forniti dal Master o già registrati nei verbali di sessione.
- **Campi Mancanti**: Inserisci `[DA_DEFINIRE_MASTER: elemento mancante]` (es. per sottoclasse non ancora scelta, divinità patrona o segreto DM non svelato).
- **Interazione Strutturata**: Se il Master fornisce indicazioni parziali per un nuovo personaggio, chiedi i dati essenziali (Tipo: PG o PNG; Campagna di destinazione; Ruolo marziale/arcano/sociale; Allineamento o codice morale) usando lo strumento di domande strutturate dell'ambiente (`vscode_askQuestions`, `AskUserQuestion`) se disponibile, altrimenti direttamente in chat.
- **Tracciamento Temporale**: Ogni file o modulo creato o modificato deve contenere il badge di stato:
  `> 🛡️ *Verificato: AAAA-MM-GG | Modificato: AAAA-MM-GG*`
  Se il file viene modificato a seguito di una sessione, aggiorna unicamente la data di `Modificato`.

---

## 2. Creazione di un Dossier PG (5 Moduli)

Quando il Master introduce o documenta un nuovo Personaggio Giocante:

1. **Acquisizione Guidata (se necessario)**: Conferma con il Master nome esatto, classe, livello e campagna di appartenenza.
2. **Creazione della Cartella**:
   `05_personaggi/Giocanti/<Campagna>/<Nome_PG>/`
3. **Generazione dei File Modulari**:
   - `README.md`: Hub del personaggio con ruolo, tratti morali e indice dei 5 file.
   - `01_anagrafica_e_tratti.md`: Dati anagrafici, classe, livello, tratti e aspetto.
   - `02_backstory_integrata.md`: Passato, eventi di svolta, radici nel mondo.
   - `03_relazioni_e_dinamiche.md`: Legami con compagni di gruppo, fazioni e PNG.
   - `04_equipaggiamento_e_capacita.md`: Oggetti caratteristici, armi, focus e capacità uniche.
   - `05_ganci_e_segreti_dm.md`: Spunti riservati per il Master, enigmi e rivelazioni.
4. **Aggiornamento Hub Campagna e Gruppo**:
   Aggiungi il nuovo PG al file `README.md` in `05_personaggi/Giocanti/<Campagna>/README.md` e nell'indice generale `05_personaggi/README.md`.

---

## 3. Creazione o Aggiornamento Scheda PNG

Quando il Master introduce un Personaggio Non Giocante rilevante:

1. **Acquisizione Guidata**: Se mancano elementi essenziali, chiarisci con il Master fazione di appartenenza, stato vitale e ubicazione.
2. **Percorso**:
   `05_personaggi/Non-Giocanti/<Nome_PNG>.md`
3. **Struttura**:
   - Intestazione con ruolo, fazione (con link a `07_fazioni/`), residenza (link a `06_luoghi/`), allineamento e stato vitale.
   - Sezioni su Aspetto & Indole, Ruolo Narrativo e Segreti & Ganci DM.
4. **Aggiornamento Indice PNG**:
   Aggiungi la voce nella tabella delle relazioni in `05_personaggi/Non-Giocanti/README.md`.

---

## 4. Aggiornamenti Incrociati Post-Sessione

Quando una sessione introduce novità su un PG (es. nuovo gancio scoperto, legame mutato, ferita o oggetto ottenuto):
1. Individua il modulo specifico da aggiornare (es. `03_relazioni_e_dinamiche.md` per un patto, `05_ganci_e_segreti_dm.md` per una pista svelata).
2. Apporta la modifica preservando le informazioni precedenti.
3. Avanza la data nel campo `Modificato: [DATA_ODIERNA]` lasciando inalterata la data `Verificato`.
