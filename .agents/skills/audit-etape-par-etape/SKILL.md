---
name: audit-etape-par-etape
description: "Use when: mener une révision étape par étape du lore ou des fiches de D&D avec le Maître du Jeu, valider des affirmations isolées (micro-atomique) ou des sections logiques à la demande, et apposer le badge visible de vérification et de modification."
argument-hint: "Précisez le fichier ou le sujet à réviser et la granularité (atomique ou section)"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Audit du Lore Étape par Étape (`audit-etape-par-etape`)

Cette compétence guide une révision interactive, méthodique et dénuée d'hallucinations des fichiers, fiches, dossiers ou tomes d'un univers de D&D, en interrogeant le Maître du Jeu (MJ) concept par concept.

---

## 1. Règle Fondamentale de Vérification Factuelle

- **Source de Vérité Absolue** : Le Maître du Jeu est l'unique autorité canonique.
- **Interdiction d'Inventer** : Ne modifiez, ne complétez ni ne déduisez aucun détail de lore non explicitement confirmé par le MJ pendant l'audit.
- **Marqueur d'Incertitude** : Si le MJ hésite sur un élément en cours d'examen, conservez ou insérez `[A_DEFINIR_MJ: description]` sans inventer de réponse.

---

## 2. Granularité de la Révision

Avant de commencer (ou selon la consigne du MJ), fixez la granularité du pas-à-pas :

1. **Niveau 1 : Micro-Atomique (Affirmation Unique / Puce)**
   - Utilisé pour les statistiques de personnages, accroches critiques, dates, secrets du MJ et inventaires d'objets.
   - Chaque ligne ou concept clé est présenté isolément.
2. **Niveau 2 : Section Logique (Bloc Thématique)**
   - Utilisé pour les paragraphes descriptifs, coutumes sociales, chapitres géographiques ou sections narratives (ex. `## Aspect & Facture`, `## 1. Synopsis des Événements`).
   - L'ensemble de la section cohérente est soumis à validation.

---

## 3. Syntaxe de la Balise de Vérification (Badge Visible)

À l'issue de la validation de chaque bloc ou élément, le badge Markdown officiel est apposé :

```markdown
> 🛡️ *Vérifié : AAAA-MM-JJ | Modifié : AAAA-MM-JJ*
```

* **Règles Temporelles** :
  - Lorsque le bloc est validé sans modification : les deux dates coïncident avec la date du jour.
  - Si le bloc fait l'objet d'une modification convenue : les deux dates sont réglées sur la date du jour.
  - Si un agent ou le MJ modifie ultérieurement le texte hors audit : la date `Modifié` avance tandis que `Vérifié` reste intact. Si `Modifié > Vérifié`, le bloc est signalé comme modifié post-audit.

---

## 4. Procédure Opératoire Étape par Étape

1. **Chargement du Fichier** :
   - Utilisez l'outil de lecture pour examiner le fichier indiqué par le MJ.
   - Découpez le document selon la granularité convenue (atomique ou par sections logiques).

2. **Interrogatoire Atomique** :
   - Affichez au MJ un concept ou une section à la fois dans le chat.
   - Si l'environnement dispose d'un outil interactif de questions structurées (ex. `vscode_askQuestions`, `AskUserQuestion`), utilisez-le pour proposer des choix rapides :
     - `Confirmer sans modification` (recommandé)
     - `Modifications déjà effectuées par le MJ dans le fichier source` (le MJ a déjà mis à jour le fichier, il faut actualiser le badge)
     - `Modifier / Rectifier` (ouvre un champ libre pour saisir la correction)
     - `Reporter à plus tard [A_DEFINIR_MJ]`
   - Sinon, posez la question directement dans le chat :
     > **Étape [N/Total] — [Titre de Section ou Concept]**
     > ```markdown
     > [Texte exact extrait du fichier]
     > ```
     > **Question :** *« Confirmez-vous que ce passage est exact et strictement conforme au canon, ou souhaitez-vous le rectifier ou l'enrichir ? »*

3. **Application de la Réponse** :
   - **Si approuvé sans modification** : Ajoutez ou mettez à jour le badge :
     `> 🛡️ *Vérifié : [DATE_DU_JOUR] | Modifié : [DATE_DU_JOUR]*`
   - **Si le MJ dicte des modifications** : Réécrivez le texte en intégrant uniquement les termes ou directives du MJ, puis réglez le badge à la date du jour.
   - **Si le MJ a déjà modifié le fichier** : Ajoutez ou actualisez le badge à la date du jour.
   - **Si reporté** : Ajoutez `[A_DEFINIR_MJ: élément à préciser]` et réglez `Vérifié : NON_VALIDE`.

4. **Persistance & Clôture** :
   - Appliquez les modifications directement sur le fichier via les outils d'édition.
   - Passez à l'étape suivante jusqu'à achèvement du fichier.
   - En fin de fichier, appelez la compétence `statut-revision` pour mettre à jour le tableau de bord `STATUT_REVISION.md`.
