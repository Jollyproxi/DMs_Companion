---
name: init-monde
description: "Use when: initialiser un nouveau dépôt d'univers ou de campagne D&D, guider le MJ dans la définition des coordonnées du monde et générer l'architecture modulaire en dix tomes."
argument-hint: "Lance l'entretien pour configurer et générer l'arborescence de l'univers"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Initialisation d'un Monde (`init-monde`)

Cette compétence guide le Maître du Jeu dans la configuration interactive et la génération de l'ossature en dossiers d'un univers fantastique selon l'architecture standard en dix tomes décrite dans [architecture-monde](./references/architecture-monde.md).

> **📌 Règle des Noms Propres Liés** : tout nom propre d'entité de l'univers (PJ, PNJ, factions, maisons, cités, lieux, objets magiques, coutumes, fêtes, événements…) apparaissant dans le texte produit doit être un **lien Markdown** vers le fichier `.md` canonique de l'entité (ex. `[Nom](chemin/relatif/fichier.md)`), jamais un simple texte brut. Exceptions : titres, noms de fichiers, frontmatter, blocs de code, nœuds Mermaid et sources `.mw`. Entité sans fiche : ne l'inventez pas — utilisez `[A_DEFINIR_MJ: fiche manquante pour <Nom>]` et signalez la lacune. Vérification et conversion : compétence `lier-noms-propres`.

---

## 1. Procédure Guidée (Entretien Initial)

Avant de créer des fichiers ou des dossiers, posez au MJ les questions suivantes (en utilisant l'outil de questions structurées de l'environnement, tel que `vscode_askQuestions` ou `AskUserQuestion`, s'il est disponible ; sinon directement dans le chat) :

1. **`nom_premisse`**: *Quel est le nom de l'univers et sa thématique fondamentale ?*
   - Options suggérées ou saisie libre (ex. *High Fantasy Classique*, *Dark Fantasy Gothique*, *Intrigue Politique & Arcanique*, *Autre — préciser*).
2. **`particularites_planaires`**: *Quelles particularités cosmologiques ou quels plans spéciaux caractérisent le monde ?*
   - Options à sélection multiple : *Outreterre / Abysses souterrains*, *Plans liminaux / Brumes*, *Royaumes féeriques ou astraux*, *Sphères célestes / Plans élémentaires*, *Autre (préciser)*.
3. **`factions_cles`**: *Quelles sont les 2–3 factions, maisons nobles ou royaumes dominants au départ ?* (Champ libre).
4. **`campagne_initiale`**: *Souhaitez-vous initialiser dès maintenant une première campagne avec son groupe de PJ ?*
   - Options : *Oui (préciser le nom de la campagne)*, *Non (univers seul pour l'instant)*.
5. **`coutumes_fetes_evenements`**: *Existe-t-il déjà des coutumes du quotidien, des fêtes récurrentes ou des événements historiques à recenser tout de suite ?*
   - Options à sélection multiple : *Coutumes (ex. rituels de salutation/d'adieu)*, *Fêtes/événements récurrents*, *Événements ponctuels (historiques ou en cours)*, *Aucun pour le moment (structure uniquement)*.
   - Les entrées collectées sont cataloguées via la compétence `coutume-fete-evenement` sous `03_societe_et_politique/coutumes_fetes_et_evenements/` et inscrites dans `10_chronologie/`.

---

## 2. Génération de l'Arborescence

Une fois les réponses du MJ reçues, générez la structure modulaire à l'aide des outils d'écriture ou du terminal :

1. **Fichiers Racine** :
   - `README.md` : Index général du monde et sommaire de navigation.
   - `structure_univers.json` : Schéma hiérarchique avec métadonnées, tomes et dossiers.
   - `BIBLE_DE_L_UNIVERS.md` : Document source maître contenant la prémisse convenue.

2. **Les Dix Tomes Fondateurs** :
   - `01_cosmologie/README.md`
   - `02_geographie/README.md` (avec éventuel sous-dossier `regions/` ou dénomination choisie pour les macro-zones)
   - `03_societe_et_politique/README.md` (avec sous-dossier `coutumes_fetes_et_evenements/` contenant `coutumes/`, `fetes_et_occurrences/`, `evenements/`, chacun avec `README.md`)
   - `04_droit_et_succession/README.md`
   - `05_personnages/README.md` (avec sous-dossiers `Joueurs/` et `Non_Joueurs/`, chacun avec `README.md`)
   - `06_lieux/README.md`
   - `07_factions/README.md`
   - `08_objets_magiques_singuliers/README.md`
   - `09_chroniques/README.md` (avec sous-dossiers `campagnes/<nom_campagne>/sessions/`, chacun avec `README.md`)
   - `10_chronologie/README.md` (avec sous-dossiers `chronologie_historique/`, `registre_occurrences/`, `markwhen/` — contenant `README.md`, `chronologie_generale.mw`, `epoques/`, `campagnes/` —, `calendrier/`, `exportations/README.md`)

3. **Initialisation des Fichiers README** :
   Chaque dossier reçoit un `README.md` doté de l'index thématique initial et du badge d'état :
   `> 🛡️ *Vérifié : [DATE_DU_JOUR] | Modifié : [DATE_DU_JOUR]*`

4. **Validation Finale** :
   Une fois la création terminée, appelez la compétence `valider-structure` afin de certifier que l'arborescence est complète et dépourvue de liens brisés.
