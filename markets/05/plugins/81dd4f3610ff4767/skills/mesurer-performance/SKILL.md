---
name: mesurer-performance
description: Use when performance, resource use, latency, throughput, or regression is a material part of the problem or acceptance criteria.
---
# Mesurer la performance

## Fonction
Optimiser seulement ce qui est mesuré.

## Procédure
1. Définir scénario, métrique et environnement reproductibles.
2. Établir une baseline avec plusieurs mesures lorsque la variance compte.
3. Profiler ou instrumenter le goulot réellement dominant.
4. Modifier une cause à la fois autant que possible.
5. Re-mesurer dans les mêmes conditions et comparer statistiquement si nécessaire.
6. Fixer un budget de régression lorsqu’une limite durable a une fonction.

## Preuve
Le gain ou la régression est établi par comparaison reproductible, pas par impression.