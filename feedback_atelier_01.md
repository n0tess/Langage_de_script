# Feedback — Atelier 1 (Nicolas OUTHENIN)

## Respect de la consigne

Le script appelle `getaddrinfo` et affiche les informations, mais
plusieurs points ne correspondent pas à l'attendu :

- **Pas de séparation IPv4 / IPv6 dans deux blocs** : tu imprimes
  toutes les entrées dans une seule boucle. La consigne attend
  d'abord les IPv4, puis les IPv6.
- **Format de sortie inattendu** : tu imprimes
  `IPv4  -> ('142.250.179.110', 80)` (tuple complet). L'attendu est
  `IPv4 : 142.250.179.110` (juste l'adresse).
- **Port codé en dur à 80** : la consigne dit
  `socket.getaddrinfo(nom, None)` — pas besoin de port pour cet
  exercice. Avec `80`, tu vois le port apparaître dans `sockaddr`,
  ce qui pollue la sortie.
- **`type=socket.SOCK_STREAM`** : tu filtres pour éviter les
  doublons, comme certains autres. Astucieux pour le résultat, mais
  ça contourne la question pédagogique de la déduplication.
- **Total = `len(resultats)`** : cohérent *avec le filtre*, mais
  sans le filtre ce serait incorrect.

## Côté réseau

- Bonne lecture du tuple par dépaquetage nommé — c'est l'idiome
  attendu.
- L'expression conditionnelle `nom_famille = "IPv4" if … else "IPv6"`
  est correcte tant qu'il n'y a que deux familles ; sur un script
  plus général, un `match` ou un dict de mapping serait plus clair.

## Suggestion pour aligner sur la consigne

Adaptation minimale de ton code pour respecter le format attendu :

```python
import socket, sys

infos = socket.getaddrinfo(sys.argv[1], None)
ipv4, ipv6 = [], []

for famille, _t, _p, _c, sockaddr in infos:
    ip = sockaddr[0]
    if famille == socket.AF_INET and ip not in ipv4:
        ipv4.append(ip)
    elif famille == socket.AF_INET6 and ip not in ipv6:
        ipv6.append(ip)

for ip in ipv4: print(f"IPv4 : {ip}")
for ip in ipv6: print(f"IPv6 : {ip}")
print(f"Total : {len(ipv4) + len(ipv6)} enregistrement(s)")
```

## Côté Python (à titre indicatif)

- Pas de fonction `main()` ni de garde — pas grave sur 16 lignes.
- Pas de validation de `len(sys.argv)` ni de gestion de
  `socket.gaierror`.

---
*Évalué sur le commit `c1751f0` (fichier `00_Concepts/atelier_01.py`).*
