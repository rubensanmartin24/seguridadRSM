"""
Router de Alertas.

Endpoints para gestionar alertas generadas por el motor IDS.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.utils.db import get_db
from api.models.alerta import Alerta
from api.schemas.alerta import AlertaCreate, AlertaResponse, AlertaUpdate

router = APIRouter()


@router.get("/", response_model=list[AlertaResponse])
def listar_alertas(
    skip: int = 0,
    limit: int = 100,
    severidad: str = None,
    db: Session = Depends(get_db)
):
    """
    Listar todas las alertas.
    
    Query params:
        skip: Número de registros a saltar
        limit: Número máximo de registros
        severidad: Filtrar por severidad (opcional)
    """
    query = db.query(Alerta)
    if severidad:
        query = query.filter(Alerta.severidad == severidad)
    
    alertas = query.offset(skip).limit(limit).all()
    return alertas


@router.get("/{alerta_id}", response_model=AlertaResponse)
def obtener_alerta(
    alerta_id: int,
    db: Session = Depends(get_db)
):
    """Obtener una alerta específica por ID"""
    alerta = db.query(Alerta).filter(Alerta.id == alerta_id).first()
    if not alerta:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    return alerta


@router.post("/", response_model=AlertaResponse)
def crear_alerta(
    alerta: AlertaCreate,
    db: Session = Depends(get_db)
):
    """Crear una nueva alerta"""
    db_alerta = Alerta(**alerta.model_dump())
    db.add(db_alerta)
    db.commit()
    db.refresh(db_alerta)
    return db_alerta


@router.put("/{alerta_id}", response_model=AlertaResponse)
def actualizar_alerta(
    alerta_id: int,
    alerta_update: AlertaUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar una alerta existente"""
    alerta = db.query(Alerta).filter(Alerta.id == alerta_id).first()
    if not alerta:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    
    for key, value in alerta_update.model_dump(exclude_unset=True).items():
        setattr(alerta, key, value)
    
    db.commit()
    db.refresh(alerta)
    return alerta


@router.delete("/{alerta_id}")
def eliminar_alerta(
    alerta_id: int,
    db: Session = Depends(get_db)
):
    """Eliminar una alerta"""
    alerta = db.query(Alerta).filter(Alerta.id == alerta_id).first()
    if not alerta:
        raise HTTPException(status_code=404, detail="Alerta no encontrada")
    
    db.delete(alerta)
    db.commit()
    return {"mensaje": "Alerta eliminada correctamente"}
