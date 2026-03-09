"""
Modelo de Alerta.

Representa una alerta generada por el motor IDS cuando detecta un evento sospechoso.
"""

from sqlalchemy import Column, Integer, String, DateTime, JSON, Text, Enum
from datetime import datetime
from api.utils.db import Base


class Alerta(Base):
    """
    Tabla de alertas generadas por el motor IDS.
    
    Atributos:
        id: Identificador único
        timestamp: Fecha y hora de la alerta
        evento_id: ID del evento que generó la alerta
        severidad: Nivel de severidad (bajo, medio, alto, crítico)
        descripcion: Descripción de por qué se generó la alerta
        regla_id: ID de la regla que generó la alerta
        estado: Estado actual (nuevo, revisado, falso_positivo, etc.)
        metadata: Información adicional en JSON
    """
    __tablename__ = "alertas"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    evento_id = Column(Integer, index=True)
    severidad = Column(String(20), index=True)  # bajo, medio, alto, crítico
    descripcion = Column(Text)
    regla_id = Column(Integer, nullable=True)
    estado = Column(String(50), default="nuevo", index=True)  # nuevo, revisado, falso_positivo
    metadata = Column(JSON, nullable=True)
