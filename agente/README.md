# SeguridadRSM Agent

Agente de monitorización distribuido para capturar eventos del sistema y reportarlos al backend central.

## Arquitectura

```
agente/
├── agent.py              # Agente principal
├── config.json           # Configuración del agente
├── requirements.txt      # Dependencias Python
├── collector/            # Recolección de eventos
│   ├── log_reader.py
│   ├── network_monitor.py
│   └── process_monitor.py
├── senders/              # Envío al backend
│   └── sender.py
└── detectors/            # Detección local
    └── detector.py
```

## Requisitos

- Python 3.8+
- pip (gestor de paquetes Python)
- Acceso a herramientas del sistema (netstat, ss, /proc, etc.)

## Instalación

### 1. Crear entorno virtual

```bash
cd agente
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar agente

Editar `config.json` con los datos del entorno:

```json
{
  "agente": {
    "nombre": "Agente-Casa",
    "hostname": "mi-pc"
  },
  "backend": {
    "url": "http://192.168.1.10:8000"
  }
}
```

## Ejecución

```bash
cd agente
python agent.py
```

O con logging detallado:

```bash
python agent.py --debug
```

## Módulos

### Collector (Recolección)

Responsable de capturar eventos del sistema:

- **NetworkMonitor**: Conexiones de red, puertos abiertos, DNS
- **ProcessMonitor**: Procesos ejecutados, uso de recursos
- **LogReader**: Logs del sistema, eventos importantes

### Senders (Envío)

Responsable de comunicarse con el backend:

- Envío de eventos en lote
- Reintentos automáticos
- Verificación de conectividad
- Registro de agentes

### Detectors (Detección local)

Responsable de detectar amenazas localmente:

- Detección de malware
- Detección de inyección de código
- Detección de anomalías de comportamiento
- Indicadores de compromiso (IoCs)

## Flujo de funcionamiento

```
1. Agent.start()
   ├── Cargar configuración
   └── Inicializar módulos
   
2. Loop principal (cada N segundos)
   ├── Collector.get_events()
   │   ├── NetworkMonitor.get_active_connections()
   │   ├── ProcessMonitor.get_active_processes()
   │   └── LogReader.get_logs()
   │
   ├── Detector.analyze_events()
   │   └── [Generar alertas locales]
   │
   └── Sender.send_events()
       └── POST /api/eventos
       └── POST /api/alertas (si aplica)
```

## Configuración avanzada

### Rutas a monitorizar

En el futuro, permitirá especificar rutas de archivos a vigilar:

```json
{
  "monitoreo": {
    "rutas": [
      "/home",
      "/etc/passwd",
      "/var/log"
    ]
  }
}
```

### Reglas locales

En el futuro, permitirá reglas de detección local sin depender del backend:

```json
{
  "reglas_locales": [
    {
      "nombre": "Detectar puerto SSH anómalo",
      "tipo": "network",
      "accion": "alerta"
    }
  ]
}
```

## Seguridad

- Validar certificados SSL/TLS del backend
- No almacenar credenciales en plaintext
- Encriptar datos sensibles localmente
- Limitar logs según severidad
- Ejecutar con mínimos permisos necesarios

## Monitorización

El agente genera logs con información de:

- Errores de conectividad
- Eventos capturados
- Anomalías detectadas
- Estado del sistema

## Troubleshooting

### Error: No se conecta al backend

```bash
# Verificar conectividad
curl http://localhost:8000/health
```

### Error: Permisos insuficientes

Algunos módulos requieren permisos de administrador:

```bash
sudo python agent.py
```

### Debug

Habilitar logging detallado en config.json:

```json
{
  "monitoreo": {
    "nivel_log": "DEBUG"
  }
}
```

## Características planificadas

- [ ] Soporte para Windows y macOS
- [ ] GUI de configuración
- [ ] Auto-update del agente
- [ ] Respuesta local automática
- [ ] Machine Learning para detección
- [ ] Compresión de datos
- [ ] Sincronización de hora NTP
- [ ] Rotación de logs local

## Autor

Ruben San Martin - TFG Ciberseguridad
