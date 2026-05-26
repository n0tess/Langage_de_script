# Atelier 6 - OUTHENIN Nicolas

# Usage python3 atelier06.py 

import socket
import struct

def recv_exact(sock, n: int) -> bytes:
    morceaux = []
    restant = n
    while restant:
        bloc = sock.recv(restant)
        if not bloc:
            raise ConnectionError("Connexion fermée prématurément")
        morceaux.append(bloc)
        restant -= len(bloc)
    return b"".join(morceaux)

def envoyer_message(sock, message: bytes) -> None:
    longueur = struct.pack('!I', len(message))
    sock.sendall(longueur + message)

def recevoir_message(sock) -> bytes:
    header = recv_exact(sock, 4)
    longueur = struct.unpack('!I', header)[0]
    return recv_exact(sock, longueur)
    
s1, s2 = socket.socketpair()

with s1, s2:
    envoyer_message(s1, b"a")
    envoyer_message(s1, b"bb")
    envoyer_message(s1, b"ccc")

    print(recevoir_message(s2))
    print(recevoir_message(s2))
    print(recevoir_message(s2))


