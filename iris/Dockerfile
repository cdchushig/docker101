FROM python:3.11-slim-bullseye

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de dependencias
COPY requirements.txt requirements.txt

# Configura variables de entorno para pip (sin barras de progreso)
ENV PIP_NO_PROGRESS_BAR=off
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PIP_PROGRESS_BAR=off

# Instalar dependencias del sistema necesarias para BLAS
RUN apt-get update && apt-get install -y --no-install-recommends \
    gfortran \
    libopenblas-dev \
    liblapack-dev \
    && rm -rf /var/lib/apt/lists/*

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

RUN pip list

# Copia todos los archivos del proyecto al contenedor
COPY . .

# Evitar que OpenBLAS cree hilos
ENV OPENBLAS_NUM_THREADS=1 OMP_NUM_THREADS=1

# Ejecuta en build-time, dejando el modelo guardado en la imagen
RUN python train_model.py

# Expone el puerto de la aplicación Flask / Gunicorn
EXPOSE 8082

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8082", "app:app"]
