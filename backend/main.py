"""
SeguridadRSM Backend - Punto de entrada principal

Para ejecutar:
    cd backend
    uvicorn main:app --reload --host 0.0.0.0 --port 8000
"""

from api.main import app

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True
    )
