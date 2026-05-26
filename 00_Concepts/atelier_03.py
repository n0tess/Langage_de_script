# Atelier 3 - OUTHENIN Nicolas

import socket
import argparse

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--protocole", choices=["tcp", "udp"], required=True)
    args = parser.parse_args()

    ip = ("127.0.0.1", 1)

    if args.protocole == "tcp":
        try:
            with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
                s.settimeout(1)
                s.connect(ip)
        except ConnectionRefusedError:
            print("TCP : connexion refusée")

    else:
        with socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s2:
            s2.settimeout(1)
            sent = s2.sendto(b"test", ip)

            print("UDP : datagramme envoyé, aucune confirmation possible")
            print(f"UDP : {sent} octets envoyés")

if __name__ == "__main__":
    main()  


# Pour lancer le script : python3 atelier_03.py --protocole tcp ou python3 atelier_03.py --protocole upd