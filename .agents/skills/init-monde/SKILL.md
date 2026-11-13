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
6. **`dossier_macro_zones`**: *Comment souhaitez-vous nommer le sous-dossier des régions/macro-zones dans `02_geographie/` ?*
   - Options suggérées ou nom personnalisé (ex. *`regions/`* par défaut, *`provinces/`*, *`continents/`*, *`domaines/`*, *`marches/`*, *Autre — préciser le nom du dossier*).
7. **`sous_dossier_peuples`**: *Souhaitez-vous inclure dans `03_societe_et_politique/` le sous-dossier optionnel dédié aux peuples/espèces ?*
   - Options : *Oui, utiliser le défaut `peuples/`*, *Oui, avec un nom personnalisé (ex. `especes/`, `races/`, `lignees/`, `cultures/`)*, *Non (uniquement si utile plus tard)*.
8. **`personnalisation_avancee`**: *Pour les autres tomes, souhaitez-vous conserver les noms standard ou personnaliser des dossiers / activer des sous-dossiers optionnels ?*
   - Options : *Utiliser les noms et la structure standard* (recommandé), *Personnaliser sur demande* — le cas échéant, demandez au MJ les choix souhaités (parmi : `<plans>/` et `<pantheon>/` dans `01_cosmologie/` ; branches supplémentaires `11_+` ou juridictions dans `04_droit_et_lois/` ; noms `Joueurs/`/`Non_Joueurs/`, regroupement PJ par campagne ou groupe et `<groupes_pnj>/` dans `05_personnages/` ; `<groupes_lieux>/` dans `06_lieux/` ; `<groupes_factions>/` dans `07_factions/` ; nom du Tome VIII `08_...` et `<categories>/` ; `<campagnes>/` et `<sessions>/` dans `09_chroniques/`).

---

## 2. Génération de l'Arborescence

Une fois les réponses du MJ reçues, générez la structure modulaire à l'aide des outils d'écriture ou du terminal :

1. **Fichiers Racine** :
   - `README.md` : Index général du monde et sommaire de navigation.
   - `structure_univers.json` : Schéma hiérarchique avec métadonnées, tomes et dossiers.
   - `BIBLE_DE_L_UNIVERS.md` : Document source maître contenant la prémisse convenue.

2. **Les Dix Tomes Fondateurs** :
   - `01_cosmologie/README.md` (avec éventuels sous-dossiers optionnels `<plans>/`, `<pantheon>/`, chacun avec `README.md`)
   - `02_geographie/README.md` (avec sous-dossier des macro-zones : `regions/` ou le nom personnalisé choisi par le MJ, doté de son `README.md`)
   - `03_societe_et_politique/README.md` (avec éventuel sous-dossier optionnel `peuples/` ou nom personnalisé, et sous-dossier `coutumes_fetes_et_evenements/` contenant `coutumes/`, `fetes_et_occurrences/`, `evenements/`, chacun avec `README.md`)
   - `04_droit_et_lois/README.md` (avec sous-dossiers `01_ordre_juridique_et_sources/`, `02_droits_civils_et_statuts/`, `03_droit_dynastique_et_succession/`, `04_contrats_et_pactes/`, `05_traites_et_diplomatie/`, `06_droit_penal_et_infractions/`, `07_tribunaux_et_procedure/`, `08_droit_arcanique_et_religieux/`, `09_propriete_commerce_et_fiscalite/`, `10_droit_de_la_guerre_et_aventuriers/`, plus éventuelles branches supplémentaires `11_+` ou sous-dossiers par juridiction, chacun avec `README.md`)
   - `05_personnages/README.md` (avec sous-dossiers `<Joueurs>/` [défaut `Joueurs/`] et `<Non_Joueurs>/` [défaut `Non_Joueurs/`], ainsi que `<groupes_pnj>/` optionnel, chacun avec `README.md`)
   - `06_lieux/README.md` (avec éventuels sous-dossiers optionnels `<groupes_lieux>/`, chacun avec `README.md`)
   - `07_factions/README.md` (avec éventuels sous-dossiers optionnels `<groupes_factions>/`, chacun avec `README.md`)
   - `<08_objets_magiques_singuliers>/README.md` (défaut `08_objets_magiques_singuliers/` ou nom personnalisé, avec éventuels sous-dossiers optionnels `<categories>/`, chacun avec `README.md`)
   - `09_chroniques/README.md` (avec sous-dossiers `<campagnes>/<nom_campagne>/<sessions>/` — défaut `campagnes/` et `sessions/` — chacun avec `README.md`)
   - `10_chronologie/README.md` (avec sous-dossiers `chronologie_historique/`, `registre_occurrences/`, `markwhen/` — contenant `README.md`, `chronologie_generale.mw`, `epoques/`, `campagnes/` —, `calendrier/`, `exportations/README.md`)

3. **Initialisation des Fichiers README** :
   Chaque dossier reçoit un `README.md` doté de l'index thématique initial et du badge d'état :
   `> 🛡️ *Vérifié : [DATE_DU_JOUR] | Modifié : [DATE_DU_JOUR]*`

4. **Validation Finale** :
   Une fois la création terminée, appelez la compétence `valider-structure` afin de certifier que l'arborescence est complète et dépourvue de liens brisés.
