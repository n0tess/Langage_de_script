#!/usr/bin/env python3

# Atelier 5 - OUTHENIN Nicolas

# Usage python3 atelier_05.py

import subprocess
import sys

def main():
    
    if len(sys.argv) < 2:
        print("Usage: python3 atelier_05.py <nom_du_programme>", repr(resulat.stderr))
        sys.exit(2)
    
    nom = sys.argv[1]

    try:
        resulat = subprocess.run(["which", nom], capture_output=True, text=True)

        if resulat.returncode == 0:
            print(f"{nom} : {resulat.stdout.strip()}")
        else:
            print(f"{nom} : introuvable")
            sys.exit(1)

    except FileNotFoundError:
        print("La commande 'which' est introuvable")
        sys.exit(1)
    
if __name__ == "__main__":
    main()
