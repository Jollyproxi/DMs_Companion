# Archivista di Campagna — Guida di Utilizzo

Tutto ciò che serve per mettere a lavoro l'**Archivista di Campagna** al tuo tavolo: installazione, primi passi, riferimento completo delle **12 skill**, flussi di lavoro tipici, risoluzione dei problemi e FAQ.

* Copie localizzate di questa guida: [British English](https://github.com/<owner>/DMs_Companion/blob/main/locales/en-gb/USAGE.md) · [Français](https://github.com/<owner>/DMs_Companion/blob/main/locales/fr/GUIDE-UTILISATION.md) · [Deutsch](https://github.com/<owner>/DMs_Companion/blob/main/locales/de/NUTZUNGSANLEITUNG.md) — vedi anche il [USAGE.md](https://github.com/<owner>/DMs_Companion/blob/main/USAGE.md) di progetto sul branch `main`.

---

## 1. Installazione

**Prerequisiti**: un assistente AI per la programmazione (vedi la tabella harness qui sotto) e, consigliato ma non obbligatorio, un repository Git per la tua campagna/ambientazione.

### Opzione 1 — Copia questo branch nella tua campagna (consigliata)

Stai leggendo il pacchetto `it` (clonato con `git clone --depth 1 -b it …` oppure scaricato come ZIP). Copia il suo contenuto nella radice del **tuo repository di campagna** (oppure nella directory di configurazione utente del tuo assistente AI, per rendere il toolkit disponibile in ogni progetto):

* `AGENTS.md`, `CLAUDE.md`
* `.github/agents/`
* `.agents/skills/`
* `GUIDA-UTILIZZO.md` (questa guida)

### Opzione 2 — Installa le skill tramite Agent Skills CLI (`npx skills`)

```bash
# Tutte le skill da questo branch di lingua
npx skills add https://github.com/<owner>/DMs_Companion/tree/it

# Oppure direttamente dalla cartella del locale su main
npx skills add https://github.com/<owner>/DMs_Companion/tree/main/locales/it/.agents/skills
```

*(Ricorda di copiare anche `AGENTS.md` e/o `.github/agents/*.agent.md` se vuoi la persona completa dell'Archivista e l'orchestrazione dei flussi di lavoro.)*

### Cosa Fanno i File Installati

| File / Cartella | Scopo |
| :--- | :--- |
| `AGENTS.md` | Regole e flussi universali, letti da ogni harness. |
| `CLAUDE.md` | Punto di ingresso per Claude Code; importa `AGENTS.md`. |
| `.github/agents/archivista-di-campagna.agent.md` | La persona *Archivista di Campagna* (voce nella selezione agenti di VS Code). |
| `.agents/skills/<skill>/SKILL.md` | Le 12 skill modulari (più i template in `references/`). |
| `GUIDA-UTILIZZO.md` | Questa guida. |

### Note per Harness

| Harness | Cosa Succede |
| :--- | :--- |
| **VS Code / GitHub Copilot** | L'agente compare nella selezione agenti della chat; le skill sono disponibili come comandi `/slash`; le domande di approfondimento arrivano come prompt strutturati (`vscode_askQuestions`). |
| **Claude Code** | `CLAUDE.md` viene caricato automaticamente. Se le skill non vengono rilevate, copia o crea un symlink di `.agents/skills/*` in `.claude/skills/`. |
| **OpenAI Codex CLI / Cursor / OpenCode / Gemini CLI / Antigravity** | `AGENTS.md` e `.agents/skills/` vengono scoperti automaticamente; basta chiedere in linguaggio naturale. |
| **Estensioni opzionali** | Graphify MCP (grafia dei cross-link) e la CLI/estensione Markwhen (`@markwhen/mw`) per il rendering delle timeline. Tutto funziona anche senza. |

---

## 2. Primi Cinque Minuti

1. **Apri il repository della tua campagna** nel tuo assistente AI.
2. **Seleziona l'agente *Archivista di Campagna*** nella selezione agenti (VS Code) o citalo in chat (altri harness).
3. **Spiegagli a che punto sei**:
   * *Mondo nuovo* → esegui `/init-mondo` e rispondi all'intervista guidata: genera l'alberatura a dieci tomi, l'indice radice e i semi dei file master.
   * *Mondo esistente* → esegui prima `/valida-struttura`. L'Archivista si adatta alle cartelle che hai già, inclusi i nomi legacy (`06_location/`, `07_factions/`, `08_oggetti magici peculiari/`, `cornici/`, …).
4. **Verifica il risultato**: i file master (`BIBBIA DELL'AMBIENTAZIONE.md`, `STATO_REVISIONE.md`, `struttura_ambientazione.json`) vivono nella radice del mondo; la lore vive dentro i dieci tomi.
5. **Prova un compito reale**: incolla gli appunti grezzi dell'ultima sessione e lascia che l'Archivista rediga il verbale.

---

## 3. Come Ragiona il Toolkit

### La Regola Aurea: Fedeltà Notarile (Zero Allucinazioni)

L'Archivista organizza **solo** ciò che fornisci o che hai già canonizzato. Non inventa mai personaggi, luoghi, date, risvolti di trama o cifre.

* **Informazione mancante** → te la chiede direttamente (modalità interattiva) oppure inserisce un segnaposto ben visibile `[DA_DEFINIRE_MASTER: descrizione del dettaglio mancante]` che potrai cercare in seguito.
* **Creatività solo su richiesta** → fa brainstorming (nomi, opzioni, idee) **solo** quando lo chiedi esplicitamente (es. *"Dammi 3 opzioni per…"*, *"Inventa un nome coerente"*).

### L'Architettura a Dieci Tomi

| Tomo | Contenuto |
| :--- | :--- |
| `01_cosmologia/` | Piani, meccaniche celesti, flusso magico ed etica cosmica. |
| `02_geografia/` | Cartografia, territori, regioni sotterranee, dossier regionali (`regioni/` o `cornici/`). |
| `03_societa_e_politica/` | Ordinamento civile, economia, classi sociali, giustizia; sottoserie `usi_costumi_ed_eventi/` (`usanze/`, `festival_ed_occorrenze/`, `eventi/`). |
| `04_diritto_e_successione/` | Leggi fondamentali, diritto dinastico, patti, trattati, tribunali. |
| `05_personaggi/` | Dossier modulari PG (`Giocanti/<Campagna>/<Nome_PG>/`) e schede PNG (`Non-Giocanti/`). |
| `06_luoghi/` | Nodi d'avventura, città, roccaforti, pericoli d'area. |
| `07_fazioni/` | Casate, congreghe, corporazioni, ordini, gerarchie di potere. |
| `08_oggetti_magici_peculiari/` | Manufatti unici, reliquie, registri normativi, proprietà. |
| `09_cronache/` | Hub di campagna: tabella sinottica + verbali progressivi (`campagne/<nome>/sessioni/`). |
| `10_timeline/` | Cronologia trasversale: `cronologia_storica/`, `registro_occorrenze/`, `markwhen/` (`timeline_generale.mw`, `epoche/`, `campagne/`), `calendario/`, `esportazioni/`. |

### Badge di Verifica

Ogni sezione convalidata porta il badge standard:

```markdown
> 🛡️ *Verificato: AAAA-MM-GG | Modificato: AAAA-MM-GG*
```

* **Testo nuovo** → `Verificato: NON_CONVALIDATO | Modificato: [DATA_ODIERNA]` finché non lo revisioni.
* **Le modifiche post-sessione** toccano solo `Modificato`: quando è più recente di `Verificato`, la sezione necessita un ricontrollo.
* **Durante un audit** entrambe le date vengono allineate alla data odierna.

---

## 4. Riferimento delle Skill

Invoca le skill con il relativo comando slash dove disponibile (VS Code, Claude Code), oppure cita semplicemente il nome della skill in chat — l'Archivista instrada la richiesta per te.

| # | Skill | A Cosa Serve |
| :-: | :--- | :--- |
| 1 | `init-mondo` | Impostazione guidata e scaffolding di un mondo nuovo. |
| 2 | `valida-struttura` | Controllo di salute strutturale dell'archivio. |
| 3 | `verbale-sessione` | Verbali post-sessione da appunti grezzi o intervista. |
| 4 | `dossier-personaggio` | Dossier PG a 5 moduli e schede PNG. |
| 5 | `oggetto-magico` | Registri a 4 sezioni per oggetti magici. |
| 6 | `audit-passo-passo` | Fact-checking interattivo, affermazione per affermazione. |
| 7 | `audit-file-intero` | Audit di un intero file o cartella. |
| 8 | `stato-revisione` | Dashboard di revisione costruita sui badge `🛡️`. |
| 9 | `sincronizza-bibbia-struttura` | Bibbia dell'Ambientazione master + JSON machine-readable. |
| 10 | `usanza-festa-evento` | Usanze, festival/occorrenze, eventi una tantum. |
| 11 | `timeline-markwhen` | Timeline grafiche Markwhen (`.mw`). |
| 12 | `collega-nomi-propri` | Nomi propri sempre collegati alle schede canoniche. |

### 4.1 `init-mondo` — Scaffolding del Mondo

* **Quando**: parti con un mondo o un repository di campagna completamente nuovo.
* **Come**: `/init-mondo` — *“Inizia l'intervista per configurare e generare l'alberatura del mondo.”*
* **Risultato**: l'alberatura a dieci tomi con gli indici `README.md`, i semi dei file master (`BIBBIA DELL'AMBIENTAZIONE.md`, `struttura_ambientazione.json`, …) e la premessa del mondo registrata.

### 4.2 `valida-struttura` — Diagnostica Strutturale

* **Quando**: prima/dopo grandi riorganizzazioni, o quando qualcosa sembra fuori posto.
* **Come**: `/valida-struttura` — *“Esegue il controllo di conformità strutturale dell'archivio.”*
* **Risultato**: un report su cartelle mancanti, indici `README.md` assenti, link Markdown rotti e file `.md` sparsi che apparterrebbero a uno dei dieci tomi.

### 4.3 `verbale-sessione` — Cronache e Verbali di Sessione

* **Quando**: subito dopo una sessione di gioco.
* **Come**: incolla i tuoi appunti grezzi, oppure scrivi *“inizia intervista”* (`/verbale-sessione`) per essere guidato domanda per domanda.
* **Risultato**: un file verbale formale in `09_cronache/campagne/<nome>/sessioni/XX_titolo.md` — sinossi notarile, diagramma Mermaid dei ganci PG, fasi salienti, registro meccanico opzionale — più la tabella sinottica della campagna aggiornata.

### 4.4 `dossier-personaggio` — Dossier PG e Schede PNG

* **Quando**: un nuovo personaggio giocante entra in gioco, un PNG va definito, o un modulo di dossier va aggiornato.
* **Come**: `/dossier-personaggio` — *“Specifica il tipo (PG o PNG), il nome del personaggio e l'operazione (crea, aggiorna modulo, scheda).”*
* **Risultato**: un dossier PG a 5 moduli (`01_anagrafica_e_tratti`, `02_backstory_integrata`, `03_relazioni_e_dinamiche`, `04_equipaggiamento_e_capacita`, `05_ganci_e_segreti_dm`) in `05_personaggi/Giocanti/<Campagna>/<Nome_PG>/`, oppure una scheda PNG in `05_personaggi/Non-Giocanti/`, entrambi registrati negli indici.

### 4.5 `oggetto-magico` — Oggetti Magici Peculiari

* **Quando**: un manufatto unico, una reliquia o un fuoco arcano entra nel canone.
* **Come**: `/oggetto-magico` — *“Nome dell'oggetto magico e dettagli da inserire o aggiornare.”*
* **Risultato**: un registro a 4 sezioni in `08_oggetti_magici_peculiari/`: scheda tecnica, manifattura, meccaniche e statuto giuridico.

### 4.6 `audit-passo-passo` — Fact-Checking Atomico

* **Quando**: vuoi verificare la lore affermazione per affermazione con l'assistente che ti interroga su ogni punto.
* **Come**: `/audit-passo-passo` — *“Specifica il file o l'argomento da revisionare e la granularità (atomica o sezione).”*
* **Risultato**: una revisione interattiva senza correzioni inventate; le sezioni verificate ricevono il badge aggiornato.

### 4.7 `audit-file-intero` — Audit di File Intero

* **Quando**: un intero documento o cartella necessita di una revisione organica.
* **Come**: `/audit-file-intero` — *“Percorso del file o cartella da verificare (es. `05_personaggi/` o singolo `.md`).”*
* **Risultato**: un audit strutturato di tutto il bersaglio, incongruenze segnalate, correzioni proposte per la tua approvazione.

### 4.8 `stato-revisione` — Dashboard di Revisione

* **Quando**: vuoi una panoramica di ciò che è verificato e di ciò che è obsoleto.
* **Come**: `/stato-revisione` — *“Genera o aggiorna la dashboard di revisione del workspace.”*
* **Risultato**: `STATO_REVISIONE.md` alla radice del mondo, con percentuali per file e paragrafi modificati dopo l'audit segnalati.

### 4.9 `sincronizza-bibbia-struttura` — Sincronizzazione del Canone Master

* **Quando**: dopo modifiche al canone, o quando vuoi un unico documento narrativo master / una mappa machine-readable.
* **Come**: `/sincronizza-bibbia-struttura` con un'operazione — `genera-Bibbia`, `genera-struttura-json`, `aggiorna-bibbia` o `aggiorna-struttura-json`.
* **Risultato**: `BIBBIA DELL'AMBIENTAZIONE.md` (compilazione narrativa monolitica dei dieci tomi) e `struttura_ambientazione.json` (tassonomia gerarchica con metadata).

### 4.10 `usanza-festa-evento` — Usanze, Festival ed Eventi

* **Quando**: una sessione introduce un'usanza, un festival/occorrenza ricorrente o un evento una tantum (rivolta, cataclisma, sconvolgimento storico).
* **Come**: `/usanza-festa-evento` — *“Specifica tipologia e voce (es. 'usanza: cerimonia del commiato', 'festival: festa del solstizio', 'evento: assedio della cittadella').”*
* **Risultato**: una scheda tipologica in `03_societa_e_politica/usi_costumi_ed_eventi/`, allineata con la `10_timeline/` (cronologia e registro occorrenze).

### 4.11 `timeline-markwhen` — Timeline Grafiche

* **Quando**: vuoi creare, aggiornare, validare o esportare i sorgenti Markwhen della timeline.
* **Come**: `/timeline-markwhen` con un'operazione — `crea-mw`, `aggiorna-mw`, `valida-mw` o `esporta-mw` (es. *“crea-mw epoca: Prima Era”*, *“aggiorna-mw campagna: Cronache del Nord”*).
* **Risultato**: sorgenti `.mw` in `10_timeline/markwhen/` (`timeline_generale.mw`, `epoche/`, `campagne/`) mantenuti in sincronia con cronologia, registro occorrenze e verbali; esportazioni renderizzate in `10_timeline/esportazioni/`.

### 4.12 `collega-nomi-propri` — Nomi Propri Collegati

* **Quando**: vuoi verificare o ripristinare la regola che ogni nome proprio è un link al file `.md` canonico dell'entità.
* **Come**: `/collega-nomi-propri` — *“Percorso del file o della cartella da scansionare (oppure 'intero archivio').”*
* **Risultato**: una tabella dei nomi non collegati con conversione in link proposta o applicata, e segnalazione delle entità prive di scheda.

---

## 5. Flussi di Lavoro Tipici

### A. Impostare un Mondo Nuovo

`init-mondo` (intervista guidata) → `valida-struttura` (controllo di sanità) → aggiungi le prime schede di lore → `sincronizza-bibbia-struttura` (`genera-Bibbia`, `genera-struttura-json`) quando vuoi i documenti master.

### B. Dopo una Sessione di Gioco (il Ciclo Principale)

1. `verbale-sessione` — incolla gli appunti (o “inizia intervista”); il verbale viene salvato e l'indice campagna aggiornato.
2. L'Archivista elenca ogni file impattato e prepara gli aggiornamenti incrociati (dossier, schede PNG, indici): approvali uno a uno.
3. Nuova usanza/festival/evento menzionato? → `usanza-festa-evento` propone la scheda; le ricorrenze di eventi già noti vengono registrate nella `10_timeline/`.
4. `timeline-markwhen` (`aggiorna-mw`, o `crea-mw` per nuove campagne/epoche) mantiene i sorgenti `.mw` in sincronia.
5. Se la sessione ha modificato la lore canonica → `sincronizza-bibbia-struttura` (`aggiorna-bibbia`, `aggiorna-struttura-json`).
6. I badge mostrano già cosa è cambiato (`Modificato` > `Verificato`): la tua prossima revisione parte da lì.

### C. Aggiungere Contenuti Tra una Sessione e l'Altra

PG/PNG → `dossier-personaggio` · Manufatto → `oggetto-magico` · Usanza/festival/evento → `usanza-festa-evento` · Grande riordino → `valida-struttura`.

### D. Un Passaggio di Revisione / Audit

`stato-revisione` (vedi cosa è obsoleto) → `audit-passo-passo` o `audit-file-intero` sui bersagli → `stato-revisione` di nuovo per aggiornare la dashboard.

---

## 6. Risoluzione dei Problemi

* **L'agente o le skill non compaiono in VS Code** — i file devono trovarsi alla **radice del workspace**: `.github/agents/` e `.agents/skills/`. Ricarica la finestra e riapri la selezione agenti.
* **Claude Code non rileva le skill** — copia o crea un symlink di `.agents/skills/*` in `.claude/skills/`; `CLAUDE.md` importa già `AGENTS.md`.
* **Non compare nessuna finestra di domande strutturate** — è normale fuori da VS Code: l'Archivista ripiega sulla chat testuale e pone le stesse domande come testo.
* **`esporta-mw` non riesce a renderizzare** — installa la CLI Markwhen (`npx @markwhen/mw`) oppure usa l'estensione Markwhen per VS Code / `markwhen.com`; le esportazioni sono opzionali e non bloccano mai i sorgenti `.mw`.
* **L'assistente ha inventato lore** — viola la regola aurea: riconducilo ad `AGENTS.md`, elimina il testo inventato ed esegui un `audit-passo-passo` sulla sezione colpita.
* **I segnaposto si accumulano** — cerca `[DA_DEFINIRE_MASTER:` e risolvili durante un audit, oppure chiedi all'Archivista di elencarli tutti.
* **Contenuti in lingue miste in un repo** — installa un solo pacchetto di lingua per mondo; elimina i file dell'altro pacchetto ed esegui di nuovo `valida-struttura`.
* **Nomi di cartella legacy** (`06_location/`, `07_factions/`, …) — nessun problema: l'Archivista si adatta a ciò che esiste. Sono fissi solo i *ruoli* dei dieci tomi, non le grafie.

---

## 7. FAQ

* **Mi servono tutte e 12 le skill?** No. Installale tutte (sono autosufficienti) e usa solo ciò che ti serve.
* **Posso gestire più campagne in un mondo?** Sì — `09_cronache/campagne/<nome>/` mantiene separati i verbali di ogni campagna; la lore condivisa vive negli altri tomi.
* **Posso usarlo per campagne a pagamento, stream o actual play?** Sì. La clausola non commerciale riguarda la vendita del toolkit stesso, mai i giochi che conduci con esso.
* **Posso ripacchettizzare o vendere le skill?** No — CC BY-NC-SA 4.0 (vedi `LICENSE` sul branch `main`).
* **Come aggiorno a una nuova release?** Riclona (o `git pull`) il branch di lingua e ricopia i file; reintegra eventuali personalizzazioni locali di `AGENTS.md`.
* **Dove segnalo bug o scoperte sugli harness?** GitHub Issues — vedi `CONTRIBUTING.md` sul branch `main`.

---

*DMs_Companion è gratuito da usare e condividere sotto CC BY-NC-SA 4.0. Se ti fa risparmiare tempo di preparazione, puoi supportare il progetto tramite [GitHub Sponsors](https://github.com/sponsors/Jollyproxi) o [Buy Me a Coffee](https://buymeacoffee.com/jollyproxi) — del tutto opzionale.*
