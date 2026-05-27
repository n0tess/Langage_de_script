# Feedback — Atelier 5 (R03 Socketserver, Nicolas OUTHENIN)

## Respect de la consigne

Bien :

- `ServeurMultiClient(socketserver.ThreadingMixIn, socketserver.TCPServer)`
  avec mixin en premier ✓
- `allow_reuse_address` ✓
- `BonjourHandler(StreamRequestHandler)` ✓
- `time.sleep(2)` ✓
- log de réception ✓
- `with` + `serve_forever()` ✓

## Côté Python (à titre indicatif)

- L'indentation de `def handle(self)` est de **6 espaces** au
  lieu de 4 (par rapport au début du `class BonjourHandler`).
  Fonctionne en Python (peu importe pour autant que ce soit
  cohérent dans le bloc) mais c'est inhabituel ; `black` ou un
  formateur uniformiserait.

---
*Évalué sur le commit `d02705c` (fichier `network/03_Socketserver/atelier_05.py`).*
