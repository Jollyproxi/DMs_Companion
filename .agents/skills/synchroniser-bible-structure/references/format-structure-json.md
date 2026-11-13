# Spécification et Format de `structure_univers.json`

Le fichier `structure_univers.json` constitue la carte ontologique et taxonomique lisible par machine de l'ensemble de l'univers. Il sert d'index structuré pour les agents IA, les outils de visualisation, les scripts de validation et les requêtes rapides.

---

## 1. Schéma Racine du Document

```json
{
  "nom_univers": "Nom de l'Univers",
  "version": "1.0.0",
  "document_source": "BIBLE_DE_L_UNIVERS.md",
  "description": "Synthèse concise des piliers de l'univers en 2 ou 3 phrases.",
  "structure": [
    /* Tableau des 10 tomes canoniques */
  ]
}
```

### Champs Racine
* `nom_univers` *(string)* : Titre officiel de l'univers.
* `version` *(string, SemVer)* : Version courante du canon (ex. `"1.0.0"`). Incrémentée (`patch` pour corrections/ajustements sur des modules existants, `minor` pour ajout de nouveaux modules/régions/factions).
* `document_source` *(string)* : Chemin relatif vers le document maître monolithique de la Bible.
* `description` *(string)* : Présentation générale de l'architecture et de la thématique (cosmologie, société, conflits centraux).
* `structure` *(array)* : Liste ordonnée des objets chapitre/tome (`01` à `10`).

---

## 2. Objet Tome / Chapitre

Chaque élément du tableau `structure` représente l'un des dix tomes de l'architecture :

```json
{
  "id": "cosmologie",
  "code": "01",
  "titre": "Cosmologie & Architecture Métaphysique",
  "dossier": "01_cosmologie",
  "index": "01_cosmologie/README.md",
  "description": "Synthèse des sujets traités dans ce tome.",
  "modules": [
    /* Tableau des fichiers modulaires individuels */
  ]
}
```

### Champs du Tome
* `id` *(string)* : Identifiant unique en snake_case sans préfixe numérique (ex. `"cosmologie"`, `"geographie"`, `"droit_et_lois"`).
* `code` *(string)* : Numéro du tome sur deux chiffres (`"01"`–`"10"`).
* `titre` *(string)* : Titre officiel du tome extrait de son `README.md`.
* `dossier` *(string)* : Nom du répertoire relatif à la racine (ex. `"01_cosmologie"`).
* `index` *(string)* : Chemin relatif vers le fichier `README.md` portail du tome.
* `description` *(string)* : Description du domaine couvert par le tome.
* `modules` *(array)* : Liste des modules appartenant au tome.

---

## 3. Objet Module

Chaque élément du tableau `modules` décrit un fichier `.md` atomique :

```json
{
  "id": "structure_planaire",
  "code": "1.1",
  "titre": "Structure Planaire et Cosmique",
  "fichier": "01_cosmologie/01_structure_planaire.md",
  "concepts_cles": [
    "Plan Matériel et frontières planaires",
    "Sphères célestes et royaumes extérieurs",
    "Profondeurs souterraines et failles anciennes",
    "Plans élémentaires et portails liminaux"
  ],
  "tableaux": [
    "Tableau Synoptique des Plans"
  ],
  "notes_mj": "Détail important pour le MJ (optionnel)"
}
```

### Champs du Module
* `id` *(string)* : Identifiant unique snake_case issu du nom de fichier (sans préfixe numérique ni extension).
* `code` *(string)* : Code hiérarchique décimal (ex. `"1.1"`, `"2.3"`, `"7.8"`).
* `titre` *(string)* : Titre exact du module (correspondant au titre H1 du fichier `.md`).
* `fichier` *(string)* : Chemin relatif du fichier Markdown depuis la racine.
* `concepts_cles` *(array de chaînes)* : 3 à 7 points concis résumant les règles, le lore et les institutions clés introduits dans le module.
* `tableaux` *(array de chaînes, optionnel)* : Intitulés des tableaux Markdown présents dans le document. Omettre ou laisser vide s'il n'y en a aucun.
* `notes_mj` *(string, optionnel)* : Synthèse d'éventuels encadrés `NOTE POUR LE MAÎTRE DU JEU` ou accroches narratives particulières.

---

## 4. Sous-structures Spéciales (Régions, PNJ, Campagnes, Événements, Chronologie)

Pour les tomes dotés de sous-dossiers canoniques :

### A. Tome 02 (Géographie — Sous-dossier `regions/` ou nom personnalisé)
Si un sous-répertoire régional ou de macro-zones existe :
```json
"dossier_regions": "02_geographie/regions",
"index_regions": "02_geographie/regions/README.md",
"modules_regions": [
  {
    "numero": 1,
    "titre": "1re Région — Marche Septentrionale",
    "trait_distinctif": "Climat rigoureux / Frontière minière",
    "fichier": "02_geographie/regions/01_marche_septentrionale.md"
  }
]
```
*(Le nom du sous-dossier et des clés associées est personnalisable : tout dossier choisi pour les macro-zones — ex. `provinces/`, `continents/`, `domaines/` — peut utiliser les clés standard `dossier_regions` / `index_regions` / `modules_regions` ou des clés correspondantes `dossier_<nom>` / `index_<nom>` / `modules_<nom>`.)*

### B. Tome 05 (Personnages — Sous-dossiers `<Joueurs>/` et `<Non_Joueurs>/`)
```json
"sous_dossiers": {
  "joueurs": "05_personnages/Joueurs",
  "non_joueurs": "05_personnages/Non_Joueurs"
}
```
*(Si le MJ personnalise les noms de dossiers — ex. `PJ/`, `PNJ/`, `Heros/`, sous-dossiers de regroupement PNJ ou `<Campagne_ou_Groupe>/` — les chemins consignent les répertoires réels sur disque.)*

### C. Tome 09 (Chroniques — Sous-dossier `<campagnes>/`)
```json
"dossier_campagnes": "09_chroniques/campagnes",
"campagnes_actives": [
  {
    "id": "nom_campagne",
    "index": "09_chroniques/campagnes/nom_campagne/README.md",
    "total_seances": 12
  }
]
```
*(Si `campagnes/` ou `sessions/` utilisent des noms personnalisés — ex. `expeditions/`, `aventures/`, `one_shots/`, `journaux/` — les clés reflètent les chemins réels sur disque.)*

### D. Tome 03 (Société & Politique — Sous-série `coutumes_fetes_et_evenements/` et optionnel `peuples/`)
```json
"dossier_peuples": "03_societe_et_politique/peuples",
"modules_peuples": [
  {
    "id": "peuple_exemple",
    "code": "3.8.1",
    "titre": "Nom du Peuple / Espèce",
    "fichier": "03_societe_et_politique/peuples/01_peuple_exemple.md"
  }
],
"dossier_coutumes_fetes_evenements": "03_societe_et_politique/coutumes_fetes_et_evenements",
"index_coutumes_fetes_evenements": "03_societe_et_politique/coutumes_fetes_et_evenements/README.md",
"modules_coutumes": [
  {
    "id": "ceremonie_adieu",
    "code": "3.5.1",
    "titre": "La Cérémonie d'Adieu",
    "fichier": "03_societe_et_politique/coutumes_fetes_et_evenements/coutumes/01_ceremonie_adieu.md"
  }
],
"modules_fetes_occurrences": [
  {
    "id": "tournoi_garde",
    "code": "3.6.1",
    "titre": "Le Tournoi de la Garde",
    "fichier": "03_societe_et_politique/coutumes_fetes_et_evenements/fetes_et_occurrences/01_tournoi_garde.md",
    "periodicite": "variable",
    "declencheur": "Retour d'expéditions militaires ou renouvellement des rangs"
  }
],
"modules_evenements": [
  {
    "id": "siege_citadelle",
    "code": "3.7.1",
    "titre": "Le Siège de la Citadelle",
    "fichier": "03_societe_et_politique/coutumes_fetes_et_evenements/evenements/01_siege_citadelle.md",
    "statut_occurrence": "acheve"
  }
]
```
* `periodicite` *(string, optionnel)* pour les fêtes : `"fixe"`, `"variable"` ou `"mixte"`.
* `declencheur` *(string, optionnel)* : conditions de déclenchement de l'événement récurrent.
* `statut_occurrence` *(string, optionnel)* pour les événements : `"planifie"`, `"en_cours"` ou `"acheve"`.

### D2. Tome 04 (Droit & Lois — Sous-dossiers `01_` … `10_`)
```json
{
  "id": "droit_et_lois",
  "code": "04",
  "titre": "Droit et Lois",
  "dossier": "04_droit_et_lois",
  "index": "04_droit_et_lois/README.md",
  "description": "Ordre juridique, droits civils, succession, contrats, traités, pénal, tribunaux, droit arcanique, fiscalité et droit de la guerre.",
  "modules": [],
  "branches": [
    {
      "id": "ordre_juridique_et_sources",
      "code": "4.1",
      "titre": "Ordre Juridique et Sources du Droit",
      "dossier": "04_droit_et_lois/01_ordre_juridique_et_sources",
      "index": "04_droit_et_lois/01_ordre_juridique_et_sources/README.md",
      "modules": [
        {
          "id": "cadre_general",
          "code": "4.1.1",
          "titre": "Cadre Général de l'Ordre Juridique",
          "fichier": "04_droit_et_lois/01_ordre_juridique_et_sources/01_cadre_general.md"
        }
      ]
    }
  ]
}
```
*(Les éventuelles branches supplémentaires `11_<branche>/` utilisent les codes `4.11.x`… ; les éventuels sous-dossiers par juridiction interne sont imbriqués dans la branche correspondante sous `"sous_dossiers"` ou `"juridictions"`.)*

### D3. Sous-dossiers Optionnels (Tomes I, VI, VII, VIII)
Lorsque des sous-dossiers optionnels personnalisés existent dans les Tomes `01_cosmologie/` (`<plans>/`, `<pantheon>/`), `06_lieux/` (`<groupes_lieux>/`), `07_factions/` (`<groupes_factions>/`) ou `<08_objets_magiques_singuliers>/` (`<categories>/`), chaque tome conserve son chemin effectif (`"dossier"`, `"index"`) et expose un tableau `"sous_dossiers"` (ou `"groupes"`) avec `{ "id", "titre", "dossier", "index", "modules": [...] }`.

### E. Tome 10 (Chronologie)
```json
{
  "id": "chronologie",
  "code": "10",
  "titre": "Frise & Chronologie du Monde",
  "dossier": "10_chronologie",
  "index": "10_chronologie/README.md",
  "description": "Chronologie historique, registre des occurrences, calendrier et frise graphique Markwhen.",
  "modules": [],
  "dossier_chronologie_historique": "10_chronologie/chronologie_historique",
  "modules_chronologie_historique": [
    {
      "id": "nom_epoque",
      "code": "10.1.1",
      "titre": "Titre de l'époque ou période historique",
      "fichier": "10_chronologie/chronologie_historique/01_nom_epoque.md"
    }
  ],
  "dossier_registre_occurrences": "10_chronologie/registre_occurrences",
  "modules_registre_occurrences": [
    {
      "id": "nom_periode",
      "code": "10.2.1",
      "titre": "Titre de la période du registre",
      "fichier": "10_chronologie/registre_occurrences/01_nom_periode.md"
    }
  ],
  "dossier_calendrier": "10_chronologie/calendrier",
  "modules_calendrier": [
    {
      "id": "calendrier",
      "code": "10.3.1",
      "titre": "Le Calendrier du Monde",
      "fichier": "10_chronologie/calendrier/01_calendrier.md"
    }
  ],
  "dossier_markwhen": "10_chronologie/markwhen",
  "fichiers_markwhen": [
    "10_chronologie/markwhen/chronologie_generale.mw",
    "10_chronologie/markwhen/epoques/<nom_epoque>.mw",
    "10_chronologie/markwhen/campagnes/<nom_campagne>.mw"
  ],
  "dossier_exportations": "10_chronologie/exportations"
}
```
* Les fichiers `.mw` et les exportations ne sont **pas** transposés dans la Bible : ils figurent uniquement dans `fichiers_markwhen` et dans les propriétés de dossier.
* Le tableau `modules` du tome reste vide : les fichiers `.md` du tome 10 résident dans leurs tableaux dédiés (`modules_chronologie_historique`, `modules_registre_occurrences`, `modules_calendrier`), comme `modules_regions` pour le tome 02 et les sous-séries pour le tome 03.

---

## 5. Règles d'Analyse & d'Extraction Automatique

Lors de l'exécution de `generer-structure-json` ou `mettre-a-jour-structure-json` :
1. **Titre du Module** : Extrait du premier `# Titre` du fichier Markdown.
2. **Concepts Clés** :
   - Repérés à partir des listes à puces (`* Concept : explication`), sous-titres `##` et `###`, ou termes en gras `**Terme**`.
   - Normalisés sous forme de phrases concises et autonomes.
3. **Tableaux** : Détectés par les lignes de séparation `| :--- | :--- |` précédées d'un titre `## Tableau...` ou d'une légende.
4. **Notes MJ** : Détectées via les balises `**NOTE POUR LE MAÎTRE DU JEU :**` ou `> ⚠️ **Note MJ :**`.
5. **Code Numérique** : Si le fichier se nomme `03_flux_de_la_magie.md` dans `01_cosmologie`, son code est `"1.3"`.
6. **Codes des Sous-séries** : Les fiches de `coutumes_fetes_et_evenements/` utilisent des codes à trois niveaux par sous-dossier (`3.5.x` coutumes, `3.6.x` fêtes/occurrences, `3.7.x` événements ; `3.8.x` pour l'éventuel dossier `peuples/` ou nom personnalisé). Les branches de `04_droit_et_lois/` utilisent `4.1.x` … `4.10.x` (et `4.11.x+` pour d'éventuelles branches personnalisées ; `4.Y.1` pour `01_cadre_general.md`, `4.Y.2+` pour les actes `02_<slug_entree>.md`). Les fichiers de `10_chronologie/` utilisent `10.1.x` (chronologie historique), `10.2.x` (registre des occurrences), `10.3.x` (calendrier).
7. **Champs Typologiques** : Pour les fêtes/occurrences extrayez `periodicite` et `declencheur` depuis leurs sections du modèle ; pour les événements ponctuels extrayez `statut_occurrence`.
