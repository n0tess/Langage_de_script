# Feedback — S13 Atelier 3 (Token URL-safe, OUTHENIN Nicolas)

## Respect de la consigne

Critères attendus : `secrets.token_urlsafe(32)`, écriture/relecture dans un `.env` temporaire, comparaison via `secrets.compare_digest`

Constat sur ton code :
- ✓ `secrets.token_urlsafe(32)` utilisé.
- ✓ `tempfile.TemporaryDirectory()` avec `Path(tmpdir) / ".env"`, écriture `TOKEN={token}\n`.
- ✓ Relecture via `read_text().strip()`, extraction `cle, _, valeur = ligne.partition("=")`.
- ✓ `secrets.compare_digest(token, valeur)` — parfait.
- ⚠ Mineur : pas de `main()`/`if __name__ == "__main__"`, tout est au niveau module. Ça marche, mais c'est l'habitude à prendre pour rendre le script importable proprement.

Sinon, code court et conforme.

---
*Évalué sur le commit `294ee38` (fichier `system/13_Boite_a_outils/atelier_03.py`).*
