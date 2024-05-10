from uuid import UUID

from fastapi import Depends

from app.cruds.elastic import ElasticCrud
from app.schemas.v1.films_schemas import GetFilmSchemaOut
from app.schemas.v1.persons_schemas import GetPersonSchemaOut
from app.services.api.v1.base import BaseV1Service


class PersonsService(BaseV1Service):

    def __init__(self, crud: ElasticCrud = Depends()):
        self.crud = crud

    async def get_person(self, person_id: UUID) -> GetPersonSchemaOut:
        raise NotImplementedError

    async def get_person_films(self, person_id: UUID) -> list[GetFilmSchemaOut]:
        raise NotImplementedError

    async def search_persons(self, query: str) -> list[GetPersonSchemaOut]:
        return await self.crud.search_persons(query)
