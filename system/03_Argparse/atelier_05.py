#!/usr/bin/env python3

# Atelier 5 - OUTHENIN Nicolas

# Usage python3 atelier_05.py temperature --from celsius|fahrenheit|kelvin --to celsius|fahrenheit|kelvin [--precision N]

import argparse

def main():
    parser = argparse.ArgumentParser(
        prog="mon_script_conversion",
        description="Convertisseur de température.",
    )

    parser.add_argument("temperature", type=float)
    parser.add_argument("--from", dest="depuis", choices=["celsius", "fahrenheit", "kelvin"])
    parser.add_argument("--to", dest="vers", choices=["celsius", "fahrenheit", "kelvin"])
    parser.add_argument("--precision", type=int, default=2)

    args = parser.parse_args()

    if args.depuis == "celsius":
        celsius = args.temperature

    elif args.depuis == "fahrenheit":
        celsius = (args.temperature - 32) * 5 / 9

    elif args.depuis == "kelvin":
        celsius = args.temperature - 273.15

    if args.vers == "celsius":
        resultat = celsius
    
    elif args.vers == "fahrenheit":
        resultat = celsius * 9 / 5 + 32

    else:
        resultat = celsius + 273.15

    print(f"{args.temperature:.{args.precision}f} {args.depuis} = "
          f"{resultat:.{args.precision}f} {args.vers}"
    )

if __name__ == "__main__":
    main()