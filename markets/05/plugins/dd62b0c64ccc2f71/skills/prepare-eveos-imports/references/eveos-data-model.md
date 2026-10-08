# Modèle d'import Eveos

## Principes communs

- Une `key` est une référence externe stable. Toute clé existante est immuable.
- Les relations entre fichiers utilisent les clés externes, jamais les numéros de ligne.
- Plusieurs clés dans une cellule sont séparées par `;`, sauf indication contraire de la mission.
- Les valeurs d'une taxonomie utilisent les identifiants techniques Eveos, pas seulement leurs libellés humains.
- Les fichiers de travail et de production doivent rester de vrais fichiers `.xlsx` lorsque ce format est demandé.

## Dates et fuseau horaire

- Interpréter une date sans fuseau comme une date et une heure locales de l'événement.
- Importer l'heure civile attendue sur place, sans conversion vers GMT ou UTC.
- Lorsque la source contient explicitement UTC ou un décalage, convertir vers le fuseau du lieu de l'événement avant export.
- Ne jamais ajouter ou soustraire arbitrairement une heure en fonction du poste de travail ou du fuseau de l'agent.
- Conserver un résultat Excel sans fuseau lorsque le modèle Eveos attend une date locale, mais documenter toute conversion préalable.
- Si le lieu ou le fuseau est inconnu, l'inférer à partir des informations fiables de l'événement. Ne demander confirmation que si plusieurs lieux plausibles produisent des heures différentes.

## Conférences ou éléments de programme

Champs courants :

| Champ | Sens |
|---|---|
| `status` | `published` ou `draft` |
| `key` | Clé externe unique et stable |
| `salle` | Salle ou espace du programme |
| `debut` | Date et heure de début |
| `fin` | Date et heure de fin |
| `titre` | Intitulé public |
| `description` | Contenu source intégral |
| `description clean` | Contenu sans annonce des personnes référencées |
| Colonnes de taxonomie | Valeurs techniques autorisées par Eveos |
| `speakers` | Clés des intervenants séparées par `;` |

Ne pas considérer tous ces noms comme obligatoires dans la source. Les reconnaître sémantiquement, puis produire les en-têtes exigés par l'import cible.

## Speakers

Champs courants :

| Champ | Règle |
|---|---|
| `status` | Conserver la valeur existante ou utiliser une valeur autorisée |
| `key` | Immuable si existante ; unique si nouvelle |
| `prenom`, `nom` | Respecter l'identité fournie |
| `slug` | Stable, lisible et unique |
| `photo` | Laisser vide si l'identité ou le droit d'usage est incertain |
| `entreprise`, `poste` | Préserver l'existant ; compléter avec preuve |
| `description courte`, `biographie` | Rédiger à partir d'informations vérifiées |
| `email`, `telephone` | Ne pas inventer ni déduire |
| `site web`, `linkedin`, `twitter / x` | Utiliser uniquement une URL publique stable et attribuée sans ambiguïté |
| `tags` | Utiliser seulement si la mission définit leur sens |

Conserver séparément les sources utilisées pour les enrichissements lorsque le classeur ou le rapport le permet.

## Configuration du validateur

Exemple à adapter :

```json
{
  "conference_sheet": "2026 - Prod",
  "speaker_sheet": "Speakers 2026",
  "header_row": 1,
  "conference_columns": {
    "status": "status",
    "key": "key",
    "start": "debut",
    "end": "fin",
    "speakers": "speakers"
  },
  "speaker_columns": {
    "key": "key"
  },
  "allowed_statuses": ["published", "draft"],
  "event_start": "2026-11-04T00:00:00",
  "event_end": "2026-11-05T23:59:59",
  "event_timezone": "Europe/Paris",
  "timezone_mode": "event_local",
  "date_formats": ["%d/%m/%Y %H:%M"],
  "excel_date_number_format": "dd/mm/yyyy hh:mm",
  "max_duration_minutes": 180,
  "speaker_separator": ";",
  "taxonomies": {
    "Thématiques": ["valeur-technique-1", "valeur-technique-2"]
  },
  "required_taxonomies": ["Thématiques"],
  "allow_blank_dates_for_keys": [],
  "allow_blank_taxonomy_for_keys": {}
}
```
