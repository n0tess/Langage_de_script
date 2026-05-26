# Atelier 7 - OUTHENIN Nicolas

# Usage python3 atelier7.py

import struct
import sys

valeur = b"\x00\x00\x00\x2A"

print(f"big-endian : {int.from_bytes(valeur, "big")}")
print(f"little-endian : {int.from_bytes(valeur, "little")}")

print(f"big-endian : {int.from_bytes(inverse, "big")}")

# Pourquoi les valeurs 2 et 3 sont identiques ? 

# 