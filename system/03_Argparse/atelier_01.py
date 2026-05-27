#!/usr/bin/env python3 

# Atelier 1 - OUTHENIN Nicolas

# Usage python3 atelier_01.py x {+,-,*,/} y

import argparse
import sys

def main():
    parser = argparse.ArgumentParser(
        prog="mon_script_calculatrice",
        description="Une calculatrice minimale.",
    )

    parser.add_argument("nombre_1", type=float)
    parser.add_argument("operateur", choices=["+", "-", "*", "/"])
    parser.add_argument("nombre_2", type=float)

    args = parser.parse_args()

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