# Entrega 1 
# Pipeline de MLOps y clasificador simulado

Es un [pipeline de MLOps](pipeline.md) para un sistema de clasificación a partir de síntomas e implementa un formulario web con Flask que ejecuta una función de clasificación basada en reglas. La aplicación es una simulación con datos no reales.

## Requisito

Tener Docker en ejecución. En Windows, abrimos Docker Desktop y verificamos con `docker version` que aparezcan las secciones **Client** y **Server**.

## Construimos la imagen

Abrimos una terminal en la carpeta que contiene el `Dockerfile` y ejecutamos en PowerShell:

**docker build -t clasificador-mlops:1.0**

Ahi se indica que Docker debe usar la carpeta actual para construir la imagen.

## Ejecutamos el contenedor en PowerShell

**docker run --rm -p 127.0.0.1:5001:5000 clasificador-mlops:1.0**

Dejamos la terminal abierta y entramos en [http://127.0.0.1:5001](http://127.0.0.1:5001). El Docker se conecta el puerto 5001 del computador con el 5000 del contenedor. Para detenerlo, presionamos **Ctrl + C** en la terminal.

## Probamos el formulario

Ingresamos los tres valores y pulsamos **Clasificar**. Verificamos estos cuatro casos en el contenedor.

| Cantidad de síntomas | Días con síntomas | Intensidad (0 a 10) | Resultado |
|---:|---:|---:|---|
| 0 | 0 | 0 | NO ENFERMO |
| 2 | 3 | 4 | ENFERMEDAD LEVE |
| 2 | 3 | 8 | ENFERMEDAD AGUDA |
| 2 | 40 | 4 | ENFERMEDAD CRÓNICA |

## Archivos principales

- `pipeline.md` y `diagrama_pipeline.png` presentan la propuesta y su diagrama.
- `app.py` recibe las entradas del formulario y muestra el resultado.
- `modelo.py` contiene la función de clasificación simulada.
- `templates/index.html` contiene el formulario.
- `requirements.txt` declara la versión de Flask.
- `Dockerfile` define cómo construir la imagen y arrancar la aplicación.



**SANDRA JIMENA OROZCO LAGOS**