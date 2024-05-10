from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.v1.films_schemas import GetFilmExtendedSchemaOut


class ElasticSeachResponse(BaseModel):
    hits: dict

    @property
    def hits_list(self) -> list[GetFilmExtendedSchemaOut]:
        # a = self.hits["hits"]
        # for hit in a:
        #     d = ElasticHit(**hit)
        #     e = GetFilmExtendedSchemaOut(**hit["_source"])
        return [GetFilmExtendedSchemaOut(**hit["_source"]) for hit in self.hits["hits"]]


class ElasticGetFilmResponse(BaseModel):
    film: GetFilmExtendedSchemaOut = Field(alias='_source')
