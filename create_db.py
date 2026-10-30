from sqlalchemy import create_engine

from src.models.connection.base import Base
from src.models.entities.users import Users

engine = create_engine("sqlite:///schema.db")

Base.metadata.create_all(engine)

print("Banco criado com sucesso!")