---
name: valider-structure
description: "Use when: vérifier l'intégrité structurelle du dépôt d'un monde D&D, détecter les dossiers manquants, les index README absents, les liens Markdown rompus et les fichiers mal placés."
argument-hint: "Exécute le contrôle de conformité structurelle de l'archive"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Validation de la Structure du Monde (`valider-structure`)

Cette compétence réalise un audit diagnostique approfondi de l'arborescence des fichiers du dépôt, vérifiant sa conformité à l'architecture standard D&D et signalant rapidement toute anomalie technique.

---

## 1. Critères de Vérification Diagnostique

La compétence contrôle les quatre piliers de l'intégrité structurelle :

### A. Conformité des Dix Tomes
Vérifie la présence des répertoires canoniques (en acceptant les variantes équivalentes déjà établies dans un dépôt existant) :
1. `01_cosmologie`
2. `02_geographie`
3. `03_societe_et_politique` (avec sous-dossier `coutumes_fetes_et_evenements/` contenant `coutumes/`, `fetes_et_occurrences/`, `evenements/`)
4. `04_droit_et_succession`
5. `05_personnages` (avec sous-dossiers `Joueurs/` et `Non_Joueurs/`)
6. `06_lieux`
7. `07_factions`
8. `08_objets_magiques_singuliers`
9. `09_chroniques` (avec sous-dossier `campagnes/`)
10. `10_chronologie` (avec sous-dossiers `chronologie_historique/`, `registre_occurrences/`, `markwhen/`, `calendrier/`, `exportations/`)

### B. Présence et Validité des Index (`README.md`)
Vérifie que chaque dossier principal et sous-dossier contient un fichier `README.md` opérationnel servant de portail et d'index de section.

### C. Détection des Liens Markdown Rompus
Analyse les liens relatifs dans les fichiers `.md` (ex. `[Nom](../../05_personnages/...)`) afin de vérifier que les fichiers cibles existent sur le disque, en signalant les chemins invalides ou renommages non synchronisés.

### D. Fichiers Orphelins ou Mal Placés
Repère les fichiers `.md` enregistrés à la racine du projet ou dans des emplacements non canoniques qui devraient se trouver dans l'un des dix tomes (à l'exception des fichiers maîtres canoniques de la racine tels que `README.md`, `AGENTS.md`, `CLAUDE.md`, `BIBLE_DE_L_UNIVERS.md`, `STATUT_REVISION.md`). Pour la validation syntaxique et croisée des sources `.mw` dans `10_chronologie/markwhen/`, s'intègre avec la compétence `timeline-markwhen` (`valider-mw`).

---

## 2. Procédure Opératoire

1. **Analyse du Système de Fichiers** :
   - Inspectez les dossiers et les fichiers `.md` présents dans l'espace de travail en excluant les répertoires techniques (`.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Exécution des Tests A–D** :
   - Validez les dossiers des 10 tomes (y compris les sous-dossiers de `coutumes_fetes_et_evenements/` et `10_chronologie/`).
   - Repérez les `README.md` manquants.
   - Analysez les liens `[Texte](chemin)` et vérifiez l'existence du fichier cible via le chemin relatif.
   - Inspectez la racine pour détecter d'éventuels fichiers orphelins.
3. **Production du Rapport Diagnostique** :
   - Présentez au MJ un récapitulatif synthétique :
     - 🟢 **Conformité de l'Arborescence** : [OK / Alertes sur tomes manquants]
     - 🟢 **Couverture des Index README** : [OK / Liste des dossiers dépourvus d'index]
     - 🔗 **Intégrité des Liens** : [OK / Liste des liens brisés avec fichier et ligne]
     - 📂 **Emplacement des Fichiers** : [OK / Fichiers orphelins à déplacer]
4. **Proposition de Réparation Automatique** :
   - Si des anomalies sont détectées, demandez au MJ (à l'aide de l'outil de questions structurées de l'environnement comme `vscode_askQuestions` / `AskUserQuestion` si disponible, sinon dans le chat) la marche à suivre :
     - `Réparer automatiquement les anomalies (générer les README manquants et corriger les chemins)`
     - `Afficher uniquement le rapport sans modifier de fichiers`
