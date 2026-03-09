#!/bin/bash

# Script de inicio rápido para SeguridadRSM
# Requiere: Python 3.8+, npm

echo "============================================"
echo "SeguridadRSM - Initialization Script"
echo "============================================"
echo ""

# Colores para output
GREEN='\033[0;32m'
BLUE='\033[0;34m'
NC='\033[0m' # No Color

# 1. Backend
echo -e "${BLUE}[1/3] Configurando Backend...${NC}"
cd backend

if [ ! -d "venv" ]; then
    echo "  Creando entorno virtual..."
    python3 -m venv venv
fi

echo "  Activando entorno virtual..."
source venv/bin/activate

echo "  Instalando dependencias..."
pip install -q -r requirements.txt

echo -e "${GREEN}✓ Backend configurado${NC}"
echo ""

cd ..

# 2. Agente
echo -e "${BLUE}[2/3] Configurando Agente...${NC}"
cd agente

if [ ! -d "venv" ]; then
    echo "  Creando entorno virtual..."
    python3 -m venv venv
fi

echo "  Activando entorno virtual..."
source venv/bin/activate

echo "  Instalando dependencias..."
pip install -q -r requirements.txt

echo -e "${GREEN}✓ Agente configurado${NC}"
echo ""

cd ..

# 3. Frontend
echo -e "${BLUE}[3/3] Configurando Frontend...${NC}"

if ! command -v npm &> /dev/null; then
    echo "  npm no instalado. Saltando instalación de frontend."
else
    echo "  Instalando dependencias Node.js..."
    npm install -q
    echo -e "${GREEN}✓ Frontend configurado${NC}"
fi

echo ""
echo "============================================"
echo -e "${GREEN}✓ Inicialización completada${NC}"
echo "============================================"
echo ""
echo "Para iniciar:"
echo ""
echo "Backend:"
echo "  cd backend"
echo "  source venv/bin/activate"
echo "  uvicorn main:app --reload --host 0.0.0.0 --port 8000"
echo ""
echo "Agente:"
echo "  cd agente"
echo "  source venv/bin/activate"
echo "  python agent.py"
echo ""
echo "Frontend:"
echo "  npm run dev"
echo ""
