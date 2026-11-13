---
name: usanza-festa-evento
description: "Use when: registrare usanze e peculiarità della vita quotidiana, festival ed eventi ricorrenti (occorrenze), ed eventi peculiari una tantum dell'ambientazione; creare o aggiornare le schede in 03_societa_e_politica/usi_costumi_ed_eventi/ e mantenere la 10_timeline/ (cronologia storica, registro occorrenze e timeline grafica Markwhen)."
argument-hint: "Specifica tipologia e voce (es. 'usanza: cerimonia del commiato', 'festival: festa del solstizio', 'evento: assedio della cittadella')"
user-invocable: true
disable-model-invocation: false
---

# Skill: Usi, Costumi ed Eventi (Usanza-Festa-Evento)

Questa skill gestisce la sottoserie `03_societa_e_politica/usi_costumi_ed_eventi/` e il suo legame con il tomo `10_timeline/`: cataloga le peculiarità della vita quotidiana, i festival e le occorrenze ricorrenti, e gli eventi peculiari una tantum, con i medesimi standard di fedeltà notarile del resto dell'archivio.

---

## 1. Regola Aurea (Zero Allucinazioni)

- Non inventare usanze, date, rituali, partecipanti o esiti non forniti dal Master o non già documentati nei file canonici.
- Dettaglio mancante: in interattività chiedilo al Master (usando lo strumento di domande strutturate dell'ambiente come `vscode_askQuestions` o `AskUserQuestion` se disponibile, altrimenti direttamente in chat); in stesura diretta inserisci `[DA_DEFINIRE_MASTER: descrizione]`.

---

## 2. Tassonomia delle Tipologie

La classificazione segue la **natura** della voce, non la sua periodicità:

| Tipologia | Sottocartella | Natura | Esempi |
| :--- | :--- | :--- | :--- |
| **Usanza** | `usanze/` | Peculiarità della vita quotidiana: comportamenti, rituali sociali, forme e modi codificati (strutture e modi del rito). | Cerimonie di saluto o commiato ufficiale; rituali di ospitalità; usi a tavola; formule di indirizzo. |
| **Festival / Occorrenza** | `festival_ed_occorrenze/` | Eventi **istituzionali o rituali ricorrenti**, a periodicità **fissa** (calendario) o **variabile a scaturiggine** (condizioni d'innesto, tempi anticipabili). | Festa del Solstizio d'Inverno; torneo di selezione della guardia (al ritorno di spedizioni); elezioni (tempi previsti ma anticipabili per cause). |
| **Evento una tantum** | `eventi/` | Per natura **unico o non ripetibile**: sconvolgimenti storici, rivolte, cataclismi, svolte. Può essere **storico passato** oppure **imminente/in svolgimento** (esito deciso nelle sessioni). Anche se potrebbe ripetersi, resta qui per natura. | Assedio di una cittadella; rivolta mineraria; patto spezzato; catastrofe naturale. |

Se una voce sembra ibrida (es. un rito istituzionale che ha assunto tono di sconvolgimento), classificala per la sua natura prevalente e aggiungi un link incrociato nella scheda collegata.

---

## 3. Struttura delle Cartelle e Nomi File

```text
03_societa_e_politica/usi_costumi_ed_eventi/
├── README.md                       # Indice della sottoserie (una sezione per tipologia)
├── usanze/
│   ├── README.md
│   └── 01_<slug_voce>.md           # Prefisso numerico progressivo per sottocartella
├── festival_ed_occorrenze/
│   ├── README.md
│   └── 01_<slug_voce>.md
└── eventi/
    ├── README.md
    └── 01_<slug_voce>.md
```

- Nomi file: `NN_slug_in_snake_case.md`, numerazione progressiva per sottocartella (es. `01_cerimonia_commiato.md`, `02_...`).
- Ogni sottocartella e la cartella madre ricevono un `README.md` indice, aggiornato a ogni nuova scheda.

---

## 4. Template Scheda — Usanza

```markdown
# [Nome dell'Usanza]

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

## Inquadramento
Cos'è, dove e quando si pratica, chi è tenuto a osservarla.

## Formalismo e modi
Struttura passo-passo del rito/comportamento: gesti, formule, ordine degli atti, tempi, tono.

## Varianti e gradi
Differenze per rango sociale, fazione, regione o contesto (corte, piazza, cerimonia pubblica...).

## Significato e sanzioni
Valore simbolico e storico dell'usanza; conseguenze delle infrazioni (sociali, giuridiche, rituali).

## Legami e ganci DM
Collegamenti a PNG, fazioni, luoghi o altre schede (link relativi). Eventuali spunti riservati al Master.

## Ricadute meccaniche *(opzionale)*
Eventuali effetti di gioco (modificatori, vantaggi, ispirazione). Compilare solo dove serve.
```

---

## 5. Template Scheda — Festival / Occorrenza

```markdown
# [Nome del Festival / dell'Evento Ricorrente]

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

## Inquadramento
Cos'è, chi lo celebra/presiede, significato e posizione nella cultura del mondo.

## Periodicità e scaturiggine
- **Periodicità**: fissa (calendario) / variabile a scaturiggine / mista.
- **Scaturiggine (trigger)**: condizioni che innescano l'evento (es. "ritorno di una campagna", "morte del titolare", "decisione del consiglio").

## Finestre temporali
Tempi previsti, termini di preavviso, possibilità e cause di anticipi o posticipi (es. elezioni anticipate per cause particolari).

## Svolgimento
Rituali, fasi, cerimonie, durata, sequenza degli atti.

## Partecipanti e ruoli
Chi presiede, chi partecipa, requisiti di accesso, esclusi, ruoli istituzionali coinvolti.

## Occorrenze note
| Edizione / Data | Stato | Esito | Timeline |
| :--- | :--- | :--- | :--- |
| [anno del mondo o data] | pianificato / in svolgimento / concluso | [esito] | [link a 10_timeline] |

## Legami e ganci DM
Collegamenti a PNG, fazioni, luoghi, usanze o eventi correlati. Spunti riservati al Master.

## Ricadute meccaniche *(opzionale)*
Eventuali effetti di gioco. Compilare solo dove serve.
```

---

## 6. Template Scheda — Evento una tantum

```markdown
# [Nome dell'Evento]

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

## Inquadramento
Cos'è accaduto (o accadrà): natura dello sconvolgimento e collocazione storica. Specificare se **storico** o **in svolgimento**.

## Cause e premesse
Contesto, tensioni, decisioni o coincidenze che hanno preparato l'evento.

## Svolgimento
Fasi dell'evento in sequenza.

## Conseguenze e ricadute
Impatti su luoghi, fazioni, istituzioni, PNG ed equilibri del mondo.

## Stato dell'occorrenza
- **Stato**: pianificato / in svolgimento / concluso.
- **Esito** (se concluso): [sintesi].
- **Data / periodo**: [anno del mondo].

## Protagonisti e testimoni
PNG, PG, fazioni o popoli coinvolti o presenti (con link alle schede).

## Legami e ganci DM
Collegamenti incrociati e spunti riservati al Master.

## Ricadute meccaniche *(opzionale)*
Eventuali effetti di gioco. Compilare solo dove serve.
```

---

## 7. Procedura di Creazione (Intervista Guidata)

Poni le seguenti domande al Master (usando lo strumento interattivo dell'ambiente come `vscode_askQuestions` / `AskUserQuestion` se disponibile, altrimenti in chat):

1. **Tipologia**: *Si tratta di un'usanza, di un festival/occorrenza ricorrente o di un evento una tantum?* (Opzioni con descrizione della distinzione per natura della §2).
2. **Nome e collocazione**: *Nome della voce e, se noto, il contesto (fazione, luogo, periodo)?* (Campo libero).
3. **Campi tipologici**: raccogli i campi del template scelto (per i festival: periodicità fissa/variabile, trigger, finestre temporali; per gli eventi: storico o in svolgimento).
4. **Scrittura**: crea il file con prefisso numerico progressivo nella sottocartella corretta, compila le sezioni note e segna le lacune con `[DA_DEFINIRE_MASTER: ...]`.
5. **Badge**: imposta `> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*`.
6. **Propagazione**: aggiorna i `README.md` di raccordo, proponi l'aggiornamento della `10_timeline/` e, se la voce entra nel canone documentale, proponi `sincronizza-bibbia-struttura` (`aggiorna-bibbia`, `aggiorna-struttura-json`).

---

## 8. Gestione delle Occorrenze (Eventi già censiti)

Quando una sessione fa svolgere una ricorrenza di un festival/occorrenza già censito (es. un torneo annuale):

1. **Verbale**: documenta l'occorrenza nel verbale di sessione (`verbale-sessione`).
2. **Timeline**: registra l'occorrenza in `10_timeline/` (registro occorrenze + sorgenti Markwhen) con stato ed esito.
3. **Scheda canonica**: **chiedi al Master** se modificare la scheda.
   - Le peculiarità proprie di quell'occorrenza (numeri, partecipanti, esiti, intoppi) **restano nella timeline e nei verbali**.
   - La scheda si aggiorna **solo** se le peculiarità **stravolgono la natura** della voce (es. cambiano regole, ruolo o significato del rito). In tal caso aggiorna la scheda e la riga "Occorrenze note".

---

## 9. Aggiornamento della `10_timeline/`

Per ogni nuova voce, occorrenza o variazione di stato (pianificato → in svolgimento → concluso):

1. **Cronologia storica** (`10_timeline/cronologia_storica/`, file per epoca/periodo): per gli eventi passati, con tag di categoria (es. `#evento #storico`).
2. **Registro occorrenze** (`10_timeline/registro_occorrenze/`, file per epoca/periodo): per le verifiche di festival ed eventi ricorrenti e per gli eventi in divenire.
3. **Markwhen** (`10_timeline/markwhen/`): aggiorna o crea i sorgenti `.mw` tramite la skill dedicata `timeline-markwhen` (`crea-mw` / `aggiorna-mw`) secondo [convenzioni-markwhen](./references/convenzioni-markwhen.md).
4. **Calendario** (`10_timeline/calendario/`): se la voce introduce o usa una periodicità fissa, allinea la definizione del calendario del mondo.

Le voci interne a cronologia storica e registro occorrenze usano gli stessi tag della tassonomia Markwhen, così le due rappresentazioni restano sincronizzate.

---

## 10. Badge, Indici e Sincronizzazione

- **Badge**: usa sempre il badge standard `> 🛡️ *Verificato: ... | Modificato: ...*` con le regole temporali consuete (nuovo testo → `Verificato: NON_CONVALIDATO`; modifica post-convalida → solo `Modificato` avanzato; audit → entrambe le date).
- **Indici**: aggiorna `README.md` della sottocartella, della cartella madre `usi_costumi_ed_eventi/` e, se pertinente, quello di `03_societa_e_politica/`.
- **Codifiche canone** (Bibbia/JSON): usanze `3.5.x`, festival/occorrenze `3.6.x`, eventi `3.7.x`; tomo `10_timeline` codificato come tomo `10` (`10.1.x` cronologia storica, `10.2.x` registro occorrenze, `10.3.x` calendario). I sorgenti `.mw` e le esportazioni sono esclusi dalla Bibbia e indicizzati solo nel JSON.
- **Zero allucinazioni**: come per ogni altro modulo, mai dettagli non approvati dal Master.
