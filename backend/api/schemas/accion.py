"""
Pydantic schemas para Acciones.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any


class AccionBase(BaseModel):
    """Schema base para Acción"""
    alerta_id: int = Field(..., description="ID de la alerta asociada")
    tipo: str = Field(..., description="Tipo de acción")
    descripcion: str = Field(..., description="Descripción de la acción")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadatos adicionales")


class AccionCreate(AccionBase):
    """Schema para crear una Acción"""
    pass


class AccionUpdate(BaseModel):
    """Schema para actualizar una Acción"""
    tipo: Optional[str] = None
    descripcion: Optional[str] = None
    estado: Optional[str] = None
    resultado: Optional[str] = None
    metadata: Optional[Dict[str, Any]] = None


class AccionResponse(AccionBase):
    """Schema para respuesta de Acción"""
    id: int
    timestamp: datetime
    estado: str
    resultado: Optional[str]

    class Config:
        from_attributes = True
