#!/usr/bin/env python3

# Atelier 02 - OUTHENIN Nicolas

# Usage python3 atelier_02.py


from datetime import date

prenom = input("Ton prénom : ")

age = input("Ton âge : ")

if(age.isdigit() == False):
    print("L'âge doit être un nombre entier.")
    exit(1)

annee = date.today().year - int(age)

print(f"Bonjour, {prenom}, tu as {age} ans, donc tu es né(e) vers {annee}.")