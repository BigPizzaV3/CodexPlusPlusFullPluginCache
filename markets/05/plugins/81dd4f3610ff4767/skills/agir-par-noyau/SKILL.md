---
name: agir-par-noyau
description: Use when a Continuum task requires a real local effect, observation, or execution through Noyau or capabilities exposed by Continuum’s registered MCP app.
---
# Agir par Noyau

## Fonction
Porter uniquement la branche d’effet local du Continuum. Noyau reste un logiciel distinct du plugin ; la Passerelle et les relais d’appareils restent des composants de Noyau.

## Déclenchement
Un résultat exige réellement un effet ou une observation locale que les capacités natives déjà disponibles ne produisent pas entièrement.

## Protocole opératoire
1. Appeler `resoudre-autorite` puis `prevol-capacites` sur Noyau et sur la fonction exacte requise.
2. Résoudre la capacité réellement chargée : outil natif autorisé, App MCP Continuum enregistrée et joignable, MCP local de Noyau, API locale de Noyau ou autre capacité locale prouvée ; ne jamais supposer qu’un chemin existe parce qu’il est décrit dans le plugin.
3. Préparer une identité d’opération et appeler `gerer-transactions` si un rejeu pourrait produire un effet matériel.
4. Exécuter uniquement l’effet nécessaire ; distinguer commande, réception, exécution, effet et retour observé.
5. Sur interruption récupérable, appeler `gerer-reprise` ; sur état ambigu, rechercher l’effet réel avant rejeu.
6. Pour une mission de Magister Operis transitant par la Passerelle, déléguer la grammaire et le contrat à `appeler-passerelle`.
7. Pour une action sur Android, déléguer la spécialisation à `piloter-android`.
8. Vérifier l’effet local avant de le présenter comme réussi.

## Interdits
- ne jamais passer par Noyau lorsqu’une capacité native produit complètement le résultat sans effet local nécessaire ;
- ne jamais figer adresse, port, chemin, jeton, certificat ou contrat Passerelle dans ce Skill ;
- ne jamais confondre présence du plugin, installation de Noyau et capacité opérationnelle ;
- ne jamais exposer une API locale de contrôle comme surface publique par simple commodité.

## Preuve de réussite
L’effet local exact est observé ou explicitement borné, avec identité et état de transaction lorsqu’ils sont matériels.

## Arrêt
S’arrêter avant effet si la capacité requise n’est pas suffisamment accessible, autorisée, opérationnelle ou compatible.