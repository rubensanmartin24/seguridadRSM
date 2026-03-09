"""
SeguridadRSM Agent - Agente de Monitorización

Responsable de:
1. Recolectar eventos del sistema (network, procesos, archivos)
2. Detectar amenazas locales
3. Enviar eventos al backend central

Estructura modular:
- collector/: Recolección de datos del sistema
- detectors/: Detección local de anomalías
- senders/: Comunicación con el backend
"""

import json
import logging
import sys
from pathlib import Path

# Configurar logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)


class SeguridadRSMAgent:
    """
    Agente de monitorización principal.
    
    Orquesta los módulos de collector, detectors y senders para
    recolectar información del sistema y reportarla al backend.
    """
    
    def __init__(self, config_path: str = "config.json"):
        """
        Inicializar el agente.
        
        Args:
            config_path: Ruta al archivo de configuración
        """
        self.config_path = Path(config_path)
        self.config = self._cargar_configuracion()
        self.estado = "inicializado"
        logger.info(f"Agente SeguridadRSM v{self.config['agente']['version']} inicializado")
    
    def _cargar_configuracion(self) -> dict:
        """
        Cargar configuración desde archivo JSON.
        
        Returns:
            Diccionario de configuración
        """
        try:
            if self.config_path.exists():
                with open(self.config_path, 'r') as f:
                    config = json.load(f)
                logger.info(f"Configuración cargada desde {self.config_path}")
                return config
            else:
                logger.warning(f"Archivo de configuración no encontrado: {self.config_path}")
                return self._configuracion_por_defecto()
        except Exception as e:
            logger.error(f"Error al cargar configuración: {e}")
            return self._configuracion_por_defecto()
    
    def _configuracion_por_defecto(self) -> dict:
        """Retornar configuración por defecto"""
        return {
            "agente": {
                "nombre": "Agente SeguridadRSM",
                "version": "0.1.0",
                "hostname": "localhost"
            },
            "backend": {
                "url": "http://localhost:8000",
                "puerto": 8000
            },
            "monitoreo": {
                "intervalo_reporte": 60
            }
        }
    
    def iniciar(self):
        """Iniciar el agente y sus módulos"""
        logger.info("Iniciando agente de monitorización...")
        
        try:
            self._inicializar_modulos()
            self.estado = "ejecutando"
            logger.info("Agente ejecutándose correctamente")
            
            # TODO: Implementar bucle principal
            # - Recolectar eventos
            # - Procesar eventos
            # - Enviar al backend
            
        except Exception as e:
            logger.error(f"Error al iniciar agente: {e}")
            self.estado = "error"
            sys.exit(1)
    
    def _inicializar_modulos(self):
        """
        Inicializar módulos del agente.
        
        TODO:
        - Inicializar collector
        - Inicializar detectors
        - Inicializar senders
        - Validar conectividad con backend
        """
        logger.info("Inicializando módulos...")
        
        modulos = self.config.get('modulos', {})
        
        if modulos.get('collector', {}).get('habilitado'):
            logger.info("✓ Módulo collector habilitado")
        
        if modulos.get('detectors', {}).get('habilitado'):
            logger.info("✓ Módulo detectors habilitado")
        
        if modulos.get('senders', {}).get('habilitado'):
            logger.info("✓ Módulo senders habilitado")
    
    def detener(self):
        """Detener el agente correctamente"""
        logger.info("Deteniendo agente...")
        self.estado = "detenido"
        logger.info("Agente detenido correctamente")
    
    def obtener_estado(self) -> dict:
        """Obtener estado actual del agente"""
        return {
            "estado": self.estado,
            "agente": self.config.get('agente', {}),
            "timestamp": str(__import__('datetime').datetime.utcnow())
        }


def main():
    """Punto de entrada principal del agente"""
    agente = SeguridadRSMAgent()
    
    try:
        agente.iniciar()
        
        # Mantener el agente ejecutándose
        import time
        while agente.estado == "ejecutando":
            time.sleep(1)
            
    except KeyboardInterrupt:
        logger.info("Interrupción del usuario detectada")
        agente.detener()
    except Exception as e:
        logger.error(f"Error no manejado: {e}")
        sys.exit(1)


if __name__ == "__main__":
    main()
