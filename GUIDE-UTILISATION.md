# Archiviste de Campagne — Guide d'utilisation

Tout ce qu'il faut pour mettre l'**Archiviste de Campagne** au travail à votre table : installation, premiers pas, référence complète des **12 compétences**, flux de travail typiques, dépannage et FAQ.

* Copies localisées de ce guide : [Italiano](https://github.com/<owner>/DMs_Companion/blob/main/locales/it/GUIDA-UTILIZZO.md) · [British English](https://github.com/<owner>/DMs_Companion/blob/main/locales/en-gb/USAGE.md) · [Deutsch](https://github.com/<owner>/DMs_Companion/blob/main/locales/de/NUTZUNGSANLEITUNG.md) — voir aussi le [USAGE.md](https://github.com/<owner>/DMs_Companion/blob/main/USAGE.md) du projet sur la branche `main`.

---

## 1. Installation

**Prérequis** : un assistant IA de programmation (voir le tableau des environnements ci-dessous) et, recommandé mais non obligatoire, un dépôt Git pour votre campagne/univers.

### Option 1 — Copier cette branche dans votre campagne (recommandé)

Vous lisez le paquet `fr` (cloné avec `git clone --depth 1 -b fr …` ou téléchargé en ZIP). Copiez son contenu à la racine de **votre propre dépôt de campagne** (ou dans le répertoire de configuration utilisateur de votre assistant IA, pour rendre la boîte à outils disponible dans tous vos projets) :

* `AGENTS.md`, `CLAUDE.md`
* `.github/agents/`
* `.agents/skills/`
* `GUIDE-UTILISATION.md` (ce guide)

### Option 2 — Installer les compétences via l'Agent Skills CLI (`npx skills`)

```bash
# Toutes les compétences depuis cette branche de langue
npx skills add https://github.com/<owner>/DMs_Companion/tree/fr

# Ou directement depuis le dossier du locale sur main
npx skills add https://github.com/<owner>/DMs_Companion/tree/main/locales/fr/.agents/skills
```

*(Pensez à copier aussi `AGENTS.md` et/ou `.github/agents/*.agent.md` si vous voulez la persona complète de l'Archiviste et l'orchestration des flux de travail.)*

### Ce que font les fichiers installés

| Fichier / Dossier | Rôle |
| :--- | :--- |
| `AGENTS.md` | Règles et flux universels, lus par tous les environnements. |
| `CLAUDE.md` | Point d'entrée pour Claude Code ; importe `AGENTS.md`. |
| `.github/agents/archiviste-de-campagne.agent.md` | La persona *Archiviste de Campagne* (entrée dans le sélecteur d'agents de VS Code). |
| `.agents/skills/<competence>/SKILL.md` | Les 12 compétences modulaires (plus les modèles dans `references/`). |
| `GUIDE-UTILISATION.md` | Ce guide. |

### Notes par environnement

| Environnement | Ce qui se passe |
| :--- | :--- |
| **VS Code / GitHub Copilot** | L'agent apparaît dans le sélecteur d'agents du chat ; les compétences sont disponibles en commandes `/slash` ; les questions de suivi arrivent sous forme de prompts structurés (`vscode_askQuestions`). |
| **Claude Code** | `CLAUDE.md` est chargé automatiquement. Si les compétences ne sont pas détectées, copiez ou créez un lien symbolique de `.agents/skills/*` vers `.claude/skills/`. |
| **OpenAI Codex CLI / Cursor / OpenCode / Gemini CLI / Antigravity** | `AGENTS.md` et `.agents/skills/` sont découverts automatiquement ; il suffit de poser vos questions en langage naturel. |
| **Extensions optionnelles** | Graphify MCP (graphe des liens croisés) et la CLI/extension Markwhen (`@markwhen/mw`) pour le rendu des chronologies. Tout fonctionne sans elles. |

---

## 2. Les Cinq Premières Minutes

1. **Ouvrez le dépôt de votre campagne** dans votre assistant IA.
2. **Sélectionnez l'agent *Archiviste de Campagne*** dans le sélecteur d'agents (VS Code) ou mentionnez-le dans le chat (autres environnements).
3. **Expliquez-lui où vous en êtes** :
   * *Univers nouveau* → lancez `/init-monde` et répondez à l'entretien guidé : il génère l'arborescence en dix tomes, l'index racine et les amorces des fichiers maîtres.
   * *Univers existant* → lancez d'abord `/valider-structure`. L'Archiviste s'adapte aux dossiers déjà présents, y compris les noms historiques (`06_location/`, `07_factions/`, `08_oggetti magici peculiari/`, `cornici/`, …).
4. **Vérifiez le résultat** : les fichiers maîtres (`BIBLE_DE_L_UNIVERS.md`, `STATUT_REVISION.md`, `structure_univers.json`) vivent à la racine de l'univers ; la lore vit dans les dix tomes.
5. **Essayez une tâche réelle** : collez les notes brutes de votre dernière séance et laissez l'Archiviste rédiger le compte rendu.

---

## 3. Comment pense la boîte à outils

### La règle d'or : fidélité notariale (zéro hallucination)

L'Archiviste organise **uniquement** ce que vous fournissez ou que vous avez déjà canonisé. Il n'invente jamais de personnages, de lieux, de dates, de rebondissements ni de chiffres.

* **Information manquante** → il vous la demande directement (mode interactif) ou insère un marqueur bien visible `[A_DEFINIR_MJ: description du détail manquant]` que vous pourrez rechercher ensuite.
* **Créativité sur demande uniquement** → il fait du brainstorming (noms, options, idées) **seulement** quand vous le demandez explicitement (ex. *« Donnez-moi 3 options pour… »*, *« Inventez un nom cohérent »*).

### L'architecture en dix tomes

| Tome | Contenu |
| :--- | :--- |
| `01_cosmologie/` | Plans, mécaniques célestes, flux de la magie, éthique cosmique (`<plans>/`, `<pantheon>/` optionnels). |
| `02_geographie/` | Cartographie, territoires, régions souterraines, dossiers régionaux (`regions/` ou nom personnalisé, ex. `provinces/`, `domaines/`). |
| `03_societe_et_politique/` | Ordre civil, économie, classes sociales, ordre public ; `peuples/` optionnel (ou nom personnalisé) et sous-série `coutumes_fetes_et_evenements/` (`coutumes/`, `fetes_et_occurrences/`, `evenements/`). |
| `04_droit_et_lois/` | 10 branches juridiques (`01_ordre_juridique_et_sources/` … `10_droit_de_la_guerre_et_aventuriers/`), plus éventuelles branches supplémentaires `11_+` ou juridictions. |
| `05_personnages/` | Dossiers modulaires PJ (`<Joueurs>/<Campagne_ou_Groupe>/<Nom_PJ>/`, défaut `Joueurs/<Campagne>/`) et fiches PNJ (`<Non_Joueurs>/[<groupe_pnj>/]`, défaut `Non_Joueurs/`). |
| `06_lieux/` | Nœuds d'aventure, cités, forteresses, dangers locaux (`<groupes_lieux>/` optionnels). |
| `07_factions/` | Maisons nobles, congrégations, guildes, ordres, hiérarchies de pouvoir (`<groupes_factions>/` optionnels). |
| `<08_objets_magiques_singuliers>/` | Artefacts uniques, reliques, registres juridiques, propriétés (nom du tome personnalisable et `<categories>/` optionnelles). |
| `09_chroniques/` | Portail des campagnes : tableau synoptique + comptes rendus progressifs (`<campagnes>/<nom>/<sessions>/`, défaut `campagnes/` et `sessions/`). |
| `10_chronologie/` | Chronologie transversale : `chronologie_historique/`, `registre_occurrences/`, `markwhen/` (`chronologie_generale.mw`, `epoques/`, `campagnes/`), `calendrier/`, `exportations/`. |

### Badges de vérification

Chaque section validée porte le badge standard :

```markdown
> 🛡️ *Vérifié : AAAA-MM-JJ | Modifié : AAAA-MM-JJ*
```

* **Nouveau texte** → `Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]` jusqu'à votre relecture.
* **Les modifications post-séance** ne touchent que `Modifié` : quand il est plus récent que `Vérifié`, la section nécessite un nouveau contrôle.
* **Pendant un audit** les deux dates sont alignées sur la date du jour.

---

## 4. Référence des compétences

Invoquez les compétences avec leur commande slash quand elle est disponible (VS Code, Claude Code), ou mentionnez simplement leur nom dans le chat — l'Archiviste route la demande pour vous.

| # | Compétence | À quoi elle sert |
| :-: | :--- | :--- |
| 1 | `init-monde` | Mise en place guidée et arborescence d'un univers nouveau. |
| 2 | `valider-structure` | Contrôle de santé structurelle de l'archive. |
| 3 | `compte-rendu-session` | Comptes rendus post-séance à partir de notes brutes ou d'entretien. |
| 4 | `dossier-personnage` | Dossiers PJ à 5 modules et fiches PNJ. |
| 5 | `objet-magique` | Registres à 4 sections pour objets magiques. |
| 6 | `audit-etape-par-etape` | Fact-checking interactif, affirmation par affirmation. |
| 7 | `audit-fichier-complet` | Audit d'un fichier ou dossier entier. |
| 8 | `statut-revision` | Tableau de bord de révision construit à partir des badges `🛡️`. |
| 9 | `synchroniser-bible-structure` | Bible de l'Univers maître + JSON lisible par machine. |
| 10 | `coutume-fete-evenement` | Coutumes, fêtes/occurrences, événements ponctuels. |
| 11 | `timeline-markwhen` | Chronologies graphiques Markwhen (`.mw`). |
| 12 | `lier-noms-propres` | Noms propres toujours liés aux fiches canoniques. |

### 4.1 `init-monde` — Arborescence de l'univers

* **Quand** : vous démarrez un univers ou un dépôt de campagne entièrement nouveau.
* **Comment** : `/init-monde` — *« Lance l'entretien pour configurer et générer l'arborescence de l'univers. »*
* **Résultat** : l'arborescence en dix tomes avec les index `README.md`, les amorces des fichiers maîtres (`BIBLE_DE_L_UNIVERS.md`, `structure_univers.json`, …) et la prémisse de l'univers consignée.

### 4.2 `valider-structure` — Diagnostic structurel

* **Quand** : avant/après de grandes réorganisations, ou dès qu'un élément semble mal placé.
* **Comment** : `/valider-structure` — *« Exécute le contrôle de conformité structurelle de l'archive. »*
* **Résultat** : un rapport sur les dossiers manquants, les index `README.md` absents, les liens Markdown cassés et les fichiers `.md` égarés qui appartiennent à l'un des dix tomes.

### 4.3 `compte-rendu-session` — Chroniques et comptes rendus

* **Quand** : juste après une séance de jeu.
* **Comment** : collez vos notes brutes, ou écrivez *« démarrer entretien »* (`/compte-rendu-session`) pour être guidé question par question.
* **Résultat** : un fichier de compte rendu formel dans `09_chroniques/campagnes/<nom>/sessions/NN_titre.md` — synopsis notarial, diagramme Mermaid des accroches PJ, phases marquantes, registre mécanique optionnel — plus le tableau synoptique de la campagne mis à jour.

### 4.4 `dossier-personnage` — Dossiers PJ et fiches PNJ

* **Quand** : un nouveau personnage joueur rejoint la campagne, un PNJ est approfondi, ou un module de dossier doit être mis à jour.
* **Comment** : `/dossier-personnage` — *« Précisez le type (PJ ou PNJ), le nom du personnage et l'opération (creer, mettre a jour module, fiche). »*
* **Résultat** : un dossier PJ à 5 modules (`01_etat_civil_et_traits`, `02_historique_integre`, `03_relations_et_dynamiques`, `04_equipement_et_capacites`, `05_accroches_et_secrets_mj`) dans `05_personnages/Joueurs/<Campagne>/<Nom_PJ>/`, ou une fiche PNJ dans `05_personnages/Non_Joueurs/`, tous deux inscrits dans les index.

### 4.5 `objet-magique` — Objets magiques singuliers

* **Quand** : un artefact unique, une relique ou un foyer arcanique entre dans le canon.
* **Comment** : `/objet-magique` — *« Nom de l'objet magique et détails à enregistrer ou actualiser. »*
* **Résultat** : un registre à 4 sections dans `08_objets_magiques_singuliers/` : fiche technique, manufacture, mécaniques et statut juridique.

### 4.6 `audit-etape-par-etape` — Fact-checking atomique

* **Quand** : vous voulez vérifier la lore affirmation par affirmation, l'assistant vous interrogeant sur chaque point.
* **Comment** : `/audit-etape-par-etape` — *« Précisez le fichier ou le sujet à réviser et la granularité (atomique ou section). »*
* **Résultat** : une révision interactive sans corrections inventées ; les sections vérifiées reçoivent leur badge mis à jour.

### 4.7 `audit-fichier-complet` — Audit de fichier entier

* **Quand** : un document ou un dossier entier nécessite une relecture organique.
* **Comment** : `/audit-fichier-complet` — *« Chemin du fichier ou dossier à contrôler (ex. `05_personnages/` ou fichier `.md` unique). »*
* **Résultat** : un audit structuré de l'ensemble visé, incohérences signalées, corrections proposées pour votre approbation.

### 4.8 `statut-revision` — Tableau de bord de révision

* **Quand** : vous voulez une vue d'ensemble de ce qui est vérifié et de ce qui est périmé.
* **Comment** : `/statut-revision` — *« Génère ou actualise le tableau de bord de révision de l'espace de travail. »*
* **Résultat** : `STATUT_REVISION.md` à la racine de l'univers, avec les pourcentages par fichier et les paragraphes modifiés après audit signalés.

### 4.9 `synchroniser-bible-structure` — Synchronisation du canon maître

* **Quand** : après des changements de canon, ou quand vous voulez un document narratif maître unique / une carte lisible par machine.
* **Comment** : `/synchroniser-bible-structure` avec une opération — `generer-Bible`, `generer-structure-json`, `mettre-a-jour-bible` ou `mettre-a-jour-structure-json`.
* **Résultat** : `BIBLE_DE_L_UNIVERS.md` (compilation narrative monolithique des dix tomes) et `structure_univers.json` (taxonomie hiérarchique avec métadonnées).

### 4.10 `coutume-fete-evenement` — Coutumes, fêtes et événements

* **Quand** : une séance introduit une coutume, une fête/occurrence récurrente ou un événement ponctuel (révolte, cataclysme, bouleversement historique).
* **Comment** : `/coutume-fete-evenement` — *« Précisez type et entrée (ex. 'coutume : cérémonie d'adieu', 'fête : fête du solstice', 'événement : siège de la citadelle'). »*
* **Résultat** : une fiche typologique dans `03_societe_et_politique/coutumes_fetes_et_evenements/`, alignée avec `10_chronologie/` (chronologie et registre des occurrences).

### 4.11 `timeline-markwhen` — Chronologies graphiques

* **Quand** : vous voulez créer, actualiser, valider ou exporter les sources Markwhen de la chronologie.
* **Comment** : `/timeline-markwhen` avec une opération — `creer-mw`, `mettre-a-jour-mw`, `valider-mw` ou `exporter-mw` (ex. *« creer-mw epoque : Premier Âge »*, *« mettre-a-jour-mw campagne : Chroniques du Nord »*).
* **Résultat** : les sources `.mw` dans `10_chronologie/markwhen/` (`chronologie_generale.mw`, `epoques/`, `campagnes/`) maintenues en synchronie avec chronologie, registre des occurrences et comptes rendus ; exportations rendues dans `10_chronologie/exportations/`.

### 4.12 `lier-noms-propres` — Noms Propres Liés

* **Quand** : vous voulez vérifier ou rétablir la règle selon laquelle tout nom propre est un lien vers le fichier `.md` canonique de l'entité.
* **Comment** : `/lier-noms-propres` — *« Chemin du fichier ou du dossier à analyser (ou 'dépôt entier'). »*
* **Résultat** : un tableau des noms non liés avec conversion en lien proposée ou appliquée, et signalement des entités dépourvues de fiche.

---

## 5. Flux de travail typiques

### A. Mettre en place un univers nouveau

`init-monde` (entretien guidé) → `valider-structure` (contrôle de cohérence) → ajoutez vos premières fiches de lore → `synchroniser-bible-structure` (`generer-Bible`, `generer-structure-json`) quand vous voulez les documents maîtres.

### B. Après une séance de jeu (le cycle principal)

1. `compte-rendu-session` — collez les notes (ou « démarrer entretien ») ; le compte rendu est enregistré et l'index de campagne mis à jour.
2. L'Archiviste liste chaque fichier impacté et prépare les mises à jour croisées (dossiers, fiches PNJ, index) : vous les approuvez une par une.
3. Nouvelle coutume/fête/événement mentionné ? → `coutume-fete-evenement` propose la fiche ; les occurrences d'événements déjà connus sont inscrites dans `10_chronologie/`.
4. `timeline-markwhen` (`mettre-a-jour-mw`, ou `creer-mw` pour les nouvelles campagnes/époques) maintient les sources `.mw` en synchronie.
5. Si la séance a modifié la lore canonique → `synchroniser-bible-structure` (`mettre-a-jour-bible`, `mettre-a-jour-structure-json`).
6. Les badges montrent déjà ce qui a changé (`Modifié` > `Vérifié`) : votre prochaine révision part de là.

### C. Ajouter du contenu entre deux séances

PJ/PNJ → `dossier-personnage` · Artefact → `objet-magique` · Coutume/fête/événement → `coutume-fete-evenement` · Grand réarrangement → `valider-structure`.

### D. Un passage de révision / audit

`statut-revision` (voir ce qui est périmé) → `audit-etape-par-etape` ou `audit-fichier-complet` sur les cibles → `statut-revision` de nouveau pour rafraîchir le tableau de bord.

---

## 6. Dépannage

* **L'agent ou les compétences n'apparaissent pas dans VS Code** — les fichiers doivent se trouver à la **racine de l'espace de travail** : `.github/agents/` et `.agents/skills/`. Rechargez la fenêtre et rouvrez le sélecteur d'agents.
* **Claude Code ne détecte pas les compétences** — copiez ou créez un lien symbolique de `.agents/skills/*` vers `.claude/skills/` ; `CLAUDE.md` importe déjà `AGENTS.md`.
* **Aucune boîte de questions structurées n'apparaît** — c'est normal hors de VS Code : l'Archiviste se rabat sur le chat textuel et pose les mêmes questions en texte.
* **`exporter-mw` ne peut pas rendre** — installez la CLI Markwhen (`npx @markwhen/mw`) ou utilisez l'extension Markwhen pour VS Code / `markwhen.com` ; les exportations sont optionnelles et ne bloquent jamais les sources `.mw`.
* **L'assistant a inventé de la lore** — cela viole la règle d'or : ramenez-le à `AGENTS.md`, supprimez le texte inventé et lancez un `audit-etape-par-etape` sur la section touchée.
* **Les marqueurs s'accumulent** — recherchez `[A_DEFINIR_MJ:` et résolvez-les pendant un audit, ou demandez à l'Archiviste de tous les lister.
* **Contenus en langues mélangées dans un dépôt** — n'installez qu'un seul paquet de langue par univers ; supprimez les fichiers de l'autre paquet et relancez `valider-structure`.
* **Noms de dossiers historiques** (`06_location/`, `07_factions/`, …) — aucun problème : l'Archiviste s'adapte à ce qui existe. Seuls les *rôles* des dix tomes sont fixes, pas les graphies.

---

## 7. FAQ

* **Faut-il les 12 compétences ?** Non. Installez-les toutes (elles sont autonomes) et n'utilisez que ce dont vous avez besoin.
* **Puis-je gérer plusieurs campagnes dans un univers ?** Oui — `09_chroniques/campagnes/<nom>/` garde les comptes rendus de chaque campagne séparés ; la lore partagée vit dans les autres tomes.
* **Puis-je l'utiliser pour des campagnes payantes, des streams ou des actual plays ?** Oui. La clause non commerciale porte sur la vente de la boîte à outils elle-même, jamais sur les jeux que vous menez avec.
* **Puis-je reconditionner ou vendre les compétences ?** Non — CC BY-NC-SA 4.0 (voir `LICENSE` sur la branche `main`).
* **Comment mettre à jour vers une nouvelle version ?** Reclonez (ou `git pull`) la branche de langue et recopiez les fichiers ; réintègrez vos éventuelles personnalisations locales de `AGENTS.md`.
* **Où signaler les bugs ou les trouvailles sur les environnements ?** GitHub Issues — voir `CONTRIBUTING.md` sur la branche `main`.

---

*DMs_Companion est gratuit à utiliser et à partager sous CC BY-NC-SA 4.0. S'il vous fait gagner du temps de préparation, vous pouvez soutenir le projet via [GitHub Sponsors](https://github.com/sponsors/Jollyproxi) ou [Buy Me a Coffee](https://buymeacoffee.com/jollyproxi) — entièrement facultatif.*
