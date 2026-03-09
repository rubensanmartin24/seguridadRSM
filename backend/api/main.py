from fastapi import FastAPI
from backend.api.utils.db import Base, engine
from api.routes import eventos, alertas, acciones

app = FastAPI(
    title="IDS + SOAR Backend",
    description="Backend del sistema de detección y respuesta automática",
    version="1.0.0"
)

# Crear tablas en PostgreSQL al arrancar
Base.metadata.create_all(bind=engine)

# Registrar rutas
app.include_router(eventos.router, prefix="/eventos", tags=["Eventos"])
app.include_router(alertas.router, prefix="/alertas", tags=["Alertas"])
app.include_router(acciones.router, prefix="/acciones", tags=["Acciones"])

@app.get("/")
def root():
    return {"status": "ok", "message": "Backend IDS + SOAR funcionando"}
