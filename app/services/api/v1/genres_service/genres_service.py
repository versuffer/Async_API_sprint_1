from uuid import UUID

from app.schemas.v1.genres_schemas import GetGenreSchemaOut
from app.services.api.v1.base import BaseV1Service


class GenresService(BaseV1Service):
    async def get_genres(self) -> list[GetGenreSchemaOut]:
        raise NotImplementedError

    async def get_genre(self, genre_id: UUID) -> GetGenreSchemaOut:
        raise NotImplementedError
