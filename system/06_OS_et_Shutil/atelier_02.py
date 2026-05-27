#!/usr/bin/env python3

# Atelier 2 - OUTHENIN Nicolas

# Usage python3 atelier_02.py 

import shutil
import argparse
from datetime import datetime
from pathlib import Path

def count_files(directory: Path) -> int:
    return sum(1 for p in directory.rglob("*") if p.is_file())

def main():
    parser = argparse.ArgumentParser(
        prog="mon_script_backup",
        description="Backup et ajoute un horodatage",
    )

    parser.add_argument("chemin", type=str)

    args = parser.parse_args()
    
    src = Path(args.chemin).resolve()

    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")

    dst = src.parent / f"backup_{timestamp}"

    if dst.exists():
        raise FileExistsError(f"Le dossier de destination {dst} existe déjà.")

    shutil.copytree(src, dst)

    nb_fichiers = count_files(dst)

    print(f"Backup créé : {dst}")
    print(f"Fichiers copiés : {nb_fichiers}")


if __name__ == "__main__":
    main()
