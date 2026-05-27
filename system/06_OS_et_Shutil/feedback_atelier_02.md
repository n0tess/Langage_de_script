# Feedback — S06 Atelier 2 (Backup horodaté, OUTHENIN Nicolas)

## Respect de la consigne

Critères attendus : `shutil.copytree(src, dst)` vers `backup_<strftime YYYYMMDD_HHMMSS>/` à côté du source

Constat sur ton code :

- ✓ `shutil.copytree` (préserve métadonnées)
- ✓ `strftime` pour l'horodatage
- ✓ nommage `backup_<timestamp>`
- ✓ gestion d'erreur sur dossier existant

---
*Évalué sur le commit `f98c3b7` (fichier `system/06_OS_et_Shutil/atelier_02.py`).*
