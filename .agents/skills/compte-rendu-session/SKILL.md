---
name: compte-rendu-session
description: "Use when: rédiger un compte rendu de séance D&D, mener l'entretien post-séance avec le MJ, établir le procès-verbal officiel avec diagramme Mermaid des accroches PJ et mettre à jour l'index de campagne."
argument-hint: "Collez vos notes de séance ou écrivez 'démarrer entretien' pour lancer la procédure guidée"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Compte Rendu de Séance (`compte-rendu-session`)

Cette compétence encadre la collecte, la structuration et la mise en forme des comptes rendus de séance pour toute campagne D&D, en garantissant la conformité au modèle standard documenté dans [modele-compte-rendu](./references/modele-compte-rendu.md).

---

## 1. Règle d'Or (Zéro Hallucination)

- **Fidélité Absolue** : N'inventez jamais de PNJ, dialogues, lieux ou éléments d'intrigue non décrits par le MJ.
- **Lacunes** : S'il manque des précisions essentielles (ex. nom d'un PNJ ou issue d'un affrontement), demandez-les pendant l'entretien ou signalez-les avec `[A_DEFINIR_MJ: description]`.

---

## 2. Modes de Collecte des Données

### Canal A : Entretien Guidé Post-Séance
Déclenché par *« démarrer entretien »* ou juste après une partie. Posez les questions de manière structurée (en utilisant l'outil interactif de l'environnement tel que `vscode_askQuestions` ou `AskUserQuestion` s'il est disponible, sinon directement dans le chat) :
1. **`coordonnees_session`** : *Numéro de la séance, date en jeu et théâtre géographique des événements ?* (Champ libre avec invite concise).
2. **`pj_presents`** : *Quels Personnages Joueurs étaient présents ?*
   - Options à sélection multiple issues des dossiers recensés dans `05_personnages/Joueurs/<nom_campagne>/` (avec champ libre pour nouveaux PJ ou PNJ majeurs).
3. **`chronologie_evenements`** : *Que s'est-il passé dans l'ordre (ouverture, temps forts, affrontements/négociations, épilogue) ?* (Champ libre).
4. **`accroches_revelations`** : *Quelles découvertes, indices ou tournants ont touché plus particulièrement chaque PJ ?* (Champ libre servant à générer le diagramme Mermaid).
5. **`donnees_mecaniques`** : *Y a-t-il des éléments mécaniques ou ressources à consigner ?*
   - Options : *Aucun (narration seule)*, *Monnaie & Dépenses*, *Objets magiques / Butin*, *Blessures permanentes, états ou dettes* (avec saisie détaillée si sélectionné).

### Canal B : Mise en Forme de Notes Brutes
Si le MJ colle des notes désordonnées, extrayez la chronologie, isolez les faits avérés et rédigez directement le brouillon. S'il manque des informations critiques, demandez uniquement de combler ces lacunes (via l'outil de questions structurées si disponible, ou dans le chat) avant d'enregistrer le fichier.

---

## 3. Rédaction du Compte Rendu

Le compte rendu est structuré selon les sections canoniques :
1. **En-tête** : Données techniques et liens Markdown relatifs vers les dossiers des PJ et des lieux.
2. **Synopsis des Événements** : Registre notarial formel à la troisième personne, fluide et chronologique.
3. **Les Accroches des Protagonistes** :
   - Diagramme Mermaid `flowchart TD` reliant l'événement pivot ou la menace aux différents PJ.
   - Sous-sections par PJ décrivant l'élément révélé/obtenu et son impact narratif.
4. **Phases Saillantes** : Liste numérotée synthétique pour consultation rapide en cours de jeu.
5. **Journal Mécanique (Optionnel)** : Inclus uniquement sur demande expresse.

---

## 4. Archivage et Propagation

1. **Enregistrement du Fichier** :
   Enregistrez sous `09_chroniques/campagnes/<nom_campagne>/sessions/XX_titre_session.md`.
2. **Mise à Jour de l'Index de Campagne** :
   Ajoutez la nouvelle ligne au tableau synoptique dans `09_chroniques/campagnes/<nom_campagne>/README.md` :
   `| **XX** | [Titre] | [Date] | [Lieu] | [Axe Principal] | [Compte rendu](sessions/XX_titre.md) |`
3. **Propositions de Mises à Jour Croisées (A + B)** :
   - Listez en fin de réponse tous les fichiers du dépôt impactés (nouveaux PNJ, objets magiques découverts, accroches à actualiser dans les dossiers PJ via `dossier-personnage`).
   - **Coutumes, fêtes et événements** : si la séance introduit ou mentionne une nouvelle coutume, fête/occurrence récurrente ou événement ponctuel, **proposez systématiquement** la création de sa fiche dans `03_societe_et_politique/coutumes_fetes_et_evenements/` via `coutume-fete-evenement`.
   - **Occurrences d'événements déjà recensés & Frise Markwhen** : si la séance met en scène une récurrence connue (ex. un tournoi annuel ou une fête saisonnière) ou introduit des événements datés, documentez-les dans le compte rendu et consignez-les dans `10_chronologie/` (registre des occurrences et sources `.mw` via `timeline-markwhen`), puis **demandez au MJ** s'il faut modifier la fiche canonique : les particularités propres à cette occurrence restent dans la chronologie et le compte rendu, et la fiche n'est modifiée que si elles en changent la nature.
   - Affichez les modifications proposées et offrez de les appliquer après confirmation.
