# Feedback — S05 Atelier 3 (Journal horodaté, OUTHENIN Nicolas)

## Respect de la consigne

Critères attendus : fonction `journaliser(chemin, message)` qui ouvre le fichier en mode `"a"`
et écrit `<horodatage ISO> <message>` (datetime.now().isoformat())

Constat sur ton code :

- ✓ ouverture en mode append (`'a'`)
- ✓ utilisation de `datetime`
- ⚠ pas d'encoding explicite

---
*Évalué sur le commit `c7138e1` (fichier `system/05_Fichiers/atelier_03.py`).*
