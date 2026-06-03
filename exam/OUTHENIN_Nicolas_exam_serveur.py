#!/usr/bin/env python3

# OUTHENIN Nicolas - exam_serveur.py

#----------#
# Partie 1 #
#----------#

import re
import platform
import subprocess
import socketserver
import json
import os
import argparse
import logging
from pydantic import BaseModel, EmailStr
from sqlalchemy import create_engine, Integer, String, DateTime, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session
from sqlalchemy.exc import IntegrityError
from pathlib import Path

HOTE = "127.0.0.1"
PORT = 8888

# 1.3 - Modèle Pydantic et fonction de synthèse
class Domaine(BaseModel):
    hote: str
    ip: str | None
    contact: str | None
    email: EmailStr | None

# 1.1 - Résolution IP cross-platform
# Détermine la commande à utiliser en fonction du système d'exploitation et exécute la commande pour obtenir l'adresse IP du domaine
def resoudre_ip(hote: str) -> str | None:
    os_name = platform.system()
    commande = ["host", hote] if os_name in ["Linux", "Darwin"] else ["nslookup", hote]
    
    try:
        resultat = subprocess.run(commande, capture_output=True, text=True, timeout=5.0)
        
        if resultat.returncode != 0:
            return None
            
        lignes = resultat.stdout.splitlines()
        
        if commande[0] == "nslookup":
            for ligne in reversed(lignes):
                if "Address:" in ligne and "#" not in ligne:
                    return ligne.split("Address:")[1].strip()
        else:
            for ligne in lignes:
                if "has address" in ligne:
                    return ligne.split("has address")[1].strip()
                    
        return None

    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None
    
# 1.2 - Informations whois 
# Récupère les informations du domaine en interrogeant le service whois et extrait le nom du registrant et son adresse email
def interroger_whois(hote: str) -> tuple[str | None, str | None]:
    try:
        resultat = subprocess.run(["whois", hote], capture_output=True, text=True, timeout=10)
        
        registrant_name = None
        registrant_email = None
        
        for ligne in resultat.stdout.splitlines():
            if "Registrant Name:" in ligne or "Registrant:" in ligne:
                if registrant_name is None:
                    registrant_name = ligne.split(":", 1)[1].strip()
                    
        match_email = re.search(r'\S+@\S+', resultat.stdout)
        if match_email:
            registrant_email = match_email.group(0)
            
        return registrant_name, registrant_email
        
    except (FileNotFoundError, subprocess.TimeoutExpired):
        return None, None

# Fin 1.3
# Collecte toutes les informations d'un domaine en utilisant les fonctions précédentes et retourne une instance de Domaine
def collecter(hote: str) -> Domaine:
    ip = resoudre_ip(hote)
    contact, email = interroger_whois(hote)
    return Domaine(hote=hote, ip=ip, contact=contact, email=email)


#----------#
# Partie 2 #
#----------#

# 2.1 - Modèle SQLAlchemy
class Base(DeclarativeBase):
    pass

class DomaineORM(Base):
    __tablename__ = "domaines"

    hote: Mapped[str] = mapped_column(String, primary_key=True)
    ip: Mapped[str] = mapped_column(String, nullable=True)
    contact: Mapped[str] = mapped_column(String, nullable=True)
    email: Mapped[str] = mapped_column(String, nullable=True)


# 2.2 - Session et BDD 
BDD_PATH = Path(__file__).parent / "domaines.db"

engine = create_engine(f"sqlite:///{BDD_PATH}", echo=False)
Base.metadata.create_all(engine)

# 2.3 - Fonctions CRUD 
# Enregistre un domaine dans la base de données en utilisant une session. Si le domaine existe déjà, une exception est levée et gérée pour éviter les doublons
def enregistrer(domaine: Domaine) -> None:
    with Session(engine) as session:
        try:
            session.add(DomaineORM(**domaine.model_dump()))
            session.commit()
        except IntegrityError:
            session.rollback()
            raise
    
# Liste tous les domaines enregistrés dans la base de données et retourne une liste d'instances de Domaine
def lister() -> list[Domaine]:
    with Session(engine) as session:
        resultats = session.execute(select(DomaineORM)).scalars().all()
        return [Domaine(hote=res.hote, ip=res.ip, contact=res.contact, email=res.email) for res in resultats]
    
# Cherche un domaine par son hôte dans la base de données et retourne une instance de Domaine si trouvée, sinon None
def chercher(hote: str) -> Domaine | None:
    with Session(engine) as session:
        resultat = session.execute(select(DomaineORM).where(DomaineORM.hote == hote)).scalar_one_or_none()
        return Domaine(hote=resultat.hote, ip=resultat.ip, contact=resultat.contact, email=resultat.email) if resultat else None
    

#----------#
# Partie 3 #
#----------#

# 3.1 - Choix du protocole 

"""
Mon choix s'est orienté vers le JSON ligne car il est directement valide avec Pydantic et permet une communication simple entre client et serveur. De plus, il est facilement lisible et débogable.
"""

# 3.2 - Commandes 
# Classe de gestion des requêtes entrantes. Elle lit une ligne JSON, détermine la commande et les arguments, exécute la logique correspondante et renvoie une réponse JSON au client
class AnnuaireHandler(socketserver.StreamRequestHandler):
    def handle(self):
        ligne = self.rfile.readline().decode('utf-8').strip()
        if not ligne:
            return
            
        try:
            requete = json.loads(ligne)
            cmd = requete.get("cmd")
            args = requete.get("args", {})
            
            reponse = {}
            
            if cmd == "SEARCH":
                domaine = chercher(args.get("hote"))
                if domaine:
                    reponse = {"status" : "OK", "domaine" : domaine.model_dump()}
                else:
                    reponse = {"status": "NOT_FOUND"}
                    
            elif cmd == "RECORD":
                hote = args.get("hote")
                try:
                    domaine = collecter(hote)
                    enregistrer(domaine)
                    reponse = {"status": "OK", "domaine": domaine.model_dump()}
                except IntegrityError:
                    reponse = {"status" : "ALREADY_EXISTS"}
                except Exception:
                    reponse = {"status" : "erreur"}
                
            elif cmd == "COUNT":
                domaines = lister()
                reponse = {"count": len(domaines)}
                
            elif cmd == "LIST":
                domaines = lister()
                reponse = {"hotes": [d.hote for d in domaines]}
                
            else:
                reponse = {"erreur": "Commande inconnue"}
                
            self.wfile.write((json.dumps(reponse) + "\n").encode('utf-8'))
            
        except json.JSONDecodeError:
            self.wfile.write(b'{"erreur": "Format JSON invalide"}\n')

# 3.3 - Serveur threadé 
# Classe de serveur qui gère les connexions entrantes en créant un thread pour chaque client, permettant ainsi de gérer plusieurs clients simultanément 
class AnnuaireServer(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True  

# Fonction pour lancer le serveur sur l'hôte et le port spécifiés
def lancer_serveur(HOTE, PORT):
    serveur = AnnuaireServer((HOTE, PORT), AnnuaireHandler)
    print(f"Serveur démarré sur {HOTE}:{PORT}")
    try:
        serveur.serve_forever()
    except KeyboardInterrupt:
        print("\nArrêt du serveur demandé...")
    finally:
        serveur.shutdown()
        serveur.server_close()
        print("Serveur arrêté.")


#----------#
# Partie 5 #
#----------#

# 5.2 - Logging avec niveaux verbosité
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    # 5.1 - Structure CLI
    parser = argparse.ArgumentParser(description="Serveur d'annuaire de domaines")

    # Utilisation de action="count" pour compter les -v
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Niveaux de verbosité (-v = INFO, -vv = DEBUG)")
    parser.add_argument("--env", type=Path, default=Path(".env"), help="Fichier .env")
    
    subparsers = parser.add_subparsers(dest="commande", required=True)
    
    serve_parser = subparsers.add_parser("serve", help="Lance le serveur")
    serve_parser.add_argument("--host", help="Forcer l'hôte")
    serve_parser.add_argument("--port", type=int, help="Forcer le port")

    args = parser.parse_args()

    # Définition du niveau de log en fonction du nombre de -v
       # Format par défaut
    fmt = "%(asctime)s | %(levelname)s | %(message)s"

    # Définition du niveau de log en fonction du nombre de -v
    if args.verbose == 0:
        niveau = logging.WARNING  # Par défaut, on n'affiche que les warnings et erreurs
    elif args.verbose == 1:
        niveau = logging.INFO     # -v : Informations générales
    elif args.verbose == 2:
        niveau = logging.DEBUG    # -vv : Débogage détaillé
    else:
        niveau = logging.DEBUG    # -vvv et plus
        fmt = "%(asctime)s | %(levelname)s | %(filename)s:%(lineno)d | %(threadName)s | %(message)s" 

    logging.basicConfig(level=niveau, format=fmt)

    hote_final = args.host or os.environ.get("HOTE", HOTE)
    port_str = args.port or os.environ.get("PORT", PORT)
    port_final = int(port_str)

    if args.commande == "serve":
        logger.info(f"Lancement du serveur sur {hote_final}:{port_final}")
        lancer_serveur(hote_final, port_final)