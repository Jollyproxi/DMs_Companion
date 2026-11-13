---
name: timeline-markwhen
description: "Use when: créer, générer, mettre à jour, valider ou exporter les fichiers de frise chronologique graphique Markwhen (.mw) sous 10_chronologie/markwhen/ (chronologie_generale.mw, epoques/<epoque>.mw, campagnes/<campagne>.mw), synchroniser dates, statuts et tags avec chronologie_historique/, registre_occurrences/, comptes rendus de séance et structure_univers.json, ou produire des rendus graphiques dans 10_chronologie/exportations/."
argument-hint: "Précisez l'opération : creer-mw, mettre-a-jour-mw, valider-mw ou exporter-mw (ex. 'creer-mw epoque : Premier Âge', 'mettre-a-jour-mw campagne : Chroniques du Nord')"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Gestion de la Frise Graphique Markwhen (`timeline-markwhen`)

Cette compétence régit le cycle de vie complet des sources **Markwhen (`.mw`)** dans `10_chronologie/markwhen/` et de leurs exportations dans `10_chronologie/exportations/`. Elle maintient la représentation temporelle graphique du monde synchronisée avec la chronologie historique (`10_chronologie/chronologie_historique/`), le registre des occurrences (`10_chronologie/registre_occurrences/`), le calendrier (`10_chronologie/calendrier/`), les fiches de coutumes, fêtes et événements (`03_societe_et_politique/coutumes_fetes_et_evenements/`) et les comptes rendus de campagne (`09_chroniques/campagnes/`).

Consultez les références techniques jointes :
- [syntaxe-et-modeles-mw](./references/syntaxe-et-modeles-mw.md) : syntaxe Markwhen canonique, en-tête YAML, taxonomie des tags et modèles pour `chronologie_generale.mw`, `epoques/<epoque>.mw` et `campagnes/<campagne>.mw`.
- [synchronisation-et-export](./references/synchronisation-et-export.md) : règles de correspondance bidirectionnelle avec le Tome 10, indexation dans `structure_univers.json`, liste de validation et pipeline d'exportation vers `10_chronologie/exportations/`.

> **📌 Règle des Noms Propres Liés** : tout nom propre d'entité de l'univers (PJ, PNJ, factions, maisons, cités, lieux, objets magiques, coutumes, fêtes, événements…) apparaissant dans le texte produit doit être un **lien Markdown** vers le fichier `.md` canonique de l'entité (ex. `[Nom](chemin/relatif/fichier.md)`), jamais un simple texte brut. Exceptions : titres, noms de fichiers, frontmatter, blocs de code, nœuds Mermaid et sources `.mw`. Entité sans fiche : ne l'inventez pas — utilisez `[A_DEFINIR_MJ: fiche manquante pour <Nom>]` et signalez la lacune. Vérification et conversion : compétence `lier-noms-propres`.

---

## 1. Règle d'Or : Fidélité Notariale (Zéro Hallucination)

- **Interdiction d'Inventer** : N'inventez jamais de votre propre chef de dates, d'années du monde, de noms d'époques, de durées, de participants ou d'issues non expressément fournis par le MJ ou déjà attestés dans les fichiers canoniques.
- **Gestion des Dates ou Détails Manquants** :
  - **Demande obligatoire avant écriture** : dans Markwhen, chaque événement visible requiert une date avant les `:`. Si un événement ne dispose pas encore d'une date ou année du monde dans les fichiers canoniques, **arrêtez-vous et demandez toujours au MJ** (à l'aide de l'outil de questions structurées de l'environnement comme `vscode_askQuestions` ou `AskUserQuestion` s'il est disponible, sinon directement dans le chat) une date canonique ou une **année provisoire** avant d'inscrire l'entrée dans le fichier `.mw`.
  - Si le MJ fournit une année provisoire, insérez l'événement avec cette année, ajoutez le tag `#date_provisoire` et indiquez en sous-puce `- [A_DEFINIR_MJ: date définitive à confirmer]`, afin que l'événement apparaisse sur la frise tout en restant signalé comme à consolider.

---

## 2. Architecture de `10_chronologie/markwhen/`

```text
10_chronologie/
├── markwhen/
│   ├── README.md                     # Index des sources .mw et synthèse des conventions
│   ├── chronologie_generale.mw       # Index/légende générale (NON un agrégat des sources)
│   ├── epoques/
│   │   └── <slug_epoque>.mw          # Une source .mw par époque/période historique
│   └── campagnes/
│       └── <slug_campagne>.mw        # Tout ce qui touche la campagne (passé, présent, planifié)
└── exportations/
    ├── README.md                     # Registre des rendus graphiques dérivés
    └── <nom_fichier>.(html|svg|png|pdf)
```

- **Rôle de `chronologie_generale.mw`** : contient l'en-tête de configuration et la légende des tags/couleurs, le résumé du calendrier du monde ainsi que l'index commenté des sources dans `epoques/` et `campagnes/`. Il ne duplique pas les événements individuels des fichiers spécifiques.
- **Exclusion de la Bible** : les fichiers `.mw` et le contenu de `exportations/` sont **exclus de la Bible de l'Univers** et recensés uniquement dans `structure_univers.json` (champ `fichiers_markwhen` du Tome `10`).

---

## 3. Matrice des Sous-Opérations

| Commande / Argument | Cible Principale | Mode | Objectif |
| :--- | :--- | :--- | :--- |
| **`creer-mw`** *(ou `generer-mw`)* | `chronologie_generale.mw`, `epoques/*.mw`, `campagnes/*.mw` | Initialisation / Ex-nihilo | Crée la structure `markwhen/`, génère `chronologie_generale.mw` ou crée un nouveau fichier `.mw` d'époque ou de campagne à partir des modules canoniques. |
| **`mettre-a-jour-mw`** | Fichiers `.mw` existants + `markwhen/README.md` | Incrémental / Delta | Ajoute de nouveaux événements/occurrences, met à jour les tags de statut (`#planifie` → `#en_cours` → `#historique`), ajoute des séances et actualise la légende. |
| **`valider-mw`** | `10_chronologie/markwhen/**/*.mw` | Diagnostic / Audit technique | Vérifie la syntaxe Markwhen, la présence des tags obligatoires, les liens relatifs vers fiches/comptes rendus et l'alignement avec le Tome 10 et `structure_univers.json`. |
| **`exporter-mw`** | `10_chronologie/exportations/` | Rendu / Dérivation | Exporte les sources `.mw` vers des rendus dérivés (HTML/SVG/PNG/PDF via CLI `mw` optionnelle ou export manuel depuis extension/web app) et actualise `exportations/README.md`. |

---

## 4. Procédure 1 : `creer-mw` (Initialisation & Génération des Sources `.mw`)

Utilisez cette procédure pour initialiser `10_chronologie/markwhen/` ou créer un nouveau fichier `.mw` pour une époque historique ou une campagne.

### Étapes Opératoires :
1. **Détection du Contexte et des Sources** :
   - Lisez `10_chronologie/README.md`, `10_chronologie/calendrier/` et `10_chronologie/markwhen/README.md`.
   - Selon la cible demandée (`generale`, `epoque`, `campagne`, ou `tout`), examinez les sources pertinentes :
     - Pour une **époque** : `10_chronologie/chronologie_historique/`, `10_chronologie/registre_occurrences/` et les fiches de `03_societe_et_politique/coutumes_fetes_et_evenements/`.
     - Pour une **campagne** : `09_chroniques/<campagnes>/<nom_campagne>/README.md`, les comptes rendus dans `<sessions>/`, les dossiers PJ (`05_personnages/<Joueurs>/<Campagne_ou_Groupe>/`) et les événements historiques/en cours associés.
2. **Entretien Préliminaire** :
   - Si des coordonnées essentielles manquent (ex. nom/slug de l'époque, année de début/fin, année courante de la campagne), demandez-les au MJ avant de générer le fichier (via l'outil de questions structurées si disponible, sinon dans le chat).
3. **Génération des Fichiers d'après les Modèles** :
   - Appliquez les modèles de [syntaxe-et-modeles-mw](./references/syntaxe-et-modeles-mw.md) :
     - Créez les sous-dossiers `10_chronologie/markwhen/epoques/` et `10_chronologie/markwhen/campagnes/` s'ils sont absents.
     - Générez `chronologie_generale.mw` avec en-tête, définition des tags/couleurs, notes calendaires et carte des fichiers `.mw`.
     - Générez `epoques/<slug_epoque>.mw` ou `campagnes/<slug_campagne>.mw` en ordonnant les événements chronologiquement par année du monde (`AAAA`, `AAAA-MM`, `AAAA-MM-JJ` ou plages `debut/fin`) et en les regroupant dans des blocs `section` thématiques ou par phase.
     - Incluez sous chaque événement le lien Markdown relatif vers sa fiche canonique ou son compte rendu de séance.
4. **Propagation des Index et du JSON** :
   - Mettez à jour `10_chronologie/markwhen/README.md` en listant les nouveaux fichiers `.mw` créés et en avançant la date `Modifié` du badge `🛡️`.
   - Proposez la mise à jour de `fichiers_markwhen` dans `structure_univers.json` (`mettre-a-jour-structure-json`).

---

## 5. Procédure 2 : `mettre-a-jour-mw` (Mise à Jour Incrémentale)

Utilisez cette procédure après un compte rendu de séance (`compte-rendu-session`), la création/modification d'une fiche dans `coutumes_fetes_et_evenements/` (`coutume-fete-evenement`), ou sur demande directe du MJ.

### Étapes Opératoires :
1. **Identification du Delta Temporel** :
   - Déterminez ce qui a changé :
     - **Nouvel événement / nouvelle occurrence** : date/année du monde, titre, type (`#coutume`, `#fete`, `#evenement`, `#occurrence`), statut (`#planifie`, `#en_cours`, `#historique`) et tags thématiques (`#faction_<slug>`, `#lieu_<slug>`, `#PJ_<slug>`, `#PNJ_<slug>`, `#campagne_<slug>`).
     - **Transition de statut** : passage d'une entrée existante de `#planifie` à `#en_cours` ou `#historique` (avec synthèse de l'issue).
     - **Nouvelle séance de campagne** : événements datés issus de `09_chroniques/campagnes/<nom>/sessions/XX_titre.md`.
2. **Actualisation des Sources `.mw`** :
   - Ouvrez le fichier `.mw` de l'époque concernée dans `10_chronologie/markwhen/epoques/` et insérez ou mettez à jour la ligne de l'événement en conservant l'ordre chronologique.
   - Si l'événement touche une campagne, mettez également à jour `10_chronologie/markwhen/campagnes/<slug_campagne>.mw` en ajoutant le lien relatif vers le compte rendu ou la fiche.
   - Si de nouveaux tags (ex. nouvelle faction ou campagne) ou récurrences calendaires fixes ont été introduits, actualisez l'en-tête et la légende dans `10_chronologie/markwhen/chronologie_generale.mw`.
3. **Alignement Croisé avec le Tome 10** :
   - Vérifiez que la même entrée/occurrence et les mêmes tags figurent dans `10_chronologie/chronologie_historique/` (si `#historique`) ou `10_chronologie/registre_occurrences/` (si `#occurrence`, `#en_cours` ou `#planifie`), en proposant l'alignement si nécessaire.

---

## 6. Procédure 3 : `valider-mw` (Diagnostic et Vérification de Cohérence)

Utilisez cette procédure pour vérifier la correction formelle et structurelle des sources `.mw` selon la liste de contrôle de [synchronisation-et-export](./references/synchronisation-et-export.md).

### Contrôles Effectués :
1. **Syntaxe Markwhen** : validité de l'en-tête YAML (`---`, absence de clés `#Catégorie` sans `:` et de `dateFormat`), fermeture correcte des blocs `section` / `endSection` (ou `group` / `endGroup`) et format valide des dates (`AAAA`, `AAAA-MM`, `AAAA-MM-JJ`, `date1/date2`) avant `:`.
2. **Taxonomie des Tags** : chaque événement doit porter au moins un tag de **type** (`#coutume`, `#fete`, `#evenement`, `#occurrence`) et un tag de **statut** (`#historique`, `#en_cours`, `#planifie`).
3. **Intégrité des Liens Relatifs** : vérifiez que tous les liens Markdown `[Texte](../../...)` dans les descriptions pointent vers des fichiers existants dans l'espace de travail.
4. **Cohérence Bidirectionnelle Tome 10 & JSON** :
   - Comparez les événements des fichiers `.mw` avec `chronologie_historique/` et `registre_occurrences/`, en signalant les écarts de dates ou de tags de statut.
   - Vérifiez que chaque fichier `.mw` présent sur disque est listé dans `fichiers_markwhen` au sein de `structure_univers.json`.
5. **Rapport Diagnostique** : restituez un tableau de résultats (`OK` / `WARN` / `ERREUR`) et demandez au MJ (via outil structuré si disponible, sinon dans le chat) s'il souhaite appliquer les corrections automatiques.

---

## 7. Procédure 4 : `exporter-mw` (Exportations Graphiques dans `10_chronologie/exportations/`)

Utilisez cette procédure lorsque le MJ demande de générer ou mettre à jour les rendus de la frise chronologique.

### Étapes Opératoires :
1. **Vérification des Outils Optionnels (CLI `mw` / Extension / Web App)** :
   - Vérifiez si la CLI Markwhen (`@markwhen/mw`) est disponible dans l'environnement ou guidez le MJ via l'extension Markwhen de l'éditeur ou `markwhen.com`, selon [synchronisation-et-export](./references/synchronisation-et-export.md).
2. **Génération & Exportation** :
   - Exportez les sources `.mw` demandées vers `10_chronologie/exportations/` selon la convention de nommage (`frise_<slug>_<format>.<ext>`).
3. **Actualisation de l'Index des Exportations** :
   - Mettez à jour `10_chronologie/exportations/README.md` avec le tableau des rendus générés (fichier, source `.mw`, date de génération) et avancez `Modifié` dans le badge `🛡️`.

---

## 8. Interaction Structurée

Si la compétence est appelée sans argument précis ou avec des paramètres partiels, demandez au MJ (à l'aide de l'outil de questions structurées de l'environnement comme `vscode_askQuestions` / `AskUserQuestion` s'il est disponible, sinon dans le chat) quelle opération exécuter :
- `creer-mw` — Initialise `chronologie_generale.mw` ou crée un nouveau fichier `.mw` par époque ou campagne
- `mettre-a-jour-mw` — Ajoute de nouveaux événements/occurrences ou met à jour statuts et tags dans les fichiers `.mw` existants
- `valider-mw` — Contrôle la syntaxe `.mw`, les tags, les liens relatifs et la synchronisation avec le Tome 10 et le JSON
- `exporter-mw` — Exporte les sources `.mw` en rendus dérivés dans `10_chronologie/exportations/`
