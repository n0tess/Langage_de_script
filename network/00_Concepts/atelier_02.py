# Atelier 02 - OUTHENIN Nicolas

import socket

with (
    socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s,
    socket.socket(socket.AF_INET, socket.SOCK_DGRAM) as s2, 
    socket.socket(socket.AF_UNIX, socket.SOCK_STREAM) as s3,
):  
    sockets = [s, s2, s3]

    for i in sockets:
        print("Descripteur OS (fileno) :", i.fileno())
        print("Famille :", i.family.name)
        print("Type :", i.type.name)



# Question : si on instancie les trois en parallèle (un seul with imbriqué), les trois fileno() doivent-ils être nécessairement différents ? Pourquoi ?

# Oui ils doivent être différents. Si ce n'est pas le cas le socket ne pourra pas être créé car pour chaque socket le système utilise un numéro de socket unique.  