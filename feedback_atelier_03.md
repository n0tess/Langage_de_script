# Feedback — Atelier 3 (Nicolas OUTHENIN)

## Respect de la consigne

Très bien :

- argparse `--protocole tcp|udp` requis ✓
- TCP : `with` + `settimeout(1)` + `ConnectionRefusedError` →
  « TCP : connexion refusée » ✓
- UDP : `with` + `settimeout(1)` + `sendto` → message conforme
  + nombre d'octets en bonus ✓
- structure `main()` + garde — bonne pratique.

Petit point : tu utilises `else:` plutôt qu'`elif args.protocole == "udp":`.
Cela fonctionne grâce à `choices=["tcp","udp"]` qui restreint
argparse aux deux valeurs. Pratique défensive : préférer
`elif` quand on n'est pas certain.

La note de fin (`# Pour lancer le script : ...`) avec la typo
`upd` au lieu de `udp` — détail à corriger.

## Côté Python (à titre indicatif)

- Pas de docstring de module.
- Le timeout est posé après l'entrée dans le `with` — c'est
  correct (et même la pratique habituelle).
- Code compact et lisible.

---
*Évalué sur le commit `c1751f0` (fichier `00_Concepts/atelier_03.py`).*
