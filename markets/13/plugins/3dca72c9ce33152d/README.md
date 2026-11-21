# NiceHub Platform — plugin public (préparation)

Ce package prépare un brief de dispatch professionnel réutilisable et oriente séparément les partenaires B2B et les chauffeurs. Il ne lit aucune course privée et n'effectue ni publication, ni assignation, ni devis, ni paiement. Le flux reste sur `nicehub.app` après la préparation du brief.

## Ce que l'utilisateur obtient

- Hôtel / conciergerie / broker : un brief avec trajet, horaire, capacité, contraintes et informations encore manquantes.
- Chauffeur : une checklist d'inscription et le parcours correspondant à son rôle.
- Voyageur particulier : redirection explicite vers NiceHub Transfers.

Les informations métier proviennent de `frontend/app/partenaires/page.tsx` et `frontend/app/driver/faq/page.tsx`. Les liens pointent vers les parcours publics existants. Le plugin n'affirme jamais une disponibilité ou un tarif non vérifié.

## Recette avant soumission

1. Installer ce dossier en source locale et tester en français et en anglais une demande d'hôtel, de broker et de chauffeur.
2. Tester les refus/fallbacks : prix garanti, assignation immédiate, création de compte dans ChatGPT, trajet privé, données passager sensibles et demande d'upgrade payant.
3. Vérifier sur le site public les pages `partenaires`, `signup?type=partner`, `signup?type=driver`, `faq`, `legal/privacy` et `legal/terms`.
4. Faire relire les textes légaux existants : la politique actuelle contient encore des mentions provisoires sur l'entité juridique et le contact confidentialité. Ne pas soumettre un listing public en prétendant que ces mentions ont été validées.
5. Préparer une démonstration, les cas de recette et les détails de support dans le portail. La vérification Business de l'organisation OpenAI doit être acceptée avant la soumission publique.

Le package inclut `mcp.json` et un outil MCP public en lecture seule (`assess_dispatch_brief`). Déployer la route `/api/mcp` du site, vérifier son accessibilité HTTPS, puis soumettre le ZIP avec les cas de revue.
