#class BaseService:
 #   def get_health_status(self):
  #      return {
   #         "status": "online",
    #        "project": "GaidenMX Template",
     #       "version": "1.0.0"
      #  }
    

#from app.core.config import settings

#class BaseService:
#    def get_health_status(self):
#        return {
#            "project": settings.PROJECT_NAME, # <--- Uso de la configuración
#            "version": settings.VERSION,
#            "status": "ok"
#        }


from app.models.domain.health import HealthStatus
from app.infrastructure.repositories.base_repository import BaseRepository
from app.core.config import Settings
from datetime import datetime

class BaseService:
    def __init__(self, repository: BaseRepository, settings: Settings):
        self._repository = repository
        self._settings = settings

    def get_health_status(self) -> HealthStatus:
        status = HealthStatus(
            status="online",
            project=self._settings.PROJECT_NAME,  # <--- Usando la configuración inyectada
            version=self._settings.VERSION,
            server_time=datetime.now(),
            environment=self._settings.ENV
        )
        self._repository.add(status)
        return status