---
name: audit-etape-par-etape
description: "Use when: mener une révision étape par étape du lore ou des fiches de D&D avec le Maître du Jeu, valider des affirmations isolées (micro-atomique) ou des sections logiques à la demande, et apposer le badge visible de vérification et de modification."
argument-hint: "Précisez le fichier ou le sujet à réviser et la granularité (atomique ou section)"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Audit du Lore Étape par Étape (`audit-etape-par-etape`)

> **Connaissances dans la fiction** — Pour le fait examiné, utilisez la **Consultation** de `connaissances-campagne`. Lorsque le MJ confirme qui connaît le fait, appliquez la **Mise à jour**. Si la compétence est installée mais non détectée, lisez directement son `SKILL.md`. Si elle est absente, poursuivez la procédure habituelle.

Cette compétence guide une révision interactive, méthodique et dénuée d'hallucinations des fichiers, fiches, dossiers ou tomes d'un univers de D&D, en interrogeant le Maître du Jeu (MJ) concept par concept.

> **📌 Règle des Noms Propres Liés** : tout nom propre d'entité de l'univers (PJ, PNJ, factions, maisons, cités, lieux, objets magiques, coutumes, fêtes, événements…) apparaissant dans le texte produit doit être un **lien Markdown** vers le fichier `.md` canonique de l'entité (ex. `[Nom](chemin/relatif/fichier.md)`), jamais un simple texte brut. Exceptions : titres, noms de fichiers, frontmatter, blocs de code, nœuds Mermaid et sources `.mw`. Entité sans fiche : ne l'inventez pas — utilisez `[A_DEFINIR_MJ: fiche manquante pour <Nom>]` et signalez la lacune. Vérification et conversion : compétence `lier-noms-propres`.

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
   - Présentez un seul concept ou une seule section à la fois. Insérez le passage exact et la question dans le formulaire.
   - Dans Codex, utilisez `request_user_input` si l’outil est disponible et autorisé, puis `request_user_input_async` aux mêmes conditions. Dans les autres environnements, utilisez l’équivalent natif. En tant que sous-agent, transmettez la question et les choix au coordinateur si seul le fil principal peut ouvrir le formulaire.
   - Avec `request_user_input`, proposez ces trois choix et indiquez au MJ que le champ libre permet de dicter une correction :
     - `Confirmer (recommandé)` : valider le passage tel quel.
     - `Fichier modifié` : relire le passage modifié par le MJ avant de mettre à jour le badge.
     - `Reporter` : reporter la validation de ce passage.
   - Exception pour `request_user_input_async` et les formulaires équivalents : si l’outil accepte quatre choix, ajoutez `Modifier / Rectifier`. Si le MJ choisit cette option sans donner de correction, demandez-la avant de poursuivre. Si le formulaire est limité à trois choix, utilisez les choix ci-dessus et le champ libre.
   - Utilisez le chat uniquement si le formulaire est indisponible ou interdit, y compris via le coordinateur. Indiquez la raison précise et incluez le passage exact et la question.
   - Attendez la réponse avant d’appliquer les modifications ou les badges. Avec le formulaire asynchrone, gardez le tour ouvert et reprenez au point en attente dès réception de la réponse.

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
