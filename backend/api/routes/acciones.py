"""
Router de Acciones.

Endpoints para gestionar acciones automáticas ejecutadas por el motor SOAR.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.utils.db import get_db
from api.models.accion import Accion
from api.schemas.accion import AccionCreate, AccionResponse, AccionUpdate

router = APIRouter()


@router.get("/", response_model=list[AccionResponse])
def listar_acciones(
    skip: int = 0,
    limit: int = 100,
    estado: str = None,
    db: Session = Depends(get_db)
):
    """
    Listar todas las acciones.
    
    Query params:
        skip: Número de registros a saltar
        limit: Número máximo de registros
        estado: Filtrar por estado (opcional)
    """
    query = db.query(Accion)
    if estado:
        query = query.filter(Accion.estado == estado)
    
    acciones = query.offset(skip).limit(limit).all()
    return acciones


@router.get("/{accion_id}", response_model=AccionResponse)
def obtener_accion(
    accion_id: int,
    db: Session = Depends(get_db)
):
    """Obtener una acción específica por ID"""
    accion = db.query(Accion).filter(Accion.id == accion_id).first()
    if not accion:
        raise HTTPException(status_code=404, detail="Acción no encontrada")
    return accion


@router.post("/", response_model=AccionResponse)
def crear_accion(
    accion: AccionCreate,
    db: Session = Depends(get_db)
):
    """Crear una nueva acción"""
    db_accion = Accion(**accion.model_dump())
    db.add(db_accion)
    db.commit()
    db.refresh(db_accion)
    return db_accion


@router.put("/{accion_id}", response_model=AccionResponse)
def actualizar_accion(
    accion_id: int,
    accion_update: AccionUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar una acción existente"""
    accion = db.query(Accion).filter(Accion.id == accion_id).first()
    if not accion:
        raise HTTPException(status_code=404, detail="Acción no encontrada")
    
    for key, value in accion_update.model_dump(exclude_unset=True).items():
        setattr(accion, key, value)
    
    db.commit()
    db.refresh(accion)
    return accion


@router.delete("/{accion_id}")
def eliminar_accion(
    accion_id: int,
    db: Session = Depends(get_db)
):
    """Eliminar una acción"""
    accion = db.query(Accion).filter(Accion.id == accion_id).first()
    if not accion:
        raise HTTPException(status_code=404, detail="Acción no encontrada")
    
    db.delete(accion)
    db.commit()
    return {"mensaje": "Acción eliminada correctamente"}
