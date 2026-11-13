# Convenzioni di Compilazione della Bibbia dell'Ambientazione

La Bibbia dell'Ambientazione (`BIBBIA DELL'AMBIENTAZIONE.md` o titolo esteso adottato nel workspace) è il documento master narrativo monolitico del mondo. Riunisce in una sequenza fluida, continua e consultabile l'intero corpus di conoscenze ripartito nei dieci tomi.

---

## 1. Frontespizio e Metadati

In testa al file viene inserita la testata canonica:

```markdown
### BIBBIA DELL'AMBIENTAZIONE: [NOME_AMBIENTAZIONE]

> 📜 **Documento Master Monolitico del Canone**  
> *Versione Canone:* [VERSIONE] | *Ultima Compilazione:* [DATA_ODIERNA]  
> 🛡️ *Verificato: [DATA_V] | Modificato: [DATA_M]*

---
```

---

## 2. Gerarchia delle Intestazioni (Mapping Livelli)

Poiché il documento include molti tomi e moduli annidati, le intestazioni dei singoli file `.md` vengono trasposte secondo la seguente scala canonica:

| Livello nel Modulo Atomico | Livello nella Bibbia Master | Formato Esempio |
| :--- | :--- | :--- |
| **Titolo Tomo (dal README)** | Livello 5 (`#####`) | `##### 1. Cosmologia & Architettura Metafisica` |
| **Titolo Modulo (`# Titolo`)** | Livello 6 Corsivo (`###### *...*`) o `### X.Y` | `###### *1.1 La Struttura Planare e Cosmica*` |
| **Sezione Interna (`## Sezione`)** | Titolo `###` o `####` | `### I Piani Elementali e le Terre Liminali` |
| **Sottosezione (`### Sotto`)** | Grassetto puntato o `#####` | `* **Corte Astrale:** ...` |

> **Nota di Continuità**: Se il workspace contiene già un file master della Bibbia, adotta esattamente lo stile e i tag di intestazione già utilizzati nel file esistente.

---

## 3. Ordine Sequenziale di Compilazione dei Tomi

La compilazione procede rigorosamente secondo la sequenza numerica canonica:

1. **##### 1. Cosmologia & Architettura Metafisica** (`01_cosmologia/`)
   - `01_struttura_verticale.md`
   - `02_ciclo_stagioni_e_meccaniche_celesti.md`
   - `03_flusso_della_magia_e_ordine_divino.md`
   - `04_sistema_morale_o_filosofico.md`
   - Eventuali sottocartelle opzionali custom (`<piani>/`, `<pantheon>/`).
2. **##### 2. Geografia Fisica, Territoriale e Ambientale** (`02_geografia/`)
   - Moduli principali di geografia, mappe, sottosuolo e piani liminali.
   - Trattazione delle singole regioni o macro-aree nella sottocartella dedicata (`regioni/` o nome custom scelto nel workspace), ordinate per numero crescente.
3. **##### 3. Ordinamento Sociale, Politico ed Economico** (`03_societa_e_politica/`)
   - Modelli sociali, economia, classi, ordine pubblico e forze dell'ordine.
   - Eventuale sottocartella opzionale `popoli/` (o nome custom per specie/razze/stirpi/culture, codici `3.8.x`).
   - Sottoserie `usi_costumi_ed_eventi/`: usanze (`3.5.x`), festival/occorrenze (`3.6.x`), eventi una tantum (`3.7.x`), in ordine numerico progressivo per sottocartella.
4. **##### 4. Diritto e Leggi** (`04_diritto_e_leggi/`)
   - Ordinamento e fonti (`4.1.x`), diritti civili e status (`4.2.x`), diritto dinastico e successione (`4.3.x`), contratti e patti (`4.4.x`), trattati e diplomazia (`4.5.x`), diritto penale e reati (`4.6.x`), tribunali e procedura (`4.7.x`), diritto arcano e religioso (`4.8.x`), proprietà, commercio e fisco (`4.9.x`), diritto bellico e avventurieri (`4.10.x`), più eventuali branche extra (`4.11.x+`) o sottocartelle per giurisdizione, ciascuna con quadro generale (`4.Y.1`) e atti censiti (`4.Y.2+`) in ordine numerico progressivo.
5. **##### 5. Anagrafica dei Personaggi del Mondo** (`05_personaggi/`)
   - Roster PNG significativi (`<Non-Giocanti>/`, con eventuali sottocartelle custom), raggruppati per fazione o regione.
   - Sintesi dei legami del party se presente una campagna/gruppo canonico.
6. **##### 6. Atlante dei Luoghi e Nodi d'Avventura** (`06_luoghi/` o `06_location/`)
   - Luoghi salienti, fortezze, città e varchi (anche raggruppati in sottocartelle opzionali `<gruppi_luoghi>/`).
7. **##### 7. Registro Geopolitico delle Fazioni e Casate** (`07_fazioni/` o `07_factions/`)
   - Statuti, gerarchie e rivalità delle potenze dominanti (anche raggruppati in sottocartelle opzionali `<gruppi_fazioni>/`).
8. **##### 8. Registro degli Oggetti Magici Peculiari e Reliquie** (`<08_oggetti_magici_peculiari>/` o variante/nome custom)
   - Manufatti unici, storia, inquadramento giuridico e meccaniche peculiari (anche divisi in sottocartelle opzionali `<categorie>/`).
9. **##### 9. Cronache Storiche e Compendio Campagne** (`09_cronache/`)
   - Compendio delle campagne/spedizioni attive (`<campagne>/`) e verbali progressivi (`<sessioni>/`).
10. **##### 10. Timeline e Cronologia del Mondo** (`10_timeline/`)
    - Cronologia storica (`10.1.x`, file per epoca/periodo), registro occorrenze (`10.2.x`, file per epoca/periodo) e calendario (`10.3.x`).
    - I sorgenti Markwhen (`markwhen/*.mw`) e le esportazioni grafiche (`esportazioni/`) sono **esclusi** dalla Bibbia: restano indicizzati solo in `struttura_ambientazione.json`.
    - Le voci interne usano la tassonomia di tag Markwhen (es. `#usanza #festival #evento #occorrenza`) per restare sincronizzate con la timeline grafica.

---

## 4. Trattamento di Tabelle, Diagrammi e Note DM

1. **Tabelle Markdown**: Vengono riportate integralmente, verificando che la formattazione a colonne con trattini `| :--- | :--- |` sia integra e priva di righe spezzate.
2. **Diagrammi Mermaid**: Vengono mantenuti nei rispettivi blocchi ` ```mermaid `, assicurando che la sintassi dei nodi sia valida.
3. **Note per il DM**: I riquadri `**NOTA PER IL DUNGEON MASTER:**` o `> ⚠️ **Nota DM:**` vengono inclusi come blocchi citazione evidenziati (`> ...`), preservando il contesto operativo per la conduzione delle sessioni.
4. **Segnaposto Incompleti**: Eventuali marcatori `[DA_DEFINIRE_MASTER: ...]` vengono riportati fedelmente senza inventare contenuti.

---

## 5. Regole di Aggiornamento Incrementale (`aggiorna-bibbia`)

Quando viene invocata la modalità incrementale:
1. Non riscrivere l'intero documento master.
2. Localizza l'intestazione esatta del modulo modificato (tramite codice `X.Y` o titolo).
3. Sostituisci il blocco compreso tra l'inizio della sezione del modulo e l'inizio del modulo successivo.
4. Se il modulo è una nuova aggiunta, inseriscilo al termine del tomo di appartenenza, rispettando l'ordinamento numerico.
5. Aggiorna la riga di metadati in testa al file impostando la data odierna in `Modificato: [DATA_ODIERNA]`.
