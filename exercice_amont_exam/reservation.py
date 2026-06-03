#!/usr/bin/env python3

import socketserver
from datetime import datetime

from sqlalchemy import create_engine, Integer, String, DateTime, select
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, Session

HOTE = "127.0.0.1"
PORT = 8808

class Base(DeclarativeBase):
    pass


class ReservationDB(Base):
    __tablename__ = "reservations"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    nom: Mapped[str] = mapped_column(String, nullable=False)
    salle: Mapped[int] = mapped_column(Integer, nullable=False)
    date: Mapped[datetime] = mapped_column(DateTime, nullable=False)


engine = create_engine("sqlite:///reservations.db", echo=False)
Base.metadata.create_all(engine)


def salle_disponible(session: Session, salle: int, date_reservation: datetime) -> bool:
    return session.scalar(
        select(ReservationDB).where(
            ReservationDB.salle == salle,
            ReservationDB.date == date_reservation,
        )
    ) is None


def creer_reservation(session: Session, nom: str, salle: int, date: datetime):
    session.add(ReservationDB(nom=nom, salle=salle, date=date))
    session.commit()


class ReservationHandler(socketserver.StreamRequestHandler):

    def handle(self):
        data = self.rfile.readline().strip().decode()

        if not data:
            return

        print(f"Reçu : {data}")

        try:
            nom, salle_str, date_str = data.split(";")

            salle = int(salle_str)
            date_reservation = datetime.strptime(date_str, "%d/%m/%Y")

            with Session(engine) as session:

                if not salle_disponible(session, salle, date_reservation):
                    self.wfile.write(f"Erreur : salle déjà réservée\n".encode())
                    return

                creer_reservation(session, nom, salle, date_reservation)

            self.wfile.write(f"OK : réservation confirmée\n".encode())

        except Exception as e:
            self.wfile.write(f"Erreur : format invalide\n".encode())


class ServeurMultiClient(socketserver.ThreadingMixIn, socketserver.TCPServer):
    allow_reuse_address = True


if __name__ == "__main__":
    with ServeurMultiClient((HOTE, PORT), ReservationHandler) as server:
        print(f"Serveur en ecoute sur {HOTE}:{PORT}")
        server.serve_forever()