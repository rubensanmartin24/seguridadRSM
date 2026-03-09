"""
Modelo de Acción.

Representa una acción automática ejecutada por el motor SOAR.
"""

from sqlalchemy import Column, Integer, String, DateTime, JSON, Text
from datetime import datetime
from api.utils.db import Base


class Accion(Base):
    """
    Tabla de acciones ejecutadas automáticamente por el motor SOAR.
    
    Atributos:
        id: Identificador único
        timestamp: Fecha y hora de ejecución
        alerta_id: ID de la alerta que disparó la acción
        tipo: Tipo de acción (bloqueo, aislamiento, notificación, etc.)
        descripcion: Descripción de la acción ejecutada
        estado: Estado de la ejecución (pendiente, completada, fallida)
        resultado: Resultado de la ejecución
        metadata: Información adicional en JSON
    """
    __tablename__ = "acciones"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    alerta_id = Column(Integer, index=True)
    tipo = Column(String(100), index=True)  # bloqueo, aislamiento, notificación, etc.
    descripcion = Column(Text)
    estado = Column(String(50), default="pendiente", index=True)  # pendiente, completada, fallida
    resultado = Column(Text, nullable=True)
    metadata = Column(JSON, nullable=True)
