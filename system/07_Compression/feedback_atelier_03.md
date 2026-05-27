# Feedback — S07 Atelier 3 (Extraire un .tar.gz en sécurité, OUTHENIN Nicolas)

## Respect de la consigne

Critères attendus : création d'une archive `.tar.gz` factice dans un tempfile, extraction avec
`tar.extractall(cible, filter="data")`, listage du résultat

Constat sur ton code :

- ✓ création d'archive `.tar.gz` avec `tarfile.open(..., 'w:gz')`
- ✓ `filter='data'` pour extraction sécurisée
- ✓ `tempfile` pour le dossier temporaire
- ✓ listage du résultat avec `(r)glob`

---
*Évalué sur le commit `0605efc` (fichier `system/07_Compression/atelier_03.py`).*
