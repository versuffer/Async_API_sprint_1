from uuid import UUID

from fastapi import Depends

from app.schemas.v1.films_schemas import GetFilmExtendedSchemaOut, GetFilmSchemaOut
from app.services.api.v1.base import BaseV1Service
from app.services.elastic.search_service import SearchService


class FilmsService(BaseV1Service):

    def __init__(self, search_service: SearchService = Depends()):
        self.search_service = search_service

    async def get_films(self, sort: str | None, genre: UUID | None) -> list[GetFilmSchemaOut]:
        raise NotImplementedError

    async def get_film(self, film_id: UUID) -> GetFilmExtendedSchemaOut:
        raise NotImplementedError

    async def search_films(self, query: str) -> list[GetFilmSchemaOut]:
        return await self.search_service.search_films(query)
