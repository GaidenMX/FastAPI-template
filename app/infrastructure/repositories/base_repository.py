from typing import TypeVar, Generic, List, Optional
from pydantic import BaseModel

# Definimos un tipo genérico 'T' que debe ser un modelo de Pydantic
T = TypeVar("T", bound=BaseModel)

class BaseRepository(Generic[T]):
    """
    Repositorio base genérico con operaciones CRUD básicas.
    Por ahora maneja datos en memoria (lista), ideal para tu fase de plantilla.
    """
    
    def __init__(self):
        # Almacén temporal en memoria
        self._storage: List[T] = []

    def add(self, entity: T) -> T:
        """Guarda una entidad en el almacén."""
        self._storage.append(entity)
        return entity

    def get_all(self) -> List[T]:
        """Retorna todos los registros."""
        return self._storage

    def get_first(self) -> Optional[T]:
        """Retorna el primer registro o None si está vacío."""
        return self._storage[0] if self._storage else None

    def clear(self) -> None:
        """Limpia el almacén."""
        self._storage = []