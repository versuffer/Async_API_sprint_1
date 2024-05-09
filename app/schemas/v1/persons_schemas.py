from enum import StrEnum
from uuid import UUID

from pydantic import BaseModel


class Roles(StrEnum):
    ACTOR = 'actor'
    WRITER = 'writer'
    DIRECTOR = 'director'


class PersonFilm(BaseModel):
    uuid: UUID
    roles: list[Roles]


class GetPersonSchemaOut(BaseModel):
    uuid: UUID
    full_name: str
    films: list[PersonFilm]
