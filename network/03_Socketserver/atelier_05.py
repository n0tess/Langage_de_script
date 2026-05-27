#!/usr/bin/env python3

# Atelier 5 - OUTHENIN Nicolas

import socketserver
import time

socketserver.TCPServer.allow_reuse_address = True

HOTE = "127.0.0.1"
PORT = 8808

class BonjourHandler(socketserver.StreamRequestHandler):
      
      def handle(self) -> None:
        ligne = self.rfile.readline().rstrip(b"\n")

        if not ligne:
            return

        print(f"    Reçu de {self.client_address} : {ligne!r}")
        time.sleep(2)

        self.wfile.write(b"Bonjour " + ligne + b".\n")

class ServeurMultiClient(socketserver.ThreadingMixIn, socketserver.TCPServer):
    pass

if __name__ == "__main__": 
    with ServeurMultiClient((HOTE, PORT), BonjourHandler) as serveur:
        print(f"Serveur en écoute sur {HOTE}:{PORT}...")
        serveur.serve_forever()
