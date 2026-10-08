---
name: gerer-livrables
description: Use whenever the request produces an executable or non-executable deliverable whose installation, upgrade, one-shot execution, packaging, or handoff must match its real function.
---
# Gérer les livrables

## Procédure
1. Qualifier le livrable : installation durable, exécution ponctuelle ou non exécutable.
2. Ne jamais inventer installation, migration, désinstallation ou mise à niveau lorsque la fonction ne l’exige pas.
3. Pour une installation durable, prévoir identité stable, reconnaissance de l’état précédent, préservation des données, remplacement cohérent, récupération et tests première installation + mise à niveau.
   Appliquer le contrat complet de `10 — Livraison et acceptation.md` : exécution directe depuis Téléchargements sans préparation manuelle, détection indépendante de l’ancien fichier téléchargé, sauvegarde avant destruction, migration des réglages et données, remplacement de l’état installé, récupération explicite en cas d’échec et un seul état courant fonctionnel. Les versions restent des métadonnées et ne deviennent pas une tâche manuelle d’Axel.
4. Pour une exécution ponctuelle, livrer un état directement utilisable sans fausse infrastructure de maintenance.
5. Pour tout livrable, appliquer `verifier-acceptation` avant l’état PRÊT.
   Les contrôles portent sur les frontières utiles au bénéficiaire ; une exécution ponctuelle clairement réussie peut suffire. Ne pas simuler une infrastructure durable absente du besoin.

## Preuve
Le régime choisi correspond à la fonction réelle et le livrable est utilisable depuis son état de remise.
