# Feedback — Atelier 8 (Nicolas OUTHENIN)

## Respect de la consigne

Très bien :

- `socket.socketpair()` + `with` ✓
- test 1 : `settimeout(0.2)` + `recv` + `socket.timeout` + mesure ✓
- test 2 : `setblocking(False)` + `recv` + `BlockingIOError` +
  mesure ✓
- affichage en millisecondes ✓
- **réponse correcte** : « recv() attend indéfiniment […] il
  faudrait un timeout ou une autre tâche qui envoie des
  données » ✓

C'est concis et juste. Petite précision : pour aller au bout
de la réponse, on dirait « un autre **thread/processus** qui
envoie » (la concurrence) — c'est l'argument central.

Petite typo : « (san timeout) » → « (sans timeout) ».

## Côté Python (à titre indicatif)

- Pas de fonction `main()` ni de garde — pas grave sur 39
  lignes.
- Code lisible.
- `socket.timeout` est un alias historique de `TimeoutError`.

---
*Évalué sur le commit `4003ee4` (fichier `00_Concepts/atelier_08.py`).*
