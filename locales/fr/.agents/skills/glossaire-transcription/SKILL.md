---
name: glossaire-transcription
description: "Use when: générer la liste textuelle compacte des noms propres déjà connus (orthographe exacte seule, sans faits ni divulgâchage) à charger dans NotebookLM ou un autre LLM avec le prompt de transcription de séance afin de réduire les `[?]`."
argument-hint: "Précisez campagne/séance (ex. 'campagne : Chroniques du Nord'), dossier/zone ou 'dépôt entier', d'éventuels noms prononcés en plus, et s'il faut aussi enregistrer un fichier .txt"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Glossaire des Noms Propres pour Transcription (`glossaire-transcription`)

Cette compétence extrait du dépôt une **liste textuelle compacte contenant uniquement l'orthographe exacte des noms propres canoniques** (PJ, PNJ, lieux, factions, objets, coutumes, fêtes, événements, divinités et termes clés) à fournir comme source d'appui à **NotebookLM** ou à un autre LLM avec [prompt-transcription-session](../compte-rendu-session/references/prompt-transcription-session.md), afin de réduire au minimum les marqueurs `[?]` et les erreurs phonétiques lors de la transcription des séances.

> **📌 Exception à la Règle des Noms Propres Liés** : le bloc textuel exporté pour NotebookLM/LLM (ainsi que l'éventuel fichier `.txt` enregistré sur disque) est destiné à un outil externe et doit rester du **texte brut sans liens Markdown** (`[Nom](...)`). Toute explication dans le chat hors du bloc et tout fichier canonique `.md` demeurent en revanche soumis à la compétence `lier-noms-propres`.

---

## 1. Règle d'Or : Orthographe Seule, Zéro Fait et Zéro Hallucination

- **Orthographe Uniquement** : ne consignez **que** l'orthographe canonique exacte de chaque nom propre, les éventuelles variantes graphiques ou alias/diminutifs explicitement documentés dans la fiche canonique (ex. `Nom Canonique (alias : Surnom)`) et, facultativement pour les seuls PJ actifs, la correspondance `Joueur → PJ` si elle est déjà documentée ou fournie par le MJ.
- **Interdiction Stricte des Faits et Divulgâchages** : n'incluez **jamais** de descriptions, rôles narratifs, affiliations, relations, statut vital (vivant/mort/traître), position actuelle, caractéristiques, secrets du MJ ou extraits de lore. Tout ajout au-delà de l'orthographe risque d'amener le modèle de transcription à réimporter dans le rapport des éléments absents de la séance.
- **Clause Anti-Intrusion en En-Tête** : chaque glossaire généré commence par une ligne fixe enjoignant au LLM transcripteur d'utiliser la liste **exclusivement pour l'orthographe** des noms entendus, sans importer de noms non prononcés ni déduire de faits ou de liens.
- **Noms Supplémentaires de la Dernière Séance** : si le MJ communique à l'oral ou dans le chat de nouveaux noms prononcés durant la partie mais pas encore recensés dans l'archive, placez-les dans une section dédiée pour aider la transcription, sans créer de fiche ni modifier le canon.
- **Zéro Invention** : si l'archive présente une incertitude ou une graphie manquante, ne devinez jamais et ne normalisez pas arbitrairement ; signalez-le hors du bloc avec `[A_DEFINIR_MJ: ...]` ou demandez confirmation au MJ avant d'exporter.

---

## 2. Périmètres de Sélection (Maîtrise du Bruit)

Pour éviter d'encombrer le contexte de transcription avec des dizaines de noms étrangers à la scène qui créent de faux rapprochements phonétiques, proposez ou appliquez l'un de ces trois périmètres :

- **Mode A — Ciblé Campagne / Séance *(Défaut recommandé)*** :
  - PJ actifs de la campagne (`05_personnages/<Joueurs>/<Campagne_ou_Groupe>/`, défaut `Joueurs/<Campagne>/`).
  - Noms propres déjà mentionnés dans le `README.md` de la campagne et dans les **N derniers comptes rendus** (défaut : les **5** derniers dans `09_chroniques/<campagnes>/<nom_campagne>/<sessions>/`).
  - Entités canoniques du théâtre géographique ou de la région en cours, s'ils sont précisés par le MJ ou indiqués dans l'en-tête du dernier compte rendu.
  - Éventuels noms supplémentaires ou ponctuels fournis par le MJ pour la séance qui vient d'être enregistrée.
- **Mode B — Zone, Dossier ou Faction Spécifique** :
  - PJ actifs de la campagne (si pertinent) + toutes les entités recensées dans les dossiers, régions, factions ou tomes désignés par le MJ (ex. `06_lieux/<region>/`, `07_factions/<maison>/`, `04_droit_et_lois/`).
- **Mode C — Dépôt Entier** :
  - Tous les noms propres canoniques présents dans les Dix Tomes.
  - **Seuil Anti-Bruit** : si la liste dépasse environ **250–300 entrées**, avertissez explicitement le MJ qu'un glossaire trop vaste favorise les fausses correspondances phonétiques dans NotebookLM/LLM et proposez de resserrer le périmètre sur le Mode A ou B.

---

## 3. Sources et Règles d'Extraction

1. **Index Privilégié** : si `structure_univers.json` existe à la racine de l'espace de travail, lisez-le d'abord pour repérer rapidement tomes, modules et chemins canoniques sans parcourir de prose superflue.
2. **Balayage Direct / Complément dans les Dix Tomes** : parcourez (ou complétez depuis) les dossiers de l'univers en respectant l'arborescence réelle du dépôt — y compris les noms personnalisés ou historiques (`06_location/`, `07_factions/`, `08_oggetti magici peculiari/`, `cornici/`, `expeditions/`, `journaux/`) et la convention de l'archive PNJ documentée dans les instructions du projet et l'index de `05_personnages/` :
   - `05_personnages/` (dossiers modulaires PJ et fiches PNJ)
   - `06_lieux/` (cités, nœuds d'aventure, forteresses, dangers locaux) et `02_geographie/` (régions/macro-zones)
   - `07_factions/` (maisons nobles, congrégations, guildes, ordres, institutions)
   - `<08_objets_magiques_singuliers>/` (artefacts, reliques, objets uniques)
   - `03_societe_et_politique/` (`peuples/`, `coutumes_fetes_et_evenements/`), `01_cosmologie/` (plans, panthéon/divinités), `04_droit_et_lois/` (lois, traités, juridictions) et `10_chronologie/chronologie_historique/` (époques, événements historiques)
   - `09_chroniques/` (pour le Mode A : index de campagne et comptes rendus récents)
3. **Exclusions** :
   - Excluez les répertoires techniques (`.git`, `.agents`, `.github`, `.claude`, `node_modules`, `graphify-out`) et les fichiers de service ou maîtres (`README.md`, `AGENTS.md`, `CLAUDE.md`, `BIBLE_DE_L_UNIVERS.md`, `STATUT_REVISION.md`, `GUIDE-UTILISATION.md`, `structure_univers.json`, sources `.mw` ou exportations).
   - Écartez les titres structurels génériques (ex. *Cadre général*, *Index*, *Synopsis*, *Séance 01*, *Statut de l'occurrence*) ainsi que les marqueurs `[A_DEFINIR_MJ: ...]`.
4. **Normalisation et Déduplication** :
   - Pour chaque fiche canonique, extrayez le nom propre depuis le titre H1 (en retirant préfixes numériques comme `01_`, étiquettes telles que `Fiche PNJ :` / `Dossier PJ :` / `Objet Magique :`, badges `🛡️` ou sous-titres descriptifs après `—` ou `|`), ou à défaut depuis le nom du fichier nettoyé.
   - Pour les dossiers PJ à 6 modules, n'extrayez l'identité qu'**une seule fois** à partir du dossier ou du module d'état civil (`01_etat_civil...`), sans répéter les noms des 6 sous-fichiers.
   - Ne recueillez les alias ou diminutifs que s'ils sont explicitement documentés dans la fiche (`Alias`, `Surnoms`, `Variantes`) ; n'ajoutez jamais d'explications entre parenthèses.
   - Supprimez les graphies strictement identiques et triez les entrées par ordre alphabétique au sein de chaque catégorie.

---

## 4. Procédure Opératoire et Interaction Structurée

1. **Collecte des Paramètres (s'ils ne sont pas déjà précisés par le MJ)** :
   Interrogez le MJ via l'outil de questions structurées de l'environnement (`vscode_askQuestions`, `AskUserQuestion`, `ask_question`, `request_user_input` si disponibles, sinon directement dans le chat) :
   - **`perimetre`** : *Quel périmètre le glossaire doit-il couvrir ?*
     - Options : *Campagne / Séance en cours — recommandé* (en listant les campagnes détectées sous `09_chroniques/`), *Zone, dossier ou faction spécifique*, *Dépôt entier (tous les Dix Tomes)*.
   - **`noms_extra`** : *Y a-t-il de nouveaux noms prononcés lors de la dernière séance (PJ invités, nouveaux PNJ, lieux ou termes non encore archivés) à inclure uniquement pour la transcription ?* (Champ libre optionnel ou *Aucun*).
   - **`destination`** : *Comment souhaitez-vous recevoir le glossaire ?*
     - Options : *Dans le chat uniquement (prêt à copier-coller dans NotebookLM) — recommandé*, *Dans le chat + enregistrer un fichier `.txt` dans le dépôt*.
2. **Extraction et Contrôle Anti-Divulgâchage** :
   - Appliquez les règles du §3 au périmètre choisi.
   - Vérifiez qu'aucune entrée ne comporte de description, parenté, allégeance, statut ou indice d'intrigue.
   - Omettez les catégories vides. Si le total dépasse ~250–300 entrées, prévenez le MJ et proposez une sélection resserrée sur la campagne ou la scène en cours.
3. **Remise du Glossaire** :
   - Affichez **toujours** le résultat complet dans le chat à l'intérieur d'un bloc de code `text`, prêt à être collé dans NotebookLM (*Ajouter une source → Texte copié*) ou dans un autre LLM.
   - Juste après le bloc, présentez un bref récapitulatif : périmètre retenu, nombre d'entrées par catégorie et total, sources consultées et éventuelles graphies douteuses relevées dans l'archive.
   - Si l'enregistrement sur disque a été demandé, créez un fichier **`.txt` UTF-8** dans le dossier de la campagne — `09_chroniques/<campagnes>/<nom_campagne>/glossaire_transcription.txt` *(défaut : `09_chroniques/campagnes/<nom_campagne>/glossaire_transcription.txt` ; ou à la racine / chemin indiqué s'il n'existe pas encore de campagne)* — en évitant l'extension `.md` afin de ne jamais perturber `valider-structure`, `lier-noms-propres`, `statut-revision` ni `synchroniser-bible-structure`.

---

## 5. Modèle Canonique de Sortie

Produisez uniquement un bloc compact selon ce format (en omettant toute catégorie vide) :

````text
# GLOSSAIRE DES NOMS PROPRES (ORTHOGRAPHE SEULE — NE PAS IMPORTER DE FAITS ABSENTS DE LA SÉANCE)
Campagne / Périmètre : <Nom de campagne ou périmètre>

## Personnages Joueurs (PJ)
- <Nom du PJ> (<Joueur → PJ> uniquement si documenté/fourni, optionnel)
- <Nom du PJ> (alias : <Surnom documenté>)

## Personnages Non Joueurs (PNJ) et Créatures Notables
- <Nom du PNJ>
- <Nom du PNJ> (alias : <Diminutif / Variante graphique documentée>)

## Lieux, Cités et Régions
- <Lieu / Région>

## Factions, Maisons et Institutions
- <Faction / Maison>

## Objets, Artefacts et Reliques
- <Objet>

## Coutumes, Fêtes, Événements, Divinités et Termes Clés
- <Coutume / Fête / Événement / Divinité / Loi>

## Noms Supplémentaires de la Séance (non encore recensés)
- <Nom prononcé fourni par le MJ>
````

---

## 6. Intégration avec les Autres Compétences

- **`compte-rendu-session` et `prompt-transcription-session`** : cette compétence produit exactement la source optionnelle décrite à l'étape 2 de [prompt-transcription-session](../compte-rendu-session/references/prompt-transcription-session.md) ; elle réduit les `Nom[?]` avant l'importation via le Canal C de `compte-rendu-session`.
- **`lier-noms-propres`** : partage la logique d'inventaire des entités canoniques dans les Dix Tomes et l'index JSON ; le glossaire produit est dispensé des liens Markdown car il constitue un texte de référence externe pour NotebookLM/LLM.
- **`synchroniser-bible-structure`** : lorsqu'il existe, `structure_univers.json` sert d'index rapide pour collecter les intitulés canoniques sans charger toute la prose de `BIBLE_DE_L_UNIVERS.md`.
- **`valider-structure`** : l'export optionnel utilise l'extension `.txt` dans le dossier de campagne afin de rester neutre vis-à-vis des contrôles de liens cassés, de badges `🛡️` et de fichiers `.md` orphelins.
