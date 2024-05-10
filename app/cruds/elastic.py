from elasticsearch import Elasticsearch

from app.core.config import es_settings
from app.schemas.v1.films_schemas import GetFilmSchemaOut
from app.schemas.v1.persons_schemas import GetPersonSchemaOut


class ElasticCrud:
    def __init__(self):
        self.elastic = Elasticsearch([es_settings.dict()], timeout=5)

    async def search_films(self, query: str) -> list[GetFilmSchemaOut]:
        return self.elastic.get("movies")

    async def search_persons(self, query: str) -> list[GetPersonSchemaOut]:
        raise NotImplementedError

    async def get_films(self) -> list[GetFilmSchemaOut]:
        try:
            result = self.elastic.search(index="movies", body={"query": {"match_all": {}}})
            films = [GetFilmSchemaOut(**hit["_source"]) for hit in result["hits"]["hits"]]
            return films
        except Exception as e:
            print(f"Ошибка при получении фильмов: {e}")
            return []

