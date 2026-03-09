"""
Modelo de Agente.

Representa un agente de monitorización conectado al sistema.
"""

from sqlalchemy import Column, Integer, String, DateTime, JSON, Text, Boolean
from datetime import datetime
from api.utils.db import Base


class Agente(Base):
    """
    Tabla de agentes de monitorización.
    
    Atributos:
        id: Identificador único
        nombre: Nombre del agente
        hostname: Nombre de host donde se ejecuta
        ip_address: Dirección IP del agente
        sistema_operativo: SO (Linux, Windows, macOS, etc.)
        version: Versión del agente
        activo: Si el agente está activo o inactivo
        ultimo_heartbeat: Último latido del corazón del agente
        metadata: Información adicional en JSON
    """
    __tablename__ = "agentes"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(255), index=True)
    hostname = Column(String(255), unique=True, index=True)
    ip_address = Column(String(45), index=True)  # IPv4 o IPv6
    sistema_operativo = Column(String(100))
    version = Column(String(50))
    activo = Column(Boolean, default=True, index=True)
    registered_at = Column(DateTime, default=datetime.utcnow)
    ultimo_heartbeat = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    metadata = Column(JSON, nullable=True)
