# Template di Riferimento per Dossier Personaggi

## 1. Dossier Modulare Personaggio Giocante (PG)

Ogni PG possiede una cartella dedicata in `05_personaggi/<Giocanti>/<Campagna_o_Party>/<Nome_PG>/` (default: `05_personaggi/Giocanti/<Campagna>/<Nome_PG>/`) con un `README.md` di raccordo e sei moduli tematici:

### `README.md` (Hub del Personaggio)
```markdown
# [Nome Personaggio]

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

* **Campagna:** [Nome Campagna]
* **Ruolo nel Gruppo:** [Sintesi del ruolo marziale/arcano/sociale]
* **Allineamento / Codice Morale:** [Allineamento o principi etici]

## Indice dei Moduli
1. [01. Anagrafica & Tratti Fondamentali](01_anagrafica_e_tratti.md)
2. [02. Backstory Integrata](02_backstory_integrata.md)
3. [03. Relazioni & Dinamiche di Gruppo](03_relazioni_e_dinamiche.md)
4. [04. Equipaggiamento & Capacità Peculiari](04_equipaggiamento_e_capacita.md)
5. [05. Dicerie e convinzioni](05_dicerie_e_convinzioni.md)
6. [06. Ganci Narrativi & Segreti del DM](06_ganci_e_segreti_dm.md)
```

### `01_anagrafica_e_tratti.md`
```markdown
# 01. Anagrafica & Tratti Fondamentali

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

* **Nome:** [Nome Completo]
* **Razza / Stirpe:** [Razza D&D 5e / stirpe del mondo]
* **Classe & Livello:** [Classe, Sottoclasse, Livello]
* **Allineamento / Codice Morale:** [Allineamento o principi cardine]
* **Aspetto Fisico:** [Descrizione visiva, tratti distintivi, cicatrici, abbigliamento]
* **Tratti di Personalità, Ideali, Legami, Difetti:** [Elenchi sintetici]
```

### `02_backstory_integrata.md`
```markdown
# 02. Backstory Integrata nel Canone

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

## Origini & Radici
[Descrizione dell'origine geografica e sociale con link relativi ai luoghi del mondo.]

## L'Evento di Svolta
[L'evento o trauma fondativo che ha spinto il personaggio all'avventura.]

## Sviluppi Recenti prima della Campagna
[Cosa è accaduto nel periodo immediatamente precedente all'inizio della campagna.]
```

### `03_relazioni_e_dinamiche.md`
```markdown
# 03. Relazioni & Dinamiche

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

## Legami con i Compagni di Gruppo
* **[Nome Compagno 1]:** [Dinamica relazionale, fiducia, attriti]
* **[Nome Compagno 2]:** [...]

## Legami con PNG & Fazioni
* **[Nome PNG / Fazione]:** [Tipo di relazione, debiti d'onore, rivalità]
```

### `04_equipaggiamento_e_capacita.md`
```markdown
# 04. Equipaggiamento & Capacità Peculiari

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

## Dotazione Principale & Focus
* [Oggetto Magico / Focus con eventuale link a 08_oggetti_magici_peculiari/]

## Capacità & Tratti Peculiari
* **[Nome Capacità]:** [Descrizione narrativa e meccanica]
```

### `05_dicerie_e_convinzioni.md`

Per ogni ruolo attestato inserisci un punto con una riga sulla versione e il link relativo alla variante. Annota la posizione del soggetto se documentata.

```markdown
# 05. Dicerie e convinzioni

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

## Dicerie conosciute

## Dicerie a cui crede

## Dicerie che diffonde

## Dicerie sul suo conto

## Convinzioni personali
```

### `06_ganci_e_segreti_dm.md`
```markdown
# 06. Ganci Narrativi & Segreti del DM

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

> ⚠️ *Sezione confidenziale ad uso esclusivo del Dungeon Master.*

## Piste Investigative Aperte
* **[Pista 1]:** [Dettagli, agganci, possibili sviluppi]

## Verità Nascoste & Rivelazioni Future
* **[Segreto 1]:** [Verità sul passato del PG ignota al personaggio stesso]
```

---

## 2. Scheda Personaggio Non Giocante (PNG)

Applica la convenzione PNG del progetto. Leggila nelle istruzioni del progetto e nell’indice del tomo dei personaggi. Nei progetti esistenti privi di una regola esplicita, rispetta la struttura e gli indici in uso e segnala eventuali conflitti o ambiguità al Master. Cerca la scheda esistente negli indici, nei file e tramite eventuali alias. Mantieni un solo file canonico per identità e usa link da campagne, fazioni e altri luoghi. Per i livelli geografici o narrativi, usa il legame stabile documentato e registrane il motivo. Primo incontro (luogo e verbale) e posizione attuale sono campi distinti. Per riferimenti incerti, segnala il dato da definire e conserva i livelli accertati. Usa una collocazione provvisoria solo se prevista dal progetto, altrimenti chiedi al Master di risolvere la collocazione gerarchica. Usa categorie itineranti o trasversali solo se previste e documentate nel canone. In un archivio piatto registra queste informazioni nella scheda o nell’indice secondo la convenzione.

```markdown
# [Nome PNG] — [Titolo o Ruolo]

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

* **Legame stabile e motivo:** [Valori dei livelli, eventuale categoria o dato da definire secondo la convenzione]
* **Posizione attuale:** [Link al luogo, se noto; dato distinto dal riferimento principale]
* **Primo incontro:** [Link al verbale e al luogo, se documentati]
* **Fazione / Casata:** [Nome Fazione con link relativo a 07_fazioni/]
* **Luogo di Residenza / Operatività:** [Luogo con link a 06_luoghi/]
* **Allineamento / Morale:** [Allineamento o principi morali]
* **Stato Attuale:** [Vivo, Latitante, Deceduto, Disperso]

---

## Aspetto & Indole
[Descrizione fisica, postura, modo di parlare, temperamento.]

---

## Ruolo Narrativo & Rapporti con il Party
[Chi è nel mondo e come interagisce con i PG.]

---

## Segreti & Ganci per il DM
* **[Segreto / Motivazione Nascosta]:** [Cosa persegue realmente]
* **[Gancio d'Avventura]:** [Come coinvolgerlo nelle prossime sessioni]

## Dicerie

### Dicerie conosciute

### Dicerie a cui crede

### Dicerie che diffonde

### Dicerie sul suo conto
```
