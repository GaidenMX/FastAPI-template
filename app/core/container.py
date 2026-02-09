#from app.services.base_service import BaseService

#class Container:
#    def __init__(self):
        # Mantenemos el enfoque POO: instanciamos nuestros servicios aquí
#        self.base_service = BaseService()

# Creamos una instancia única (Singleton)
#container = Container()

# Esta función será nuestra "llave" para la inyección
#def get_container():
#    return container

from app.core.config import get_settings
from app.infrastructure.repositories.base_repository import BaseRepository
from app.services.base_service import BaseService

class Container:
    def __init__(self):
        # 1. Cargamos la configuración validada
        self.settings = get_settings()
        
        # 2. Instanciamos la infraestructura
        self.health_repository = BaseRepository()
        
        # 3. Inyectamos configuración y repositorio en el servicio
        self.base_service = BaseService(
            repository=self.health_repository,
            settings=self.settings
        )

container = Container()

def get_container():
    return container