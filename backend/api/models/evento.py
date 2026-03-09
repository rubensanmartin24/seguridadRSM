"""
Modelo de Evento.

Representa un evento bruto capturado por el agente de monitorización.
Ejemplos: conexión de red, cambio de archivo, proceso ejecutado, etc.
"""

from sqlalchemy import Column, Integer, String, DateTime, JSON, Text
from sqlalchemy.orm import relationship
from datetime import datetime
from api.utils.db import Base


class Evento(Base):
    """
    Tabla de eventos capturados por agentes de monitorización.
    
    Atributos:
        id: Identificador único
        timestamp: Fecha y hora del evento
        agente_id: ID del agente que reportó el evento
        tipo: Tipo de evento (network, process, file, etc.)
        descripcion: Descripción del evento
        fuente: Fuente del evento (IP, proceso, ruta, etc.)
        destino: Destino del evento (si aplica)
        metadata: Información adicional en JSON
    """
    __tablename__ = "eventos"

    id = Column(Integer, primary_key=True, index=True)
    timestamp = Column(DateTime, default=datetime.utcnow, index=True)
    agente_id = Column(Integer, index=True)
    tipo = Column(String(50), index=True)  # network, process, file, etc.
    descripcion = Column(Text)
    fuente = Column(String(255))
    destino = Column(String(255), nullable=True)
    metadata = Column(JSON, nullable=True)
