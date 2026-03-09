"""
Router de Agentes.

Endpoints para gestionar agentes de monitorización.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.utils.db import get_db
from api.models.agente import Agente
from api.schemas.agente import AgenteCreate, AgenteResponse, AgenteUpdate

router = APIRouter()


@router.get("/", response_model=list[AgenteResponse])
def listar_agentes(
    skip: int = 0,
    limit: int = 100,
    activo: bool = None,
    db: Session = Depends(get_db)
):
    """
    Listar todos los agentes.
    
    Query params:
        skip: Número de registros a saltar
        limit: Número máximo de registros
        activo: Filtrar por estado activo (opcional)
    """
    query = db.query(Agente)
    if activo is not None:
        query = query.filter(Agente.activo == activo)
    
    agentes = query.offset(skip).limit(limit).all()
    return agentes


@router.get("/{agente_id}", response_model=AgenteResponse)
def obtener_agente(
    agente_id: int,
    db: Session = Depends(get_db)
):
    """Obtener un agente específico por ID"""
    agente = db.query(Agente).filter(Agente.id == agente_id).first()
    if not agente:
        raise HTTPException(status_code=404, detail="Agente no encontrado")
    return agente


@router.post("/", response_model=AgenteResponse)
def crear_agente(
    agente: AgenteCreate,
    db: Session = Depends(get_db)
):
    """Registrar un nuevo agente"""
    # Verificar que el hostname sea único
    agente_existente = db.query(Agente).filter(Agente.hostname == agente.hostname).first()
    if agente_existente:
        raise HTTPException(status_code=400, detail="Un agente con ese hostname ya existe")
    
    db_agente = Agente(**agente.model_dump())
    db.add(db_agente)
    db.commit()
    db.refresh(db_agente)
    return db_agente


@router.put("/{agente_id}", response_model=AgenteResponse)
def actualizar_agente(
    agente_id: int,
    agente_update: AgenteUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar un agente existente"""
    agente = db.query(Agente).filter(Agente.id == agente_id).first()
    if not agente:
        raise HTTPException(status_code=404, detail="Agente no encontrado")
    
    for key, value in agente_update.model_dump(exclude_unset=True).items():
        setattr(agente, key, value)
    
    db.commit()
    db.refresh(agente)
    return agente


@router.delete("/{agente_id}")
def eliminar_agente(
    agente_id: int,
    db: Session = Depends(get_db)
):
    """Eliminar un agente"""
    agente = db.query(Agente).filter(Agente.id == agente_id).first()
    if not agente:
        raise HTTPException(status_code=404, detail="Agente no encontrado")
    
    db.delete(agente)
    db.commit()
    return {"mensaje": "Agente eliminado correctamente"}
