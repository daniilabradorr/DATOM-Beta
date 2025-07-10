# DATOM - Gestión de Recursos y Datos

ES UNA BETA POR TANTO ESTA EN CONSTANTE MEJORA

(https://datom-beta.onrender.com/)

**DATOM** es una aplicación web desarrollada con Django que permite gestionar el Scrap, Down y Producción de una empresa. Su objetivo es proporcionar una interfaz intuitiva para la administración de recursos, mejorar la eficiencia operativa y optimizar la gestión de tareas de producción.

EL OBJETIVO REAL ES QUE SE VEA LA FUNCIONALIDAD QUE TIENE LA APLICACIÓN Y QUE SE PUEDE GESTIONAR LO QUE QUERAMOS (productos, trabajores, etc.)

## Características

- **Gestión de Tareas**: Administra y organiza tareas de manera eficiente.
- **Base de Datos SQLite**: Usa SQLite para el almacenamiento de datos.
- **Interfaz de Usuario**: Diseño sencillo y fácil de usar con HTML, CSS y Bootstrap.
- **Autenticación de Usuarios**: Permite crear y gestionar usuarios con roles específicos.
- **Panel de Administración**: Uso de Django Admin para gestionar datos.

## Tecnologías Utilizadas

- **Backend**: Django (Python)
- **Base de Datos**: PostgreSQL (para producción)
- **Frontend**: HTML, CSS, Bootstrap 5
- **Servidor**: Gunicorn (servidor WSGI para producción)
- **Despliegue**: Render

## Requisitos

Antes de comenzar, asegúrate de tener las siguientes herramientas instaladas:

- [Python](https://www.python.org/downloads/) (versión 3.6 o superior)
- [Pip](https://pip.pypa.io/en/stable/) (para instalar dependencias)
- [Git](https://git-scm.com/) (para control de versiones)
- [PostgreSQL](https://www.postgresql.org/download/) (base de datos en producción)

## Instalación

1. Clona este repositorio:

    ```bash
    git clone https://github.com/tu_usuario/datom.git
    cd datom
    ```

2. Crea un entorno virtual e instala las dependencias:

    ```bash
    python -m venv env
    source env/bin/activate  # En Windows usa 'env\Scripts\activate'
    pip install -r requirements.txt
    ```

3. Configura las variables de entorno necesarias en el archivo `.env` (puedes copiar el contenido de `.env.example` si lo tienes):

    - `SECRET_KEY`: Clave secreta para Django.
    - `DEBUG`: Pon `False` para producción.
    - `DATABASE_URL`: URL de la base de datos de PostgreSQL en producción (por ejemplo, `postgres://usuario:contraseña@host:puerto/base_de_datos`).
    - `ALLOWED_HOSTS`: Configura los hosts permitidos (por ejemplo, `['.onrender.com']` para producción en Render).

4. Realiza las migraciones:

    ```bash
    python manage.py migrate
    ```

5. Corre el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

   Ahora podrás acceder a la aplicación en `http://127.0.0.1:8000`.

## Despliegue en Producción

Este proyecto está diseñado para ser desplegado en [Render](https://render.com). Si deseas desplegarlo, sigue los siguientes pasos:

1. **Sube el proyecto a GitHub** (si no lo has hecho ya).
2. **Crea una cuenta en Render** y conecta tu repositorio de GitHub.
3. **Configura las variables de entorno** en Render para conectar con PostgreSQL.
4. **Configura el comando de despliegue** (Build Command: `pip install -r requirements.txt`, Start Command: `gunicorn DATOM.wsgi`).
5. **Realiza migraciones de base de datos** en la consola de Render.

## Contribuciones

Si deseas contribuir a este proyecto, por favor sigue estos pasos:

1. Haz un fork de este repositorio.
2. Crea una rama para tu nueva característica o corrección de bug.
3. Realiza tus cambios y haz un commit.
4. Sube tu rama a tu repositorio remoto.
5. Crea un Pull Request describiendo tus cambios.

## Licencia

Este proyecto está bajo la Licencia MIT. Para más detalles, consulta el archivo [LICENSE](LICENSE).
