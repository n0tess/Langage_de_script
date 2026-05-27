# Feedback — Atelier 2 (Nicolas OUTHENIN)

> **Note du formateur (mise à jour 2026-05-27)** : la présence ou
> l'absence de `AF_UNIX` n'est **plus prise en compte** dans la
> notation. Plusieurs étudiants travaillent sous Windows où cette
> famille de sockets n'est pas (ou peu) supportée. Les remarques
> ci-dessous qui critiquaient l'absence ou le remplacement de
> `AF_UNIX` (par `AF_INET6` notamment) sont à considérer comme
> **caduques**.


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
*Évalué sur le commit `579fbdb` (fichier `network/00_Concepts/atelier_02.py`).*
