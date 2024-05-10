from abc import ABC, abstractmethod
from uuid import UUID

from app.schemas.v1.films_schemas import (
    FilmParams,
    GetFilmExtendedSchemaOut,
    GetFilmSchemaOut,
)
from app.schemas.v1.genres_schemas import GetGenreSchemaOut


class CrudInterface(ABC):
    @abstractmethod
    async def get_film(self, film_id: UUID) -> GetFilmExtendedSchemaOut | None:
        pass

    @abstractmethod
    async def search_films(self, query: str, page: int, page_size: int) -> list[GetFilmSchemaOut] | None:
        pass

    @abstractmethod
    async def get_films(self, params: FilmParams) -> list[GetFilmSchemaOut] | None:
        pass

    @abstractmethod
    async def get_genres(self) -> list[GetGenreSchemaOut] | None:
        pass

    @abstractmethod
    async def get_genre(self, genre_id: UUID) -> GetGenreSchemaOut | None:
        pass