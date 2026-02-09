from pydantic import BaseModel
from datetime import datetime
from typing import Optional

class HealthStatus(BaseModel):
    """
    Define el esquema de datos para el estado del sistema.
    """
    status: str
    project: str
    version: str
    server_time: datetime
    environment: str
    # Puedes agregar campos opcionales si lo deseas en el futuro
    uptime: Optional[float] = None