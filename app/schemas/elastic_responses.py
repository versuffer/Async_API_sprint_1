from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.v1.films_schemas import GetFilmExtendedSchemaOut


class ElasticSeachResponse(BaseModel):
    films: dict = Field(alias='hits')

    @property
    def films_list(self) -> list[GetFilmExtendedSchemaOut]:
        return [GetFilmExtendedSchemaOut(**film["_source"]) for film in self.films["hits"]]


class ElasticGetFilmResponse(BaseModel):
    film: GetFilmExtendedSchemaOut = Field(alias='_source')
