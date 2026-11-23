---
name: dossier-personaggio
description: "Use when: creare, aggiornare o modularizzare i dossier dei Personaggi Giocanti (PG) a sei moduli o le schede dei Personaggi Non Giocanti (PNG) secondo gli standard canonici della campagna."
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

## 2. Creazione di un Dossier PG (6 Moduli)

Quando il Master introduce o documenta un nuovo Personaggio Giocante:

1. **Acquisizione Guidata (se necessario)**: Conferma con il Master nome esatto, classe, livello e campagna/gruppo di appartenenza.
2. **Creazione della Cartella**:
   `05_personaggi/<Giocanti>/<Campagna_o_Party>/<Nome_PG>/` *(default: `05_personaggi/Giocanti/<Campagna>/<Nome_PG>/`, rispettando eventuali nomi custom nel workspace)*
3. **Generazione dei File Modulari**:
   - `README.md`: Hub del personaggio con ruolo, tratti morali e indice dei 6 file.
   - `01_anagrafica_e_tratti.md`: Dati anagrafici, classe, livello, tratti e aspetto.
   - `02_backstory_integrata.md`: Passato, eventi di svolta, radici nel mondo.
   - `03_relazioni_e_dinamiche.md`: Legami con compagni di gruppo, fazioni e PNG.
   - `04_equipaggiamento_e_capacita.md`: Oggetti caratteristici, armi, focus e capacità uniche.
   - `05_dicerie_e_convinzioni.md` — Dicerie e convinzioni.
   - `06_ganci_e_segreti_dm.md`: Spunti riservati per il Master, enigmi e rivelazioni.
4. **Struttura**:
   - Intestazione con ruolo, fazione (con link al Tomo VII `07_fazioni/`), residenza (link al Tomo VI `06_luoghi/`), allineamento e stato vitale.
   - Sezioni su Aspetto & Indole, Ruolo Narrativo e Segreti & Ganci DM.
   - **Aggiornamento Hub Campagna e Gruppo**:
   Aggiungi il nuovo PG al file `README.md` in `05_personaggi/<Giocanti>/<Campagna_o_Party>/README.md` e nell'indice generale `05_personaggi/README.md`.

---

## 3. Creazione o Aggiornamento Scheda PNG

## Convenzione dell’archivio PNG

Applica la convenzione PNG del progetto. Leggila nelle istruzioni del progetto e nell’indice del tomo dei personaggi. Nei progetti esistenti privi di una regola esplicita, rispetta la struttura e gli indici in uso e segnala eventuali conflitti o ambiguità al Master.

Cerca la scheda esistente negli indici, nei file e tramite eventuali alias. Mantieni un solo file canonico per identità e usa link da campagne, fazioni e altri luoghi. Per i livelli geografici o narrativi, usa il legame stabile documentato e registrane il motivo. Primo incontro (luogo e verbale) e posizione attuale sono campi distinti.

Per riferimenti incerti, segnala il dato da definire e conserva i livelli accertati. Usa una collocazione provvisoria solo se prevista dal progetto, altrimenti chiedi al Master di risolvere la collocazione gerarchica. Usa categorie itineranti o trasversali solo se previste e documentate nel canone. In un archivio piatto registra queste informazioni nella scheda o nell’indice secondo la convenzione.

Prima di uno spostamento autorizzato, mappa origine e destinazione e controlla che la destinazione sia libera. Aggiorna gli indici precedenti e nuovi, tutti i riferimenti in entrata e i link relativi in uscita. Conserva i dati del primo incontro, rigenera i documenti derivati previsti dal progetto e verifica che tutti i link risolvano verso le destinazioni canoniche e che resti una sola scheda.

Per Dante resta in uso `<Cornice>/<Luogo_riferimento>/<Nome_PNG>.md` sotto la radice PNG.

Usa il [template](./references/template-dossier.md) e aggiorna gli indici previsti.

---

## 4. Aggiornamenti Incrociati Post-Sessione

Quando una sessione introduce novità su un PG (es. nuovo gancio scoperto, legame mutato, ferita o oggetto ottenuto):
1. Individua il modulo specifico da aggiornare (es. `03_relazioni_e_dinamiche.md` per un patto, `06_ganci_e_segreti_dm.md` per una pista svelata).
2. Apporta la modifica preservando le informazioni precedenti.
3. Avanza la data nel campo `Modificato: [DATA_ODIERNA]` lasciando inalterata la data `Verificato`.

Nel dossier esistente conserva il contenuto dei ganci, rinomina il vecchio modulo 05 in 06, crea il nuovo 05 e aggiorna indice e link in entrata, incluse le ancore. Se il 06 esiste già, confronta i contenuti prima di spostare file. Verifica i link anche dopo una seconda esecuzione.

## Pettegolezzi e dicerie

Per ogni ruolo attestato inserisci un punto con una riga sulla versione e il link relativo alla variante. Annota la posizione del soggetto se documentata.
