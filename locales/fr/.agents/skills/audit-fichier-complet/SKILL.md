---
name: audit-fichier-complet
description: "Use when: réviser et auditer un document entier, un dossier ou un répertoire D&D en une seule passe, repérer les incohérences, proposer des ajustements et apposer les badges visibles de vérification."
argument-hint: "Chemin du fichier ou dossier à contrôler (ex. 05_personnages/ ou fichier .md unique)"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Audit Complet d'un Document ou Dossier (`audit-fichier-complet`)

Cette compétence permet une révision rapide, globale et cohérente d'un fichier complet ou d'un ensemble de fichiers (dossier thématique) de D&D, idéale lorsque le MJ préfère une vue d'ensemble avec validation par blocs plutôt qu'un questionnaire atomique concept par concept.

> **📌 Règle des Noms Propres Liés** : tout nom propre d'entité de l'univers (PJ, PNJ, factions, maisons, cités, lieux, objets magiques, coutumes, fêtes, événements…) apparaissant dans le texte produit doit être un **lien Markdown** vers le fichier `.md` canonique de l'entité (ex. `[Nom](chemin/relatif/fichier.md)`), jamais un simple texte brut. Exceptions : titres, noms de fichiers, frontmatter, blocs de code, nœuds Mermaid et sources `.mw`. Entité sans fiche : ne l'inventez pas — utilisez `[A_DEFINIR_MJ: fiche manquante pour <Nom>]` et signalez la lacune. Vérification et conversion : compétence `lier-noms-propres`.

---

## 1. Règles de Révision

- **Détection des Incohérences** : Comparez les affirmations du document avec la cosmologie et les chroniques de l'espace de travail (ex. dates, noms de maisons, hiérarchies de faction) afin de signaler tout conflit éventuel au MJ.
- **Interdiction de Réécrire Sans Accord** : Présentez toujours le bilan et les propositions de correction avant de modifier le fichier.
- **Respect de la Structure** : Respectez la modularité de l'espace de travail (cosmologie, géographie, politique, droit, personnages, lieux, factions, objets, chroniques, coutumes-fêtes-événements, chronologie).

---

## 2. Syntaxe de la Balise de Vérification (Badge Visible)

Chaque section principale ou fiche validée reçoit le badge Markdown standard :

```markdown
> 🛡️ *Vérifié : AAAA-MM-JJ | Modifié : AAAA-MM-JJ*
```

Si le fichier est découpé en sections thématiques (`## Titre`), placez le badge juste sous le titre de chaque section validée.

---

## 3. Procédure Opératoire

1. **Analyse du Document ou du Dossier** :
   - Lisez le fichier (ou listez les fichiers du dossier désigné).
   - Extrayez la carte conceptuelle : entités impliquées, faits narratifs et liens avec le reste du monde.

2. **Présentation du Bilan d'Audit** :
   - Soumettez au MJ une synthèse structurée :
     - **Fichier Examiné** : Chemin du fichier.
     - **Points Forts / Canon Reconnu** : Liste des faits cohérents.
     - **Éventuelles Incohérences ou Zones d'Ombre** : Signalez les contradictions ou champs `[A_DEFINIR_MJ]`.
     - **Ébauche des Modifications Proposées** : Présentez les rectifications suggérées s'il y en a.

3. **Validation par le MJ** :
   - Demandez confirmation au MJ (à l'aide de l'outil de questions structurées de l'environnement comme `vscode_askQuestions` ou `AskUserQuestion` s'il est disponible, sinon directement dans le chat) avec des options claires :
     - `Tout approuver et appliquer les badges 🛡️` (recommandé en l'absence d'incohérence)
     - `Demander des rectifications précises` (permet de saisir les corrections en texte libre)
     - `Annuler l'audit / Aucune modification`

4. **Application des Balises** :
   - Après confirmation, appliquez les modifications et apposez les badges `> 🛡️ *Vérifié : [DATE_DU_JOUR] | Modifié : [DATE_DU_JOUR]*` sur chaque section validée.

5. **Actualisation du Tableau de Bord** :
   - Appelez la compétence `statut-revision` pour actualiser la synthèse globale dans `STATUT_REVISION.md`.
