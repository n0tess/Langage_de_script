# Atelier 8 - OUTHENIN Nicolas

# Usage python3 atelier8.py

import socket
import time

s1, s2 = socket.socketpair()

with s1, s2:
    s1.settimeout(0.2)

    debut = time.perf_counter()

    try:
        s1.recv(1)
    except socket.timeout:
        pass

    fin = time.perf_counter()

    print(f"Timeout 0.2s : {(fin - debut) * 1000:.2f} ms")

    s1.setblocking(False)

    debut = time.perf_counter()

    try:
        s1.recv(1)
    except BlockingIOError:
        pass

    fin = time.perf_counter()

    print(f"Non bloquant : {(fin - debut) * 1000:.2f} ms")

# Question : pourquoi ne peut-on pas tester aussi simplement le mode bloquant par défaut (san timeout) ? Que faudrait-il pour le faire ? 

# En mode bloquant par défaut, la méthode recv() attend indéfiniment jusqu'à ce qu'elle reçoive des données. Il faudrait ainsi un timeout ou une autre tâche qui envoie des données.