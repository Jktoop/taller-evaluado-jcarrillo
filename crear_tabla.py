from conexiones import engine
from modelos import Base

Base.metadata.create_all(engine)
print("Tablas creadas exitosamente en reservas.db")