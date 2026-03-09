"""
Pydantic schemas para Alertas.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any


class AlertaBase(BaseModel):
    """Schema base para Alerta"""
    evento_id: int = Field(..., description="ID del evento asociado")
    severidad: str = Field(..., description="Nivel de severidad")
    descripcion: str = Field(..., description="Descripción de la alerta")
    regla_id: Optional[int] = Field(None, description="ID de la regla")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadatos adicionales")


class AlertaCreate(AlertaBase):
    """Schema para crear una Alerta"""
    pass


class AlertaUpdate(BaseModel):
    """Schema para actualizar una Alerta"""
    severidad: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class AlertaResponse(AlertaBase):
    """Schema para respuesta de Alerta"""
    id: int
    timestamp: datetime
    estado: str

    class Config:
        from_attributes = True
