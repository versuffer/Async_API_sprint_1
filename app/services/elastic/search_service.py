from app.schemas.v1.films_schemas import GetFilmSchemaOut
from app.schemas.v1.persons_schemas import GetPersonSchemaOut


class SearchService:

    async def search_films(self, query: str) -> list[GetFilmSchemaOut]:
        raise NotImplementedError

    async def search_persons(self, query: str) -> list[GetPersonSchemaOut]:
        raise NotImplementedError
