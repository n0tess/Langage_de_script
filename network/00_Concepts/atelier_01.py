# Atelier 1 - OUTHENIN Nicolas

import socket
import sys

resultats = socket.getaddrinfo(sys.argv[1], 80, type=socket.SOCK_STREAM)
total_enregistrement = len(resultats)


for info in resultats:
    famille, _type, _proto, _canon, sockaddr = info
    nom_famille = "IPv4" if famille == socket.AF_INET else "IPv6"

    print(f"  {nom_famille:5s} -> {sockaddr}")

print(f"Total : {total_enregistrement} enregistrement(s)")
