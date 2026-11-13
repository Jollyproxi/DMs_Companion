---
name: lier-noms-propres
description: "Use when: vérifier ou convertir les noms propres de personnes, lieux, cités, objets, factions, coutumes et événements en liens Markdown vers leurs fichiers `.md` canoniques ; analyser des fichiers, dossiers ou l'ensemble du dépôt pour repérer les noms non liés et rétablir la conformité à la règle des noms propres liés."
argument-hint: "Chemin du fichier ou du dossier à analyser (ou 'dépôt entier')"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Liaison Obligatoire des Noms Propres (`lier-noms-propres`)

Cette compétence fait respecter la règle universelle selon laquelle tout nom propre d'entité de l'univers doit être un lien Markdown vers le fichier `.md` canonique de l'entité : elle analyse les documents, détecte les noms apparaissant comme simple texte, les classe et propose ou applique leur conversion en liens, en signalant au MJ les entités dépourvues de fiche.

---

## 1. Règle de Référence

- Tout **nom propre** d'entité de l'univers — personnes (PJ, PNJ), maisons, factions, guildes, cités, lieux, régions, plans, objets magiques, coutumes, fêtes, événements, époques, lois, institutions — apparaissant dans le texte produit doit être un **lien Markdown** vers le fichier `.md` canonique de cette entité, le nom propre servant de texte du lien : `[Nom](chemin/relatif/fichier.md)`.
- Le chemin est **relatif au fichier rédigé** et doit pointer vers un fichier réellement présent sur le disque.
- Le texte du lien est le nom propre de l'entité dans sa forme canonique (celle du titre H1 ou du nom de fichier de la fiche).
- **Exceptions** (noms admis sans lien) :
  1. Titres et noms de fichiers.
  2. Frontmatter YAML, blocs de code, commandes et chemins.
  3. Étiquettes des diagrammes Mermaid et des sources Markwhen `.mw` (les liens Markdown n'y sont pas rendus).
  4. Désignations génériques ne renvoyant à aucune entité recensée.
- **Entité Sans Fiche** : n'inventez jamais la fiche. Insérez le marqueur `[A_DEFINIR_MJ: fiche manquante pour <Nom>]` et signalez la lacune, ou — en mode interactif — demandez au MJ s'il faut recenser l'entité avec la compétence pertinente (`dossier-personnage`, `objet-magique`, `coutume-fete-evenement`, etc.).

---

## 2. Construction de l'Index des Entités

Avant l'analyse, construisez la table `nom → chemin du fichier canonique` :

1. **Source privilégiée** : si `structure_univers.json` est présent à la racine de l'espace de travail, utilisez-le comme index (noms des modules et chemins associés).
2. **Balayage direct** : à défaut (ou en complément) parcourez les dix tomes — `05_personnages/` (PJ et PNJ), `06_lieux/`, `07_factions/`, `08_objets_magiques_singuliers/`, `03_societe_et_politique/coutumes_fetes_et_evenements/`, `02_geographie/` (régions), `01_cosmologie/` (plans), `04_droit_et_lois/` (ou `04_droit_et_succession/`, lois, traités, pactes, juridictions), `10_chronologie/chronologie_historique/` (époques, événements historiques) — en collectant les titres H1 et les noms de fichiers.
3. **Noms canoniques** : pour chaque fiche, le nom propre est le titre du document (H1) ou le nom du fichier sans extension ; consignez également les variantes ou alias explicitement documentés dans la fiche.
4. **Homonymes** : si deux entités partagent le même nom, marquez l'ambiguïté et demandez au MJ quelle fiche lier.

---

## 3. Procédure Opératoire

1. **Déterminez le Périmètre** : fichier unique, dossier ou dépôt entier (en excluant les répertoires techniques comme `.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`).
2. **Analysez le Texte** : examinez les fichiers `.md` ligne par ligne en excluant les exceptions de la §1 (frontmatter, blocs de code, étiquettes Mermaid, sources `.mw`, titres).
3. **Classez Chaque Occurrence** :
   - ✅ **Déjà Lié** : le nom est déjà un lien valide (vérifiez que la cible existe sur le disque).
   - 🔗 **À Lier** : nom brut avec fiche existante → conversion en lien.
   - ⚠️ **Sans Fiche** : nom brut d'entité non recensée → marqueur `[A_DEFINIR_MJ: ...]`.
   - ❓ **Ambigu** : homonymie ou correspondance incertaine → interrogez le MJ.
4. **Rapportez le Résultat** au MJ sous forme de tableau (`fichier:ligne | nom | statut | action proposée`).
5. **Appliquez après Confirmation** : convertissez les noms en liens relatifs corrects (recalculez le chemin en fonction de la position du fichier) ; pour les cas ⚠️ insérez le marqueur et proposez le recensement avec la compétence pertinente ; pour les cas ❓ attendez la décision du MJ.
6. **Récapitulatif Final** : listez les fichiers modifiés, les noms convertis et les lacunes encore ouvertes.

---

## 4. Intégration avec les Autres Compétences

- **`valider-structure`** : cette compétence constitue le **pilier E** du diagnostic structurel (couverture des noms propres liés) ; exécutez-la avec les contrôles A–D pour un audit complet.
- **Compétences d'audit (`audit-etape-par-etape`, `audit-fichier-complet`)** : lors de l'audit, vérifiez aussi que les noms propres sont liés et rétablissez la conformité au fil des corrections validées par le MJ.
- **Compétences de création de fiches (`dossier-personnage`, `objet-magique`, `coutume-fete-evenement`)** : chaque nouvelle fiche rend son nom liable ; à la création, signalez dans quels fichiers existants le nouveau nom devra être lié et proposez la mise à jour des références.
- **`synchroniser-bible-structure`** : dans la Bible de l'Univers, les noms propres suivent la même convention et restent des liens vers leurs modules d'origine.
- **`statut-revision`** : les lacunes ouvertes (noms sans fiche) peuvent être suivies dans le tableau de bord `STATUT_REVISION.md` comme entrées en attente de recensement.
