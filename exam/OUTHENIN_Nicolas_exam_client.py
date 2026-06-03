#!/usr/bin/env python3

# OUTHENIN Nicolas - exam_client.py

#----------#
# Partie 4 #
#----------#

import socket
import json
import argparse
import logging
from pydantic import BaseModel, EmailStr

logger = logging.getLogger(__name__)

HOTE = "127.0.0.1"
PORT = 8888

class Domaine(BaseModel):
    hote: str
    ip: str | None
    contact: str | None
    email: EmailStr | None

# Envoie une requête au serveur et retourne la réponse sous forme de dictionnaire
def envoyer_requete(cmd: str, args: dict = None) -> dict | None:
    try:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.settimeout(5.0) 
            s.connect((HOTE, PORT))
            
            # Envoi
            requete = json.dumps({"cmd": cmd, "args": args or {}}) + "\n"
            s.sendall(requete.encode('utf-8'))
            
            # Lecture bas niveau jusqu'au '\n' sans makefile
            reponse_bytes = b""
            while True:
                octet = s.recv(1)
                if not octet: # Le serveur a fermé la connexion
                    break
                reponse_bytes += octet
                if octet == b'\n':
                    break
            
            if not reponse_bytes:
                logger.error("Aucune réponse du serveur")
                return None
                
            return json.loads(reponse_bytes.decode('utf-8'))

    except ConnectionRefusedError:
        logger.error("Connexion refusée. Le serveur est-il démarré ?")
        return None
    except socket.timeout:
        logger.error("Le serveur n'a pas répondu à temps.")
        return None
    except Exception as e:
        logger.error(f"Erreur réseau : {e}")
        return None

# Fonctions de commande pour chaque action qui utilisent envoyer_requete et traitent les réponses du serveur
def cmd_search(hote: str) -> Domaine | None:
    reponse = envoyer_requete("SEARCH", {"hote": hote})
    if not reponse:
        return None
    if reponse.get("status") == "OK":
        return Domaine(**reponse["domaine"])
    elif reponse.get("status") == "NOT_FOUND":
        print(f"Domaine non trouvé : {hote}")
    return None

def cmd_record(hote: str) -> Domaine | None:
    reponse = envoyer_requete("RECORD", {"hote": hote})
    if not reponse:
        return None
    status = reponse.get("status")
    if status == "OK":
        return Domaine(**reponse["domaine"])
    elif status == "ALREADY_EXISTS":
        print(f"Domaine déjà enregistré : {hote}")
    elif status == "erreur":
        print(f"erreur lors de l'enregistrement du domaine : {hote}")
    return None

def cmd_count() -> int:
    reponse = envoyer_requete("COUNT")
    if reponse and "count" in reponse:
        return int(reponse["count"])
    return 0

def cmd_list() -> list[str]:
    reponse = envoyer_requete("LIST")
    if reponse and "hotes" in reponse:
        return reponse["hotes"]
    return []

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Client Annuaire de domaines")
    subparsers = parser.add_subparsers(dest="commande", required=True)

    parser_search = subparsers.add_parser("search", help="Cherche un domaine en BDD")
    parser_search.add_argument("hote", help="Nom du domaine (ex: mines-ales.fr)")

    parser_record = subparsers.add_parser("record", help="Résout et enregistre un domaine")
    parser_record.add_argument("hote", help="Nom du domaine")

    parser_count = subparsers.add_parser("count", help="Affiche le nombre de domaines connus")

    parser_list = subparsers.add_parser("list", help="Liste tous les hôtes connus")

    parser.add_argument("-v", "--verbose", action="count", default=0, help="Niveau de verbosité (-v INFO, -vv DEBUG, -vvv DEBUG détaillé)")       

    args = parser.parse_args()

    niveaux = [logging.WARNING, logging.INFO, logging.DEBUG]
    niveau = niveaux[min(args.verbose, 2)]
    fmt = ("%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(threadName)s | %(message)s"
        if args.verbose >= 3 else "%(asctime)s | %(levelname)s | %(message)s")
    logging.basicConfig(level=niveau, format=fmt)

    if args.commande == "search":
        domaine = cmd_search(args.hote)
        if domaine:
            print(f"Trouvé : {domaine}")
            
    elif args.commande == "record":
        domaine = cmd_record(args.hote)
        if domaine:
            print(f"Enregistré : {domaine}")
            
    elif args.commande == "count":
        nb = cmd_count()
        print(f"Total en base : {nb}")
        
    elif args.commande == "list":
        hotes = cmd_list()
        print("Domaines connus :")
        for h in hotes:
            print(f" - {h}")