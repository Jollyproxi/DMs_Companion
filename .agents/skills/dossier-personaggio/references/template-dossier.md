# Template di Riferimento per Dossier Personaggi

## 1. Dossier Modulare Personaggio Giocante (PG)

Ogni PG possiede una cartella dedicata in `05_personaggi/Giocanti/<Campagna>/<Nome_PG>/` con un `README.md` di raccordo e cinque moduli tematici:

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
5. [05. Ganci Narrativi & Segreti del DM](05_ganci_e_segreti_dm.md)
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

### `05_ganci_e_segreti_dm.md`
```markdown
# 05. Ganci Narrativi & Segreti del DM

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

> ⚠️ *Sezione confidenziale ad uso esclusivo del Dungeon Master.*

## Piste Investigative Aperte
* **[Pista 1]:** [Dettagli, agganci, possibili sviluppi]

## Verità Nascoste & Rivelazioni Future
* **[Segreto 1]:** [Verità sul passato del PG ignota al personaggio stesso]
```

---

## 2. Scheda Personaggio Non Giocante (PNG)

Ogni PNG risiede come singolo file in `05_personaggi/Non-Giocanti/[Nome_PNG].md`:

```markdown
# [Nome PNG] — [Titolo o Ruolo]

> 🛡️ *Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]*

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
```
