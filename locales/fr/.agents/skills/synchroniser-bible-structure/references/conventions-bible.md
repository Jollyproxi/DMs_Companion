# Conventions de Compilation de la Bible de l'Univers

La Bible de l'Univers (`BIBLE_DE_L_UNIVERS.md` ou titre étendu adopté dans l'espace de travail) constitue le document narratif maître monolithique du monde. Elle rassemble en un enchaînement fluide, continu et consultable tout le corpus de connaissances réparti dans les dix tomes.

---

## 1. Page de Titre & Métadonnées

L'en-tête canonique figure au tout début du fichier :

```markdown
### BIBLE DE L'UNIVERS : [NOM_UNIVERS]

> 📜 **Document Maître Monolithique du Canon**  
> *Version du Canon :* [VERSION] | *Dernière Compilation :* [DATE_DU_JOUR]  
> 🛡️ *Vérifié : [DATE_V] | Modifié : [DATE_M]*

---
```

---

## 2. Hiérarchie des Titres (Correspondance des Niveaux)

Comme le document réunit de nombreux tomes et modules imbriqués, les titres des fichiers `.md` individuels sont transposés selon l'échelle canonique suivante :

| Niveau dans le Module Atomique | Niveau dans la Bible Maîtresse | Exemple de Format |
| :--- | :--- | :--- |
| **Titre du Tome (depuis README)** | Niveau 5 (`#####`) | `##### 1. Cosmologie & Architecture Métaphysique` |
| **Titre du Module (`# Titre`)** | Niveau 6 Italique (`###### *...*`) ou `### X.Y` | `###### *1.1 Structure Planaire et Cosmique*` |
| **Section Interne (`## Section`)** | Titre `###` ou `####` | `### Plans Élémentaires et Terres Liminales` |
| **Sous-section (`### Sous-section`)** | Puce en gras ou `#####` | `* **Cour Astrale :** ...` |

> **Note de Continuité** : Si l'espace de travail comporte déjà une Bible maîtresse, reprenez exactement le style et les niveaux de titres déjà employés dans ce fichier.

---

## 3. Ordre Séquentiel de Compilation des Tomes

La compilation suit strictement la séquence numérique canonique :

1. **##### 1. Cosmologie & Architecture Métaphysique** (`01_cosmologie/`)
   - `01_structure_planaire.md`
   - `02_cycles_saisons_et_mecaniques_celestes.md`
   - `03_flux_de_la_magie_et_ordre_divin.md`
   - `04_systeme_moral_ou_philosophique.md`
2. **##### 2. Géographie Physique, Territoriale et Environnementale** (`02_geographie/`)
   - Modules principaux de géographie, carte, souterrains et plans liminaux.
   - Traitement des régions/provinces dans `regions/`, classées par numéro croissant.
3. **##### 3. Ordre Social, Politique et Économique** (`03_societe_et_politique/`)
   - Modèles sociaux, économie, classes, droit pénal.
   - Sous-série `coutumes_fetes_et_evenements/` : coutumes (`3.5.x`), fêtes/occurrences (`3.6.x`), événements ponctuels (`3.7.x`), dans l'ordre numérique croissant par sous-dossier.
4. **##### 4. Droit, Pactes et Règles de Succession** (`04_droit_et_succession/`)
   - Contrats, pactes, traités, hiérarchie successorale, tribunaux.
5. **##### 5. Répertoire des Personnages du Monde** (`05_personnages/`)
   - Répertoire des PNJ notables (`Non_Joueurs/`), regroupés par faction ou région.
   - Synthèse des liens du groupe si une campagne canonique est présente.
6. **##### 6. Atlas des Lieux & Nœuds d'Aventure** (`06_lieux/`)
   - Lieux notables, forteresses, cités et portails.
7. **##### 7. Registre Géopolitique des Factions & Maisons** (`07_factions/`)
   - Chartes, hiérarchies et rivalités des puissances dominantes.
8. **##### 8. Registre des Objets Magiques Singuliers & Reliques** (`08_objets_magiques_singuliers/`)
   - Artefacts uniques, histoire, statut juridique et mécaniques propres.
9. **##### 9. Chroniques Historiques & Compendium des Campagnes** (`09_chroniques/`)
   - Compendium des campagnes actives et comptes rendus progressifs de séance.
10. **##### 10. Frise et Chronologie du Monde** (`10_chronologie/`)
    - Chronologie historique (`10.1.x`, fichiers par époque/période), registre des occurrences (`10.2.x`, fichiers par époque/période) et calendrier (`10.3.x`).
    - Les sources Markwhen (`markwhen/*.mw`) et exportations graphiques (`exportations/`) sont **exclues** de la Bible : elles demeurent indexées uniquement dans `structure_univers.json`.
    - Les entrées internes utilisent la taxonomie de tags Markwhen (ex. `#coutume #fete #evenement #occurrence`) afin de rester synchronisées avec la frise graphique.

---

## 4. Traitement des Tableaux, Diagrammes et Notes MJ

1. **Tableaux Markdown** : Reproduits intégralement en veillant à préserver la syntaxe `| :--- | :--- |` sans rupture de ligne.
2. **Diagrammes Mermaid** : Conservés dans leurs blocs ```` ```mermaid ```` respectifs avec une syntaxe de nœuds valide.
3. **Notes pour le MJ** : Les encadrés `**NOTE POUR LE MAÎTRE DU JEU :**` ou `> ⚠️ **Note MJ :**` sont conservés sous forme de citations mises en relief (`> ...`) afin de préserver le contexte opérationnel.
4. **Marqueurs Incomplets** : Tous les marqueurs `[A_DEFINIR_MJ: ...]` sont reproduits fidèlement sans inventer de contenu.

---

## 5. Règles de Mise à Jour Incrémentale (`mettre-a-jour-bible`)

Lorsque le mode incrémental est appelé :
1. Ne réécrivez pas l'intégralité du document maître.
2. Repérez le titre exact du module modifié (via le code `X.Y` ou l'intitulé).
3. Remplacez le bloc compris entre le début de la section du module et le début du module suivant.
4. Si le module est un nouvel ajout, insérez-le à la fin de son tome en respectant l'ordre numérique.
5. Mettez à jour la ligne de métadonnées en tête en inscrivant la date du jour dans `Modifié : [DATE_DU_JOUR]`.
