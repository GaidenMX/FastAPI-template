from pydantic_settings import BaseSettings, SettingsConfigDict
from functools import lru_cache

class Settings(BaseSettings):
    # Variables con valores por defecto
    PROJECT_NAME: str = "GaidenMX API"
    VERSION: str = "1.0.0"
    ENV: str = "development"
    PORT: int = 8000
    
    model_config = SettingsConfigDict(
        # Pydantic buscará ambos. El .env (si existe) tiene prioridad.
        env_file=(".env.example", ".env"), 
        
        env_file_encoding="utf-8",
        extra="ignore" 
    )

@lru_cache
def get_settings():
    return Settings()

settings = get_settings()