# Feedback — Atelier 2 (Nicolas OUTHENIN)

## Respect de la consigne

Très bien :

- les trois sockets demandés (TCP, UDP, AF_UNIX) dans un `with`
  parenthésé multi-lignes (Python 3.10+) — l'idiome moderne,
- `fileno()`, `family.name`, `type.name` imprimés pour chacun via
  une boucle sur la liste `[s, s2, s3]`,
- la question est répondue : descripteur unique par socket.

L'explication peut être plus précise : ce n'est pas que « le
socket ne pourra pas être créé », c'est que le noyau **alloue le
plus petit entier libre** dans la table des descripteurs du
processus. Il ne peut pas y avoir deux ressources qui partagent
le même slot ; donc avec trois sockets coexistants, on a trois
slots distincts.

## Côté Python (à titre indicatif)

- Très propre, lisible.
- Petit détail : la variable du loop s'appelle `i`, ce qui suggère
  un entier (un index). Comme c'est en réalité un socket, `s` ou
  `sock` serait plus parlant.

---
*Évalué sur le commit `c1751f0` (fichier `00_Concepts/atelier_02.py`).*
