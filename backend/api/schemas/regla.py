"""
Pydantic schemas para Reglas.
"""

from pydantic import BaseModel, Field
from datetime import datetime
from typing import Optional, Dict, Any


class ReglaBase(BaseModel):
    """Schema base para Regla"""
    nombre: str = Field(..., description="Nombre de la regla")
    descripcion: str = Field(..., description="Descripción de la regla")
    patron: str = Field(..., description="Patrón a detectar")
    tipo: str = Field(..., description="Tipo de regla")
    severidad: str = Field(..., description="Severidad asignada")
    metadata: Optional[Dict[str, Any]] = Field(None, description="Metadatos adicionales")


class ReglaCreate(ReglaBase):
    """Schema para crear una Regla"""
    pass


class ReglaUpdate(BaseModel):
    """Schema para actualizar una Regla"""
    nombre: Optional[str] = None
    descripcion: Optional[str] = None
    patron: Optional[str] = None
    tipo: Optional[str] = None
    severidad: Optional[str] = None
    activa: Optional[bool] = None
    metadata: Optional[Dict[str, Any]] = None


class ReglaResponse(ReglaBase):
    """Schema para respuesta de Regla"""
    id: int
    activa: bool
    created_at: datetime
    updated_at: datetime

    class Config:
        from_attributes = True
