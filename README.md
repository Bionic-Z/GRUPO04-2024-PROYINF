# Proyecto Ingeniería de Software

## Integrantes

- Rodrigo Flores – 202173523-2
- Aylin Rojas – 202173531-3
- Nestor Guajardo – 202173132-6
- Francisca Zavala – 202173632-8
- **Tutor:** Benjamín Daza

---

## Descripción

Este proyecto es la refactorización de la versión previa desarrollada en PHP a Python, utilizando las siguientes tecnologías:

- **Django:** Framework de servidor
- **PostgreSQL:** Sistema gestor de base de datos
- **Docker & Docker Compose:** Contenerización y orquestación
- **Bootstrap:** Framework CSS para el front-end

---

## Requisitos previos

- Docker (v20.10 o superior)
- Docker Compose (v1.29 o superior)
- Git (opcional, dependiendo de la forma de descarga)

---

## Instalación y ejecución

1. **Clonar el repositorio**
   ```bash
   git clone https://github.com/Bionic-Z/GRUPO04-2024-PROYINF.git
   cd GRUPO04-2024-PROYINF
   ```

2. **Configurar variables de entorno**
   Copiar el archivo de ejemplo y utilizar a gusto:
   ```bash
   cp .env.example .env
   ```

   Asegurar de que `.env` contenga al menos:
   ```ini
   POSTGRES_USER=django_user
   POSTGRES_PASSWORD=secretpassword
   POSTGRES_DB=django_db
   POSTGRES_HOST=db
   POSTGRES_PORT=5432

   DJANGO_SECRET_KEY=tu_clave_secreta_aqui
   DJANGO_DEBUG=True
   ```
> [!NOTE]
> Con las credenciales por defecto, el proyecto puede funcionar perfectamente.

3. **Construir y levantar los contenedores**

   ```bash
   docker-compose up -d --build
   ```

4. **Aplicar migraciones**

   ```bash
   docker-compose run --rm web python manage.py migrate
   ```

5. **Cargar datos de prueba**

   ```bash
   docker-compose run --rm web python manage.py create_roles
   docker-compose run --rm web python manage.py seed_users --count 50
   ```

6. **Abrir la aplicación**

   Navega a [http://localhost:8000/](http://localhost:8000/)


> [!WARNING]  
> Si el puerto de host `5433` está ocupado, puedes mapear otro puerto en `docker-compose.yml`:
>
> ```yaml
> services:
>   db:
>     ports:
>       - "<PUERTO_HOST>:5432"
> ```

---

## Estructura del proyecto

```text
.
├── README.md
├── backend
│   ├── Dockerfile
│   ├── app
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── docker
│   │   └── postgres-init
│   ├── manage.py
│   ├── requirements.txt
│   └── users
│       ├── __init__.py
│       ├── admin.py
│       ├── apps.py
│       ├── forms.py
│       ├── management
│       ├── migrations
│       ├── models.py
│       ├── templates
│       ├── tests.py
│       └── views.py
└── docker-compose.yml
```

---

## Información histórica (versión previa en PHP)

> La versión anterior fue desarrollada para el curso **Análisis y Diseño de Software (INF236)** en PHP, utilizando XAMPP, Apache y MySQL.

<details>
<summary>Ver detalles de la versión previa</summary>

**Repositorio antiguo:** [GRUPO04-2024-PROYINF (tag `hito-5`)](https://github.com/Bionic-Z/GRUPO04-2024-PROYINF/tree/hito-5)

**Aspectos técnicos:**
- Apache HTTP 2.4.58 + PHP 8.2.12
- MySQL / MariaDB 10.4.32
- XAMPP v3.3.0
- Dependencias Python (scrapers): `mysql-connector-python`, `requests`, `beautifulsoup4`

**Flujo de instalación:**
1. Instalar XAMPP (Windows)
2. Colocar archivos en `htdocs/proyecto-hito5`
3. Importar `boletines.sql` en PhpMyAdmin
4. Ejecutar `python scrape.py` para poblar tablas
5. Acceder a `http://localhost/proyecto-hito5/proyecto/init.html`

</details>

