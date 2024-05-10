from uuid import UUID

from pydantic import BaseModel, Field


class GetGenreSchemaOut(BaseModel):
    id: UUID = Field(serialization_alias="uuid")
    name: str
    description: str
