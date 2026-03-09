"""
Pydantic schemas para Agentes.
"""

from pydantic import BaseModel, Field, IPvAnyAddress
from datetime import datetime
from typing import Optional, Dict, Any


class AgenteBase(BaseModel):
    """Schema base para Agente"""
    nombre: str = Field(..., description="Nombre del agente")
    hostname: str = Field(..., description="Nombre de host")
    ip_address: str = Field(..., description="Dirección IP")
    sistema_operativo: str = Field(..., description="Sistema operativo")
    version: str = Field(..., description="Versión del agente")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadatos adicionales")


class AgenteCreate(AgenteBase):
    """Schema para crear un Agente"""
    pass


class AgenteUpdate(BaseModel):
    """Schema para actualizar un Agente"""
    nombre: Optional[str] = None
    ip_address: Optional[str] = None
    sistema_operativo: Optional[str] = None
    version: Optional[str] = None
    activo: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None


class AgenteResponse(AgenteBase):
    """Schema para respuesta de Agente"""
    id: int
    activo: bool
    registered_at: datetime
    ultimo_heartbeat: datetime

    class Config:
        from_attributes = True
