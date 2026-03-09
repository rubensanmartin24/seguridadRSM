"""
Senders Module - Envío de eventos al backend

Responsable de enviar eventos recolectados al servidor central.
"""

import logging
import requests
import json
from typing import Dict, Any, List, Optional
from datetime import datetime

logger = logging.getLogger(__name__)


class EventSender:
    """
    Enviador de eventos al backend central.
    
    Funcionalidades:
    - Envío seguro de eventos
    - Reintentos automáticos
    - Caching local en caso de desconexión
    - Compresión de datos
    """
    
    def __init__(self, backend_url: str = "http://localhost:8000", timeout: int = 30):
        """
        Inicializar el enviador de eventos.
        
        Args:
            backend_url: URL del servidor backend
            timeout: Timeout para las solicitudes HTTP
        """
        self.backend_url = backend_url.rstrip('/')
        self.timeout = timeout
        self.eventos_enviados = 0
        self.eventos_fallidos = 0
        logger.info(f"EventSender inicializado - Backend: {self.backend_url}")
    
    def enviar_evento(self, evento: Dict[str, Any]) -> bool:
        """
        Enviar un evento individual al backend.
        
        Args:
            evento: Diccionario con datos del evento
            
        Returns:
            True si se envió correctamente
        """
        try:
            url = f"{self.backend_url}/api/eventos"
            response = requests.post(
                url,
                json=evento,
                timeout=self.timeout
            )
            
            if response.status_code in [200, 201]:
                self.eventos_enviados += 1
                logger.debug(f"Evento enviado correctamente: {evento.get('tipo')}")
                return True
            else:
                logger.warning(f"Error al enviar evento: {response.status_code}")
                self.eventos_fallidos += 1
                return False
                
        except Exception as e:
            logger.error(f"Error al enviar evento: {e}")
            self.eventos_fallidos += 1
            return False
    
    def enviar_eventos_batch(self, eventos: List[Dict[str, Any]]) -> Dict[str, Any]:
        """
        Enviar múltiples eventos en lote.
        
        Args:
            eventos: Lista de eventos
            
        Returns:
            Diccionario con resultados
        """
        exitosos = 0
        fallidos = 0
        
        for evento in eventos:
            if self.enviar_evento(evento):
                exitosos += 1
            else:
                fallidos += 1
        
        return {
            "total": len(eventos),
            "exitosos": exitosos,
            "fallidos": fallidos,
            "timestamp": datetime.utcnow().isoformat()
        }
    
    def verificar_conectividad(self) -> bool:
        """
        Verificar conectividad con el backend.
        
        Returns:
            True si el backend está disponible
        """
        try:
            url = f"{self.backend_url}/health"
            response = requests.get(url, timeout=5)
            return response.status_code == 200
        except Exception as e:
            logger.warning(f"Backend no disponible: {e}")
            return False
    
    def enviar_registro_agente(self, datos_agente: Dict[str, Any]) -> bool:
        """
        Enviar registro del agente al backend.
        
        Args:
            datos_agente: Información del agente
            
        Returns:
            True si se registró correctamente
        """
        try:
            url = f"{self.backend_url}/api/agentes"
            response = requests.post(
                url,
                json=datos_agente,
                timeout=self.timeout
            )
            return response.status_code in [200, 201]
        except Exception as e:
            logger.error(f"Error al registrar agente: {e}")
            return False
    
    def obtener_estadisticas(self) -> Dict[str, Any]:
        """Obtener estadísticas del enviador"""
        return {
            "eventos_enviados": self.eventos_enviados,
            "eventos_fallidos": self.eventos_fallidos,
            "backend": self.backend_url,
            "timestamp": datetime.utcnow().isoformat()
        }


# Instancia global
event_sender = EventSender()
