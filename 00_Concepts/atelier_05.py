# Atelier 5 - OUTHENIN Nicolas

# Usage : python3 atelier_05.py

def recv_ligne(sock) -> bytes:
    data = b""
    while not data.endswith(b"\n"):
        chunk = sock.recv(1)
        if not chunk:
            break
        data += chunk
    return data