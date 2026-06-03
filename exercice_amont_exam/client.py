#!/usr/bin/env python3

import socket
from datetime import datetime
from pydantic import BaseModel, Field, ValidationError


HOTE = "127.0.0.1"
PORT = 8808


class Reservation(BaseModel):
    nom: str
    salle: int = Field(ge=1, le=3)
    date: datetime


def saisir_reservation() -> Reservation:
    nom = input("Nom : ")
    salle = int(input("Salle (1, 2 ou 3) : "))
    date_str = input("Date (jj/mm/aaaa) : ")

    return Reservation(
        nom=nom,
        salle=salle,
        date=datetime.strptime(date_str, "%d/%m/%Y"),
    )


def main():
    try:
        reservation = saisir_reservation()

        message = f"{reservation.nom};{reservation.salle};{reservation.date.strftime('%d/%m/%Y')}\n"

        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((HOTE, PORT))
            s.sendall(message.encode())

            response = s.recv(1024).decode()
            print("\nRéponse serveur :", response)

    except ValidationError as e:
        print("\nErreur de validation :", e)

    except ValueError:
        print("\nErreur : format de date ou salle invalide")


if __name__ == "__main__":
    main()