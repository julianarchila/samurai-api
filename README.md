# Samurai API

## Estructura del Proyecto

El proyecto está compuesto por múltiples servicios que interactúan mediante un reverse proxy para facilitar la comunicación entre las diferentes APIs y la interfaz de usuario:

- **`wiki-frontend`**:  
  Interfaz web diseñada con **HTML**, **JavaScript** y **Tailwind CSS**.

- **`api/bakugan`**:  
  Servicio API para datos relacionados con Bakugan, construido con **Python**, **Flask** y respaldado por una base de datos **MySQL**.

- **`api/poke`**:  
  Servicio API para datos de Pokémon, implementado con **Bun** y **Hono**.

### Reverse Proxy

Un reverse proxy gestiona las rutas y redirecciona las peticiones a los servicios correspondientes:

- `/api/bakugan` → API de Bakugan
- `/api/poke` → API de Pokémon

## Cómo Ejecutar

Sigue estos pasos para configurar y ejecutar el proyecto:

1. ** Inicia los servicios con Docker Compose:**

   ```bash
   docker compose up -d
   ```

2. **Inicia la base de datos:**
   ```bash
   ./seed-database.sh
   ```
3. **Abre el navegador y accede a la interfaz web:**
   ```bash
   http://localhost:8080
   ```
