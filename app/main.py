#from fastapi import FastAPI, Depends
#from app.core.container import Container, get_container

#app = FastAPI(title="GaidenMX API Template")

#@app.get("/")
#def read_root(
#    at: Container = Depends(get_container)
#):
    # 'at' (App Container) nos da acceso a todos nuestros servicios
#    return at.base_service.get_health_status()


from fastapi import FastAPI
from app.core.container import get_container

# 1. Obtenemos el contenedor y sus configuraciones
container = get_container()
settings = container.settings

# 2. Inicializamos FastAPI con la configuración inyectada
app = FastAPI(
    title=settings.PROJECT_NAME,
    version=settings.VERSION
)

@app.get("/health", tags=["Health"])
async def health_check():
    """
    Endpoint de salud que utiliza el servicio inyectado.
    """
    # Usamos el servicio que ya tiene el repositorio y settings inyectados
    return container.base_service.get_health_status()

@app.get("/", tags=["Root"])
async def read_root():
    return {
        "message": f"Welcome to {settings.PROJECT_NAME}",
        "environment": settings.ENV
    }