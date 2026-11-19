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

1. **Acquisizione Guidata (se necessario)**: Conferma con il Master nome esatto, classe, livello e campagna/gruppo di appartenenza.
2. **Creazione della Cartella**:
   `05_personaggi/<Giocanti>/<Campagna_o_Party>/<Nome_PG>/` *(default: `05_personaggi/Giocanti/<Campagna>/<Nome_PG>/`, rispettando eventuali nomi custom nel workspace)*
3. **Generazione dei File Modulari**:
   - `README.md`: Hub del personaggio con ruolo, tratti morali e indice dei 5 file.
   - `01_anagrafica_e_tratti.md`: Dati anagrafici, classe, livello, tratti e aspetto.
   - `02_backstory_integrata.md`: Passato, eventi di svolta, radici nel mondo.
   - `03_relazioni_e_dinamiche.md`: Legami con compagni di gruppo, fazioni e PNG.
   - `04_equipaggiamento_e_capacita.md`: Oggetti caratteristici, armi, focus e capacità uniche.
   - `05_ganci_e_segreti_dm.md`: Spunti riservati per il Master, enigmi e rivelazioni.
4. **Struttura**:
   - Intestazione con ruolo, fazione (con link al Tomo VII `07_fazioni/`), residenza (link al Tomo VI `06_luoghi/`), allineamento e stato vitale.
   - Sezioni su Aspetto & Indole, Ruolo Narrativo e Segreti & Ganci DM.
   - **Aggiornamento Hub Campagna e Gruppo**:
   Aggiungi il nuovo PG al file `README.md` in `05_personaggi/<Giocanti>/<Campagna_o_Party>/README.md` e nell'indice generale `05_personaggi/README.md`.

---

## 3. Creazione o Aggiornamento Scheda PNG

Quando il Master introduce un Personaggio Non Giocante rilevante:

1. Organizza i PNG per **cornice e luogo principale di riferimento**, usando il legame territoriale o narrativo stabile documentato nel canone. Il primo incontro e la posizione attuale sono dati distinti e non determinano automaticamente la collocazione. Mantieni una sola scheda canonica; fazioni, campagne e altri luoghi la richiamano tramite link.
2. `05_personaggi/<Non-Giocanti>/<Cornice>/<Luogo_riferimento>/<Nome_PNG>.md` (default: `05_personaggi/Non-Giocanti/<Cornice>/<Luogo_riferimento>/<Nome_PNG>.md`).
3. Se il riferimento è ambiguo, chiedi al Master; in stesura diretta usa `DA_DEFINIRE_MASTER/` al livello ignoto (cornice o luogo), senza inventare affiliazioni. Per PNG esplicitamente itineranti o trasversali usa `Trasversali/` e/o `Itineranti/` solo se documentato. Riutilizza i nomi canonici di cornici e luoghi, rispettando i nomi custom dei tomi.
4. **Struttura**:
   - Intestazione con ruolo, fazione (con link al Tomo VII `07_fazioni/`), residenza (link al Tomo VI `06_luoghi/`), allineamento e stato vitale.
   - Sezioni su Aspetto & Indole, Ruolo Narrativo e Segreti & Ganci DM.
   - **Cornice di riferimento:** [Link alla scheda canonica nel Tomo II]
   - **Luogo principale di riferimento:** [Link alla scheda canonica nel Tomo VI e motivo del legame]
   - **Posizione attuale:** [Link al luogo, se noto; dato distinto dal riferimento principale]
   - **Primo incontro:** [Link al verbale e al luogo, se documentati]
5. Crea o aggiorna i `README.md` del tomo, dei PNG, della cornice e del luogo; gli indici riportano cornice, luogo principale e link alla scheda unica.
6. Per riorganizzare schede esistenti, prepara la mappa origine → destinazione sulla base del canone e applica gli spostamenti autorizzati. Ricalcola i link relativi in uscita e aggiorna tutti i riferimenti in entrata (verbali, dossier, luoghi, fazioni, timeline), i README vecchi e nuovi, la Bibbia e il JSON. Non duplicare le schede né riscrivere il luogo storico del primo incontro. I casi irrisolti restano segnalati; verifica i link dopo gli spostamenti.

---

## 4. Aggiornamenti Incrociati Post-Sessione

Quando una sessione introduce novità su un PG (es. nuovo gancio scoperto, legame mutato, ferita o oggetto ottenuto):
1. Individua il modulo specifico da aggiornare (es. `03_relazioni_e_dinamiche.md` per un patto, `05_ganci_e_segreti_dm.md` per una pista svelata).
2. Apporta la modifica preservando le informazioni precedenti.
3. Avanza la data nel campo `Modificato: [DATA_ODIERNA]` lasciando inalterata la data `Verificato`.
