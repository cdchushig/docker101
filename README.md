Docker first examples
====

Este repositorio es parte del curso de MLOps para la Semana de la Ciencia URJC 2025. 
Contiene varios ejemplos prácticos de Docker aplicados y que servirán para el desarrollo 
de proyectos con MLOps.

Cada ejemplo demuestra un caso distinto de uso de contenedores: (1) desde un script básico,
(2) pasando por una aplicación web con Flask, (3) hasta un proyecto de ML completo y 
(4) un ejemplo de sistema de archivos compartido entre host y contenedor.

Este repositorio fue ejecutado con Docker version 19.03.1.

### Comandos básicos de Docker

Antes de empezar, algunos comandos útiles:
```shell
# Ver todos los contenedores (en ejecución o detenidos)
docker ps -a 
```

```shell
# Ver todas las imágenes Docker en local
docker images
```

```shell
# Detener todos los contenedores en ejecución
docker stop $(docker ps -q)
```

```shell
# Eliminar todos los contenedores detenidos
docker container prune
```


### Primer ejemplo (basic)

En este ejemplo, ejecutaremos un contenedor simple con un script Python para mostrar 
cómo Docker encapsula un entorno mínimo de ejecución.

Ir al directorio del proyecto:
```shell
cd basic
```

Construir la imagen de Docker:
```shell
docker build -t basic-app .
```

Ejecutar el contenedor:
```shell
docker run basic-app
```

### Segundo ejemplo (webapp)

Crearemos una aplicación web basada en Flask, sirviendo una página simple.
Es el primer paso hacia la creación de APIs para modelos de ML.

Ir al directorio del proyecto:
```shell
cd webapp
```

Construir la imagen de Docker:
```shell
docker build -t flask-webapp .
```

Ejecutar el contenedor:
```shell
docker run -p 8081:8081 flask-webapp
docker run --rm --ulimit nproc=4096 --ulimit nofile=1024:1024 flask-webapp
```

Ver la app en el navegador: http://0.0.0.0:8081 

### Tercer ejemplo (iris)

Crearemos una API que sirve un modelo de clasificación de Iris usando scikit-learn.

Ir al directorio del proyecto:
```shell
cd iris
```

Construir la imagen Docker:
```shell
docker build -t iris-web .
```

Ejecutar el contenedor:
```shell
docker run -p 8082:8082 -e OPENBLAS_NUM_THREADS=1 iris-web
```

Ver la app en el navegador: http://localhost:8082

### Cuarto ejemplo (fisystem)

Demostraemos cómo compartir archivos entre el sistema anfitrión y el contenedor usando volúmenes (-v).
Cualquier archivo creado dentro de /app/shared será visible también en la carpeta shared/ del host.

Ir al directorio del proyecto:
```shell
cd fisystem
```

Construir la imagen Docker:
```shell
docker build -t fisystem .
```

Ejecutar el contenedor en Linux:
```shell
docker run -it --name contenedor100 -v "$(pwd)/shared":/app/shared fisystem
```

Ejecutar el contenedor en Windows:
```shell
$ docker run -it --name contenedor100 -v ${PWD}/shared:/app/shared fisystem
```


