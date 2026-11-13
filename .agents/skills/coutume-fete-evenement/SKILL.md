---
name: coutume-fete-evenement
description: "Use when: enregistrer des coutumes et particularités de la vie quotidienne, des fêtes et événements récurrents (occurrences) et des événements ponctuels de l'univers ; créer ou mettre à jour les fiches sous 03_societe_et_politique/coutumes_fetes_et_evenements/ et maintenir 10_chronologie/ (chronologie historique, registre des occurrences et frise graphique Markwhen)."
argument-hint: "Précisez type et entrée (ex. 'coutume : cérémonie d'adieu', 'fête : fête du solstice', 'événement : siège de la citadelle')"
user-invocable: true
disable-model-invocation: false
---

# Compétence : Coutumes, Fêtes & Événements (`coutume-fete-evenement`)

Cette compétence gère la sous-série `03_societe_et_politique/coutumes_fetes_et_evenements/` et son lien avec le tome `10_chronologie/` : elle recense les particularités de la vie quotidienne, les fêtes et occurrences récurrentes, ainsi que les événements singuliers ponctuels avec le même niveau de fidélité notariale que le reste de l'archive.

> **📌 Règle des Noms Propres Liés** : tout nom propre d'entité de l'univers (PJ, PNJ, factions, maisons, cités, lieux, objets magiques, coutumes, fêtes, événements…) apparaissant dans le texte produit doit être un **lien Markdown** vers le fichier `.md` canonique de l'entité (ex. `[Nom](chemin/relatif/fichier.md)`), jamais un simple texte brut. Exceptions : titres, noms de fichiers, frontmatter, blocs de code, nœuds Mermaid et sources `.mw`. Entité sans fiche : ne l'inventez pas — utilisez `[A_DEFINIR_MJ: fiche manquante pour <Nom>]` et signalez la lacune. Vérification et conversion : compétence `lier-noms-propres`.

---

## 1. Règle d'Or (Zéro Hallucination)

- N'inventez jamais de coutumes, dates, rituels, participants ou issues non fournis par le MJ ou non déjà attestés dans les fichiers canoniques.
- Détail manquant : en mode interactif, demandez-le au MJ (à l'aide de l'outil de questions structurées de l'environnement comme `vscode_askQuestions` ou `AskUserQuestion` s'il est disponible, sinon dans le chat) ; en rédaction directe, insérez `[A_DEFINIR_MJ: description]`.

---

## 2. Taxonomie des Typologies

La classification repose sur la **nature** de l'entrée et non sur sa seule périodicité :

| Type | Sous-dossier | Nature | Exemples |
| :--- | :--- | :--- | :--- |
| **Coutume** | `coutumes/` | Particularités de la vie quotidienne : comportements sociaux, rituels, formes et manières codifiées (structure et modalités du rite). | Cérémonies de salutation ou d'adieu officiel ; rituels d'hospitalité ; usages à table ; formules de politesse. |
| **Fête / Occurrence** | `fetes_et_occurrences/` | Événements **institutionnels ou rituels récurrents**, à périodicité **fixe** (calendrier) ou **variable à déclencheur** (conditions d'amorce, calendrier avançable). | Fête du Solstice d'Hiver ; Tournoi de Sélection de la Garde (au retour d'expéditions) ; élections (dates prévues mais avançables pour cause exceptionnelle). |
| **Événement ponctuel** | `evenements/` | Par nature **unique ou non répétable** : bouleversements historiques, révoltes, cataclysmes, tournants. Peut être **historique (passé)** ou **imminent/en cours** (issue décidée en jeu). Même si un fait similaire pouvait se reproduire, il reste ici par nature. | Siège d'une citadelle ; révolte minière ; pacte brisé ; catastrophe naturelle. |

Si une entrée semble hybride (ex. un rite institutionnel qui a dégénéré en bouleversement), classez-la selon sa nature dominante et ajoutez un lien croisé vers la fiche associée.

---

## 3. Structure des Dossiers & Noms de Fichiers

```text
03_societe_et_politique/coutumes_fetes_et_evenements/
├── README.md                       # Index de la sous-série (une section par type)
├── coutumes/
│   ├── README.md
│   └── 01_<slug_entree>.md         # Préfixe numérique progressif par sous-dossier
├── fetes_et_occurrences/
│   ├── README.md
│   └── 01_<slug_entree>.md
└── evenements/
    ├── README.md
    └── 01_<slug_entree>.md
```

- Noms de fichiers : `NN_slug_en_snake_case.md`, numérotation progressive par sous-dossier (ex. `01_ceremonie_adieu.md`, `02_...`).
- Chaque sous-dossier et le dossier parent reçoivent un fichier index `README.md`, mis à jour à chaque nouvelle fiche.

---

## 4. Modèle de Fiche — Coutume

```markdown
# [Nom de la Coutume]

> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*

## Présentation
Ce que c'est, où et quand cela se pratique, qui est tenu de l'observer.

## Formalisme & Manières
Déroulement étape par étape du rite ou comportement : gestes, formules, ordre des actes, durée, ton.

## Variantes & Degrés
Différences selon le rang social, la faction, la région ou le cadre (cour, place publique, cérémonie officielle...).

## Signification & Sanctions
Valeur symbolique et historique de la coutume ; conséquences des infractions (sociales, juridiques, rituelles).

## Liens & Accroches MJ
Liens vers PNJ, factions, lieux ou autres fiches (liens relatifs). Pistes réservées au MJ.

## Effets Mécaniques *(optionnel)*
Éventuels effets en jeu (modificateurs, avantage, inspiration). À remplir uniquement si pertinent.
```

---

## 5. Modèle de Fiche — Fête / Occurrence

```markdown
# [Nom de la Fête / de l'Événement Récurrent]

> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*

## Présentation
Ce que c'est, qui le célèbre ou le préside, signification et place dans la culture du monde.

## Périodicité & Déclencheur
- **Périodicité** : fixe (calendrier) / variable à déclencheur / mixte.
- **Déclencheur** : conditions amorçant l'événement (ex. « retour d'une campagne », « décès du titulaire », « décret du conseil »).

## Fenêtres Temporelles
Délais prévus, préavis, possibilités et causes d'anticipation ou de report (ex. élections anticipées pour motif grave).

## Déroulement
Rituels, phases, cérémonies, durée, séquence des actes.

## Participants & Rôles
Qui préside, qui participe, conditions d'accès, exclus, fonctions institutionnelles impliquées.

## Occurrences Connues
| Édition / Date | Statut | Issue | Chronologie |
| :--- | :--- | :--- | :--- |
| [année du monde ou date] | planifié / en cours / achevé | [issue] | [lien vers 10_chronologie] |

## Liens & Accroches MJ
Liens vers PNJ, factions, lieux, coutumes ou événements associés. Pistes réservées au MJ.

## Effets Mécaniques *(optionnel)*
Éventuels effets en jeu. À remplir uniquement si pertinent.
```

---

## 6. Modèle de Fiche — Événement Ponctuel

```markdown
# [Nom de l'Événement]

> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*

## Présentation
Ce qui s'est produit (ou se produira) : nature du bouleversement et ancrage historique. Préciser s'il est **historique** ou **en cours**.

## Causes & Prémisses
Contexte, tensions, décisions ou coïncidences ayant préparé l'événement.

## Déroulement
Phases successives de l'événement.

## Conséquences & Retombées
Impacts sur les lieux, factions, institutions, PNJ et équilibres du monde.

## Statut de l'Occurrence
- **Statut** : planifié / en cours / achevé.
- **Issue** (si achevé) : [synthèse].
- **Date / période** : [année du monde].

## Protagonistes & Témoins
PNJ, PJ, factions ou peuples impliqués ou présents (avec liens vers les fiches).

## Liens & Accroches MJ
Liens croisés et pistes réservées au MJ.

## Effets Mécaniques *(optionnel)*
Éventuels effets en jeu. À remplir uniquement si pertinent.
```

---

## 7. Procédure de Création (Entretien Guidé)

Posez les questions suivantes au MJ (à l'aide de l'outil interactif de l'environnement comme `vscode_askQuestions` ou `AskUserQuestion` s'il est disponible, sinon dans le chat) :

1. **Typologie** : *S'agit-il d'une coutume, d'une fête/occurrence récurrente ou d'un événement ponctuel ?* (Options présentant la distinction par nature de la §2).
2. **Nom & Contexte** : *Nom de l'entrée et, s'il est connu, le contexte (faction, lieu, période) ?* (Champ libre).
3. **Champs typologiques** : recueillez les champs du modèle choisi (pour les fêtes : périodicité fixe/variable, déclencheur, fenêtres temporelles ; pour les événements : historique ou en cours).
4. **Rédaction** : créez le fichier avec préfixe numérique progressif dans le bon sous-dossier, remplissez les sections connues et marquez les lacunes avec `[A_DEFINIR_MJ: ...]`.
5. **Badge** : inscrivez `> 🛡️ *Vérifié : NON_VALIDE | Modifié : [DATE_DU_JOUR]*`.
6. **Propagation** : mettez à jour les `README.md` de liaison, proposez l'actualisation de `10_chronologie/` et, si l'entrée intègre le canon documentaire, proposez `synchroniser-bible-structure` (`mettre-a-jour-bible`, `mettre-a-jour-structure-json`).

---

## 8. Gestion des Occurrences (Événements déjà recensés)

Lorsqu'une séance met en scène une récurrence d'une fête ou occurrence déjà recensée (ex. un tournoi annuel) :

1. **Compte Rendu** : documentez l'occurrence dans le compte rendu de séance (`compte-rendu-session`).
2. **Chronologie** : enregistrez l'occurrence dans `10_chronologie/` (registre des occurrences + sources Markwhen) avec statut et issue.
3. **Fiche canonique** : **demandez au MJ** s'il faut modifier la fiche.
   - Les particularités propres à cette occurrence (chiffres, participants, issues, incidents) **restent dans la chronologie et les comptes rendus**.
   - La fiche n'est mise à jour **que** si ces particularités **modifient profondément la nature** de l'entrée (ex. changement de règles, de rôle ou de sens du rite). Le cas échéant, actualisez la fiche et la ligne « Occurrences connues ».

---

## 9. Mise à Jour de `10_chronologie/`

Pour chaque nouvelle entrée, occurrence ou transition d'état (planifié → en cours → achevé) :

1. **Chronologie historique** (`10_chronologie/chronologie_historique/`, par époque/période) : pour les événements passés, avec tags de catégorie (ex. `#evenement #historique`).
2. **Registre des occurrences** (`10_chronologie/registre_occurrences/`, par époque/période) : pour les occurrences de fêtes/événements récurrents et les entrées en cours.
3. **Markwhen** (`10_chronologie/markwhen/`) : mettez à jour ou créez les sources `.mw` via la compétence dédiée `timeline-markwhen` (`creer-mw` / `mettre-a-jour-mw`) selon [conventions-markwhen](./references/conventions-markwhen.md).
4. **Calendrier** (`10_chronologie/calendrier/`) : si l'entrée introduit ou utilise une périodicité fixe, alignez la définition du calendrier du monde.

Les entrées dans `chronologie_historique` et `registre_occurrences` emploient la même taxonomie de tags que Markwhen afin que les deux représentations restent synchronisées.

---

## 10. Badges, Index & Synchronisation

- **Badge** : utilisez toujours le badge standard `> 🛡️ *Vérifié : ... | Modifié : ...*` selon les règles temporelles habituelles (nouveau texte → `Vérifié : NON_VALIDE` ; édition post-validation → avancer uniquement `Modifié` ; audit → aligner les deux dates).
- **Index** : mettez à jour le `README.md` du sous-dossier, du dossier parent `coutumes_fetes_et_evenements/` et de `03_societe_et_politique/` si pertinent.
- **Codes du canon** (Bible/JSON) : coutumes `3.5.x`, fêtes/occurrences `3.6.x`, événements `3.7.x` ; tome `10_chronologie` codé comme tome `10` (`10.1.x` chronologie historique, `10.2.x` registre des occurrences, `10.3.x` calendrier). Les sources `.mw` et exportations sont exclues de la Bible et indexées uniquement dans le JSON.
- **Zéro hallucination** : comme pour tout autre module, aucun détail non approuvé par le MJ.
