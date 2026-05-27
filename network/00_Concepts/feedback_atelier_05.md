# Feedback — Atelier 5 (Nicolas OUTHENIN)

## Respect de la consigne

Très bien :

- `recv_ligne(sock) -> bytes` lit octet par octet, gère EOF (`b""`)
  et `\n` séparément ✓
- délimiteur non inclus ✓
- test avec `socketpair` dans un `with`, envoi correct, deux
  appels `recv_ligne` ✓

**Réponse au bonus à enrichir** : tu dis « une structure de
données plus efficace serait une liste de bytes ». Mais ce n'est
pas l'idée principale — le problème n'est pas la structure
**d'accumulation** (la liste de morceaux fait déjà ce job), c'est
le **nombre d'appels système**. La structure optimisée est un
**buffer persistant entre les appels** (`bytearray`), dans
lequel on lit par blocs (`recv(4096)`) puis on cherche `\n` avec
`.find()`. Ainsi on fait 1 appel système par bloc, pas par octet.

## Côté Python (à titre indicatif)

- Code propre.
- Pas de fonction `main()` ni de garde — pas grave sur 27
  lignes.

---
*Évalué sur le commit `579fbdb` (fichier `network/00_Concepts/atelier_05.py`).*
