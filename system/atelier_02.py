# Atelier 02 - OUTHENIN Nicolas

# Usage python3 atelier_02.py

#!/usr/bin/env python3

from datetime import date

prenom = input("Ton prénom : ")

age = input("Ton âge : ")

annee = date.today().year - int(age)

print(f"Bonjour, {prenom}, tu as {age} ans, donc tu es né(e) vers {annee}.")