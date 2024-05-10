from uuid import UUID

import elasticsearch
from elasticsearch import Elasticsearch

from app.core.config import es_settings
from app.core.logs import logger
from app.cruds.base import CrudInterface
from app.schemas.elastic_responses import (
    ElasticFilmSeachResponse,
    ElasticGetFilmResponse,
)
from app.schemas.v1.films_schemas import (
    FilmParams,
    GetFilmExtendedSchemaOut,
    GetFilmSchemaOut,
)
from app.schemas.v1.persons_schemas import GetPersonSchemaOut


class ElasticCrud(CrudInterface):
    def __init__(self):
        self.elastic = Elasticsearch([es_settings.dict()], timeout=5)

    @staticmethod
    async def build_film_search_body(
            query: str | None,
            page: int,
            page_size: int,
            sort: str | None,
            genre: UUID | None
    ):
        body: dict = {"query": {"match_all": {}}}

        if query:
            body["query"] = {
                "multi_match": {
                    "query": query,
                    "fields": ["title", "genres", "description", "directors_names", "actors_names", "writers_names"]
                }
            }

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

        body["size"] = page_size
        body["from"] = (page - 1) * page_size

        return body

    async def get_film(self, film_id: UUID) -> GetFilmExtendedSchemaOut | None:
        try:
            result = self.elastic.get(index="movies", id=str(film_id))
            # TODO запрос жанров через сервис жанров
            parsed_result = ElasticGetFilmResponse(**result)
            return parsed_result.film
        except elasticsearch.NotFoundError as error:
            logger.warning(f"Не найден фильм с {film_id=}: {error}")
            return None
        except Exception as error:
            logger.error(f"Неизвестная ошибка при получении фильма с {film_id=}: {error}")
            return None

    async def search_films(self, query: str, page: int, page_size: int) -> list[GetFilmSchemaOut]:
        try:
            body = await self.build_film_search_body(query, page, page_size, None, None)
            results = self.elastic.search(index="movies", body=body)
            parsed_results = ElasticFilmSeachResponse(**results)
            return parsed_results.films_list  # type:ignore
        except Exception as error:
            logger.error(f"Неизвестная ошибка при получении фильмов с {query}: {error}")
            return []

    async def get_films(self, params: FilmParams) -> list[GetFilmSchemaOut]:
        try:
            body = await self.build_film_search_body(
                query=None, **params.dict()
            )
            results = self.elastic.search(index="movies", body=body)
            parsed_results = ElasticFilmSeachResponse(**results)
            return parsed_results.films_list  # type:ignore
        except Exception as error:
            logger.error(f"Неизвестная ошибка при получении фильмов: {error}")
            return []

    async def search_persons(self, query: str) -> list[GetPersonSchemaOut]:
        raise NotImplementedError
