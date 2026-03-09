"""
Router de Reglas.

Endpoints para gestionar reglas de detección IDS.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.utils.db import get_db
from api.models.regla import Regla
from api.schemas.regla import ReglaCreate, ReglaResponse, ReglaUpdate

router = APIRouter()


@router.get("/", response_model=list[ReglaResponse])
def listar_reglas(
    skip: int = 0,
    limit: int = 100,
    activa: bool = None,
    db: Session = Depends(get_db)
):
    """
    Listar todas las reglas.
    
    Query params:
        skip: Número de registros a saltar
        limit: Número máximo de registros
        activa: Filtrar por estado activo (opcional)
    """
    query = db.query(Regla)
    if activa is not None:
        query = query.filter(Regla.activa == activa)
    
    reglas = query.offset(skip).limit(limit).all()
    return reglas


@router.get("/{regla_id}", response_model=ReglaResponse)
def obtener_regla(
    regla_id: int,
    db: Session = Depends(get_db)
):
    """Obtener una regla específica por ID"""
    regla = db.query(Regla).filter(Regla.id == regla_id).first()
    if not regla:
        raise HTTPException(status_code=404, detail="Regla no encontrada")
    return regla


@router.post("/", response_model=ReglaResponse)
def crear_regla(
    regla: ReglaCreate,
    db: Session = Depends(get_db)
):
    """Crear una nueva regla de detección"""
    db_regla = Regla(**regla.model_dump())
    db.add(db_regla)
    db.commit()
    db.refresh(db_regla)
    return db_regla


@router.put("/{regla_id}", response_model=ReglaResponse)
def actualizar_regla(
    regla_id: int,
    regla_update: ReglaUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar una regla existente"""
    regla = db.query(Regla).filter(Regla.id == regla_id).first()
    if not regla:
        raise HTTPException(status_code=404, detail="Regla no encontrada")
    
    for key, value in regla_update.model_dump(exclude_unset=True).items():
        setattr(regla, key, value)
    
    db.commit()
    db.refresh(regla)
    return regla


@router.delete("/{regla_id}")
def eliminar_regla(
    regla_id: int,
    db: Session = Depends(get_db)
):
    """Eliminar una regla"""
    regla = db.query(Regla).filter(Regla.id == regla_id).first()
    if not regla:
        raise HTTPException(status_code=404, detail="Regla no encontrada")
    
    db.delete(regla)
    db.commit()
    return {"mensaje": "Regla eliminada correctamente"}
