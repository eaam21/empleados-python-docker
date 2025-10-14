# Proyecto CRUD de Empleados con Flask y Docker

Este es un proyecto de ejemplo de una aplicación web CRUD (Crear, Leer, Actualizar, Eliminar) de empleados, desarrollada con Flask y Docker.

## Requisitos

- Docker
- Docker Compose

## Cómo ejecutar el proyecto

1. **Clonar el repositorio:**

   ```bash
   git clone https://github.com/jfarfannet/flask-poo-docker
   ```

2. **Levantar los contenedores:**

   Navegue hasta el directorio raíz del proyecto y ejecute el siguiente comando:

   ```bash
   docker-compose up --build -d
   ```

   Este comando construirá las imágenes de Docker y levantará los contenedores de la aplicación y la base de datos en segundo plano.

3. **Acceder a la aplicación:**

   Una vez que los contenedores estén en funcionamiento, puede acceder a la aplicación en su navegador web en la siguiente URL:

   [http://localhost:5000](http://localhost:5000)

## Servicios

El proyecto utiliza dos servicios de Docker:

- **`app`**: El contenedor de la aplicación Flask. Se expone en el puerto 5000.
- **`db`**: El contenedor de la base de datos MySQL. Se expone en el puerto 32000.

## Comandos útiles de Docker

- **Ver los logs de los contenedores:**

  ```bash
  docker-compose logs -f
  ```

- **Detener y eliminar los contenedores:**

  ```bash
  docker-compose down
  ```

- **Listar los volúmenes de Docker:**

  ```bash
  docker volume ls
  ```
