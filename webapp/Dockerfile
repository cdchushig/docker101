FROM python:3.11

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de librerías Python
COPY requirements.txt requirements.txt

# Configura variables de entorno para pip (sin barras de progreso)
ENV PIP_NO_PROGRESS_BAR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_PROGRESS_BAR=off

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir --progress-bar=off -r requirements.txt

COPY . .

EXPOSE 8081

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8081", "app:app"]
