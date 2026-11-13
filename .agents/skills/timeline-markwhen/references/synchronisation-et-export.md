# Synchronisation, Validation & Exportation Markwhen

Règles d'alignement entre `10_chronologie/markwhen/`, les autres modules de l'univers, `structure_univers.json` et le dossier `10_chronologie/exportations/`.

---

## 1. Correspondance Bidirectionnelle entre Modules & Fichiers `.mw`

Chaque événement dans les fichiers `.mw` correspond à une source documentaire canonique :

| Source Canonique | Destination dans `markwhen/` | Tags requis |
| :--- | :--- | :--- |
| `10_chronologie/chronologie_historique/*.md` | `epoques/<epoque>.mw` (et `campagnes/<campagne>.mw` si pertinent) | `#evenement` (ou `#fete`/`#coutume`) + `#historique` |
| `10_chronologie/registre_occurrences/*.md` | `epoques/<epoque>.mw` + éventuel `campagnes/<campagne>.mw` | `#fete #occurrence` ou `#evenement` + `#historique` / `#en_cours` / `#planifie` |
| `03_societe_et_politique/coutumes_fetes_et_evenements/fetes_et_occurrences/*.md` (Tableau *Occurrences connues*) | `epoques/<epoque>.mw` + `chronologie_generale.mw` (si récurrence fixe) | `#fete #occurrence` + statut correspondant |
| `03_societe_et_politique/coutumes_fetes_et_evenements/evenements/*.md` | `epoques/<epoque>.mw` + éventuel `campagnes/<campagne>.mw` | `#evenement` + statut correspondant (`achevé` → `#historique`) |
| `09_chroniques/campagnes/<nom>/sessions/*.md` | `campagnes/<slug_campagne>.mw` (et `epoques/<epoque>.mw` si portée historique) | `#evenement` ou `#occurrence` + `#campagne_<slug>` + statut |
| `10_chronologie/calendrier/*.md` | `chronologie_generale.mw` (section commentée légende calendrier) | — |

### Règle de Conversion Statut de Fiche → Tag Markwhen

- Fiche / Registre au statut `achevé` ou événement passé → `#historique`
- Fiche / Registre au statut `en cours` → `#en_cours`
- Fiche / Registre au statut `planifié` → `#planifie`

---

## 2. Synchronisation avec `structure_univers.json`

Les sources `.mw` et rendus dans `exportations/` :

1. **Ne doivent JAMAIS être inclus dans la Bible de l'Univers** (`BIBLE_DE_L_UNIVERS.md`).
2. **Doivent être recensés dans `structure_univers.json`** au sein de l'objet du Tome `10` (`id: "chronologie"`), dans le tableau `fichiers_markwhen` :

```json
"dossier_markwhen": "10_chronologie/markwhen",
"fichiers_markwhen": [
  "10_chronologie/markwhen/chronologie_generale.mw",
  "10_chronologie/markwhen/epoques/01_premier_age.mw",
  "10_chronologie/markwhen/campagnes/chroniques_du_nord.mw"
],
"dossier_exportations": "10_chronologie/exportations"
```

Lorsque `creer-mw` ajoute ou supprime un fichier `.mw`, actualisez `10_chronologie/markwhen/README.md` et proposez (ou exécutez sur confirmation) la mise à jour de `fichiers_markwhen` dans `structure_univers.json`.

---

## 3. Liste de Contrôle de Validation (`valider-mw`)

Lors de l'exécution de `valider-mw`, vérifiez les points suivants dans l'ordre :

1. **Structure des dossiers et index** :
   - Existence de `10_chronologie/markwhen/README.md` et `10_chronologie/markwhen/chronologie_generale.mw`.
   - Tous les fichiers `.mw` présents dans `epoques/` et `campagnes/` doivent être répertoriés à la fois dans `10_chronologie/markwhen/README.md` et dans l'index commenté de `chronologie_generale.mw`.
2. **Syntaxe Markwhen** :
   - En-tête YAML proprement délimité par deux lignes `---`, sans clé `#Catégorie` dépourvue de `:` ni `dateFormat: yyyy-MM-dd` (le format ISO est natif ; spécifiez plutôt `timezone: UTC`).
   - Équilibre entre chaque `section` et son `endSection` (ainsi que `group` / `endGroup`).
   - Format de date valide avant `:` sur chaque ligne d'événement (aucune date inventée ni texte libre non commenté à la place de la date).
3. **Couverture des Tags** :
   - Chaque ligne d'événement porte au moins 1 tag de type (`#coutume`, `#fete`, `#evenement`, `#occurrence`) et 1 tag de statut (`#historique`, `#en_cours`, `#planifie`).
   - Tous les tags employés dans `epoques/*.mw` et `campagnes/*.mw` figurent dans la légende de `chronologie_generale.mw`.
4. **Liens Markdown** :
   - Les chemins relatifs dans les sous-puces d'événements (ex. `../../../03_societe_et_politique/...`) pointent vers des fichiers existants sur disque et encodent les espaces avec `%20`.
5. **Alignement avec le Tome 10 et `structure_univers.json`** :
   - Chaque entrée dans `chronologie_historique/` et `registre_occurrences/` dispose de son équivalent dans le fichier `.mw` de l'époque.
   - Le tableau `fichiers_markwhen` du Tome 10 dans `structure_univers.json` correspond exactement aux fichiers `.mw` présents sur disque.

---

## 4. Pipeline d'Exportation (`exporter-mw`) *(Optionnel)*

Le dossier `10_chronologie/exportations/` accueille les rendus dérivés (exclus de la Bible).

### Mode A — Via Markwhen CLI (`@markwhen/mw`)

Si Node.js / `npx` ou la commande `mw` sont disponibles dans l'environnement :

- **Frise HTML interactive** :
  `npx @markwhen/mw <chemin_fichier.mw> -o 10_chronologie/exportations/<nom_fichier>.html`
- Vérifiez toujours d'abord la disponibilité de la commande (`command -v mw` sous macOS/Linux ou `Get-Command mw` sous PowerShell, ou `npx --version`).

### Mode B — Via Extension IDE (`Markwhen`) ou Web App

Si le MJ préfère exporter en PNG/SVG/PDF depuis l'extension Markwhen de l'éditeur ou `markwhen.com` :

1. Préparez et validez le fichier `.mw` source en vérifiant que l'en-tête YAML comporte `title` et des couleurs complètes pour les tags.
2. Indiquez le nom de fichier canonique d'enregistrement dans `10_chronologie/exportations/` :
   - `frise_epoque_<slug>.(html|svg|png|pdf)`
   - `frise_campagne_<slug>.(html|svg|png|pdf)`
3. Mettez à jour `10_chronologie/exportations/README.md` avec un tableau récapitulatif :

```markdown
## Fichiers Exportés

| Rendu Exporté | Source `.mw` | Format | Dernière Mise à Jour |
| :--- | :--- | :--- | :--- |
| [frise_campagne_...](frise_campagne_....html) | [campagnes/....mw](../markwhen/campagnes/....mw) | HTML | AAAA-MM-JJ |
```
