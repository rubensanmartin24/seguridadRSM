"""
Database configuration and session management.

Soporta tanto SQLite como PostgreSQL mediante variable de entorno DATABASE_URL.
Preparado para migrar a PostgreSQL sin rehacer la estructura.
"""

from sqlalchemy import create_engine, event
from sqlalchemy.orm import sessionmaker, declarative_base
from pydantic_settings import BaseSettings
from typing import Generator
import os

# Cargar variables de entorno
class Settings(BaseSettings):
    database_url: str = "sqlite:///./seguridadrsm.db"
    app_name: str = "SeguridadRSM"
    debug: bool = True
    
    class Config:
        env_file = ".env"


settings = Settings()

# Crear engine según el tipo de base de datos
DATABASE_URL = settings.database_url

if DATABASE_URL.startswith("sqlite"):
    # SQLite: desactivar restricción de threads para desarrollo
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False},
        echo=settings.debug
    )
    
    # Habilitar foreign keys en SQLite
    @event.listens_for(engine, "connect")
    def set_sqlite_pragma(dbapi_conn, connection_record):
        cursor = dbapi_conn.cursor()
        cursor.execute("PRAGMA foreign_keys=ON")
        cursor.close()
else:
    # PostgreSQL u otra base de datos relacional
    engine = create_engine(
        DATABASE_URL,
        echo=settings.debug,
        pool_pre_ping=True
    )

# Session factory
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Base para los modelos
Base = declarative_base()


def get_db() -> Generator:
    """
    Dependencia de FastAPI para obtener sesión de base de datos.
    
    Yields:
        SessionLocal: Sesión de SQLAlchemy para la solicitud
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
    tipo = Column(String, index=True)
    origen = Column(String)
    datos = Column(JSON)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Alerta(Base):
    __tablename__ = "alertas"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    descripcion = Column(String)
    criticidad = Column(String)
    timestamp = Column(DateTime, default=datetime.utcnow)


class Accion(Base):
    __tablename__ = "acciones"

    id = Column(Integer, primary_key=True, index=True)
    tipo = Column(String)
    resultado = Column(String)
    ejecutada = Column(Boolean, default=False)
    timestamp = Column(DateTime, default=datetime.utcnow)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
