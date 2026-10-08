---
name: appeler-passerelle
description: Use when a prepared Continuum mission or message must actually traverse the local Passerelle through Noyau.
---
# Appeler la Passerelle

## Préconditions
- mission et courrier préparés ;
- route réellement résolue ;
- Noyau et capacité locale pré-volés ;
- contrat local courant vérifié ;
- identité d’opération stable créée lorsque le rejeu pourrait produire un doublon.

## Procédure
1. Résoudre le contrat de Passerelle réellement exposé par Noyau ; ne pas traiter `AppelPasserelle_V1` comme vérité normative éternelle.
2. Si ce contrat est bien le contrat courant, produire le PUSH autonome dans sa grammaire exacte, sans prose ajoutée.
3. Distinguer émission du PUSH, réception, CREATE, travail du Magister, PULL, retour observé et effet final.
4. Ne jamais confondre signal et matière transportée.
5. En cas de doute sur l’effet, appliquer `gerer-transactions` et rechercher l’état réel avant rejeu.

## Preuve
Le niveau exact atteint par la circulation est observé ou explicitement borné.