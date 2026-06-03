# Examen - Langage de Script - 03/06/2026 

## Choix du protocole : 

J'ai choisi d'utiliser l'option C JSON ligne car il est directement valide avec Pydantic et permet une communication simple entre client et serveur. De plus, il est facilement lisible et débogable

## Installation de Whois : 

```
sudo apt update && sudo apt install whois -y
```

## Usage : 

### Installation des requirements.txt 

```
pip install -r requirements.txt
```

### Fichier OUTHENIN_Nicolas_exam_serveur.py 

```
python3 OUTHENIN_Nicolas_exam_serveur.py [-v|-vv|-vvv] serve 
```

### Fichier OUTHENIN_Nicolas_exam_client.py 

```
python3 OUTHENIN_Nicolas_exam_client.py record mines-ales.fr
```

```
python3 OUTHENIN_Nicolas_exam_client.py search mines-ales.fr
```

```
python3 OUTHENIN_Nicolas_exam_client.py list
```

```
python3 OUTHENIN_Nicolas_exam_client.py count
```

## Informations 

### Serveur 

La base de données est créée automatique lors de son premier lancement. De plus, le serveur écoute par défaut sur l'adresse 127.0.0.1:8888 et gère les clients de manière concurrente.

### Client 

Le client communique avec le serveur pour lui soumettre des requêtes. Un timeout de 5 secondes est configuré pour éviter un blocage en cas de dysfonctionnement du réseau.
