---
name: dossier-personnage
description: "Use when: créer, mettre à jour ou modulariser les dossiers des Personnages Joueurs (PJ) en cinq modules ou les fiches des Personnages Non-Joueurs (PNJ) selon les standards canoniques de la campagne."
argument-hint: "Précisez le type (PJ ou PNJ), le nom du personnage et l'opération (creer, mettre a jour module, fiche)"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Gestion des Dossiers Personnages (PJ & PNJ)

Cette compétence régit la création, la modularisation et l'actualisation méthodique des dossiers des Personnages Joueurs (PJ) et des fiches des Personnages Non-Joueurs (PNJ), en assurant rigueur formelle, liens croisés et respect du canon sans jamais inventer de détails non autorisés par le Maître du Jeu.

Les modèles complets sont consultables dans [modele-dossier](./references/modele-dossier.md).

> **📌 Règle des Noms Propres Liés** : tout nom propre d'entité de l'univers (PJ, PNJ, factions, maisons, cités, lieux, objets magiques, coutumes, fêtes, événements…) apparaissant dans le texte produit doit être un **lien Markdown** vers le fichier `.md` canonique de l'entité (ex. `[Nom](chemin/relatif/fichier.md)`), jamais un simple texte brut. Exceptions : titres, noms de fichiers, frontmatter, blocs de code, nœuds Mermaid et sources `.mw`. Entité sans fiche : ne l'inventez pas — utilisez `[A_DEFINIR_MJ: fiche manquante pour <Nom>]` et signalez la lacune. Vérification et conversion : compétence `lier-noms-propres`.

---

## 1. Règles de Rédaction (Zéro Hallucination)

- **Données Avérées Uniquement** : Ne remplissez que les champs fournis par le MJ ou déjà consignés dans les comptes rendus de séance.
- **Champs Manquants** : Insérez `[A_DEFINIR_MJ: élément manquant]` (ex. sous-classe non encore choisie, divinité tutélaire ou secret du MJ non dévoilé).
- **Interaction Structurée** : Si le MJ fournit des informations partielles pour un nouveau personnage, demandez les données essentielles (Type : PJ ou PNJ ; Campagne cible ; Rôle martial/arcanique/social ; Alignement ou code moral) à l'aide de l'outil de questions structurées de l'environnement (`vscode_askQuestions`, `AskUserQuestion`) s'il est disponible, sinon directement dans le chat.
- **Suivi Temporel** : Chaque fichier ou module créé ou modifié doit comporter le badge d'état :
  `> 🛡️ *Vérifié : AAAA-MM-JJ | Modifié : AAAA-MM-JJ*`
  Si le fichier est modifié à la suite d'une séance, actualisez uniquement la date `Modifié`.

---

## 2. Création d'un Dossier PJ (5 Modules)

Lorsque le MJ introduit ou documente un nouveau Personnage Joueur :

1. **Acquisition Guidée (si nécessaire)** : Confirmez avec le MJ le nom exact, la classe, le niveau et la campagne/groupe d'appartenance.
2. **Création du Dossier** :
   `05_personnages/<Joueurs>/<Campagne_ou_Groupe>/<Nom_PJ>/` *(défaut : `05_personnages/Joueurs/<Campagne>/<Nom_PJ>/`, en respectant les noms personnalisés de l'espace de travail)*
3. **Génération des Fichiers Modulaires** :
   - `README.md` : Portail du personnage avec rôle, traits moraux et index des 5 fichiers.
   - `01_etat_civil_et_traits.md` : Données d'identité, classe, niveau, traits et apparence.
   - `02_historique_integre.md` : Passé, événements fondateurs et racines dans l'univers.
   - `03_relations_et_dynamiques.md` : Liens avec les compagnons, factions et PNJ.
   - `04_equipement_et_capacites.md` : Objets marquants, armes, focaliseurs et capacités uniques.
   - `05_accroches_et_secrets_mj.md` : Pistes réservées au MJ, mystères et révélations.
4. **Structure** :
   - En-tête avec rôle, faction (lien vers le Tome VII `07_factions/`), résidence (lien vers le Tome VI `06_lieux/`), alignement et statut vital.
   - Sections Apparence & Tempérament, Rôle Narratif et Secrets & Accroches MJ.
   - **Mise à Jour des Portails Campagne et Groupe** :
   Ajoutez le nouveau PJ au `README.md` dans `05_personnages/<Joueurs>/<Campagne_ou_Groupe>/README.md` et à l'index général `05_personnages/README.md`.

---

## 3. Création ou Mise à Jour d'une Fiche PNJ

## Convention de l’archive PNJ

Appliquez la convention PNJ du projet. Consultez les instructions du projet et l’index du tome des personnages. Pour un projet existant sans règle explicite, suivez la structure et les index en usage et signalez les conflits ou ambiguïtés au MJ.

Recherchez la fiche existante dans les index, les fichiers et par ses alias éventuels. Conservez un fichier canonique par identité et liez-le depuis les campagnes, factions et autres lieux. Pour les niveaux géographiques ou narratifs, utilisez le lien stable documenté et indiquez son fondement. La première rencontre (lieu et compte rendu) et la position actuelle sont des champs distincts.

Signalez les données à définir et conservez les niveaux confirmés. Utilisez un emplacement provisoire si le projet le prévoit, sinon demandez au MJ de trancher le classement hiérarchique. Utilisez une catégorie itinérante ou transversale si le projet la prévoit et que le canon l’atteste. Dans une archive à plat, consignez ces informations dans la fiche ou l’index selon la convention.

Avant un déplacement autorisé, associez chaque source à sa destination et vérifiez que celle-ci est libre. Actualisez les anciens et nouveaux index, toutes les références entrantes et les liens relatifs sortants. Préservez l’historique de la première rencontre, actualisez les documents dérivés prévus et vérifiez les cibles canoniques des liens et l’unicité de la fiche.

Dante conserve `<Cornice>/<Luogo_riferimento>/<Nome_PNG>.md` sous sa racine PNJ.

Utilisez le [modèle](./references/modele-dossier.md) et actualisez les index prévus.

---

## 4. Mises à Jour Croisées Post-Séance

Lorsqu'une séance apporte des nouveautés concernant un PJ (ex. nouvelle piste découverte, lien modifié, blessure ou objet obtenu) :
1. Identifiez le module précis à actualiser (ex. `03_relations_et_dynamiques.md` pour un pacte, `05_accroches_et_secrets_mj.md` pour une piste révélée).
2. Appliquez la modification en préservant les informations antérieures.
3. Avancez la date dans `Modifié : [DATE_DU_JOUR]` tout en laissant `Vérifié` inchangé.
