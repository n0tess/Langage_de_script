#!/usr/bin/env python3

# Atelier 02 - OUTHENIN Nicolas

# Usage python3 atelier_02.py


from datetime import date

prenom = input("Ton prénom : ")

if(prenom.isalpha() == False) or not prenom:
    print("Le prénom doit être composé de lettres uniquement et celui-ci ne doit pas être vide.")
    exit(1)

age = input("Ton âge : ")

if(age.isdigit() == False) or not age:
    print("L'âge doit être un nombre entier et celui-ci ne doit pas être vide.")
    exit(1)

annee = date.today().year - int(age)

print(f"Bonjour, {prenom}, tu as {age} ans, donc tu es né(e) vers {annee}.")