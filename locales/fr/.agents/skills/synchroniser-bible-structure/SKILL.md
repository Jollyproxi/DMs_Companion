---
name: synchroniser-bible-structure
description: "Use when: générer ou mettre à jour la Bible de l'Univers (generer-Bible, mettre-a-jour-bible) et structure_univers.json (generer-structure-json, mettre-a-jour-structure-json), synchroniser les modifications du lore entre les modules des dix tomes et les documents maîtres."
argument-hint: "Précisez l'opération : generer-Bible, generer-structure-json, mettre-a-jour-bible, ou mettre-a-jour-structure-json"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Synchronisation du Canon Maître (`synchroniser-bible-structure`)

Cette compétence régit le cycle de vie des deux artefacts maîtres du monde D&D :
1. **La Bible de l'Univers** (`BIBLE_DE_L_UNIVERS.md` ou éventuel document maître monolithique déjà présent) : le texte unique continu permettant la lecture narrative de l'ensemble du canon.
2. **Le Schéma Structurel** (`structure_univers.json`) : la carte ontologique et taxonomique lisible par machine des dix tomes, modules, régions/sous-dossiers et concepts clés.

La compétence gère la génération complète et l'alignement incrémental bidirectionnel entre les fichiers modulaires des dix tomes et les documents maîtres, en garantissant une fidélité stricte au canon sans altération non approuvée par le MJ.

Consultez les documents de référence associés :
- [format-structure-json](./references/format-structure-json.md) : standard du schéma JSON, champs obligatoires et extraction des concepts.
- [conventions-bible](./references/conventions-bible.md) : règles de transposition des titres, ordre de compilation et mise en forme des tableaux.

---

## Matrice des Opérations Prises en Charge

| Argument / Commande | Artefact Cible | Mode | Objectif Principal |
| :--- | :--- | :--- | :--- |
| **`generer-Bible`** | `BIBLE_DE_L_UNIVERS.md` | Monolithique / Intégral | Compile tous les fichiers des 10 tomes en un unique document narratif maître. |
| **`generer-structure-json`** | `structure_univers.json` | Inventaire Complet | Scanne l'arborescence des tomes et génère le JSON taxonomique à partir de zéro. |
| **`mettre-a-jour-bible`** | `BIBLE_DE_L_UNIVERS.md` | Incrémental / Delta | Met à jour dans la Bible uniquement les sections correspondant aux modules modifiés. |
| **`mettre-a-jour-structure-json`** | `structure_univers.json` | Incrémental / Delta | Synchronise le JSON avec les modules ajoutés, renommés ou modifiés. |

> **📌 Règle des Noms Propres Liés** : tout nom propre d'entité de l'univers (PJ, PNJ, factions, maisons, cités, lieux, objets magiques, coutumes, fêtes, événements…) apparaissant dans le texte produit doit être un **lien Markdown** vers le fichier `.md` canonique de l'entité (ex. `[Nom](chemin/relatif/fichier.md)`), jamais un simple texte brut. Exceptions : titres, noms de fichiers, frontmatter, blocs de code, nœuds Mermaid et sources `.mw`. Entité sans fiche : ne l'inventez pas — utilisez `[A_DEFINIR_MJ: fiche manquante pour <Nom>]` et signalez la lacune. Vérification et conversion : compétence `lier-noms-propres`.

---

## 1. Procédure : `generer-Bible` (Compilation Maîtresse)

Utilisez cette procédure pour régénérer ou créer `BIBLE_DE_L_UNIVERS.md` à partir de zéro en assemblant les modules individuels.

### Étapes Opératoires :
1. **Détection du Fichier Cible** :
   - Recherchez à la racine de l'espace de travail un fichier maître existant (ex. `BIBLE_DE_L_UNIVERS.md` ou document équivalent déjà nommé dans le dépôt).
   - S'il n'en existe aucun, créez `BIBLE_DE_L_UNIVERS.md`.
2. **Détermination de l'Ordre des Tomes** :
   - Lisez `structure_univers.json` s'il existe pour récupérer l'ordre officiel des tomes et des modules.
   - Sinon, triez les répertoires à préfixe numérique : `01_cosmologie`, `02_geographie` (y compris `regions/` trié numériquement), `03_societe_et_politique` (y compris `coutumes_fetes_et_evenements/` : `coutumes/` = 3.5.x, `fetes_et_occurrences/` = 3.6.x, `evenements/` = 3.7.x), `04_droit_et_lois` (ou variante historique `04_droit_et_succession` ; avec branches `01_ordre_juridique_et_sources/` … `10_droit_de_la_guerre_et_aventuriers/` = 4.1.x … 4.10.x), `05_personnages` (`Non_Joueurs/`), `06_lieux`, `07_factions`, `08_objets_magiques_singuliers`, `09_chroniques`, `10_chronologie` (`chronologie_historique/` = 10.1.x, `registre_occurrences/` = 10.2.x, `calendrier/` = 10.3.x ; les sources `.mw` de `markwhen/` et `exportations/` sont exclues de la Bible).
3. **Composition du Texte Monolithique** :
   - Insérez l'en-tête canonique avec métadonnées et badge d'état :
     ```markdown
     ### BIBLE DE L'UNIVERS : [NOM_UNIVERS]
     
     > 📜 **Document Maître Monolithique du Canon**
     > *Version du Canon :* [VERSION] | *Dernière Compilation :* [DATE_DU_JOUR]
     > 🛡️ *Vérifié : [DATE_V] | Modifié : [DATE_DU_JOUR]*
     ```
   - Pour chaque tome, insérez un titre H5 (ex. `##### 1. Cosmologie & Architecture Métaphysique`).
   - Pour chaque fichier modulaire, adaptez la hiérarchie des titres comme indiqué dans [conventions-bible](./references/conventions-bible.md) :
     - Le titre H1 du module devient `###### *X.Y Titre du Module*` (ou `### X.Y Titre du Module`).
     - Préservez fidèlement les tableaux Markdown, les diagrammes Mermaid et les encadrés `**NOTE POUR LE MAÎTRE DU JEU :**`.
     - Préservez tous les marqueurs `[A_DEFINIR_MJ]`.
4. **Écriture et Rapport** :
   - Enregistrez le fichier maître compilé.
   - Présentez au MJ un bilan : nombre de tomes traités, fichiers inclus et volume total du document.

---

## 2. Procédure : `generer-structure-json` (Cartographie Taxonomique Complète)

Utilisez cette procédure pour inspecter tous les fichiers de l'espace de travail et produire une carte complète lisible par machine au format JSON.

### Étapes Opératoires :
1. **Collecte des Informations Générales** :
   - Lisez le `README.md` racine ou l'en-tête de la Bible pour extraire `nom_univers`, `description` et déterminer `document_source`.
   - Fixez la version initiale à `"1.0.0"` (ou conservez la version existante le cas échéant).
2. **Analyse Systématique des 10 Tomes** :
   - Parcourez les dossiers de `01_` à `10_` :
     - Extrayez `id`, `code`, `titre` et `description` depuis le `README.md` du tome.
     - Recensez tous les fichiers `.md` modulaires du dossier (hors `README.md`).
     - Pour chaque module `.md` :
       - `id` : slug snake_case issu du nom de fichier sans préfixe numérique.
       - `code` : numérotation hiérarchique (ex. `"1.1"` pour `01_cosmologie/01_structure_planaire.md`).
       - `titre` : extrait du premier titre `#` du fichier.
       - `fichier` : chemin relatif normalisé avec `/`.
       - `concepts_cles` : extrayez 3 à 7 points clés tirés des sous-titres et définitions en gras.
       - `tableaux` : détectez et listez les titres des tableaux Markdown présents.
       - `notes_mj` : extrayez le contenu des éventuelles notes réservées au MJ.
   - Traitez les sous-dossiers canoniques (`02_geographie/regions/`, `03_societe_et_politique/coutumes_fetes_et_evenements/`, `04_droit_et_lois/`, `05_personnages/Non_Joueurs/`, `09_chroniques/campagnes/`, `10_chronologie/` avec les sources `markwhen/`) en renseignant les propriétés dédiées définies dans [format-structure-json](./references/format-structure-json.md).
3. **Validation Syntaxique et Écriture** :
   - Générez `structure_univers.json` indenté à 2 espaces.
   - Vérifiez que le JSON est strictement valide, sans clés dupliquées ni caractères parasites.
   - Communiquez au MJ le récapitulatif du total des modules et sous-structures indexés.

---

## 3. Procédure : `mettre-a-jour-bible` (Synchronisation Incrémentale)

Utilisez cette procédure lorsqu'un ou plusieurs modules atomiques ont été modifiés ou ajoutés, afin d'aligner la Bible monolithique sans régénérer l'intégralité du fichier.

### Étapes Opératoires :
1. **Identification des Fichiers Modifiés** :
   - Repérez les modules cibles désignés par le MJ ou les fichiers dont `Modifié > Vérifié` en inspectant les badges ou `STATUT_REVISION.md`.
2. **Localisation de la Section dans le Fichier Maître** :
   - Ouvrez le fichier maître de la Bible.
   - Pour chaque module modifié, localisez l'ancre de la section via son code hiérarchique (`X.Y`) ou son titre.
3. **Mise à Jour Ciblée de la Section** :
   - Si la section existe : remplacez le texte obsolète par la nouvelle version du module (en adaptant les niveaux de titres selon [conventions-bible](./references/conventions-bible.md)).
   - Si le module est nouveau : insérez la nouvelle section à la position ordinale adéquate dans son tome.
   - Laissez toutes les autres sections strictement intactes.
4. **Actualisation des Métadonnées Maîtresses** :
   - Mettez à jour la ligne de métadonnées en tête :
     `> 🛡️ *Vérifié : [DATE_V] | Modifié : [DATE_DU_JOUR]*`
5. **Rapport d'Alignement** :
   - Listez au MJ les sections mises à jour dans la Bible.

---

## 4. Procédure : `mettre-a-jour-structure-json` (Synchronisation Delta JSON)

Utilisez cette procédure pour garder `structure_univers.json` synchronisé lors de l'ajout, du renommage ou de l'enrichissement de fichiers.

### Étapes Opératoires :
1. **Chargement de l'État Actuel** :
   - Lisez le fichier `structure_univers.json` existant.
2. **Détection du Delta** :
   - Comparez les fichiers physiques sur disque dans les dossiers des 10 tomes avec le contenu du tableau `structure`.
   - Identifiez :
     - ➕ **Modules Ajoutés** : fichiers `.md` sur disque absents du JSON.
     - 🔄 **Modules Modifiés** : fichiers dont le titre, les tableaux ou les concepts clés ont changé.
     - ➖ **Modules Supprimés ou Renommés** : chemins dans le JSON qui n'existent plus sur disque.
3. **Application des Modifications au JSON** :
   - Pour les modules ajoutés : créez le nouvel objet (`id`, `code`, `titre`, `fichier`, `concepts_cles`, `tableaux`, `notes_mj`) et placez-le dans l'ordre.
   - Pour les modules modifiés : actualisez `titre`, `concepts_cles` et `tableaux`, en préservant les éventuelles annotations personnalisées existantes.
   - Pour les modules supprimés/déplacés : mettez à jour `fichier` ou supprimez l'entrée obsolète (après confirmation du MJ avant suppression).
4. **Incrémentation de Version** :
   - Incrémentez la version selon SemVer (ex. `"1.0.0"` → `"1.0.1"` pour des retouches de contenu, ou `"1.1.0"` pour de nouveaux modules/régions).
5. **Sauvegarde et Diff** :
   - Réécrivez `structure_univers.json` formaté.
   - Présentez au MJ le détail des entités ajoutées, actualisées ou supprimées.

---

## Interaction Structurée

Si la compétence est invoquée sans préciser clairement l'opération ou si des conflits surviennent lors d'une mise à jour, demandez au MJ quelle opération lancer (à l'aide de l'outil de questions structurées de l'environnement comme `vscode_askQuestions` / `AskUserQuestion` s'il est disponible, sinon dans le chat) :
- `generer-Bible` — Compile tous les modules des 10 tomes dans le document maître monolithique
- `generer-structure-json` — Régénère intégralement `structure_univers.json` en scannant l'archive
- `mettre-a-jour-bible` — Synchronise dans la Bible uniquement les modules récemment modifiés ou ajoutés
- `mettre-a-jour-structure-json` — Met à jour incrémentalement `structure_univers.json` selon les changements de fichiers

---

## Critères de Qualité & Validation Finale

À l'issue de chaque opération :
1. **Vérification Syntaxique JSON** : Pour toute écriture dans `structure_univers.json`, assurez-vous que le JSON est strictement valide.
2. **Contrôle des Liens et Chemins** : Les chemins `fichier` du JSON et les renvois dans la Bible doivent pointer vers des fichiers existants.
3. **Zéro Hallucination** : N'insérez jamais de concepts, PNJ ou factions absents des fichiers sources ou non approuvés par le MJ.
4. **Intégration avec d'Autres Compétences** :
   - Après des changements structurels majeurs, suggérez d'exécuter `valider-structure`.
   - Après mise à jour de la Bible ou des modules, rappelez d'actualiser le tableau de bord via `statut-revision`.
