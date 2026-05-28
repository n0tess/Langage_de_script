# Feedback — S08 Atelier 5 (Mini `which`, OUTHENIN Nicolas)

## Respect de la consigne

Critères attendus : `subprocess.run(["which", nom])`, gérer code retour 0/!=0, gérer `FileNotFoundError` (which absent)

Constat sur ton code :
- ✓ `subprocess.run(["which", nom], capture_output=True, text=True)` conforme.
- ✓ Branche `returncode == 0` : chemin imprimé avec `.strip()`.
- ✓ Branche `returncode != 0` : `<nom> : introuvable` + `sys.exit(1)`.
- ✓ `FileNotFoundError` capturé avec message et `sys.exit(1)`.
- ⚠ Message du `FileNotFoundError` imprimé sur stdout au lieu de stderr.
- ⚠ Bug ligne 13 : `print("Usage: ...", repr(resulat.stderr))` — `resulat` n'existe pas dans ce scope, `NameError` si `sys.argv` est trop court. Le message d'usage est imprimé sur stdout au lieu de stderr.
- ✓ Bonus usage : présent mais cassé (cf. ci-dessus).
- ⚠ Pas de `timeout` (bonus optionnel).

---
*Évalué sur le commit `a460121` (fichier `system/08_Sous_processus/atelier_05.py`).*
