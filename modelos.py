from sqlalchemy import String, CheckConstraint, ForeignKey
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship

class Base(DeclarativeBase):
    pass

class Sala(Base):

    __tablename__ = "sala"


    __table_args__ = (
        CheckConstraint("capacidad > 0", name="capacidad_positiva_mayor_a_cero"),
    )


    id: Mapped[int] = mapped_column(primary_key=True, nullable=False)
    nombre: Mapped[str] = mapped_column(String(100), nullable=False)
    capacidad: Mapped[int] = mapped_column(nullable=False)
    disponible: Mapped[bool] = mapped_column(nullable=False)


    reservas: Mapped[list["Reserva"]] = relationship(back_populates="sala")


    def __repr__(self):
        return f"Sala(id={self.id}, nombre={self.nombre!r}, capacidad={self.capacidad}, disponible={self.disponible})"


class Reserva(Base):
    __tablename__ = 'reserva'

    id: Mapped[int] = mapped_column(primary_key=True)
    estudiante: Mapped[str] = mapped_column(String(100), nullable=False)
    sala_id: Mapped[int] = mapped_column(ForeignKey("sala.id"), nullable=False)
    fecha: Mapped[str] = mapped_column(String(10), nullable=False)

    sala: Mapped["Sala"] = relationship(back_populates="reservas")