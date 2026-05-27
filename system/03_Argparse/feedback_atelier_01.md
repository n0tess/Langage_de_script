# Feedback — Atelier 1 (S03 Argparse, OUTHENIN Nicolas)

## Respect de la consigne

- `argparse` avec 3 arguments positionnels (deux floats + un opérateur via `choices`) ✓
- division par zéro gérée (stderr + `sys.exit(1)` quand fait correctement) ✓
- format de sortie type `a OP b = res` ✓

Conforme : main(), positionnels, division par zéro. Détail : le message d'erreur va sur stdout (pas `file=sys.stderr`). Le corrigé l'envoie sur stderr pour permettre de distinguer sortie normale et erreur.

---
*Évalué sur le commit `861e09f` (fichier `system/03_Argparse/atelier_01.py`).*
