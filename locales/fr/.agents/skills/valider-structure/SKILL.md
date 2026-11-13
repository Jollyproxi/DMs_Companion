---
name: valider-structure
description: "Use when: vérifier l'intégrité structurelle du dépôt d'un monde D&D, détecter les dossiers manquants, les index README absents, les liens Markdown rompus, les noms propres non liés et les fichiers mal placés."
argument-hint: "Exécute le contrôle de conformité structurelle de l'archive"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Validation de la Structure du Monde (`valider-structure`)

Cette compétence réalise un audit diagnostique approfondi de l'arborescence des fichiers du dépôt, vérifiant sa conformité à l'architecture standard D&D et signalant rapidement toute anomalie technique.

> **📌 Règle des Noms Propres Liés** : tout nom propre d'entité de l'univers (PJ, PNJ, factions, maisons, cités, lieux, objets magiques, coutumes, fêtes, événements…) apparaissant dans le texte produit doit être un **lien Markdown** vers le fichier `.md` canonique de l'entité (ex. `[Nom](chemin/relatif/fichier.md)`), jamais un simple texte brut. Exceptions : titres, noms de fichiers, frontmatter, blocs de code, nœuds Mermaid et sources `.mw`. Entité sans fiche : ne l'inventez pas — utilisez `[A_DEFINIR_MJ: fiche manquante pour <Nom>]` et signalez la lacune. Vérification et conversion : compétence `lier-noms-propres`.

---

## 1. Critères de Vérification Diagnostique

La compétence contrôle les cinq piliers de l'intégrité structurelle :

### A. Conformité des Dix Tomes
Vérifie la présence des répertoires canoniques (en acceptant les variantes équivalentes ou les noms personnalisés choisis par le MJ dans le dépôt) :
1. `01_cosmologie` *(avec éventuels sous-dossiers optionnels personnalisés pour plans/sphères et panthéon/divinités)*
2. `02_geographie` *(avec éventuel sous-dossier `regions/` ou nom personnalisé choisi pour les macro-zones, ex. `provinces/`, `continents/`, `domaines/`)*
3. `03_societe_et_politique` *(avec éventuel sous-dossier optionnel `peuples/` ou nom personnalisé, et sous-dossier obligatoire `coutumes_fetes_et_evenements/` contenant `coutumes/`, `fetes_et_occurrences/`, `evenements/`)*
4. `04_droit_et_lois` *(avec sous-dossiers `01_ordre_juridique_et_sources/` … `10_droit_de_la_guerre_et_aventuriers/`, plus éventuelles branches supplémentaires `11_+` ou sous-dossiers par juridiction)*
5. `05_personnages` *(avec sous-dossiers `<Joueurs>/` [défaut `Joueurs/`, ex. `PJ/`, `Heros/`] organisés par `<Campagne_ou_Groupe>/`, et `<Non_Joueurs>/` [défaut `Non_Joueurs/`, ex. `PNJ/`] avec éventuels sous-dossiers de regroupement optionnels)*
6. `06_lieux` *(avec éventuels sous-dossiers optionnels personnalisés `<groupes_lieux>/` par type ou macro-zone)*
7. `07_factions` *(avec éventuels sous-dossiers optionnels personnalisés `<groupes_factions>/` par type)*
8. `08_objets_magiques_singuliers` *(ou nom personnalisé du Tome VIII, ex. `08_objets_magiques/`, `08_artefacts_et_reliques/`, avec éventuels sous-dossiers optionnels `<categories>/`)*
9. `09_chroniques` *(avec sous-dossier `<campagnes>/` [défaut `campagnes/`, ex. `expeditions/`, `aventures/`, `one_shots/`] et `<sessions>/` [défaut `sessions/`, ex. `journaux/`, `chapitres/`])*
10. `10_chronologie` (avec sous-dossiers `chronologie_historique/`, `registre_occurrences/`, `markwhen/`, `calendrier/`, `exportations/`)

### B. Présence et Validité des Index (`README.md`)
Vérifie que chaque dossier principal et sous-dossier contient un fichier `README.md` opérationnel servant de portail et d'index de section.

### C. Détection des Liens Markdown Rompus
Analyse les liens relatifs dans les fichiers `.md` (ex. `[Nom](../../05_personnages/...)`) afin de vérifier que les fichiers cibles existent sur le disque, en signalant les chemins invalides ou renommages non synchronisés.

### D. Fichiers Orphelins ou Mal Placés
Repère les fichiers `.md` enregistrés à la racine du projet ou dans des emplacements non canoniques qui devraient se trouver dans l'un des dix tomes (à l'exception des fichiers maîtres canoniques de la racine tels que `README.md`, `AGENTS.md`, `CLAUDE.md`, `BIBLE_DE_L_UNIVERS.md`, `STATUT_REVISION.md`). Pour la validation syntaxique et croisée des sources `.mw` dans `10_chronologie/markwhen/`, s'intègre avec la compétence `timeline-markwhen` (`valider-mw`).

### E. Couverture des Noms Propres Liés
Vérifie que tout nom propre d'entité recensée (PJ, PNJ, factions, maisons, cités, lieux, objets magiques, coutumes, fêtes, événements…) apparaît dans le texte sous forme de **lien Markdown** vers le fichier `.md` canonique de l'entité et non comme simple texte brut (règle des noms propres liés, sous réserve des exceptions prévues). L'analyse approfondie et la conversion sont déléguées à la compétence `lier-noms-propres`, dont ce pilier constitue le contrôle diagnostique de surface.

---

## 2. Procédure Opératoire

1. **Analyse du Système de Fichiers** :
   - Inspectez les dossiers et les fichiers `.md` présents dans l'espace de travail en excluant les répertoires techniques (`.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Exécution des Tests A–E** :
   - Validez les dossiers des 10 tomes et leurs sous-dossiers canoniques, optionnels ou personnalisés (`<plans>/`, `<pantheon>/`, `<regions>/`, `peuples/`, `coutumes_fetes_et_evenements/`, `04_droit_et_lois/`, `05_personnages/`, `<groupes_lieux>/`, `<groupes_factions>/`, `<categories>/`, `<campagnes>/<sessions>/` et `10_chronologie/`).
   - Repérez les `README.md` manquants.
   - Analysez les liens `[Texte](chemin)` et vérifiez l'existence du fichier cible via le chemin relatif.
   - Inspectez la racine pour détecter d'éventuels fichiers orphelins.
   - Vérifiez que les noms propres des entités recensées apparaissent comme liens et non comme texte brut (déléguer l'analyse approfondie à `lier-noms-propres`).
3. **Production du Rapport Diagnostique** :
   - Présentez au MJ un récapitulatif synthétique :
     - 🟢 **Conformité de l'Arborescence** : [OK / Alertes sur tomes manquants]
     - 🟢 **Couverture des Index README** : [OK / Liste des dossiers dépourvus d'index]
     - 🔗 **Intégrité des Liens** : [OK / Liste des liens brisés avec fichier et ligne]
     - 🏷️ **Noms Propres Liés** : [OK / Liste des noms non liés avec fichier et ligne]
     - 📂 **Emplacement des Fichiers** : [OK / Fichiers orphelins à déplacer]
4. **Proposition de Réparation Automatique** :
   - Si des anomalies sont détectées, demandez au MJ (à l'aide de l'outil de questions structurées de l'environnement comme `vscode_askQuestions` / `AskUserQuestion` si disponible, sinon dans le chat) la marche à suivre :
     - `Réparer automatiquement les anomalies (générer les README manquants et corriger les chemins)`
     - `Afficher uniquement le rapport sans modifier de fichiers`
