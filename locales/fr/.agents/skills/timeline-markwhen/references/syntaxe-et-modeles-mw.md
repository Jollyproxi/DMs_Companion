# Syntaxe et Modèles Markwhen (`.mw`)

Référence opérationnelle pour rédiger et mettre à jour les fichiers `.mw` dans `10_chronologie/markwhen/`.

---

## 1. Syntaxe Canonique Markwhen

### En-tête YAML (`---`)

Chaque fichier `.mw` débute par un bloc YAML encadré par `---` définissant `title`, `description`, `timezone: UTC` (recommandé pour éviter les décalages LMT historiques sur des années anciennes) et la palette de couleurs des tags standards (tout intitulé descriptif doit être rédigé en commentaire `//`, jamais comme `#NomCategorie` sans `:`, afin de ne pas invalider l'analyseur YAML ; le format ISO `AAAA-MM-JJ` est natif et ne requiert pas `dateFormat`) :

```yaml
---
title: "Titre de la Frise"
description: "Description synthétique du fichier .mw"
timezone: UTC

// Type
#coutume: #8b5cf6
#fete: #f59e0b
#evenement: #ef4444
#occurrence: #ec4899

// Statut
#historique: #64748b
#en_cours: #10b981
#planifie: #3b82f6
#date_provisoire: #eab308
---
```

### Formats des Dates (Années du Monde)

Les dates utilisent les **années du monde** au format ISO (`AAAA`, `AAAA-MM`, `AAAA-MM-GG`), avec des années sur 4 chiffres (éventuellement précédées de zéros pour les années `< 1000`, ex. `0512-03-01` ou `512-03-01` de façon uniforme dans un même fichier) :

- **Jour précis** : `512-03-01: Fête du Solstice #fete #historique`
- **Mois approximatif** : `512-03: Convocation du Conseil #evenement #historique`
- **Année seule** : `514: Tournoi de la Garde #fete #occurrence #en_cours`
- **Plage de dates** : `512-03-01/512-03-07: Foire d'Automne #fete #historique` ou `512/513: Siège de la Citadelle #evenement #historique`
- **Date non encore définie** : n'inventez jamais de chiffres et n'omettez pas l'événement ; **demandez toujours d'abord au MJ** (via l'outil de questions structurées s'il est disponible, sinon dans le chat) une date ou une **année provisoire** et, si elle est provisoire, ajoutez le tag `#date_provisoire` accompagné de `- [A_DEFINIR_MJ: date définitive à confirmer]`.

### Descriptions, Sous-puces & Liens Relatifs

Sous la ligne de l'événement (en retrait ou sur les lignes immédiatement suivantes avant la ligne vide), inscrivez :

- Un bref résumé notarial ou l'issue (si `#historique` / `#en_cours`).
- Des liens Markdown relatifs (sans guillemets inversés) vers les fiches canoniques ou comptes rendus, rapportés à l'emplacement du fichier `.mw` :
  - Depuis `10_chronologie/markwhen/chronologie_generale.mw` : `../../03_societe_et_politique/...`
  - Depuis `10_chronologie/markwhen/epoques/<epoque>.mw` ou `campagnes/<campagne>.mw` : `../../../03_societe_et_politique/...` et `../../../09_chroniques/campagnes/...`

Exemple complet d'entrée :

```text
514-06-12: Tournoi de la Garde — Édition 514 #fete #occurrence #en_cours #lieu_haute_citadelle
- Statut : en cours.
- Fiche canonique : [Le Tournoi de la Garde](../../../03_societe_et_politique/coutumes_fetes_et_evenements/fetes_et_occurrences/01_tournoi_garde.md)
- Compte rendu associé : [Séance 02](../../../09_chroniques/campagnes/Chroniques%20du%20Nord/sessions/02_seance.md)
```

### Regroupements (`section` / `endSection`)

Utilisez `section Nom de Section` ... `endSection` pour regrouper logiquement les événements (ex. par sous-période historique dans les fichiers d'époque, ou par arc narratif / acte dans les fichiers de campagne).

---

## 2. Taxonomie Obligatoire des Tags

Chaque événement d'un fichier `.mw` doit comporter **au moins 1 tag de Type** et **1 tag de Statut**, plus d'éventuels tags thématiques et de campagne :

| Catégorie | Tags autorisés | Règle d'usage |
| :--- | :--- | :--- |
| **Type** *(obligatoire)* | `#coutume` `#fete` `#evenement` `#occurrence` | `#occurrence` accompagne `#fete` ou `#evenement` lors de l'inscription d'une occurrence datée précise. |
| **Statut** *(obligatoire)* | `#historique` `#en_cours` `#planifie` | Aligné avec le champ statut du registre des occurrences et des fiches. |
| **Thématiques** *(optionnels)* | `#faction_<slug>` `#lieu_<slug>` `#PJ_<slug>` `#PNJ_<slug>` | Utilisez le `snake_case` cohérent avec les `id` de `structure_univers.json`. |
| **Campagne** *(optionnel/oblig. dans campagnes/)* | `#campagne_<slug>` | Obligatoire pour les événements touchant une campagne donnée. |

---

## 3. Modèle 1 : `10_chronologie/markwhen/chronologie_generale.mw`

`chronologie_generale.mw` est l'**index/légende générale** (il ne duplique pas les événements des autres fichiers) :

```text
---
title: "Chronologie Générale — Légende et Index Chronologique"
description: "Index général, légende des tags et conventions du calendrier du monde. Les événements individuels résident dans epoques/ et campagnes/."
timezone: UTC

// Type
#coutume: #8b5cf6
#fete: #f59e0b
#evenement: #ef4444
#occurrence: #ec4899

// Statut
#historique: #64748b
#en_cours: #10b981
#planifie: #3b82f6
#date_provisoire: #eab308
---

// ============================================================================
// LÉGENDE ET CONVENTIONS DU CALENDRIER
// - Dates exprimées en Années du Monde (format AAAA, AAAA-MM, AAAA-MM-JJ).
// - Correspondance du calendrier : [Calendrier du Monde](../calendrier/README.md)
// - Récurrences fixes : [A_DEFINIR_MJ: liste des récurrences annuelles fixes]
// ============================================================================

// ============================================================================
// INDEX DES SOURCES PAR ÉPOQUE (10_chronologie/markwhen/epoques/)
// - [Époque 01](epoques/01_<slug_epoque>.mw) — [Chronologie Historique](../chronologie_historique/01_<slug_epoque>.md)
// ============================================================================

// ============================================================================
// INDEX DES SOURCES PAR CAMPAGNE (10_chronologie/markwhen/campagnes/)
// - [Campagne](campagnes/<slug_campagne>.mw) — [Portail Campagne](../../09_chroniques/campagnes/<Nom_Campagne>/README.md)
// ============================================================================

section Panorama des Époques
// Indiquer uniquement les macro-plages temporelles des époques (sans dupliquer les événements)
// [A_DEFINIR_MJ: plage d'années Époque 1]: Premier Âge #historique
endSection
```

---

## 4. Modèle 2 : `10_chronologie/markwhen/epoques/<NN_slug_epoque>.mw`

```text
---
title: "Époque : [Nom de l'Époque]"
description: "Chronologie Markwhen de l'époque [Nom de l'Époque] — synchronisée avec chronologie_historique et registre_occurrences."
timezone: UTC

#coutume: #8b5cf6
#fete: #f59e0b
#evenement: #ef4444
#occurrence: #ec4899
#historique: #64748b
#en_cours: #10b981
#planifie: #3b82f6
#date_provisoire: #eab308
---

// Sources canoniques synchronisées :
// - Chronologie historique : [../../chronologie_historique/NN_<slug_epoque>.md](../../chronologie_historique/NN_<slug_epoque>.md)
// - Registre des occurrences : [../../registre_occurrences/NN_<slug_epoque>.md](../../registre_occurrences/NN_<slug_epoque>.md)

section Événements Historiques & Fondateurs
// Exemple :
// 512/513: Siège de la Citadelle #evenement #historique #faction_garde_du_nord
// - Issue : [synthèse canonique]
// - Fiche : [Le Siège de la Citadelle](../../../03_societe_et_politique/coutumes_fetes_et_evenements/evenements/01_siege_citadelle.md)
endSection

section Occurrences & Entrées Évolutives
// Exemple :
// 514: Tournoi de la Garde #fete #occurrence #en_cours
// - Fiche : [Le Tournoi de la Garde](../../../03_societe_et_politique/coutumes_fetes_et_evenements/fetes_et_occurrences/01_tournoi_garde.md)
endSection
```

---

## 5. Modèle 3 : `10_chronologie/markwhen/campagnes/<slug_campagne>.mw`

```text
---
title: "Campagne : [Nom de la Campagne]"
description: "Frise complète de la campagne [Nom de la Campagne] : antécédents des PJ, séances jouées et événements futurs/planifiés."
timezone: UTC

#coutume: #8b5cf6
#fete: #f59e0b
#evenement: #ef4444
#occurrence: #ec4899
#historique: #64748b
#en_cours: #10b981
#planifie: #3b82f6
#date_provisoire: #eab308
#campagne_<slug_campagne>: #f43f5e
---

// Portail de la campagne : [../../../09_chroniques/campagnes/<Nom_Campagne>/README.md](../../../09_chroniques/campagnes/<Nom_Campagne>/README.md)

section Antécédents & Historique PJ
// Événements passés pertinents pour les PJ de la campagne (#historique #campagne_<slug_campagne>)
endSection

section Chronique des Séances
// Événements survenus lors des séances consignées (#historique ou #en_cours)
// Liés vers ../../../09_chroniques/campagnes/<Nom_Campagne>/sessions/XX_titre.md
endSection

section Événements en Cours & Planifiés
// Fenêtres temporelles, échéances et occurrences futures (#en_cours / #planifie)
endSection
```
