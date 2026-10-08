---
name: produire-commandes
description: Use when a Continuum need must be satisfied by a shell command, script, executable block, repair command, installation command, or other technical one-shot instruction.
---
# Produire des commandes

## Fonction
Produire une instruction exécutable dans le runtime réel, bornée à son effet et accompagnée d’un critère de preuve.

## Protocole opératoire
1. Résoudre objectif, shell/runtime, environnement cible, périmètre, privilèges, entrées, chemins, effets, réversibilité et preuve attendue.
2. Si une valeur indispensable manque, retourner un besoin de preuve au lieu d’inventer un placeholder présenté comme exécutable.
3. Appeler `prevol-capacites` puis le spécialiste adapté : `executer-powershell`, `agir-par-noyau` ou `piloter-android` selon le Réel.
4. Pour une correction après échec, déléguer d’abord à `corriger-et-reprendre`; ce Skill n’invente pas le diagnostic.
5. Avant suppression, remplacement ou migration, préférer un préflight non destructif et utiliser `gerer-transactions` si le rejeu peut produire un double effet.
6. Ne jamais exposer secret, jeton ou clé privée dans un bloc lorsqu’un canal sûr existe.
7. Fournir une seule voie active par bloc; quoter et échapper selon le runtime exact.
8. Éviter téléchargement + exécution opaque; vérifier source et intégrité lorsqu’un téléchargement est réellement nécessaire.
9. Un code de sortie réussi ne prouve pas à lui seul l’effet métier; utiliser `prouver-resultat` ou `qualifier-preuve` pour l’effet réel.
10. Aucun reboot, élévation, arrêt de service ou effet externe irréversible n’est caché dans une commande.

## Preuve
Le bloc correspond au runtime et aux chemins réels, ses effets sont bornés et le succès possède une observation suffisante au-delà de la simple absence d’erreur.
