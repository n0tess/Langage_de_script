# Atelier 7 - OUTHENIN Nicolas

# Usage python3 atelier7.py

import struct
import sys

valeur = b"\x00\x00\x00\x2A"

big = int.from_bytes(valeur, "big")
little = int.from_bytes(valeur, "little")

inverse = valeur[::-1]
inverse_big = int.from_bytes(inverse, "big")

print(f"big-endian : {big}")
print(f"little-endian : {little}")
print(f"octets inversés puis big-endian : {inverse_big}")

# Pourquoi les valeurs 2 et 3 sont identiques ? 

# Lire des octets en little-endian revient à inverser leur ordre puis les lire en big-endian. 