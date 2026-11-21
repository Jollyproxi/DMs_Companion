# Prompt di Trascrizione Sessione (NotebookLM / LLM)

Usa questo prompt in **NotebookLM** (o in un altro LLM capace di elaborare file audio o trascrizioni lunghe) per estrarre un resoconto notarile prima di passare il risultato all'**Archivista di Campagna** (`verbale-sessione`):

1. Carica nel notebook la registrazione audio o la trascrizione grezza della sessione (anche divisa in più file).
2. *(Opzionale)* Carica un piccolo elenco testuale con la sola grafia esatta dei nomi propri già noti (PG, PNG, luoghi ricorrenti) per ridurre i `[?]` — puoi generarlo direttamente dal tuo archivio con la skill `glossario-trascrizione`.
3. Copia e incolla il blocco sottostante nella chat. Se la sessione è lunga e il modello chiude con `[CONTINUA DA: Sezione X / HH:MM:SS]`, chiedigli di continuare da quel punto fino a completare la **Sezione 12 (Copertura)**.
4. Incolla o salva l'output completo e avvia `/verbale-sessione` (Canale C) per compilare il verbale canonico e proporre gli aggiornamenti incrociati.

---

````markdown
# COMPITO
Ricevi la trascrizione (o la registrazione) di una sessione di gioco di ruolo.
Produci un resoconto strutturato e fedele di ciò che è stato detto e fatto.
NON conosci l'ambientazione, i personaggi, le regole della campagna né chi parla:
tutto ciò che sai è contenuto nella fonte. Se tra le fonti è presente un glossario
o elenco nomi fornito dal Master, usalo soltanto per la grafia dei nomi propri,
senza importare fatti o retroscena che non emergano dalla sessione.
Il tuo output sarà riletto e riorganizzato da un'altra persona: non devi
interpretare, devi restituire.

# REGOLE
1. Solo ciò che è nella fonte. Nessuna deduzione presentata come fatto:
   `(inferenza)` è ammessa solo per raccordi tecnici evidenti (es. speaker o
   pronome evidente), mai per motivazioni, cause o retroscena non esplicitati.
2. Non correggere, non tradurre, non "normalizzare" arbitrariamente i nomi propri:
   riportali come sono pronunciati (salvo eventuale grafia nel glossario del
   Master). Grafia dubbia → `Nome[?]`. Parola o passaggio incomprensibile →
   `[incomprensibile 00:12:34]`.
3. Attribuisci ogni azione a chi l'ha compiuta, usando il nome del personaggio se
   detto, altrimenti quello del giocatore. In `NARRAZIONE`, distingui le
   descrizioni oggettive del Master dalle affermazioni in-character di PNG o PG
   (es. `"<PNG> dichiara che …"`), senza trasformare le parole di un personaggio
   in fatti oggettivi del mondo.
4. Distingui sempre tre registri e non mescolarli:
   - `NARRAZIONE` = fiction, ciò che accade nel mondo (sempre inclusa in Cronologia)
   - `TAVOLO` = regole, tiri, iniziativa, discussioni meccaniche (inclusa in
     Cronologia solo se determina un esito meccanico rilevante o una decisione
     di regola/campagna)
   - `FUORI GIOCO` = battute, pause, logistica, argomenti personali (esclusa dalla
     Cronologia; segnalala solo in Copertura, o in Scheda se riguarda assenze
     o logistica)
5. Dialoghi: non riscriverli. Cita testualmente tra virgolette, con timestamp,
   assegnando un ID progressivo (`[C1]`–`[C20]`, massimo 20 citazioni) secondo
   questa priorità: patti/giuramenti/minacce → rivelazioni/indizi → decisioni →
   nomi/numeri. Scrivi ogni citazione testuale una sola volta nella sezione 4
   sotto l'elemento principale coinvolto, e richiamala solo per codice (`[C#]`)
   negli altri elementi.
6. Non inventare titoli, temi, cause o motivazioni. Ciò che non è detto resta non
   detto. Non riempire i vuoti con la logica narrativa.
7. Multi-fonte e timestamp: se nel notebook sono presenti più file della
   sessione, anteponi al timestamp il nome della fonte (es. `[Parte1 00:12:34]`).
   Se la fonte non contiene timestamp, non inventarli mai: scrivi
   `[senza timestamp]` (o il riferimento presente, es. `[parte 2]`).
8. Anti-troncamento: se la trascrizione è lunga e ti avvicini al limite di
   risposta, non riassumere né omettere eventi; chiudi alla fine di una sezione o
   riga completa con `[CONTINUA DA: Sezione X / HH:MM:SS]`.
9. Italiano, Markdown valido. Usa esattamente le intestazioni indicate, nello
   stesso ordine. Nessuna introduzione, nessun commento finale, nessun giudizio.

# OUTPUT

## 1. Scheda
Elenco puntato: nome campagna e numero sessione (se detti); partecipanti e in che
ruolo (con abbinamento `Giocatore → PG` se dichiarato); riferimento temporale
reale e/o in-game della sessione (se detto); punto di partenza; punto di arrivo;
salti di scena o di tempo rilevati; eventuali dati di gioco o logistica
dichiarati (livello, esperienza, risorse, assenze) — solo se espliciti.

## 2. Chi c'è
| Nome (come pronunciato) | Giocatore / Voce (nome giocatore / master / incerto) | Tipo (PG / PNG / creatura / gruppo / altro / non chiaro) | In scena (sì / no / solo citato) | Nota in una riga |

## 3. Cronologia
| # | Timestamp | Dove | Chi | Cosa succede (3-5 frasi fattuali) | Conseguenza immediata | Registro |
Segna le discontinuità di tempo o scena con una riga di tabella valida:
`| — | <timestamp> | SALTO | — | Da <luogo/momento A> a <luogo/momento B> | — | NARRAZIONE |`
Sotto la tabella: **Elenco secco** — una riga per evento, massimo 20 parole l'una.

## 4. Fatti per elemento
Un blocco per ogni nome proprio citato, dal più presente al meno presente:

### <Nome>
- Tipo: PG / PNG / creatura / luogo / fazione-istituzione / oggetto-artefatto / usanza-festa / evento / legge-norma / concetto / non chiaro
- Varianti / alias uditi: elenco delle grafie fonetiche o soprannomi alternativi (includere questa riga solo se presenti; se c'è il dubbio che siano entità distinte, tenerle separate e segnalarlo in `Domande aperte`)
- Fatti: elenco puntato. Un solo fatto per punto, verificabile, con timestamp (distinguendo descrizione del Master e dichiarazione di PNG/PG).
- Relazioni: `<Nome> → <altro nome>: cosa` (una riga per relazione)
- Prima menzione: timestamp
- Citazioni: solo se presenti per la regola 5 (`[C#] "..." (timestamp)` o rimando `[C#]`)

Se un elemento viene solo nominato senza dettagli, scrivilo:
"nominato soltanto, nessun dettaglio".

## 5. Cambi di stato e indizi
| Chi | Categoria (oggetto / condizione-ferita / risorsa / indizio-rivelazione / posizione) | Fatto dichiarato | Timestamp |
Solo fatti espliciti (oggetti acquisiti/ceduti, ferite o condizioni persistenti,
variazioni di risorse, indizi/rivelazioni rivolti a un PG, spostamenti rilevanti).
Se non ce ne sono: "Nessuno".

## 6. Impegni
| Chi | Verso chi | Cosa | Condizione | Testimoni | Timestamp |
Promesse, minacce, patti, debiti, accordi, giuramenti. Se non ce ne sono: "Nessuno".

## 7. Numeri
| Dato | Valore | Contesto | Timestamp |
Ogni cifra pronunciata: monete, prezzi, danni, punti ferita, distanze, quantità,
età, date, percentuali, durate.

## 8. Tempo
| Espressione (testuale) | Contesto / evento associato | Timestamp |
Ogni indicazione temporale: "ieri", "tre giorni", "l'anno scorso", stagioni,
anniversari, scadenze, "molto tempo fa".

## 9. Domande aperte
Elenco numerato. Formulazione: "Non è detto se / chi / quando / perché ..." +
timestamp del punto in cui l'informazione sarebbe attesa (includi eventuali dubbi
su varianti fonetiche che potrebbero indicare la stessa entità o entità diverse).

## 10. Contraddizioni
Solo incoerenze interne alla fonte: `A afferma X (timestamp)` / `B afferma Y (timestamp)`.
Nessuna correzione, solo la segnalazione. Se non ce ne sono: "Nessuna".

## 11. Blocco dati
Un unico blocco YAML valido, senza commenti. Includi solo le chiavi con contenuto reale.
Mantieni i campi descrittivi (`cosa`, `fatto`, `fatti`) sintetici (una riga per voce).

```yaml
sessione:
  campagna: ""
  numero: ""
  riferimento: ""
  inizio: ""
  fine: ""
chi:
  - nome: ""
    giocatore_voce: ""
    tipo: ""
    in_scena: ""
    note: ""
eventi:
  - ordine: 1
    timestamp: ""
    dove: ""
    attori: []
    cosa: ""
    conseguenza: ""
    registro: ""
elementi:
  - nome: ""
    tipo: ""
    varianti: []
    fatti: []
    relazioni: []
    prima_menzione: ""
    citazioni: []
cambi_stato_indizi:
  - chi: ""
    categoria: ""
    fatto: ""
    timestamp: ""
impegni:
  - chi: ""
    verso_chi: ""
    cosa: ""
    condizione: ""
    testimoni: []
    timestamp: ""
numeri:
  - dato: ""
    valore: ""
    contesto: ""
    timestamp: ""
tempo:
  - espressione: ""
    contesto: ""
    timestamp: ""
aperte:
  - domanda: ""
    timestamp: ""
contraddizioni:
  - affermazione_a: ""
    timestamp_a: ""
    affermazione_b: ""
    timestamp_b: ""
```

## 12. Copertura
| Intervallo | Contenuto | Qualità (chiaro / confuso / incomprensibile) |
````
