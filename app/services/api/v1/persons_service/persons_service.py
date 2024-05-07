from uuid import UUID

from fastapi import Depends

from app.schemas.v1.films_schemas import GetFilmSchemaOut
from app.schemas.v1.persons_schemas import GetPersonSchemaOut
from app.services.api.v1.base import BaseV1Service
from app.services.elastic.search_service import SearchService


class PersonsService(BaseV1Service):

    def __init__(self, search_service: SearchService = Depends()):
        self.search_service = search_service

    async def get_person(self, person_id: UUID) -> GetPersonSchemaOut:
        raise NotImplementedError

    async def get_person_films(self, person_id: UUID) -> list[GetFilmSchemaOut]:
        raise NotImplementedError

    async def search_persons(self, query: str) -> list[GetPersonSchemaOut]:
        return await self.search_service.search_persons(query)
