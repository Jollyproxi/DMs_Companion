# Conventions de la Frise Graphique Markwhen

Standard de rédaction des sources Markwhen conservées dans `10_chronologie/markwhen/`, la frise chronologique graphique de l'univers.

---

## 1. Structure du Dossier `markwhen/`

```text
10_chronologie/markwhen/
├── README.md                   # Index des sources .mw et synthèse des conventions
├── chronologie_generale.mw     # Index/légende générale (NON un agrégat des sources)
├── epoques/
│   └── <nom_epoque>.mw         # Une source par époque/période historique
└── campagnes/
    └── <nom_campagne>.mw       # Une source par campagne : tout ce qui la concerne
```

- `chronologie_generale.mw` fait office d'**index/légende** : il contient la légende des tags, les conventions de dates et les liens vers les sources d'époques et de campagnes. Il ne duplique pas le contenu des autres fichiers.
- Les fichiers sous `epoques/` sont les sources effectives de la chronologie, consultables isolément.
- Les fichiers sous `campagnes/` contiennent **tout ce qui concerne** la campagne (passé et futur), avec liens vers les comptes rendus de `09_chroniques/`.

---

## 2. Syntaxe de Base

Un événement par ligne, avec date, titre et tags :

```text
512-03-01: Fête du Solstice #fete #historique
512/513: Siège de la Citadelle #evenement #historique #faction_garde_du_nord
514: Tournoi de la Garde #fete #occurrence #en_cours
```

- **Intervalles** : `date_debut/date_fin` (ex. `512-03-01/512-03-07`).
- **Dates approximatives** : année seule (ex. `512`) ou année et mois approximatif (`512-03`).
- **Tags** : suffixes `#tag` sur la même ligne que l'événement.
- **Liens vers les fiches** : dans les descriptions/sous-puces de l'événement, liens Markdown relatifs vers les fiches canoniques (ex. `[Tournoi de la Garde](../../../03_societe_et_politique/coutumes_fetes_et_evenements/fetes_et_occurrences/01_tournoi_garde.md)`), adaptés à la position du fichier `.mw`.

---

## 3. Convention des Dates

- Les dates utilisent les **années du monde** exprimées au format ISO (ex. `512-03-01`, `512`, `512/513`).
- La correspondance avec le calendrier réel du monde (mois, saisons, jours intercalaires) est documentée dans `10_chronologie/calendrier/` et résumée dans la légende de `chronologie_generale.mw`.
- Si un événement possède une périodicité fixe, sa date/récurrence doit également figurer dans la légende du calendrier.

---

## 4. Taxonomie des Tags

| Catégorie | Tags | Usage |
| :--- | :--- | :--- |
| **Type** | `#coutume` `#fete` `#evenement` `#occurrence` | Nature de l'entrée ; `#occurrence` marque une vérification datée d'un événement récurrent. |
| **Statut** | `#historique` `#en_cours` `#planifie` | État de l'occurrence aligné sur le modèle des fiches. |
| **Thématiques** | `#faction_<slug>` `#lieu_<slug>` `#PJ_<slug>` `#PNJ_<slug>` | Filtres par acteur ou cadre (ex. `#faction_ligue_marchande`, `#lieu_haut_port`). |
| **Campagne** | `#campagne_<nom>` | Isole ce qui concerne une campagne donnée. |

Les mêmes catégories de tags doivent être utilisées dans `10_chronologie/chronologie_historique/` et `10_chronologie/registre_occurrences/` pour maintenir la synchronisation des deux représentations.

---

## 5. Règles de Mise à Jour

1. **Nouvelle entrée ou occurrence** : ajoutez la ligne à la source d'époque adéquate dans `epoques/` ; si l'événement concerne une campagne, ajoutez-le aussi à `campagnes/<nom>.mw`.
2. **Changement de statut** (planifié → en cours → achevé) : mettez à jour le tag de statut sur la ligne et l'issue dans les notes.
3. **Légende** : si de nouveaux tags ou entrées calendaires apparaissent, mettez à jour `chronologie_generale.mw`.
4. **Exclusions du canon** : les fichiers `.mw` et le contenu de `exportations/` sont **exclus de la Bible** de l'Univers ; ils sont uniquement indexés dans `structure_univers.json` (sous-structure dédiée du tome `10`).
5. **Zéro hallucination** : aucun événement, date ou issue non approuvé par le MJ.
