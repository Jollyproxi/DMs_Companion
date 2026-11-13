# World Reference Architecture (Modular D&D Taxonomy)

This document defines the standard folder and file structure for encyclopaedic archiving of a D&D setting and its campaigns.

> **Adaptation Note**: If the workspace already holds an existing setting with equivalent folder names, respect and preserve the existing structure without forcibly renaming established files.

```text
├── README.md                                               # General world index and navigation guidelines
├── setting_structure.json                                  # Hierarchical map, metadata, and world taxonomy
├── SETTING_BIBLE.md                                        # Full source document / Master lore book
│
├── 01_cosmology/                                           # Tome I: Cosmology, metaphysics, planes, flow of magic, and ethics
│   ├── README.md                                           # Cosmological overview
│   ├── 01_planar_structure.md                              # Planes, celestial spheres, infernal or abyssal realms
│   ├── 02_seasons_and_celestial_mechanics.md               # Temporal dynamics, astronomical cycles, and planar transits
│   ├── 03_flow_of_magic_and_divine_order.md                # Nature of the arcane, theurgy, monopolies, and limitations
│   └── 04_moral_or_philosophical_system.md                 # Values, virtues, vices, or cosmic ethical code
│
├── 02_geography/                                           # Tome II: Physical geography, cartography, and regions
│   ├── README.md                                           # General geographical overview and territorial cross-sections
│   ├── 01_main_map_and_biomes.md                           # Territories, climates, and borders
│   ├── 02_subterranean_regions_and_abysses.md              # Underdark, rifts, and caverns
│   ├── 03_special_domains_and_connected_planes.md          # Suspended realms, gates, and liminal lands
│   └── regions/                                            # Dossiers per region/kingdom/province (with README.md)
│
├── 03_society_and_politics/                                # Tome III: Social, economic, and cultural model
│   ├── README.md                                           # Overview of the social order
│   ├── 01_social_philosophy_and_customs.md                 # Social values, ethics, and conventions
│   ├── 02_power_monopoly_and_economy.md                    # Military, trade, currency, and taxation
│   ├── 03_social_classes_and_roles.md                      # Civic stratification, guilds, and aesthetics
│   ├── 04_criminal_law_and_justice.md                      # Ordinary courts, penalties, and civil laws
│   └── customs_festivals_and_events/                       # Sub-series: customs, recurring festivals, and one-off events
│       ├── README.md                                       # Sub-series index by type
│       ├── customs/                                        # Everyday-life peculiarities (structures and manner)
│       │   ├── README.md
│       │   └── 01_<entry_slug>.md                          # Custom sheet (sequential numbering)
│       ├── festivals_and_occurrences/                      # Recurring institutional/ritual feasts and events
│       │   ├── README.md
│       │   └── 01_<entry_slug>.md                          # Festival/occurrence sheet (fixed or variable periodicity)
│       └── events/                                         # Inherently one-off peculiar events
│           ├── README.md
│           └── 01_<entry_slug>.md                          # Event sheet (historical or ongoing)
│
├── 04_law_and_succession/                                  # Tome IV: Fundamental laws, dynastic law, pacts, and treaties
│   ├── README.md                                           # Legal-institutional overview
│   ├── 01_contracts_pacts_and_treaties.md                  # Norms, formal alliances, and blood pacts
│   ├── 02_hierarchy_and_succession.md                      # Orders of succession, offices, and inheritance
│   └── 03_courts_and_disputes.md                           # Resolution of legal or hereditary disputes and rulings
│
├── 05_characters/                                          # Tome V: Player and Non-Player Character Roster
│   ├── README.md                                           # General character index and relationship matrix
│   ├── Player_Characters/                                  # PC Archive
│   │   ├── README.md                                       # Party overview and synergies
│   │   └── [Campaign_Name]/                                # Specific party/campaign folder
│   │       ├── README.md                                   # Party relationship hub
│   │       └── [PC_Name]/                                  # Modular PC dossier:
│   │           ├── README.md                               # Character summary and index
│   │           ├── 01_profile_and_traits.md                # Stats, species, class, traits
│   │           ├── 02_integrated_backstory.md              # History tied to world lore
│   │           ├── 03_relationships_and_dynamics.md        # Bonds with other PCs and NPCs
│   │           ├── 04_equipment_and_abilities.md           # Key items, feats, and abilities
│   │           └── 05_dm_hooks_and_secrets.md              # Narrative hooks reserved for the DM
│   └── Non_Player_Characters/                              # Setting NPC Archive
│       ├── README.md                                       # Index grouped by faction
│       └── [NPC_Name].md                                   # Sheet with role, temperament, secrets, and hooks
│
├── 06_locations/                                           # Tome VI: Notable locations and adventure hubs
│   ├── README.md                                           # List of points of interest and connections
│   └── [XX_location_name].md                               # Location sheet (atmosphere, hazards, NPCs, hooks)
│
├── 07_factions/                                            # Tome VII: Factions, noble houses, covens, and guilds
│   ├── README.md                                           # Geopolitical power map and conflicts
│   └── [XX_faction_name].md                                # Charter, hierarchy, alliances, resources, and aims
│
├── 08_unique_magic_items/                                  # Tome VIII: Artefacts, relics, and unique devices
│   ├── README.md                                           # Legal magic register and item index
│   └── [Item_Name].md                                      # Technical sheet, provenance, powers, and DM hooks
│
├── 09_chronicles/                                          # Tome IX: Chronicles and campaign minutes
│   ├── README.md                                           # Chronological index of all active campaigns
│   └── campaigns/
│       └── [campaign_name]/                                # Individual campaign folder
│           ├── README.md                                   # Hub: party roster, aim, session summary table
│           └── sessions/                                   # Numbered progressive minutes:
│               ├── README.md                               # Minutes index
│               ├── 01_session_title.md                     # Session 1 Minutes
│               └── 02_session_title.md                     # Session 2 Minutes...
│
└── 10_timeline/                                            # Tome X: Cross-cutting timeline and world chronology
    ├── README.md                                           # General legend: dates (world years), tags, navigation
    ├── historical_chronology/                              # Past events, files per epoch/period (with category tags)
    │   └── 01_<epoch_name>.md
    ├── occurrence_register/                                # Festival/event occurrences and evolving entries, per epoch/period
    │   └── 01_<period_name>.md
    ├── markwhen/                                           # Graphical timeline (Markwhen sources, excluded from Bible)
    │   ├── README.md                                       # Index of .mw sources and summary of conventions
    │   ├── general_timeline.mw                             # Index/legend (non-aggregated)
    │   ├── epochs/
    │   │   └── <epoch_name>.mw                             # Source per historical epoch/period
    │   └── campaigns/
    │       └── <campaign_name>.mw                          # Everything relevant to the campaign (with links to minutes)
    ├── calendar/                                           # World calendar: months, seasons, intercalary days, date mapping
    │   └── 01_calendar.md
    └── exports/                                            # Derived graphical renders (HTML/PNG/SVG/PDF of the timeline)
        └── README.md                                       # Register of derived graphical renders
```
