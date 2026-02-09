# --- Etapa 1: Builder ---
#FROM python:3.11-slim as builder

#WORKDIR /app
#COPY requirements.txt .
# Instalamos dependencias
#RUN pip install --user --no-cache-dir -r requirements.txt

# --- Etapa 2: Runtime (Imagen Final) ---
#FROM python:3.11-slim
#WORKDIR /app

# Copiamos las librerías instaladas
#COPY --from=builder /root/.local /root/.local
# Copiamos el código fuente
#COPY ./app ./app

# IMPORTANTE: Si tienes archivos de configuración en la raíz (como el .env.example) 
# podrías querer copiarlos si el código los usa para algo.
# COPY .env.example .

#ENV PATH=/root/.local/bin:$PATH
#ENV PYTHONPATH=/app
# Aseguramos que Python no genere archivos .pyc innecesarios y envíe logs en tiempo real
#ENV PYTHONDONTWRITEBYTECODE=1
#ENV PYTHONUNBUFFERED=1

#EXPOSE 8000

# Tu comando dinámico es perfecto para la nube
#CMD uvicorn app.main:app --host 0.0.0.0 --port ${PORT:-8000}


FROM python:3.11-slim

# Crear usuario vscode
RUN useradd -ms /bin/bash vscode

WORKDIR /workspace

# Optimizaciones de Python
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PYTHONPATH=/workspace

# Instalación de herramientas de desarrollo necesarias
RUN apt-get update && apt-get install -y \
    git \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Instalamos dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# En desarrollo NO solemos hacer "COPY . ." aquí, 
# porque el docker-compose monta el código con "volumes".
# Pero dejarlo no hace daño.

USER vscode

# IMPORTANTE: No pongas CMD aquí si ya lo tienes en el docker-compose.yml
# El docker-compose sobrescribirá este comando de todas formas.
