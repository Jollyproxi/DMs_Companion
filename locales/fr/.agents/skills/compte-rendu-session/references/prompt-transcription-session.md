# Prompt de Transcription de Séance (NotebookLM / LLM)

Utilisez ce prompt dans **NotebookLM** (ou un autre LLM capable de traiter des enregistrements audio ou des transcriptions longues) pour extraire un rapport notarié avant de transmettre le résultat à l'**Archiviste de Campagne** (`compte-rendu-session`) :

1. Importez dans le carnet l'enregistrement audio ou la transcription brute de la séance (éventuellement répartie en plusieurs fichiers).
2. *(Optionnel)* Importez une courte liste textuelle contenant uniquement l'orthographe exacte des noms propres déjà connus (PJ, PNJ, lieux récurrents) afin de réduire les `[?]` — vous pouvez la générer directement depuis votre archive avec la compétence `glossaire-transcription`.
3. Copiez et collez le bloc ci-dessous dans le chat. Si la séance est longue et que le modèle s'arrête avec `[CONTINUER DEPUIS : Section X / HH:MM:SS]`, demandez-lui de reprendre à partir de ce point jusqu'à achever la **Section 12 (Couverture)**.
4. Collez ou enregistrez le rapport complet puis lancez `/compte-rendu-session` (Canal C) pour rédiger le compte rendu canonique et proposer les mises à jour croisées.

---

````markdown
# TÂCHE
Vous recevez la transcription (ou l'enregistrement) d'une séance de jeu de rôle.
Produisez un rapport structuré et fidèle de ce qui a été dit et fait.
Vous ne connaissez NI l'univers, NI les personnages, NI les règles de la campagne,
NI qui parle : tout ce que vous savez se trouve dans la source. Si un glossaire ou
une liste de noms fournie par le MJ figure aussi parmi les sources, utilisez-la
uniquement pour l'orthographe des noms propres, sans importer de faits ni d'éléments
d'historique absents de la séance.
Votre sortie sera relue et réorganisée par une autre personne : vous ne devez pas
interpréter, vous devez restituer.

# RÈGLES
1. Uniquement ce qui est dans la source. Aucune déduction présentée comme un fait :
   `(inférence)` n'est admis que pour un raccord technique évident (ex. locuteur ou
   pronom manifeste), jamais pour des intentions, causes ou éléments d'intrigue
   non explicités.
2. Ne corrigez pas, ne traduisez pas et ne « normalisez » pas arbitrairement les noms
   propres : reportez-les tels qu'ils sont prononcés (sauf orthographe attestée dans
   le glossaire du MJ). Graphie incertaine → `Nom[?]`. Mot ou passage inaudible →
   `[incompréhensible 00:12:34]`.
3. Attribuez chaque action à celui ou celle qui l'a accomplie, en utilisant le nom
   du personnage s'il est dit, sinon celui du joueur. En `NARRATION`, distinguez les
   descriptions objectives du MJ des déclarations en jeu de PNJ ou PJ (ex.
   `« <PNJ> affirme que … »`), sans transformer les propos d'un personnage en faits
   objectifs du monde.
4. Distinguez toujours trois registres sans jamais les mélanger :
   - `NARRATION` = fiction, ce qui se passe dans l'univers (toujours inclus dans la
     Chronologie)
   - `TABLE` = règles, jets, initiative, discussions mécaniques (inclus dans la
     Chronologie uniquement s'il détermine un résultat mécanique important ou une
     décision de règle/campagne)
   - `HORS JEU` = blagues, pauses, logistique, sujets personnels (exclu de la
     Chronologie ; à signaler uniquement dans Couverture, ou dans Fiche s'il concerne
     absences ou logistique)
5. Dialogues : ne les réécrivez pas. Citez textuellement entre guillemets, avec
   horodatage, en attribuant un identifiant séquentiel (`[C1]`–`[C20]`, 20 citations
   maximum) selon cette priorité : pactes/serments/menaces → révélations/indices →
   décisions → noms/chiffres. N'écrivez chaque citation textuelle qu'une seule fois
   dans la section 4 sous l'élément principal concerné, et renvoyez-y par son code
   (`[C#]`) sous les autres éléments concernés.
6. N'inventez pas de titres, thèmes, causes ou motivations. Ce qui n'est pas dit
   reste non dit. Ne comblez pas les manques par la logique narrative.
7. Multi-sources et horodatage : si plusieurs fichiers de séance figurent dans le
   carnet, préfixez chaque horodatage par le nom de la source (ex.
   `[Partie1 00:12:34]`). Si la source ne contient pas d'horodatage, n'en inventez
   jamais : écrivez `[sans horodatage]` (ou le repère présent, ex. `[partie 2]`).
8. Anti-troncature : si la transcription est longue et que vous approchez de la
   limite de réponse, ne résumez pas et n'omettez aucun événement ; terminez à la
   fin d'une section ou d'une ligne complète par
   `[CONTINUER DEPUIS : Section X / HH:MM:SS]`.
9. Français, Markdown valide. Utilisez exactement les titres indiqués, dans le même
   ordre. Aucune introduction, aucun commentaire final, aucun jugement.

# SORTIE

## 1. Fiche
Liste à puces : nom de la campagne et numéro de séance (s'ils sont dits) ;
participants et rôle de chacun (avec correspondance `Joueur → PJ` si déclarée) ;
repère temporel réel et/ou en jeu de la séance (s'il est dit) ; point de départ ;
point d'arrivée ; sauts de scène ou de temps repérés ; données de jeu ou
logistique déclarées (niveau, expérience, ressources, absences) — uniquement si
explicites.

## 2. Personnes et entités présentes
| Nom (tel que prononcé) | Joueur / Voix (nom du joueur / MJ / incertain) | Type (PJ / PNJ / créature / groupe / autre / non clair) | En scène (oui / non / seulement cité) | Note en une ligne |

## 3. Chronologie
| # | Horodatage | Où | Qui | Ce qui se passe (3-5 phrases factuelles) | Conséquence immédiate | Registre |
Signalez les discontinuités de temps ou de scène par une ligne de tableau valide :
`| — | <horodatage> | SAUT | — | De <lieu/moment A> à <lieu/moment B> | — | NARRATION |`
Sous le tableau : **Liste sèche** — une ligne par événement, 20 mots maximum chacune.

## 4. Faits par élément
Un bloc pour chaque nom propre cité, du plus présent au moins présent :

### <Nom>
- Type : PJ / PNJ / créature / lieu / faction-institution / objet-artefact / coutume-fête / événement / loi-norme / concept / non clair
- Variantes / alias entendus : liste des graphies phonétiques ou surnoms alternatifs (n'inclure cette ligne que s'il y en a ; en cas de doute sur l'identité commune, gardez-les séparés et signalez-le dans `Questions ouvertes`)
- Faits : liste à puces. Un seul fait par puce, vérifiable, avec horodatage (en distinguant narration du MJ et propos de PNJ/PJ).
- Relations : `<Nom> → <autre nom> : quoi` (une ligne par relation)
- Première mention : horodatage
- Citations : uniquement si présentes selon la règle 5 (`[C#] « ... » (horodatage)` ou renvoi `[C#]`)

Si un élément est seulement nommé sans détail, écrivez :
« nommé uniquement, aucun détail ».

## 5. Changements d'état et indices
| Qui | Catégorie (objet / état-blessure / ressource / indice-révélation / position) | Fait déclaré | Horodatage |
Uniquement des faits explicites (objets acquis/cédés, blessures ou états
persistants, variations de ressources, indices/révélations visant un PJ,
déplacements notables). S'il n'y en a aucun : « Aucun ».

## 6. Engagements
| Qui | Envers qui | Quoi | Condition | Témoins | Horodatage |
Promesses, menaces, pactes, dettes, accords, serments. S'il n'y en a aucun : « Aucun ».

## 7. Chiffres
| Donnée | Valeur | Contexte | Horodatage |
Tout chiffre prononcé : monnaies, prix, dégâts, points de vie, distances,
quantités, âges, dates, pourcentages, durées.

## 8. Temps
| Expression (textuelle) | Contexte / événement associé | Horodatage |
Toute indication temporelle : « hier », « trois jours », « l'an dernier », saisons,
anniversaires, échéances, « il y a longtemps ».

## 9. Questions ouvertes
Liste numérotée. Formulation : « Il n'est pas dit si / qui / quand / pourquoi ... » +
horodatage du moment où l'information serait attendue (incluez les doutes sur
d'éventuelles variantes phonétiques désignant la même entité ou des entités
distinctes).

## 10. Contradictions
Uniquement les incohérences internes à la source : `A affirme X (horodatage)` /
`B affirme Y (horodatage)`. Aucune correction, uniquement le signalement. S'il n'y en
a aucune : « Aucune ».

## 11. Bloc de données
Un unique bloc YAML valide, sans commentaires. N'incluez que les clés ayant un
contenu réel. Gardez les champs descriptifs (`fait`, `faits`) concis (une ligne par
entrée).

```yaml
session:
  campagne: ""
  numero: ""
  reference: ""
  debut: ""
  fin: ""
participants:
  - nom: ""
    joueur_voix: ""
    type: ""
    en_scene: ""
    notes: ""
evenements:
  - ordre: 1
    timestamp: ""
    ou: ""
    acteurs: []
    fait: ""
    consequence: ""
    registre: ""
elements:
  - nom: ""
    type: ""
    variantes: []
    faits: []
    relations: []
    premiere_mention: ""
    citations: []
changements_etat_indices:
  - qui: ""
    categorie: ""
    fait: ""
    timestamp: ""
engagements:
  - qui: ""
    envers: ""
    quoi: ""
    condition: ""
    temoins: []
    timestamp: ""
chiffres:
  - donnee: ""
    valeur: ""
    contexte: ""
    timestamp: ""
temps:
  - expression: ""
    contexte: ""
    timestamp: ""
questions_ouvertes:
  - question: ""
    timestamp: ""
contradictions:
  - affirmation_a: ""
    timestamp_a: ""
    affirmation_b: ""
    timestamp_b: ""
```

## 12. Couverture
| Intervalle | Contenu | Qualité (clair / confus / incompréhensible) |
````
