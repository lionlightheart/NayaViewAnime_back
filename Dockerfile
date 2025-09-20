# Usa Python oficial
FROM python:3.12-slim

# Variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Crear carpeta del proyecto
WORKDIR /app

# Copiar requirements
COPY requirements.txt /app/

# Instalar dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Copiar código
COPY . /app/

# Exponer puerto
EXPOSE 8000

# Comando por defecto
CMD ["gunicorn", "NayaViewAnime_Back.wsgi:application", "--bind", "0.0.0.0:8000", "--workers", "3", "--log-level", "debug", "--access-logfile", "-", "--error-logfile", "-"]

