# Atelier 5 - OUTHENIN Nicolas

# Usage : python3 atelier_05.py

import socket

def recv_ligne(sock) -> bytes:
    morceaux = []
    while True:
        chunk = sock.recv(1)
        if not chunk:
            break
        if chunk == b'\n':
            break
        morceaux.append(chunk)
    return b''.join(morceaux)

s1, s2 = socket.socketpair()

with s1, s2:
    s1.sendall(b"bonjour\nle monde\n")
    print(recv_ligne(s2))  
    print(recv_ligne(s2))
            
# Question bonus : pourquoi est-ce inefficace en pratique ? Quelle structure de données permettrait d'optimiser (sans changer la sémantique) ?

# C'est inefficace car on lit un octet à la fois. Une structure de données plus efficace serait une liste de bytes. 