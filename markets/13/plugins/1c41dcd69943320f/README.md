# NiceHub Services — Plugin OpenAI / ChatGPT

Ce package permet d'intégrer **NiceHub Services** (Artisans BTP & Dépannage en France métropolitaine et en Corse) dans ChatGPT.

## Rôles pris en charge

1. **Clients / Particuliers :** Préparation d'une demande de dépannage ou de travaux parmi 16 métiers. L'outil fournit un lien qui reprend le besoin, la ville et l'urgence renseignés ; la demande est vérifiée puis déposée sur le site.
2. **Artisans du BTP :** Présentation de l'inscription professionnelle, sans garantie de volume de demandes, avec accès direct à la création de compte ou à la page d'information.

## Structure du package

- `plugin.json` : Manifest officiel OpenAI (métadonnées, liens légaux, prompts par défaut).
- `skills/nicehub-services/SKILL.md` : Consignes concises et humaines pour ChatGPT.
- `REVIEW_CASES.md` : Cas de test positifs et négatifs pour la review OpenAI.
- `assets/icon.png` : Emblème officiel Orange Chrome.
