from uuid import UUID

from pydantic import BaseModel, Field


class GenreSchema(BaseModel):
    id: UUID = Field(serialization_alias="uuid")
    name: str
    description: str


class GenreSchemaOut(GenreSchema):
    pass
