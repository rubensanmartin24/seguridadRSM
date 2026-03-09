"""
SeguridadRSM Backend - IDS + SOAR Platform
Plataforma ligera de detección y respuesta automática para entornos domésticos y pymes.

Servidor central que orquesta:
- Motor IDS (Detección de Intrusiones)
- Motor SOAR (Orquestación y Respuesta Automática)
- Base de datos centralizada
- API REST para agentes y panel web
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from api.utils.db import Base, engine, settings
from api.routes import eventos, alertas, acciones, reglas, agentes

# Crear la aplicación FastAPI
app = FastAPI(
    title=settings.app_name,
    description="Backend del sistema IDS + SOAR para ciberseguridad",
    version=settings.app_name,
    docs_url="/docs",
    redoc_url="/redoc"
)

# Configurar CORS para desarrollo
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # TODO: Restringir en producción
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas en la base de datos
Base.metadata.create_all(bind=engine)

# Incluir routers
app.include_router(eventos.router, prefix="/api/eventos", tags=["Eventos"])
app.include_router(alertas.router, prefix="/api/alertas", tags=["Alertas"])
app.include_router(acciones.router, prefix="/api/acciones", tags=["Acciones"])
app.include_router(reglas.router, prefix="/api/reglas", tags=["Reglas"])
app.include_router(agentes.router, prefix="/api/agentes", tags=["Agentes"])


@app.get("/")
def root():
    """Endpoint raíz para verificar que el servidor está funcionando"""
    return {
        "status": "ok",
        "message": "SeguridadRSM Backend funcionando correctamente",
        "app": settings.app_name,
        "version": settings.app_name
    }


@app.get("/health")
def health_check():
    """Endpoint de health check para monitorización"""
    return {
        "status": "healthy",
        "database": "sqlite" if settings.database_url.startswith("sqlite") else "postgresql"
    }


@app.on_event("startup")
async def startup_event():
    """Eventos de inicio de la aplicación"""
    print(f"✓ {settings.app_name} iniciado correctamente")
    print(f"✓ Base de datos: {settings.database_url.split('/')[-1]}")


@app.on_event("shutdown")
async def shutdown_event():
    """Eventos de cierre de la aplicación"""
    print(f"✓ {settings.app_name} cerrado")


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=settings.debug
    )

