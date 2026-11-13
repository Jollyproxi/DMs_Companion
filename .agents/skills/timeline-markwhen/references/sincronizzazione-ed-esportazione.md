# Sincronizzazione, Validazione ed Esportazione Markwhen

Regole di allineamento tra `10_timeline/markwhen/`, gli altri moduli dell'ambientazione, `struttura_ambientazione.json` e la cartella `10_timeline/esportazioni/`.

---

## 1. Mappatura Bidirezionale tra Moduli e File `.mw`

Ogni evento nei file `.mw` corrisponde a una fonte documentale canonica:

| Fonte Canonica | Destinazione in `markwhen/` | Tag richiesti |
| :--- | :--- | :--- |
| `10_timeline/cronologia_storica/*.md` | `epoche/<epoca>.mw` (e `campagne/<campagna>.mw` se rilevante) | `#evento` (o `#festival`/`#usanza`) + `#storico` |
| `10_timeline/registro_occorrenze/*.md` | `epoche/<epoca>.mw` + eventuale `campagne/<campagna>.mw` | `#festival #occorrenza` o `#evento` + `#storico` / `#in_svolgimento` / `#pianificato` |
| `03_societa_e_politica/usi_costumi_ed_eventi/festival_ed_occorrenze/*.md` (Tabella *Occorrenze note*) | `epoche/<epoca>.mw` + `timeline_generale.mw` (se ricorrenza fissa di calendario) | `#festival #occorrenza` + stato corrispondente |
| `03_societa_e_politica/usi_costumi_ed_eventi/eventi/*.md` | `epoche/<epoca>.mw` + eventuale `campagne/<campagna>.mw` | `#evento` + stato corrispondente (`concluso` → `#storico`) |
| `09_cronache/campagne/<nome>/sessioni/*.md` | `campagne/<slug_campagna>.mw` (e `epoche/<epoca>.mw` se evento di portata storica) | `#evento` o `#occorrenza` + `#campagna_<slug>` + stato |
| `10_timeline/calendario/*.md` | `timeline_generale.mw` (sezione commentata legenda calendario) | — |

### Regola di Conversione Stato Scheda → Tag Markwhen

- Scheda / Registro con stato `concluso` o evento passato → `#storico`
- Scheda / Registro con stato `in svolgimento` → `#in_svolgimento`
- Scheda / Registro con stato `pianificato` → `#pianificato`

---

## 2. Sincronizzazione con `struttura_ambientazione.json`

I sorgenti `.mw` e i render in `esportazioni/`:

1. **NON vanno mai inseriti nella Bibbia dell'Ambientazione** (`BIBBIA DELL'AMBIENTAZIONE.md`).
2. **Vanno censiti in `struttura_ambientazione.json`** dentro l'oggetto del Tomo `10` (`id: "timeline"`), nell'array `file_markwhen`:

```json
"cartella_markwhen": "10_timeline/markwhen",
"file_markwhen": [
  "10_timeline/markwhen/timeline_generale.mw",
  "10_timeline/markwhen/epoche/01_prima_era.mw",
  "10_timeline/markwhen/campagne/cronache_del_nord.mw"
],
"cartella_esportazioni": "10_timeline/esportazioni"
```

Quando `crea-mw` aggiunge o rimuove un file `.mw`, aggiorna `10_timeline/markwhen/README.md` e proponi (o esegui su conferma) l'aggiornamento di `file_markwhen` in `struttura_ambientazione.json`.

---

## 3. Checklist di Validazione (`valida-mw`)

Durante l'esecuzione di `valida-mw`, verifica i seguenti punti in ordine:

1. **Struttura cartelle e indice**:
   - Esistenza di `10_timeline/markwhen/README.md` e `10_timeline/markwhen/timeline_generale.mw`.
   - Tutti i file `.mw` presenti in `epoche/` e `campagne/` devono essere elencati sia in `10_timeline/markwhen/README.md` sia nell'indice commentato di `timeline_generale.mw`.
2. **Sintassi Markwhen**:
   - Header YAML racchiuso correttamente tra due righe `---`, privo di chiavi `#Categoria` senza valore `:` e privo di `dateFormat: yyyy-MM-dd` (il formato ISO è nativo; specificare invece `timezone: UTC`).
   - Bilanciamento di ogni `section` con il rispettivo `endSection` (e `group` con `endGroup`).
   - Formato data valido prima dei `:` nelle righe evento (assenza di date inventate o testo libero non commentato al posto della data).
3. **Copertura Tag**:
   - Ogni riga evento possiede almeno 1 tag di tipologia (`#usanza`, `#festival`, `#evento`, `#occorrenza`) e 1 tag di stato (`#storico`, `#in_svolgimento`, `#pianificato`).
   - Tutti i tag usati nei file `epoche/*.mw` e `campagne/*.mw` sono censiti nella legenda di `timeline_generale.mw`.
4. **Link Markdown**:
   - I percorsi relativi nei sottopunti degli eventi (es. `../../../03_societa_e_politica/...`) risolvono a file esistenti su disco e usano `%20` per eventuali spazi nel target.
5. **Allineamento col Tomo 10 e `struttura_ambientazione.json`**:
   - Ogni voce in `cronologia_storica/` e `registro_occorrenze/` ha il corrispettivo nel file `.mw` dell'epoca.
   - L'array `file_markwhen` del Tomo 10 in `struttura_ambientazione.json` corrisponde esattamente ai file `.mw` presenti su disco.

---

## 4. Pipeline di Esportazione (`esporta-mw`) *(Opzionale)*

La cartella `10_timeline/esportazioni/` ospita i render derivati (esclusi dalla Bibbia).

### Modalità A — Tramite Markwhen CLI (`@markwhen/mw`)

Se nell'ambiente è disponibile Node.js / `npx` o il comando `mw`:

- **Timeline HTML interattiva**:
  `npx @markwhen/mw <percorso_file.mw> -o 10_timeline/esportazioni/<nome_file>.html`
- Verifica sempre prima se il comando è disponibile (`command -v mw` su macOS/Linux o `Get-Command mw` su PowerShell, oppure `npx --version`).

### Modalità B — Tramite Estensione IDE (`Markwhen`) o Web App

Se il Master preferisce esportare in PNG/SVG/PDF tramite l'estensione Markwhen dell'editor o `markwhen.com`:

1. Prepara e valida il file `.mw` sorgente assicurando che l'header YAML abbia `title` e colori dei tag completi.
2. Indica il nome file canonico di salvataggio in `10_timeline/esportazioni/`:
   - `timeline_epoca_<slug>.(html|svg|png|pdf)`
   - `timeline_campagna_<slug>.(html|svg|png|pdf)`
3. Aggiorna `10_timeline/esportazioni/README.md` con una tabella riepilogativa:

```markdown
## File Esportati

| Render Esportato | Sorgente `.mw` | Formato | Ultimo Aggiornamento |
| :--- | :--- | :--- | :--- |
| [timeline_campagna_...](timeline_campagna_....html) | [campagne/....mw](../markwhen/campagne/....mw) | HTML | AAAA-MM-GG |
```
