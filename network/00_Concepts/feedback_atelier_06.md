# Feedback — Atelier 6 (Nicolas OUTHENIN)

## Respect de la consigne

Très bien :

- `recv_exact` (variante de `recv_exactement`) correct, gère
  `recv` partiels et EOF ✓
- `envoyer_message` : préfixe 4 octets big-endian + `sendall` ✓
- `recevoir_message` : lit 4 octets, décode, lit la quantité ✓
- test avec `socketpair` dans un `with`, 3 messages ✓

Vérification post-réception : tu imprimes les trois messages
sans comparaison explicite. Un `assert` rendrait le test
auto-vérifiable.

Pour la cohérence avec le corrigé et les autres ateliers, le nom
de la helper reste `recv_exactement` (ton choix `recv_exact` est
plus court mais légèrement différent du nommage de référence).

## Côté Python (à titre indicatif)

- Annotations de type — bonne pratique.
- Code propre et lisible.
- Pas de fonction `main()` ni de garde — pas grave sur 40
  lignes.

---
*Évalué sur le commit `579fbdb` (fichier `network/00_Concepts/atelier_06.py`).*
