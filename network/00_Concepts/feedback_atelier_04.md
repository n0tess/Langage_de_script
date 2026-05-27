# Feedback — Atelier 4 (Nicolas OUTHENIN)

## Respect de la consigne

Très bien :

- `socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM)` ✓
  (paramètres explicites — bonne pratique de documentation)
- `with s1, s2:` ✓
- `fileno()`, `getsockname()`, `getpeername()` imprimés ✓
- Réponse à la question : « Les adresses sont vides car nous
  utilisons un socket UNIX. Anonyme signifie qu'il n'y a pas
  d'adresse associée au socket, contrairement à un socket TCP/IPv4
  classique qui a une adresse IP et un port associés. »

La réponse est juste mais peut être enrichie :

- pourquoi *exactement* les adresses Unix sont vides : aucun
  `bind` n'a été appelé sur un chemin de fichier (par exemple
  `/tmp/foo.sock`). Si on faisait `bind(...)`, on aurait une
  adresse non vide.
- conséquence pratique d'« anonyme » : aucun processus tiers ne
  peut s'y connecter par nom. C'est exactement la propriété qui
  rend `socketpair` utile pour de la communication privée.

## Côté Python (à titre indicatif)

- Pas de fonction `main()` — pas grave sur 23 lignes.
- Code lisible.

---
*Évalué sur le commit `579fbdb` (fichier `network/00_Concepts/atelier_04.py`).*
