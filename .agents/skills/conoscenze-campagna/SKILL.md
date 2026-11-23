---
name: conoscenze-campagna
description: "Raccogliere e consultare pettegolezzi e dicerie oppure verificare e aggiornare chi conosce un fatto nella fiction."
argument-hint: "Indica un fatto, un PG, un party o una scheda da controllare"
user-invocable: true
disable-model-invocation: false
---

# Conoscenze nella fiction

Crea e consulta le dicerie seguendo [Pettegolezzi e dicerie](references/pettegolezzi_e_dicerie.md). Gestisci le voci del tomo 03 separatamente dai fatti, anche durante consultazione, verbalizzazione e sincronizzazione di Bibbia, JSON e timeline.

## Per i fatti canonici

Lavora nell’archivio del Master e usa le schede canoniche. Il sapere comune è implicito e le righe di conoscenza registrano solo eccezioni.

Su una riga di citazione Markdown sotto il singolo fatto, lascia una riga vuota prima della citazione e, negli elenchi, indentala nella stessa voce.

- `> **Conoscenza:** Solo Master` — Se nessun PG sa il fatto. Eventuali PNG possono saperlo.
- `> **Conoscenza:** Party — [Nome del party](party.md) | PG — [Nome del PG](pc.md)` — Se tutti i PG del party indicato lo sanno. Puoi combinare più party e PG nominati individualmente.
- `> **Conoscenza:** Sapere comune salvo — [Nome del PG](pc.md)` — Per escludere PG specifici dal sapere comune. Gli altri mantengono l’assunzione di sapere comune.

Usa link relativi alle schede o agli indici canonici disponibili. Le tre forme sono alternative. Un’eventuale vecchia etichetta esplicita di sapere comune senza eccezioni si legge come sapere comune e si può rimuovere quando si aggiorna la voce.

## Consultazione

Per «Chi conosce questo fatto?», individua la voce canonica e riporta le assegnazioni o il sapere comune implicito, con le eccezioni registrate. Per «Cosa sa questo PG o party?», mostra le assegnazioni pertinenti e le eccezioni al sapere comune. Per un party distingui le conoscenze del gruppo da quelle dei singoli. Ricava l’appartenenza dai dossier o dagli indici pertinenti. Se fatto, personaggio o appartenenza sono ambigui, chiedi al Master.

## Verifica

Segnala file e fatto per etichette malformate, duplicate, senza un destinatario richiesto, con riferimenti rotti o con categorie incompatibili. I fatti senza riga sono validi. La verifica non modifica i file.

## Aggiornamento

Applica solo quanto confermato dal Master o esplicitato nel verbale confermato. Per nuove scoperte conserva le assegnazioni esistenti e sostituisci Solo Master quando un PG apprende il fatto. Aggiorna la sola riga e il badge di modifica secondo le convenzioni del progetto. Rimuovi la riga quando il fatto torna a ricadere nel sapere comune senza eccezioni.

Le sezioni **Party** e **PG** possono comparire ciascuna da sola. Se un PG apprende un fatto da cui era escluso, rimuovi quel PG dalle eccezioni.
