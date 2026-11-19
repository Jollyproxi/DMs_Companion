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

Lorsque le MJ introduit un Personnage Non-Joueur notable :

1. Classez les PNJ par **cadre et lieu principal de référence**, selon leur lien territorial ou narratif stable documenté dans le canon. La première rencontre et la position actuelle sont des données distinctes qui ne déterminent pas automatiquement le classement. Conservez une seule fiche canonique ; factions, campagnes et autres lieux y renvoient par des liens.
2. `05_personnages/<Non_Joueurs>/<Cadre>/<Lieu_reference>/<Nom_PNJ>.md` (default: `05_personnages/Non_Joueurs/<Cadre>/<Lieu_reference>/<Nom_PNJ>.md`).
3. Si le rattachement est ambigu, interrogez le MJ ; en rédaction directe, utilisez `A_DEFINIR_MJ/` au niveau inconnu (cadre ou lieu), sans inventer de liens. Utilisez `Transversaux/` et/ou `Itinerants/` uniquement pour les PNJ explicitement documentés comme tels. Réutilisez les noms canoniques des cadres et lieux et respectez les noms personnalisés des tomes.
4. **Structure** :
   - En-tête avec rôle, faction (lien vers le Tome VII `07_factions/`), résidence (lien vers le Tome VI `06_lieux/`), alignement et statut vital.
   - Sections Apparence & Tempérament, Rôle Narratif et Secrets & Accroches MJ.
   - **Cadre de référence :** [Lien vers la fiche canonique du Tome II]
   - **Lieu principal de référence :** [Lien vers la fiche canonique du Tome VI et motif du lien]
   - **Position actuelle :** [Lien vers le lieu, si connu ; donnée distincte du rattachement principal]
   - **Première rencontre :** [Liens vers le compte rendu et le lieu, si documentés]
5. Créez ou actualisez les `README.md` du tome, des PNJ, du cadre et du lieu ; les index indiquent cadre, lieu principal et lien vers la fiche unique.
6. Pour réorganiser les fiches existantes, préparez une table source → destination fondée sur le canon et appliquez les déplacements autorisés. Recalculez les liens relatifs sortants et actualisez tous les liens entrants (comptes rendus, dossiers, lieux, factions, chronologies), les anciens et nouveaux README, la Bible et le JSON. Ne dupliquez pas les fiches et ne réécrivez pas le lieu historique de première rencontre. Signalez les cas non résolus et vérifiez les liens après déplacement.

---

## 4. Mises à Jour Croisées Post-Séance

Lorsqu'une séance apporte des nouveautés concernant un PJ (ex. nouvelle piste découverte, lien modifié, blessure ou objet obtenu) :
1. Identifiez le module précis à actualiser (ex. `03_relations_et_dynamiques.md` pour un pacte, `05_accroches_et_secrets_mj.md` pour une piste révélée).
2. Appliquez la modification en préservant les informations antérieures.
3. Avancez la date dans `Modifié : [DATE_DU_JOUR]` tout en laissant `Vérifié` inchangé.
