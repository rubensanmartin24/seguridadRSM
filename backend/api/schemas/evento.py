"""
Pydantic schemas para Eventos.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any


class EventoBase(BaseModel):
    """Schema base para Evento"""
    tipo: str = Field(..., description="Tipo de evento")
    descripcion: str = Field(..., description="Descripción del evento")
    fuente: str = Field(..., description="Fuente del evento")
    destino: Optional[str] = Field(None, description="Destino del evento")
    agente_id: int = Field(..., description="ID del agente")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadatos adicionales")


class EventoCreate(EventoBase):
    """Schema para crear un Evento"""
    pass


class EventoUpdate(BaseModel):
    """Schema para actualizar un Evento"""
    tipo: Optional[str] = None
    descripcion: Optional[str] = None
    fuente: Optional[str] = None
    destino: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class EventoResponse(EventoBase):
    """Schema para respuesta de Evento"""
    id: int
    timestamp: datetime

    class Config:
        from_attributes = True
