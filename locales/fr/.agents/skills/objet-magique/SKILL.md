---
name: objet-magique
description: "Use when: enregistrer ou mettre en forme des objets magiques singuliers, reliques et artefacts de l'univers selon le standard canonique en quatre sections (fiche technique, facture, mécaniques, statut juridique)."
argument-hint: "Nom de l'objet magique et détails à enregistrer ou actualiser"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Gestion des Objets Magiques Singuliers (`objet-magique`)

Cette compétence régit le catalogage officiel des artefacts, reliques et focaliseurs arcaniques dans le Tome VIII (`08_objets_magiques_singuliers/` ou nom personnalisé du tome dans l'espace de travail), en respectant le modèle structurel défini dans [modele-objet](./references/modele-objet.md).

> **📌 Règle des Noms Propres Liés** : tout nom propre d'entité de l'univers (PJ, PNJ, factions, maisons, cités, lieux, objets magiques, coutumes, fêtes, événements…) apparaissant dans le texte produit doit être un **lien Markdown** vers le fichier `.md` canonique de l'entité (ex. `[Nom](chemin/relatif/fichier.md)`), jamais un simple texte brut. Exceptions : titres, noms de fichiers, frontmatter, blocs de code, nœuds Mermaid et sources `.mw`. Entité sans fiche : ne l'inventez pas — utilisez `[A_DEFINIR_MJ: fiche manquante pour <Nom>]` et signalez la lacune. Vérification et conversion : compétence `lier-noms-propres`.

---

## 1. Principes d'Enregistrement

- **Ancrage dans l'Univers** : Consignez l'origine, la rareté et le statut légal ou commercial de l'objet selon les règles du monde (bien librement négociable, licence de guilde, monopole d'État/maison noble ou contrebande prohibée).
- **Zéro Invention** : Si le MJ ne donne que les propriétés mécaniques ou l'aspect, n'inventez jamais de provenance ni de détenteurs fictifs : demandez les détails manquants ou insérez `[A_DEFINIR_MJ: ...]`.
- **Suivi par Badge** : Chaque fiche inclut le badge :
  `> 🛡️ *Vérifié : AAAA-MM-JJ | Modifié : AAAA-MM-JJ*`

---

## 2. Procédure Opératoire

1. **Collecte des Informations** :
   Si les précisions fournies par le MJ sont incomplètes, présentez un questionnaire structuré (à l'aide de l'outil interactif de l'environnement tel que `vscode_askQuestions` ou `AskUserQuestion` s'il est disponible, sinon dans le chat) :
   - **`categorie`** : Options (*Arme Magique*, *Instrument de Musique / Focaliseur*, *Relique / Artefact Ancien*, *Mécanisme / Dispositif Magique*, *Consommable Rare*).
   - **`detenteur`** : Détenteur actuel (options issues des PJ recensés ou champ libre pour un PNJ/lieu).
   - **`statut_juridique`** : Options (*Possession Libre et Licite*, *Soumis à Licence ou Monopole*, *Contrebande / Relique Prohibée*, *Autre*).
   - **`pouvoirs_mecaniques`** : Propriétés mécaniques D&D 5e et résonances sensorielles (champ libre).

2. **Création du Fichier** :
   Enregistrez la fiche dans `<08_objets_magiques_singuliers>/[<categorie>/]<Nom_Objet>.md` (en respectant tout nom personnalisé du Tome VIII et les éventuels sous-dossiers de catégorie) selon le modèle standard.

3. **Mise à Jour de l'Index du Tome** :
   Ajoutez l'entrée avec catégorie, résonance et détenteur dans le tableau ou la liste de `<08_objets_magiques_singuliers>/README.md` (et l'éventuel `README.md` de catégorie).

4. **Lien Croisé avec le Détenteur** :
   Si l'objet appartient à un PJ, actualisez le module `04_equipement_et_capacites.md` du dossier de ce PJ en ajoutant le lien vers la nouvelle fiche.
