#!/usr/bin/env python3

# Atelier 3 - OUTHENIN Nicolas

# Usage python3 atelier_03.py 

import tarfile
import tempfile
from pathlib import Path 

def main():
    with tempfile.TemporaryDirectory() as tmp:
        racine = Path(tmp) 

        projet = racine / "projet"
        (projet / "src").mkdir(parents=True)

        (projet / "src" / "main.py").write_text("print('Hello world!')\n", encoding="utf-8")

        (projet / "src" / "utils.py").write_text("def add(a, b):\n    return a + b\n", encoding="utf-8")

        (projet / "README.md").write_text("# Mon projet\n", encoding="utf-8")

        archive = racine / "projet.tar.gz"
        with tarfile.open(archive, "w:gz") as tar:
            tar.add(projet, arcname="projet")

        print(f"Archive créée : {archive}")

        cible = racine / "cible"
        cible.mkdir(parents=True, exist_ok=True)    

        with tarfile.open(archive, "r:gz") as tar:
            tar.extractall(cible, filter="data")

        print(f"Fichiers extraits dans : {cible}")

        for fichier in cible.rglob("*"):
            if fichier.is_file():
                print(f"Fichier extrait : {fichier.relative_to(cible)}")

if __name__ == "__main__":
    main()  

        