# Feedback — Atelier 7 (Nicolas OUTHENIN)

## Respect de la consigne

Très bien :

- octets bruts ✓
- valeur 1 big-endian via `int.from_bytes(valeur, "big")` ✓
- valeur 2 little-endian ✓
- valeur 3 inversion + big-endian ✓
- réponse correcte et concise : « Lire des octets en
  little-endian revient à inverser leur ordre puis les lire en
  big-endian. » ✓

**Manquant** : la vérification automatique
(`assert little == inverse_big`). La consigne demande de vérifier.

L'import `sys` est inutile (tu ne l'utilises pas).

## Côté Python (à titre indicatif)

- Code lisible.
- Pas de fonction `main()` ni de garde — pas grave sur 22
  lignes.

---
*Évalué sur le commit `579fbdb` (fichier `network/00_Concepts/atelier_07.py`).*
