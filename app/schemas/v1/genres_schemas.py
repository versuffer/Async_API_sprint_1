from uuid import UUID

from pydantic import BaseModel


class GetGenreSchemaOut(BaseModel):
    uuid: UUID
    name: str
    description: float
