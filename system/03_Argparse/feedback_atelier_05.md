# Feedback — Atelier 5 (S03 Argparse, OUTHENIN Nicolas)

## Respect de la consigne

- argument positionnel `valeur` (type `float`) ✓
- drapeaux `--from` / `--to` avec `dest="depuis"`/`"vers"` (pour
  éviter les mots-clés Python) ✓
- `choices=["celsius", "fahrenheit", "kelvin"]` ✓
- `--precision` avec valeur par défaut 2 ✓
- format de sortie `<valeur> <unité> = <valeur> <unité>` avec
  précision dynamique ✓

**Bug** : `--from` et `--to` sans `required=True` → si l'utilisateur les omet, `args.depuis`/`args.vers` valent `None` et le `if/elif` ne couvre aucun cas → `celsius`/`resultat` non définis → NameError. À ajouter : `required=True` sur les deux drapeaux.

---
*Évalué sur le commit `861e09f` (fichier `system/03_Argparse/atelier_05.py`).*
