# SeguridadRSM Backend

Backend del sistema IDS + SOAR para entornos domésticos y pymes.

## Arquitectura

```
backend/
├── main.py                 # Punto de entrada de la aplicación
├── .env                    # Variables de entorno
├── requirements.txt        # Dependencias Python
├── api/
│   ├── main.py            # Aplicación FastAPI
│   ├── routes/            # Endpoints de la API
│   │   ├── eventos.py
│   │   ├── alertas.py
│   │   ├── acciones.py
│   │   ├── reglas.py
│   │   └── agentes.py
│   ├── models/            # Modelos SQLAlchemy
│   │   ├── evento.py
│   │   ├── alerta.py
│   │   ├── accion.py
│   │   ├── regla.py
│   │   └── agente.py
│   ├── schemas/           # Schemas Pydantic para validación
│   │   ├── evento.py
│   │   ├── alerta.py
│   │   ├── accion.py
│   │   ├── regla.py
│   │   └── agente.py
│   ├── services/          # Lógica de negocio
│   │   ├── ids_engine.py        # Motor de detección IDS
│   │   ├── soar_engine.py       # Motor de respuesta SOAR
│   │   ├── rule_engine.py       # Motor de reglas
│   │   └── action_runner.py     # Ejecutor de acciones
│   └── utils/
│       └── db.py          # Configuración de base de datos
└── tests/                 # Tests unitarios
```

## Requisitos

- Python 3.8+
- pip (gestor de paquetes Python)

## Instalación

### 1. Crear entorno virtual (recomendado)

```bash
cd backend
python3 -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### 2. Instalar dependencias

```bash
pip install -r requirements.txt
```

### 3. Configurar base de datos

Editar `.env` si es necesario (por defecto usa SQLite):

```ini
DATABASE_URL=sqlite:///./seguridadrsm.db
DEBUG=True
```

Para usar PostgreSQL en el futuro:
```ini
DATABASE_URL=postgresql://usuario:contraseña@localhost:5432/seguridadrsm
DEBUG=False
```

## Ejecución

### Modo desarrollo (con recarga automática)

```bash
cd backend
uvicorn main:app --reload --host 0.0.0.0 --port 8000
```

### Modo producción

```bash
cd backend
uvicorn main:app --host 0.0.0.0 --port 8000 --workers 4
```

## Endpoints disponibles

### Documentación interactiva
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Health Check
- **GET** `/`: Estado general del sistema
- **GET** `/health`: Health check para monitorización

### Eventos
- **GET** `/api/eventos` - Listar eventos
- **GET** `/api/eventos/{id}` - Obtener evento
- **POST** `/api/eventos` - Crear evento
- **PUT** `/api/eventos/{id}` - Actualizar evento
- **DELETE** `/api/eventos/{id}` - Eliminar evento

### Alertas
- **GET** `/api/alertas` - Listar alertas
- **GET** `/api/alertas/{id}` - Obtener alerta
- **POST** `/api/alertas` - Crear alerta
- **PUT** `/api/alertas/{id}` - Actualizar alerta
- **DELETE** `/api/alertas/{id}` - Eliminar alerta

### Acciones
- **GET** `/api/acciones` - Listar acciones
- **GET** `/api/acciones/{id}` - Obtener acción
- **POST** `/api/acciones` - Crear acción
- **PUT** `/api/acciones/{id}` - Actualizar acción
- **DELETE** `/api/acciones/{id}` - Eliminar acción

### Reglas
- **GET** `/api/reglas` - Listar reglas
- **GET** `/api/reglas/{id}` - Obtener regla
- **POST** `/api/reglas` - Crear regla
- **PUT** `/api/reglas/{id}` - Actualizar regla
- **DELETE** `/api/reglas/{id}` - Eliminar regla

### Agentes
- **GET** `/api/agentes` - Listar agentes
- **GET** `/api/agentes/{id}` - Obtener agente
- **POST** `/api/agentes` - Registrar agente
- **PUT** `/api/agentes/{id}` - Actualizar agente
- **DELETE** `/api/agentes/{id}` - Eliminar agente

## Estructura de datos

### Evento
```json
{
  "agente_id": 1,
  "tipo": "network",
  "descripcion": "Conexión TCP a puerto 22",
  "fuente": "192.168.1.100",
  "destino": "192.168.1.1:22",
  "metadata": {}
}
```

### Alerta
```json
{
  "evento_id": 1,
  "severidad": "alto",
  "descripcion": "Intento de SSH detectado",
  "regla_id": 5
}
```

### Acción
```json
{
  "alerta_id": 1,
  "tipo": "bloqueo",
  "descripcion": "Bloquear IP 192.168.1.100"
}
```

### Regla
```json
{
  "nombre": "Detectar SSH Brute Force",
  "descripcion": "Detecta intentos de SSH",
  "patron": ".*ssh.*",
  "tipo": "signature",
  "severidad": "alto"
}
```

### Agente
```json
{
  "nombre": "Agente-Casa",
  "hostname": "home-pc",
  "ip_address": "192.168.1.100",
  "sistema_operativo": "Linux",
  "version": "0.1.0"
}
```

## Desarrollo

### Crear migraciones (futuro)

Con Alembic para gestionar cambios en esquema:

```bash
alembic init alembic
alembic revision --autogenerate -m "Descripción del cambio"
alembic upgrade head
```

### Tests

```bash
pytest tests/
```

## Características planificadas

- [ ] Autenticación y autorización JWT
- [ ] Rate limiting
- [ ] Logging avanzado
- [ ] Métricas y monitoring
- [ ] Transacciones distribuidas
- [ ] Cache Redis
- [ ] Soporte WebSocket para alertas en tiempo real
- [ ] Exportación de reportes
- [ ] Integración con SIEM externos

## Referencias

- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [SQLAlchemy Documentation](https://docs.sqlalchemy.org/)
- [Pydantic Documentation](https://docs.pydantic.dev/)

## Autor

Ruben San Martin - TFG Ciberseguridad
