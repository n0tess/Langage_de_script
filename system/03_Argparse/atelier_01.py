#!/usr/bin/env python3 

# Atelier 1 - OUTHENIN Nicolas

# Usage python3 atelier_01.py

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        prog="mon_script_calculatrice",
        description="Une calculatrice minimale.",
    )

    parser.add_argument("nombre_1")
    parser.add_argument("operateur", choices=["+", "-", "*", "/"])
    parser.add_argument("nombre_2")

    args = parser.parse_args()

    args.nombre_1 = float(args.nombre_1)
    args.nombre_2 = float(args.nombre_2)

    if args.operateur == "+":
        print(f"{args.nombre_1} + {args.nombre_2} = {args.nombre_1 + args.nombre_2}")
    elif args.operateur == "-":
        print(f"{args.nombre_1} - {args.nombre_2} = {args.nombre_1 - args.nombre_2}")
    elif args.operateur == "*":
        print(f"{args.nombre_1} * {args.nombre_2} = {args.nombre_1 * args.nombre_2}")
    elif args.operateur== "/":
        if args.nombre_2 != 0:
            print(f"{args.nombre_1} / {args.nombre_2} = {args.nombre_1 / args.nombre_2}")
        else:
            print("Erreur : division par zéro")
            sys.exit(1)

if __name__ == "__main__":
    main()