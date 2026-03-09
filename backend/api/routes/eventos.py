"""
Router de Eventos.

Endpoints para gestionar eventos capturados por agentes.
"""

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from api.utils.db import get_db
from api.models.evento import Evento
from api.schemas.evento import EventoCreate, EventoResponse, EventoUpdate

router = APIRouter()


@router.get("/", response_model=list[EventoResponse])
def listar_eventos(
    skip: int = 0,
    limit: int = 100,
    db: Session = Depends(get_db)
):
    """
    Listar todos los eventos.
    
    Query params:
        skip: Número de registros a saltar
        limit: Número máximo de registros
    """
    eventos = db.query(Evento).offset(skip).limit(limit).all()
    return eventos


@router.get("/{evento_id}", response_model=EventoResponse)
def obtener_evento(
    evento_id: int,
    db: Session = Depends(get_db)
):
    """Obtener un evento específico por ID"""
    evento = db.query(Evento).filter(Evento.id == evento_id).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    return evento


@router.post("/", response_model=EventoResponse)
def crear_evento(
    evento: EventoCreate,
    db: Session = Depends(get_db)
):
    """Crear un nuevo evento"""
    db_evento = Evento(**evento.model_dump())
    db.add(db_evento)
    db.commit()
    db.refresh(db_evento)
    return db_evento


@router.put("/{evento_id}", response_model=EventoResponse)
def actualizar_evento(
    evento_id: int,
    evento_update: EventoUpdate,
    db: Session = Depends(get_db)
):
    """Actualizar un evento existente"""
    evento = db.query(Evento).filter(Evento.id == evento_id).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    
    for key, value in evento_update.model_dump(exclude_unset=True).items():
        setattr(evento, key, value)
    
    db.commit()
    db.refresh(evento)
    return evento


@router.delete("/{evento_id}")
def eliminar_evento(
    evento_id: int,
    db: Session = Depends(get_db)
):
    """Eliminar un evento"""
    evento = db.query(Evento).filter(Evento.id == evento_id).first()
    if not evento:
        raise HTTPException(status_code=404, detail="Evento no encontrado")
    
    db.delete(evento)
    db.commit()
    return {"mensaje": "Evento eliminado correctamente"}
