"""
Modelo de Regla.

Representa una regla de detección IDS utilizadas para generar alertas.
"""

from sqlalchemy import Column, Integer, String, DateTime, JSON, Text, Boolean
from datetime import datetime
from api.utils.db import Base


class Regla(Base):
    """
    Tabla de reglas de detección IDS.
    
    Atributos:
        id: Identificador único
        nombre: Nombre descriptivo de la regla
        descripcion: Descripción detallada
        patron: Patrón o condición a buscar
        tipo: Tipo de detección (signature, anomaly, etc.)
        severidad: Severidad asignada por la regla
        activa: Si la regla está activa o desactivada
        metadata: Información adicional en JSON
    """
    __tablename__ = "reglas"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True)
    descripcion = Column(Text)
    patron = Column(Text)  # Puede ser JSON, regex, etc.
    tipo = Column(String(50))  # signature, anomaly, behavioral, etc.
    severidad = Column(String(20))  # bajo, medio, alto, crítico
    activa = Column(Boolean, default=True, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(JSON, nullable=True)
