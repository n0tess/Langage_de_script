#!/usr/bin/env python3

# Atelier 3 - OUTHENIN Nicolas

# Usage python3 atelier_03.py "phrase à ajouter en fin du fichier app.log"

import argparse
import datetime

def main():
    parser = argparse.ArgumentParser(
        prog="mon_script_ajout_log",
        description="Ajoute une phrase à la fin du fichier app.log.",
    )

    parser.add_argument("message", type=str)

    horodatage = datetime.datetime.now().isoformat(timespec="seconds")

    args = parser.parse_args()

    with open("app.log", "a") as f:
        f.write(f"{horodatage} {args.message}\n")

if __name__ == "__main__":
    main()
    

