# SeguridadRSM - Plataforma IDS + SOAR

Sistema ligero de detección de intrusiones y respuesta automática de seguridad (IDS + SOAR) diseñado para entornos domésticos y pymes.

**Autor**: Ruben San Martin  
**Proyecto**: TFG Ciberseguridad  
**Versión**: 0.1.0

## 🎯 Objetivo

Desarrollar un prototipo funcional de plataforma IDS + SOAR que:

1. **Detecte intrusiones** mediante análisis de eventos de red y sistema
2. **Responda automáticamente** ejecutando acciones de mitigación
3. **Sea ligero** para ejecutarse en equipos con recursos limitados
4. **Sea modular** para facilitar desarrollo y mantenimiento
5. **Sea defendible académicamente** con arquitectura clara

## 🏗️ Arquitectura

### Tres bloques principales

```
Internet/Amenazas
        ↓
┌──────────────────────────────────────────────────────┐
│                   EQUIPOS PROTEGIDOS                 │
│  ┌────────────┐  ┌────────────┐  ┌────────────┐     │
│  │  Agente 1  │  │  Agente 2  │  │  Agente N  │     │
│  │ (Host A)   │  │ (Host B)   │  │ (Host N)   │     │
│  └─────┬──────┘  └─────┬──────┘  └─────┬──────┘     │
└────────┼─────────────────┼─────────────────┼─────────┘
         │                 │                 │
         └─────────────────┼─────────────────┘
              HTTPS/TCP     │
                   ┌────────▼─────────┐
                   │  SERVIDOR CENTRAL│
                   │  (Backend)       │
                   │  ┌────────────┐  │
                   │  │   IDS      │  │
                   │  │  Motor     │  │
                   │  └────────────┘  │
                   │  ┌────────────┐  │
                   │  │   SOAR     │  │
                   │  │  Motor     │  │
                   │  └────────────┘  │
                   │  ┌────────────┐  │
                   │  │ Base Datos │  │
                   │  │ SQLite     │  │
                   │  └────────────┘  │
                   └────────┬─────────┘
                            │
                   ┌────────▼─────────┐
                   │   Panel Web      │
                   │ (Administración) │
                   └──────────────────┘
```

### Bloque 1: Agente de Monitorización (`agente/`)

Aplicación ligera que se ejecuta en cada equipo protegido.

**Responsabilidades:**
- Capturar eventos del sistema (red, procesos, archivos, logs)
- Ejecutar detección local de amenazas
- Enviar eventos al servidor central

**Módulos:**
- **Collector**: Recolección de eventos brutos
- **Detectors**: Detección local de anomalías
- **Senders**: Comunicación con el backend

**Lenguaje**: Python 3.8+

### Bloque 2: Servidor Central (`backend/`)

Aplicación FastAPI que centraliza:
- Recepción de eventos de agentes
- Motor IDS (Intrusion Detection System)
- Motor SOAR (Security Orchestration, Automation, Response)
- Base de datos centralizada
- API REST

**Servicios:**
- **IDS Engine**: Análisis de eventos y generación de alertas
- **SOAR Engine**: Orquestación de respuestas automáticas
- **Rule Engine**: Gestión de reglas de detección
- **Action Runner**: Ejecución de acciones de respuesta

**Base de datos**: SQLite (preparado para PostgreSQL)

**Lenguaje**: Python 3.8+ (FastAPI)

### Bloque 3: Panel Web de Gestión (`src/`)

Interfaz web moderna para administración del sistema.

**Características (futuro):**
- Dashboard de eventos y alertas
- Configuración de reglas
- Gestión de agentes
- Reportes de seguridad
- Respuesta manual a incidentes

**Stack**: Next.js + TypeScript + TailwindCSS

## 📂 Estructura del repositorio

```
seguridadRSM/
├── README.md                    # Este archivo
├── agente/                      # Agente de monitorización
│   ├── agent.py                # Agente principal
│   ├── config.json             # Configuración
│   ├── requirements.txt         # Dependencias Python
│   ├── collector/              # Recolección de eventos
│   │   ├── __init__.py
│   │   ├── log_reader.py
│   │   ├── network_monitor.py
│   │   ├── process_monitor.py
│   │   └── utils.py
│   ├── senders/                # Envío al backend
│   │   ├── __init__.py
│   │   └── sender.py
│   └── detectors/              # Detección local
│       ├── __init__.py
│       └── detector.py
│
├── backend/                     # Servidor central
│   ├── main.py                 # Punto de entrada
│   ├── .env                    # Variables de entorno
│   ├── requirements.txt        # Dependencias Python
│   ├── api/
│   │   ├── main.py            # Aplicación FastAPI
│   │   ├── routes/            # Endpoints
│   │   │   ├── eventos.py
│   │   │   ├── alertas.py
│   │   │   ├── acciones.py
│   │   │   ├── reglas.py
│   │   │   └── agentes.py
│   │   ├── models/            # Modelos SQLAlchemy
│   │   │   ├── evento.py
│   │   │   ├── alerta.py
│   │   │   ├── accion.py
│   │   │   ├── regla.py
│   │   │   └── agente.py
│   │   ├── schemas/           # Schemas Pydantic
│   │   ├── services/          # Lógica de negocio
│   │   │   ├── ids_engine.py
│   │   │   ├── soar_engine.py
│   │   │   ├── rule_engine.py
│   │   │   └── action_runner.py
│   │   └── utils/
│   │       └── db.py          # Base de datos
│   ├── tests/                 # Tests unitarios
│   └── README.md              # Documentación del backend
│
├── src/                        # Frontend (Next.js)
│   ├── app/
│   ├── components/
│   ├── lib/
│   └── ...
│
├── docs/                       # Documentación
│   ├── diagramas/
│   └── memoria/
│
├── package.json              # Dependencias Node.js (frontend)
└── tsconfig.json             # Config TypeScript
```

## 🚀 Quick Start

### Backend

```bash
# 1. Navegar al directorio backend
cd backend

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Ejecutar servidor
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

Backend disponible en: `http://localhost:8000`  
Documentación: `http://localhost:8000/docs`

### Agente

```bash
# 1. Navegar al directorio agente
cd agente

# 2. Crear entorno virtual
python3 -m venv venv
source venv/bin/activate

# 3. Instalar dependencias
pip install -r requirements.txt

# 4. Configurar (editar config.json)

# 5. Ejecutar agente
python agent.py
```

### Frontend

```bash
# 1. Instalar dependencias
npm install

# 2. Ejecutar en desarrollo
npm run dev

# 3. Acceder a http://localhost:3000
```

## 🔌 API REST

### Endpoints principales

**Health Check**
- `GET /health` - Verificar que el servidor está activo

**Eventos**
- `GET /api/eventos` - Listar eventos
- `POST /api/eventos` - Crear evento

**Alertas**
- `GET /api/alertas` - Listar alertas
- `POST /api/alertas` - Crear alerta

**Acciones**
- `GET /api/acciones` - Listar acciones
- `POST /api/acciones` - Crear acción

**Reglas**
- `GET /api/reglas` - Listar reglas
- `POST /api/reglas` - Crear regla

**Agentes**
- `GET /api/agentes` - Listar agentes registrados
- `POST /api/agentes` - Registrar agente nuevo

Ver [backend/README.md](backend/README.md) para documentación completa.

## 💾 Base de datos

### SQLite (por defecto)

- Ligera y sin dependencias externas
- Perfecta para desarrollo y testing
- Archivo: `backend/seguridadrsm.db`

### PostgreSQL (futuro)

- Mayor capacidad y rendimiento
- Replicación y backup
- Cambiar solo variable de entorno `DATABASE_URL`

## 🔒 Seguridad

Consideraciones implementadas/planeadas:

- [x] Validación de entrada (Pydantic)
- [x] Uso de CORS
- [ ] Autenticación JWT
- [ ] Encriptación de comunicaciones
- [ ] Rate limiting
- [ ] SQL injection prevention (SQLAlchemy ORM)
- [ ] XSS prevention (Framework defaults)
- [ ] CSRF protection

## 📊 Flujo de operación

```
1. AGENTE captura evento (red, proceso, log)
   ↓
2. AGENTE analiza localmente con Detector
   ↓
3. AGENTE envía evento al Backend
   ↓
4. BACKEND recibe evento en /api/eventos
   ↓
5. IDS ENGINE analiza evento contra reglas
   ↓
6. Si coincide → BACKEND genera Alerta
   ↓
7. SOAR ENGINE evalúa alerta
   ↓
8. Si severidad alta → SOAR ejecuta Acción automática
   ↓
9. PANEL WEB muestra evento/alerta/acción en tiempo real
   ↓
10. ADMINISTRADOR puede revisar, escalar o desmentir falsos positivos
```

## 🧪 Testing

```bash
# Backend
cd backend
pytest tests/

# Frontend
npm test
```

## 📚 Documentación

- [Backend](backend/README.md) - Documentación técnica del servidor central
- [Agente](agente/README.md) - Documentación del agente distribuido
- [docs/](docs/) - Diagramas, memoria y especificaciones

## 🗺️ Roadmap

**Fase 1 (Actual)**: Arquitectura base y endpoints básicos

**Fase 2 (Próxima):**
- Implementar lógica real de IDS
- Implementar acciones automáticas SOAR
- Autenticación JWT

**Fase 3:**
- Frontend completo
- Soporte para múltiples agentes
- Base de datos PostgreSQL

**Fase 4:**
- Machine Learning para detección de anomalías
- Integración con herramientas SIEM
- Reporting y análisis

## 🤝 Contribuciones

Este es un proyecto TFG. Se aceptan sugerencias y mejoras.

## 📄 Licencia

[Especificar licencia - MIT, GPL, etc.]

## 👨‍💼 Contacto

Ruben San Martin - TFG Ciberseguridad

---

**Nota**: Este proyecto está en fase de desarrollo. No usar en producción sin revisión de seguridad completa.
