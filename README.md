Docker first examples
====

Este repo es parte del curso para USFQ sobre MLOps

### Comandos básicos
```shell
$ docker ps -a 
$ docker stop $(docker ps -q)
```


### Primer ejemplo

Ir al directorio del proyecto:
```shell
$ cd basic
```

Construir la imagen de Docker:
```shell
$ docker build -t basic-app .
```

Ejecutar el contenedor:
```shell
$ docker run basic-app
```

### Segundo ejemplo

Ir al directorio del proyecto:
```shell
$ cd webapp
```

Construir la imagen de Docker:
```shell
$ docker build -t flask-webapp .
```

Ejecutar el contenedor:
```shell
$ docker run -p 5000:5000 flask-webapp
$ docker run --rm --ulimit nproc=4096 --ulimit nofile=1024:1024 flask-webapp
```

Ver la app en el navegador: http://localhost:5000


### Tercer ejemplo

Ir al directorio del proyecto:
```shell
$ cd iris
```

Entrenar el modelo (solo una vez). Desde tu máquina local o antes de dockerizar.
```shell
$ pip install scikit-learn==1.6.1
$ python train_model.py
```

Construir la imagen Docker:
```shell
$ docker build -t iris-web .
```

Ejecutar el contenedor:
```shell
$ docker run -p 5000:5000 -e OPENBLAS_NUM_THREADS=1 iris-web
```

Ver la app en el navegador: http://localhost:5000

### Cuarto ejemplo

Ir al directorio del proyecto:
```shell
$ cd fisystem
```

Construir la imagen Docker:
```shell
$ docker build -t fisystem .
```

Ejecutar el contenedor en Linux:
```shell
$ docker run -it --name contenedor1 -v "$(pwd)/shared":/app/shared fisystem
```

Ejecutar el contenedor en Windows:
```shell
$ docker run -it --name contenedor1 -v ${PWD}/shared:/app/shared fisystem
```


