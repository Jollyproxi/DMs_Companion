---
name: statut-revision
description: "Use when: générer ou mettre à jour le tableau de bord du statut de révision du lore (STATUT_REVISION.md), calculer les pourcentages de vérification, suivre les fichiers achevés et repérer les paragraphes modifiés après le dernier audit."
argument-hint: "Génère ou actualise le tableau de bord de révision de l'espace de travail"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Tableau de Bord & Statut de Révision du Lore (`statut-revision`)

Cette compétence génère, actualise et maintient le fichier de suivi `STATUT_REVISION.md` à la racine de l'espace de travail, offrant au Maître du Jeu une vue immédiate de la couverture de vérification et des sections nécessitant un nouveau contrôle.

---

## 1. Critères de Classification des Statuts

La compétence analyse les fichiers Markdown des dossiers canoniques de l'univers (`01_cosmologie`, `02_geographie`, `03_societe_et_politique` y compris la sous-série `coutumes_fetes_et_evenements/`, `04_droit_et_succession`, `05_personnages`, `06_lieux`, `07_factions`, `08_objets_magiques_singuliers`, `09_chroniques`, `10_chronologie`) et inspecte les badges :

```markdown
> 🛡️ *Vérifié : [DATE_V] | Modifié : [DATE_M]*
```

### États de Conformité :
* 🟢 **Vérifié Complet** : Toutes les sections du document possèdent un badge avec `DATE_V >= DATE_M` et ne contiennent aucun marqueur `[A_DEFINIR_MJ]`.
* 🟡 **Vérifié Partiel / Incomplet** : Certaines sections portent un badge mais d'autres en sont dépourvues ou contiennent des marqueurs `[A_DEFINIR_MJ]`.
* 🟠 **Modifié Post-Audit (Relecture Requise)** : Une ou plusieurs sections présentent `DATE_M > DATE_V`, indiquant une modification postérieure au dernier audit officiel.
* ⚪ **Non Vérifié** : Aucun badge de vérification présent dans le fichier.

---

## 2. Structure du Fichier `STATUT_REVISION.md`

Enregistrez `STATUT_REVISION.md` à la racine de l'espace de travail selon ce modèle :

```markdown
# Registre & Statut de Révision du Canon

Ce registre suit l'avancement de l'audit officiel du lore, en recensant les sections validées par le Maître du Jeu et celles modifiées au fil des séances.

* **Dernier Audit Général :** [DATE]
* **Couverture Globale du Canon :** [POURCENTAGE]%

---

## 1. Tableau Synoptique par Secteur

| Section / Tome | Fichiers Totaux | Vérifiés 🟢 | Post-Audit 🟠 | Partiels 🟡 | Non Vérifiés ⚪ | État |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: |
| **01 Cosmologie** | X | A | B | C | D | [Icône] |
| **02 Géographie** | X | A | B | C | D | [Icône] |
| **03 Société & Politique** | X | A | B | C | D | [Icône] |
| **03· Coutumes, Fêtes & Événements** | X | A | B | C | D | [Icône] |
| **04 Droit & Succession** | X | A | B | C | D | [Icône] |
| **05 Personnages (PJ & PNJ)** | X | A | B | C | D | [Icône] |
| **06 Lieux** | X | A | B | C | D | [Icône] |
| **07 Factions** | X | A | B | C | D | [Icône] |
| **08 Objets Magiques Singuliers** | X | A | B | C | D | [Icône] |
| **09 Chroniques de Campagne** | X | A | B | C | D | [Icône] |
| **10 Chronologie & Occurrences** | X | A | B | C | D | [Icône] |

---

## 2. Éléments Prioritaires en Attente de Contrôle

### Fichiers avec Modifications Post-Audit (🟠)
* [chemin/fichier.md](chemin/fichier.md) — *Modifié le [DATE] (Vérifié le [DATE])*

### Fichiers avec Lacunes Explicites (🟡 `[A_DEFINIR_MJ]`)
* [chemin/fichier.md](chemin/fichier.md) — *Section [Nom] : [description du doute]*

---

## 3. Historique des Séances d'Audit
* **AAAA-MM-JJ** : Audit [complet / partiel] mené sur [dossier ou fichier] via `[audit-etape-par-etape / audit-fichier-complet]`.
```

---

## 3. Procédure Opératoire

1. **Analyse** : Parcourez récursivement tous les fichiers `.md` pertinents de l'espace de travail en excluant les répertoires techniques (ex. `.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Extraction des Balises** : Relevez dans chaque fichier la présence des badges `🛡️`, les dates `Vérifié` et `Modifié`, ainsi que les marqueurs `[A_DEFINIR_MJ]`.
3. **Calcul des Statistiques** : Calculez les décomptes et pourcentages pour chacun des dix tomes canoniques (en distinguant séparément la sous-série `coutumes_fetes_et_evenements/`).
4. **Écriture / Mise à Jour** : Rédigez ou mettez à jour `STATUT_REVISION.md` à la racine de l'espace de travail.
