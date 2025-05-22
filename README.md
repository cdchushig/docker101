Docker first examples
====

Este repo es parte del curso para USFQ sobre MLOps

### Primer ejemplo

Ir al directorio del proyecto:
```shell
$ cd myapp
```

Construir la imagen de Docker:
```shell
$ docker build -t .
```

Ejecutar el contenedor:
```shell
$ docker run 
```

### Segundo ejemplo

Ir al directorio del proyecto:
```shell
$ cd myapp
```

Construir la imagen de Docker:
```shell
$ docker build -t flask-webapp .
```

Ejecutar el contenedor:
```shell
$ docker run -p 5000:5000 flask-webapp
```

Ver la app en el navegador: http://localhost:5000


### Tercer ejemplo

Ir al directorio del proyecto:
```shell
$ cd myapp
```

Entrenar el modelo (solo una vez). Desde tu máquina local o antes de dockerizar.
```shell
$ python train_model.py
```

Construir la imagen Docker:
```shell
$ docker build -t iris-predictor .
```

Ejecutar el contenedor:
```shell
$ docker run -p 5000:5000 iris-predictor
```

Ver la app en el navegador: http://localhost:5000

