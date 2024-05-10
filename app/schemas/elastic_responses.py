from enum import StrEnum

from pydantic import BaseModel, Field

from app.core.logs import logger
from app.schemas.v1.films_schemas import GetFilmExtendedSchemaOut
from app.schemas.v1.genres_schemas import GetGenreSchemaOut


class ElasticFilmSeachResponse(BaseModel):
    films: dict = Field(alias='hits')

    @property
    def films_list(self) -> list[GetFilmExtendedSchemaOut]:
        return [GetFilmExtendedSchemaOut(**film["_source"]) for film in self.films["hits"]]


class ElasticGetFilmResponse(BaseModel):
    film: GetFilmExtendedSchemaOut = Field(alias='_source')


class IndexList(StrEnum):
    MOVIES = "movies"
    GENRES = "genres"
    PERSONS = "persons"


class Object(BaseModel):
    index: IndexList = Field(alias="_index")
    id: str = Field(alias="_id")
    score: float = Field(alias="_score")
    source: dict = Field(alias="_source", exclude=True)

    @property
    def get_out_schema_source(self):
        match self.index:
            case IndexList.GENRES:
                return GetGenreSchemaOut(**self.source)
            case IndexList.MOVIES:
                return GetFilmExtendedSchemaOut(**self.source)
            case IndexList.PERSONS:
                raise NotImplementedError
            case _:
                logger.error("Ops not match index")


class Result(BaseModel):
    total: dict
    objects: list[Object] = Field(alias="hits", exclude=True)


class ElasticSearchResponse(BaseModel):
    result: Result = Field(alias="hits")

    @property
    def get_objects(self):
        return [obj.get_out_schema_source for obj in self.result.objects]