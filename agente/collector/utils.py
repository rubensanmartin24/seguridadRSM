"""
Utilidades comunes para el agente
"""

import logging
from datetime import datetime
import json

logger = logging.getLogger(__name__)


def obtener_timestamp_iso():
    """Obtener timestamp en formato ISO"""
    return datetime.utcnow().isoformat()


def guardar_json(datos: dict, ruta: str) -> bool:
    """
    Guardar datos en formato JSON.
    
    Args:
        datos: Diccionario a guardar
        ruta: Ruta del archivo
        
    Returns:
        True si se guardó correctamente
    """
    try:
        with open(ruta, 'w') as f:
            json.dump(datos, f, indent=2)
        return True
    except Exception as e:
        logger.error(f"Error al guardar JSON: {e}")
        return False


def cargar_json(ruta: str) -> dict:
    """
    Cargar datos desde archivo JSON.
    
    Args:
        ruta: Ruta del archivo
        
    Returns:
        Diccionario cargado o diccionario vacío
    """
    try:
        with open(ruta, 'r') as f:
            return json.load(f)
    except Exception as e:
        logger.error(f"Error al cargar JSON: {e}")
        return {}


def formatear_bytes(bytes_count: int) -> str:
    """Formatear bytes a formato legible"""
    for unit in ['B', 'KB', 'MB', 'GB']:
        if bytes_count < 1024.0:
            return f"{bytes_count:.2f} {unit}"
        bytes_count /= 1024.0
    return f"{bytes_count:.2f} TB"
