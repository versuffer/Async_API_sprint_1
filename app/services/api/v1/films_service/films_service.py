from uuid import UUID

from fastapi import Depends

from app.schemas.v1.films_schemas import GetFilmExtendedSchemaOut, GetFilmSchemaOut
from app.services.api.v1.base import BaseV1Service
from app.cruds.elastic import ElasticCrud


class FilmsService(BaseV1Service):

    def __init__(self, crud: ElasticCrud = Depends()):
        self.crud = crud

    async def get_films(self, sort: str | None, genre: UUID | None) -> list[GetFilmSchemaOut]:
        return await self.crud.get_films(sort, genre)

    async def get_film(self, film_id: UUID) -> GetFilmExtendedSchemaOut:
        raise NotImplementedError

    async def search_films(self, query: str) -> list[GetFilmSchemaOut]:
        return await self.crud.search_films(query)
