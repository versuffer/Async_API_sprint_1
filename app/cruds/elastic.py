from uuid import UUID

from elasticsearch import Elasticsearch

from app.core.config import es_settings
from app.schemas.v1.films_schemas import GetFilmSchemaOut, GetFilmExtendedSchemaOut
from app.schemas.v1.persons_schemas import GetPersonSchemaOut


class ElasticCrud:
    def __init__(self):
        self.elastic = Elasticsearch([es_settings.dict()], timeout=5)

    async def search_films(self, query: str) -> list[GetFilmSchemaOut]:
        return self.elastic.get("movies")

    async def search_persons(self, query: str) -> list[GetPersonSchemaOut]:
        raise NotImplementedError

    async def get_film(self, film_id: UUID) -> GetFilmExtendedSchemaOut:
        try:
            result = self.elastic.get(index="movies", id=str(film_id))
            if not result["found"]:
                raise Exception(f"Фильм с id {film_id} не найден")
            film = GetFilmExtendedSchemaOut(**result["_source"])
            return film
        except Exception as e:
            print(f"Ошибка при получении фильма: {e}")
            raise e

    async def get_films(self, sort: str | None, genre: UUID | None) -> list[GetFilmSchemaOut]:
        try:
            body = {"query": {"match_all": {}}}

            if genre:
                body["query"] = {
                    "bool": {
                        "filter": [
                            {"term": {"genre_ids": str(genre)}}
                        ]
                    }
                }

            if sort:
                if sort.startswith('-'):
                    sort = sort.split('-')[1]
                    order = "desc"
                else:
                    sort = sort
                    order = "asc"
                body["sort"] = [{f"{sort}": {"order": order}}]

            body["size"] = 10

            result = self.elastic.search(index="movies", body=body)
            films = [GetFilmSchemaOut(**hit["_source"]) for hit in result["hits"]["hits"]]
            return films
        except Exception as e:
            print(f"Ошибка при получении фильмов: {e}")
            return []

