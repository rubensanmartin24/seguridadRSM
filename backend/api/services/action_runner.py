"""
Ejecutor de Acciones.

Responsable de ejecutar acciones de respuesta automática en el sistema.
"""

from typing import List, Dict, Any
from datetime import datetime
from enum import Enum


class TipoAccion(str, Enum):
    """Tipos de acciones SOAR disponibles"""
    BLOQUEO = "bloqueo"
    AISLAMIENTO = "aislamiento"
    NOTIFICACION = "notificacion"
    RECOLECCION = "recoleccion"
    INVESTIGACION = "investigacion"
    ROLLBACK = "rollback"


class ActionRunner:
    """
    Ejecutor de acciones de respuesta automática.
    
    Funcionalidades (FUTURO):
    - Ejecución segura de acciones
    - Manejo de errores y rollback
    - Logging completo de ejecuciones
    - Timeout y límites de recursos
    """
    
    def __init__(self):
        """Inicializar el ejecutor de acciones"""
        self.acciones_en_cola = []
        self.historial_ejecuciones = []
    
    def encolar_accion(self, alerta_id: int, accion: Dict[str, Any]) -> int:
        """
        Encolar una acción para ejecución.
        
        Args:
            alerta_id: ID de la alerta que dispara la acción
            accion: Diccionario con información de la acción
            
        Returns:
            ID de la acción encolada
        """
        accion_id = len(self.historial_ejecuciones) + 1
        self.acciones_en_cola.append({
            "id": accion_id,
            "alerta_id": alerta_id,
            "accion": accion,
            "estado": "encolada",
            "timestamp": datetime.utcnow().isoformat()
        })
        return accion_id
    
    def ejecutar_bloqueo(self, destinatario: str, razon: str) -> Dict[str, Any]:
        """
        Ejecutar acción de bloqueo.
        
        Args:
            destinatario: IP, dominio o recurso a bloquear
            razon: Razón del bloqueo
            
        Returns:
            Resultado de la ejecución
        """
        return {
            "tipo": "bloqueo",
            "destinatario": destinatario,
            "razon": razon,
            "estado": "completada",
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def ejecutar_notificacion(self, destino: str, mensaje: str) -> Dict[str, Any]:
        """
        Ejecutar acción de notificación.
        
        Args:
            destino: Destino de la notificación (email, sms, webhook, etc.)
            mensaje: Mensaje a enviar
            
        Returns:
            Resultado de la ejecución
        """
        return {
            "tipo": "notificacion",
            "destino": destino,
            "estado": "completada",
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def ejecutar_recoleccion(self, fuente: str, tipo_datos: str) -> Dict[str, Any]:
        """
        Ejecutar acción de recolección de evidencia.
        
        Args:
            fuente: Fuente de datos (equipo, log, etc.)
            tipo_datos: Tipo de datos a recolectar
            
        Returns:
            Resultado de la ejecución
        """
        return {
            "tipo": "recoleccion",
            "fuente": fuente,
            "tipo_datos": tipo_datos,
            "estado": "completada",
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def obtener_cola(self) -> List[Dict[str, Any]]:
        """Obtener acciones pendientes de ejecución"""
        return self.acciones_en_cola
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """Obtener estadísticas del ejecutor"""
        return {
            "acciones_en_cola": len(self.acciones_en_cola),
            "acciones_ejecutadas": len(self.historial_ejecuciones),
            "timestamp": datetime.utcnow().isoformat()
        }


# Instancia global del ejecutor de acciones
action_runner = ActionRunner()
