# Modèles de Référence pour Dossiers Personnages

## 1. Dossier Modulaire de Personnage Joueur (PJ)

Chaque PJ possède un dossier dédié dans `05_personnages/<Joueurs>/<Campagne_ou_Groupe>/<Nom_PJ>/` (défaut : `05_personnages/Joueurs/<Campagne>/<Nom_PJ>/`) accompagné d'un `README.md` de liaison et de cinq modules thématiques :

### `README.md` (Portail du Personnage)
```markdown
# [Nom du Personnage]

> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*

* **Campagne :** [Nom de la Campagne]
* **Rôle dans le Groupe :** [Synthèse du rôle martial/arcanique/social]
* **Alignement / Code Moral :** [Alignement ou principes éthiques]

## Index des Modules
1. [01. État Civil & Traits Fondamentaux](01_etat_civil_et_traits.md)
2. [02. Historique Intégré](02_historique_integre.md)
3. [03. Relations & Dynamiques de Groupe](03_relations_et_dynamiques.md)
4. [04. Équipement & Capacités Singulières](04_equipement_et_capacites.md)
5. [05. Accroches Narratives & Secrets du MJ](05_accroches_et_secrets_mj.md)
```

### `01_etat_civil_et_traits.md`
```markdown
# 01. État Civil & Traits Fondamentaux

> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*

* **Nom :** [Nom Complet]
* **Espèce / Lignée :** [Espèce D&D 5e / lignée de l'univers]
* **Classe & Niveau :** [Classe, Sous-classe, Niveau]
* **Alignement / Code Moral :** [Alignement ou principes cardinaux]
* **Apparence Physique :** [Description visuelle, signes distinctifs, cicatrices, tenue]
* **Traits de Personnalité, Idéaux, Liens, Défauts :** [Listes synthétiques]
```

### `02_historique_integre.md`
```markdown
# 02. Historique Intégré au Canon

> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*

## Origines & Racines
[Description de l'origine géographique et sociale avec liens relatifs vers les lieux du monde.]

## Le Point de Bascule
[L'événement ou le traumatisme fondateur qui a poussé le personnage vers l'aventure.]

## Développements Récents avant la Campagne
[Ce qui s'est produit dans la période précédant immédiatement le début de la campagne.]
```

### `03_relations_et_dynamiques.md`
```markdown
# 03. Relations & Dynamiques

> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*

## Liens avec les Compagnons de Groupe
* **[Nom Compagnon 1] :** [Dynamique relationnelle, confiance, tensions]
* **[Nom Compagnon 2] :** [...]

## Liens avec les PNJ & Factions
* **[Nom PNJ / Faction] :** [Nature de la relation, dettes d'honneur, rivalités]
```

### `04_equipement_et_capacites.md`
```markdown
# 04. Équipement & Capacités Singulières

> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*

## Dotation Principale & Focaliseurs
* [Objet Magique / Focaliseur avec lien éventuel vers 08_objets_magiques_singuliers/]

## Capacités & Traits Singuliers
* **[Nom Capacité] :** [Description narrative et mécanique]
```

### `05_accroches_et_secrets_mj.md`
```markdown
# 05. Accroches Narratives & Secrets du MJ

> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*

> ⚠️ *Section confidentielle à l'usage exclusif du Maître du Jeu.*

## Pistes d'Enquête Ouvertes
* **[Piste 1] :** [Détails, accroches, évolutions possibles]

## Vérités Cachées & Révélations Futures
* **[Secret 1] :** [Vérité sur le passé du PJ ignorée du personnage lui-même]
```

---

## 2. Fiche de Personnage Non-Joueur (PNJ)

Chaque PNJ réside sous la forme d'un fichier unique dans `05_personnages/<Non_Joueurs>/[<groupe_pnj>/][Nom_PNJ].md` (défaut : `05_personnages/Non_Joueurs/[Nom_PNJ].md`) :

```markdown
# [Nom PNJ] — [Titre ou Rôle]

> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*

* **Faction / Maison :** [Nom de Faction avec lien relatif vers 07_factions/]
* **Lieu de Résidence / Activité :** [Lieu avec lien vers 06_lieux/]
* **Alignement / Morale :** [Alignement ou principes moraux]
* **Statut Actuel :** [Vivant, Fugitif, Décédé, Disparu]

---

## Apparence & Tempérament
[Description physique, posture, façon de parler, caractère.]

---

## Rôle Narratif & Rapports avec le Groupe
[Qui est-il dans le monde et comment interagit-il avec les PJ.]

---

## Secrets & Accroches pour le MJ
* **[Secret / Motivation Cachée] :** [Ce qu'il poursuit réellement]
* **[Accroche d'Aventure] :** [Comment l'impliquer dans les prochaines séances]
```
