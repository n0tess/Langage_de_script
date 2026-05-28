#!/usr/bin/env python3

# Atelier 3 - OUTHENIN Nicolas

# Usage python3 atelier_03.py

import secrets
import tempfile
from pathlib import Path

token = secrets.token_urlsafe(32)

with tempfile.TemporaryDirectory() as tmpdir:
    env_path = Path(tmpdir) / ".env"

    contenu = f"TOKEN={token}\n"
    env_path.write_text(contenu, encoding="utf-8")

    ligne = env_path.read_text(encoding="utf-8").strip()

    cle, _, valeur = ligne.partition("=")

    identique = secrets.compare_digest(token, valeur)

    print(f"fichier .env : {env_path}")
    print(f"contenu      : {ligne}")
    print(f"lu           : {valeur}")
    print(f"identique    : {identique}")