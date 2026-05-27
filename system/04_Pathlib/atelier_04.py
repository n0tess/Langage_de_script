#!/usr/bin/env python3

# Atelier 4 - OUTHENIN Nicolas

# Usage python3 atelier_04.py 

from pathlib import Path

def decomposer(chemin: str) -> tuple[str, str, str]:
    p = Path(chemin)

    dossier = str(p.parent)
    nom_sans_extension = p.stem
    extension = p.suffix

    return (dossier, nom_sans_extension, extension)

def main():
    exemples = [
        "tmp/a.txt",
        "var/log/archive.tar.gz",
        "/etc/hosts",
    ]

    for chemin in exemples:
        resultat = decomposer(chemin)
        print(f"{chemin:<30} -> {resultat}")


if __name__ == "__main__":
    main()  