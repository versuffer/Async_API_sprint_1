from uuid import UUID

from fastapi import Depends

from app.schemas.v1.films_schemas import GetFilmExtendedSchemaOut, GetFilmSchemaOut
from app.services.api.v1.base import BaseV1Service
from app.cruds.elastic import ElasticCrud


class FilmsService(BaseV1Service):

    def __init__(self, crud: ElasticCrud = Depends()):
        self.crud = crud

    async def get_films(self, page: int, page_size: int, sort: str | None, genre: UUID | None) -> list[GetFilmSchemaOut] | None:
        return await self.crud.get_films(page, page_size, sort, genre)

    async def get_film(self, film_id: UUID) -> GetFilmExtendedSchemaOut | None:
        return await self.crud.get_film(film_id)

    async def search_films(self, page: int, page_size: int, query: str) -> list[GetFilmSchemaOut]:
        return await self.crud.search_films(page=page, page_size=page_size, query=query)
