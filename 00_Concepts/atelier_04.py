# Atelier 4 - OUTHENIN Nicolas

# python3 atelier_04.py

import socket

s1, s2 = socket.socketpair(socket.AF_UNIX, socket.SOCK_STREAM)

with s1, s2:
    print("Socket 1")
    print("Descripteur OS (fileno) :", s1.fileno())
    print("Sock name :", s1.getsockname())
    print("Peer name :", s1.getpeername())

    print("\nSocket 2")
    print("Descripteur OS (fileno) :", s2.fileno())
    print("Sock name :", s2.getsockname())
    print("Peer name :", s2.getpeername())


# Question : pourquoi les adresses sont-elles vides ('') ? Que signifie "anonyme" dans ce contexte, et en quoi cela diffère-t-il d'un socket TCP/IPv4 classique ?

# Les adresses sont vides car nous utilisons un socket UNIX. Le anonyme signifie qu'il n'y a pas d'adresse associée au socket, contrairement à un socket TCP/IPv4 classique qui a une adresse IP et un port associés.