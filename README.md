# Audify API

Audify es una plataforma avanzada de transmisión y gestión musical. Su API (Interfaz de Programación de Aplicaciones) proporciona los servicios necesarios para operar el ecosistema completo de la aplicación, abarcando entidades como pistas musicales (tracks), álbumes, listas de reproducción (playlists) y control de perfiles de usuario. Diseñada con la escalabilidad y el mantenimiento a largo plazo como pilares principales, la API de Audify permite integrar de manera eficiente los flujos de reproducción y la administración de catálogo musical, ofreciendo respuestas rápidas, seguras y estructuradas a todos los clientes conectados.

## 2. Arquitectura del Proyecto
El proyecto ha sido rigurosamente estructurado siguiendo los principios de la **Arquitectura Limpia (Clean Architecture)**. Esta metodología de diseño arquitectónico garantiza un alto grado de desacoplamiento entre las reglas de negocio base de la aplicación y los detalles técnicos de hardware o servicios externos.

A continuación, se detalla la división concéntrica en capas y el propósito de cada una de sus subcarpetas internas:

- **`domain/` (Capa de Entidades y Reglas de Negocio):**
  Es el núcleo estricto e inviolable del software. No posee ningún conocimiento sobre bases de datos de red, ni de frameworks HTTP.
  - `entities/`: Define las clases puras que estructuran la base del dominio (ej. `TrackEntity`, `ArtistEntity`).
  - `interfaces/`: Agrupa contratos abstractos (como `IRepository`) que las capas exteriores deberán respetar al interactuar con recursos técnicos.
  - `exceptions/`: Aloja errores de negocio puros (ej. `NotFoundException`), permitiendo capturar fallos lógicos sin depender de componentes externos.
  - `abstractions/` y `object_values/`: Clases, enums base y objetos compuestos independientes (ej. clases de métricas, enums de género musical) que forman la columna vertebral del comportamiento semántico del Dominio sin contar con un identificador único (ID) representativo de una tabla.

- **`application/` (Capa de Casos de Uso / Servicios):**
  Representa y controla los flujos de usuario hacia las lógicas de negocio.
  - `services/`: Contiene los orquestadores principales (ej. `ArtistsService`). Interacciona con las `entities` e `interfaces` pero no implementa llamadas SQL o Pydantic explícitas. Determina qué hacer (ej. Validar si existe el usuario -> Crear la Playlist -> Guardar cambios).

- **`api/` (Capa de Adaptadores de Interfaz / Delivery):**
  Exclusivamente gestiona los formalismos de FastAPI y el tránsito HTTP hacia el exterior.
  - `controllers/`: Endpoints de red (`/tracks`, `/users`). Despachan respuestas, aplican códigos HTTP e invocan a los servicios `application`.
  - `dtos/` (Data Transfer Objects): Define esquemas estrictos de validación con librerías externas (como Pydantic) para filtrar los Bodies en Requests y modelar Reponses antes de entrar a la API.
  - `dependencies/`: Piezas exclusivas de FastAPI que resuelven automáticamente servicios complejos precargados (inyección de dependencias) al abrir un Endpoint.
  - `helpers/`: Herramientas del contexto red (ej. calculadores de paginación o extracción de parámetros Query String).

- **`infrastructure/` (Capa de Frameworks y Drivers):**
  Frontera tangible frente a hardware. Integra concretamente el almacenamiento e intercambiso de seguridad.
  - `persistence/`: Contiene el sub-ecosistema de base de datos (`mongodb/` y `postgres/`). Se divide en:
    - `repositories/`: Implementan métodos reales llamando funciones de DB y ejecutando Queries, satisfaciendo la `interface` del dominio.
    - `models/`: Esquemas de tablas de lectura para conectores de BD.
    - `mappers/`: Clases traductoras o parseadores que convierten filas crudas de DB (`models`) a Entidades formales (`entities`).
  - `security/`: Funciones periféricas para generación de JSON Web Tokens, validación y hashing (ej. `jwt_service.py`).

---

## 3. Patrones de Diseño Implementados Explicados con Código

Para asegurar mantenibilidad y blindar el sistema, Audify implementa metodologías pragmáticas de diseño de software.

### 3.1. Patrón Repositorio (Repository Pattern)
Aísla la conectividad a la base de datos permitiendo que la persistencia se modifique independiente de los lógicos de servicio.

*Implementación en `infrastructure/persistence/mongodb/repositories/artists.py`:*
```python
from infrastructure.persistence.mongodb.repositories.base import BaseRepositoryMongo
from infrastructure.persistence.mongodb.models.artist.model import Artist
from infrastructure.persistence.mongodb.mappers.artist import ArtistMapper

class ArtistRepository(BaseRepositoryMongo[ArtistEntity, Artist]):
    def __init__(self, db: AsyncIOMotorDatabase):
        super().__init__(
            db=db,
            collection_name="artists",
            mapper=ArtistMapper(),
            schema_class=Artist,
            entity_name="Artist"
        )
```

### 3.2. Mapeador de Datos (Data Mapper Pattern)
Componente bidireccional traductor que desacopla la representación estructural de la base de datos (y la librería subyacente) respecto al corazón del Software (Clean Entity).

*Implementación en `infrastructure/persistence/mongodb/mappers/playlist.py`:*
```python
from domain.entities.playlist import PlaylistEntity
from infrastructure.persistence.mongodb.models.playlist.model import Playlist
from domain.interfaces.mapper import IMapper

class PlaylistMapper(IMapper[PlaylistEntity, Playlist]):
    @staticmethod
    def to_domain(persistence_model: Playlist) -> PlaylistEntity:
        return PlaylistEntity(
            id=str(persistence_model.id),
            name=persistence_model.name or '',
            owner_id=str(persistence_model.owner_id),
            tracks=[...] # ... logic mapping
        )

    @staticmethod
    def to_persistence(domain_entity: any) -> dict:
        data = domain_entity.model_dump(exclude={"id"})
        data["_id"] = ObjectID(domain_entity.id)
        return data
```

### 3.3. Objeto de Transferencia de Datos (DTO)
Estructura rigurosamente la información transaccional entrante vía web para restringir exposición y validar nulos antes de comunicarse con un servicio.

*Implementación en `api/dtos/artists.py`:*
```python
from pydantic import BaseModel

class CreateArtistDTO(BaseModel):
    name: str
    bio: str
    image_url: str
    country: str
    verified: bool = False
    aliases: list[str] = []

class ArtistResponse(BaseModel):
    id: str
    name: str
    bio: str | None = None
    # ...
```

### 3.4. Inyección de Dependencias (Dependency Injection Pattern)
Externaliza la construcción de objetos para disminuir acoplamiento, dictándole al `Service` qué capa de infraestructura (Repositiorio / Conexión Bd) debe usar temporalmente sin que él la instancie.

*Implementación en `api/dependencies/artist_dependency.py`:*
```python
from fastapi import Depends
from application.services.artists import ArtistsService
from infrastructure.persistence.mongodb.repositories.artists import ArtistRepository
from infrastructure.persistence.mongodb.mongo import get_mongo_db

async def get_artists_repository(db = Depends(get_mongo_db)) -> ArtistRepository:
    return ArtistRepository(db)

def get_artists_service(repo: ArtistRepository = Depends(get_artists_repository)) -> ArtistsService:
    # Se inyecta 'repo' forzando su instanciación pasiva previamente
    return ArtistsService(repo)
```

### 3.5. Patrón Singleton
Resguarda que un conector o pieza fundamental limite su inicialización global a un único ejemplar concurrente, en este caso impidiendo reinicios o desgastes de memoria por llamadas a servidor MongoDB repetitivas.

*Implementación en `infrastructure/persistence/mongodb/mongo.py`:*
```python
from motor.motor_asyncio import AsyncIOMotorClient, AsyncIOMotorDatabase
from api.config import settings

class MongoDB:
    client: AsyncIOMotorClient = None

# Instancia global (Singleton en memoria global)
db = MongoDB()

async def get_mongo_db() -> AsyncIOMotorDatabase:
    # Siempre reutiliza la misma referencia db.client
    return db.client[settings.mongo_db]
```

---

## 4. Guía de Inicialización (Paso a Paso)

Para arrancar el proyecto localmente y poder testear sus Endpoints, sigue diligentemente las instrucciones a continuación:

### Paso 1: Clonar el Repositorio
```bash
git clone https://github.com/Angel-SSJ/audify.git
cd audify
```

### Paso 2: Crear el Entorno Virtual (Opcional pero recomendado)
Crea y activa un entorno virtual de Python aislando las dependencias.
**En Windows:**
```bash
python -m venv venv
venv\Scripts\activate
```
**En macOS/Linux:**
```bash
python3 -m venv venv
source venv/bin/activate
```

### Paso 3: Instalación de Dependencias
Audify emplea estándares modernos descritos en `pyproject.toml`. Para instalar todas las herramientas subyacentes como `fastapi`, `motor`, `uvicorn` entre otras, ejecuta en la raíz:
```bash
pip install -e .
```
*(Si no dispones del ejecutor local, asegura de tener Python 3.10+ instalado).*

### Paso 4: Configuración de Variables de Entorno
Crea un archivo llamado `.env` en la raíz del proyecto. Este archivo será procesado mágicamente por la configuración en `api/config.py`. En él debes proveer las credenciales de tus clusters:

```env
APP_NAME=AudifyAPI
DEBUG=True

# Configuraciones MongoDB
MONGO_USER=tu_usuario
MONGO_PASSWORD=tu_clave
MONGO_CLUSTER=tu_cluster.mongodb.net
MONGO_DB=audify
MONGO_BASE_CONNECTION_STRING=mongodb+srv://{USER}:{PASSWORD}@{CLUSTER}/?retryWrites=true&w=majority

# Configuraciones PostgreSQL
POSTGRES_USER=postgres
POSTGRES_PASSWORD=tu_clave
POSTGRES_HOST=127.0.0.1
POSTGRES_PORT=5432
POSTGRES_DB=audify
POSTGRES_BASE_CONNECTION_STRING=postgresql://{USER}:{PASSWORD}@{HOST}:{PORT}/{NAME}

# Seguridad y Autenticación JWT
SECRET_KEY=tu_super_secreto_seguro_jwt
JWT_ALGORITHM=HS256
ACCESS_TOKEN_EXPIRE_MINUTES=60
ACCESS_TOKEN_EXPIRE_HOURS=24
ACCESS_TOKEN_EXPIRE_DAYS=7
```

### Paso 5: Lanzamiento del Servidor
Finalmente arranca el motor del framework Web con su opción recargable si estás trabajando:
```bash
fastapi dev api/main.py
```
*(Alternativamente puedes usar `uvicorn api.main:app --reload`).*

La aplicación de Audify ahora se encuentra en vivo. Puedes navegar al portal inteligente generado en la ruta `http://127.0.0.1:8000/docs` para visualizar interactivamente la consola de Swagger provista para pruebas.
