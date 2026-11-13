# Architecture de Référence du Monde (Taxonomie Modulaire D&D)

Ce document définit l'arborescence standard de dossiers et de fichiers pour l'archivage encyclopédique d'un univers et des campagnes de D&D associées.

> **Note d'adaptation** : Si l'espace de travail contient déjà un univers existant doté de noms de dossiers équivalents, respectez et conservez l'organisation existante sans renommer de force les fichiers déjà établis.

```text
├── README.md                                               # Index général du monde et guide de navigation
├── structure_univers.json                                  # Carte hiérarchique, métadonnées et taxonomie du monde
├── BIBLE_DE_L_UNIVERS.md                                   # Document source intégral / Livre maître du lore
│
├── 01_cosmologie/                                          # Tome I : Cosmologie, métaphysique, plans, flux de la magie et éthique
│   ├── README.md                                           # Panorama cosmologique
│   ├── 01_structure_planaire.md                            # Plans, sphères célestes, infernales ou abyssales
│   ├── 02_cycles_saisons_et_mecaniques_celestes.md         # Dynamiques temporelles, cycles astronomiques et transits planaires
│   ├── 03_flux_de_la_magie_et_ordre_divin.md               # Nature de l'arcane, théurgie, monopoles et limites
│   └── 04_systeme_moral_ou_philosophique.md                # Valeurs, vertus, vices ou code éthique du cosmos
│
├── 02_geographie/                                          # Tome II : Géographie physique, cartographie et régions
│   ├── README.md                                           # Cadre géographique général et coupes territoriales
│   ├── 01_carte_principale_et_biomes.md                    # Territoires, climats et frontières
│   ├── 02_regions_souterraines_et_abysses.md               # Outreterre, failles et cavernes
│   ├── 03_domaines_speciaux_et_plans_connectes.md          # Royaumes suspendus, portails et terres liminales
│   └── regions/                                            # Dossiers par région/royaume/province (avec README.md)
│
├── 03_societe_et_politique/                                # Tome III : Modèle social, économique et culturel
│   ├── README.md                                           # Panorama de l'ordre social
│   ├── 01_philosophie_sociale_et_coutumes.md               # Valeurs sociales, éthique et conventions
│   ├── 02_monopole_du_pouvoir_et_economie.md               # Armée, commerce, monnaies et impôts
│   ├── 03_classes_sociales_et_roles.md                     # Stratification civique, guildes et esthétique
│   ├── 04_droit_penal_et_justice.md                        # Tribunaux ordinaires, peines et lois civiles
│   └── coutumes_fetes_et_evenements/                       # Sous-série : coutumes, fêtes récurrentes et événements ponctuels
│       ├── README.md                                       # Index de la sous-série par typologie
│       ├── coutumes/                                       # Particularités du quotidien (structures et manières)
│       │   ├── README.md
│       │   └── 01_<slug_entree>.md                         # Fiche coutume (numérotation progressive)
│       ├── fetes_et_occurrences/                           # Fêtes et événements institutionnels/rituels récurrents
│       │   ├── README.md
│       │   └── 01_<slug_entree>.md                         # Fiche fête/occurrence (périodicité fixe ou variable)
│       └── evenements/                                     # Événements singuliers ponctuels par nature
│           ├── README.md
│           └── 01_<slug_entree>.md                         # Fiche événement (historique ou en cours)
│
├── 04_droit_et_succession/                                 # Tome IV : Lois fondamentales, droit dynastique, pactes et traités
│   ├── README.md                                           # Panorama juridico-institutionnel
│   ├── 01_contrats_pactes_et_traites.md                    # Normes, alliances formelles et pactes de sang
│   ├── 02_hierarchie_et_succession.md                      # Ordres de succession, charges et héritage
│   └── 03_tribunaux_et_litiges.md                          # Règlement des litiges juridiques, successoraux et expertises
│
├── 05_personnages/                                         # Tome V : Répertoire des Personnages Joueurs et Non-Joueurs
│   ├── README.md                                           # Index général des personnages et matrice relationnelle
│   ├── Joueurs/                                            # Archive des PJ
│   │   ├── README.md                                       # Vue d'ensemble des groupes et synergies
│   │   └── [Nom_Campagne]/                                 # Dossier du groupe/campagne spécifique
│   │       ├── README.md                                   # Portail des relations du groupe
│   │       └── [Nom_PJ]/                                   # Dossier modulaire du PJ :
│   │           ├── README.md                               # Résumé et index du personnage
│   │           ├── 01_etat_civil_et_traits.md              # Statistiques, espèce, classe, traits
│   │           ├── 02_historique_integre.md                # Passé lié au lore du monde
│   │           ├── 03_relations_et_dynamiques.md           # Liens avec les autres PJ et PNJ
│   │           ├── 04_equipement_et_capacites.md           # Objets clés, dons et aptitudes
│   │           └── 05_accroches_et_secrets_mj.md           # Pistes narratives réservées au MJ
│   └── Non_Joueurs/                                        # Archive des PNJ de l'univers
│       ├── README.md                                       # Index et regroupement par faction
│       └── [Nom_PNJ].md                                    # Fiche avec rôle, tempérament, secrets et accroches
│
├── 06_lieux/                                               # Tome VI : Lieux notables et nœuds d'aventure
│   ├── README.md                                           # Liste des points d'intérêt et liaisons
│   └── [XX_nom_lieu].md                                    # Fiche du lieu (atmosphère, dangers, PNJ, accroches)
│
├── 07_factions/                                            # Tome VII : Factions, maisons nobles, congrégations et guildes
│   ├── README.md                                           # Carte géopolitique du pouvoir et des conflits
│   └── [XX_nom_faction].md                                 # Charte, hiérarchie, alliances, ressources et objectifs
│
├── 08_objets_magiques_singuliers/                          # Tome VIII : Artefacts, reliques et mécanismes uniques
│   ├── README.md                                           # Registre juridique du magique et index des objets
│   └── [Nom_Objet].md                                      # Fiche technique, provenance, pouvoirs et accroches MJ
│
├── 09_chroniques/                                          # Tome IX : Chroniques et comptes rendus de campagne
│   ├── README.md                                           # Index chronologique de toutes les campagnes actives
│   └── campagnes/
│       └── [nom_campagne]/                                 # Dossier d'une campagne
│           ├── README.md                                   # Portail : composition du groupe, objectif, tableau synoptique
│           └── sessions/                                   # Comptes rendus progressifs numérotés :
│               ├── README.md                               # Index des séances
│               ├── 01_titre_session.md                     # Compte rendu Séance 1
│               └── 02_titre_session.md                     # Compte rendu Séance 2...
│
└── 10_chronologie/                                         # Tome X : Frise et chronologie transversale du monde
    ├── README.md                                           # Légende générale : dates (années du monde), tags, navigation
    ├── chronologie_historique/                             # Événements passés, fichiers par époque/période (avec tags)
    │   └── 01_<nom_epoque>.md
    ├── registre_occurrences/                               # Occurrences de fêtes/événements et entrées évolutives, par période
    │   └── 01_<nom_periode>.md
    ├── markwhen/                                           # Frise graphique (sources Markwhen, exclus de la Bible)
    │   ├── README.md                                       # Index des sources .mw et synthèse des conventions
    │   ├── chronologie_generale.mw                         # Index/légende (non agrégé)
    │   ├── epoques/
    │   │   └── <nom_epoque>.mw                             # Source par époque/période historique
    │   └── campagnes/
    │       └── <nom_campagne>.mw                           # Tout ce qui touche la campagne (avec liens vers séances)
    ├── calendrier/                                         # Calendrier du monde : mois, saisons, jours intercalaires, correspondances
    │   └── 01_calendrier.md
    └── exportations/                                       # Rendus graphiques dérivés (HTML/PNG/SVG/PDF de la frise)
        └── README.md                                       # Registre des rendus graphiques dérivés
```
