from enum import StrEnum
from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field

from app.schemas.v1.params_schema import PaginationMixin


class Roles(StrEnum):
    ACTOR = 'actor'
    WRITER = 'writer'
    DIRECTOR = 'director'


class FilmParams(PaginationMixin):
    sort: Literal['imdb_rating', '-imdb_rating'] | None = None
    genre: UUID | None = None


class GetFilmSchemaOut(BaseModel):
    uuid: UUID = Field(alias='id')
    title: str
    imdb_rating: float


class FilmGenre(BaseModel):
    uuid: UUID = Field(alias='id')
    name: str


class FilmPerson(BaseModel):
    uuid: UUID = Field(alias='id')
    full_name: str = Field(alias='name')


class FilmActor(FilmPerson):
    pass


class FilmWriter(FilmPerson):
    pass


class FilmDirector(FilmPerson):
    pass


class GetFilmExtendedSchemaOut(GetFilmSchemaOut):
    description: str
    genres: list[str]
    actors: list[FilmActor]
    writers: list[FilmWriter]
    directors: list[FilmDirector]

    def get_person_films(self, person_id: str) -> dict:
        """Метод используется для получения списков жанров конкретной персоны в ручке persons"""

        roles: list[Roles] = []

        roles.extend([Roles.ACTOR for actor in self.actors if str(actor.uuid) == str(person_id)])
        roles.extend([Roles.WRITER for writer in self.writers if str(writer.uuid) == str(person_id)])
        roles.extend([Roles.DIRECTOR for director in self.directors if str(director.uuid) == str(person_id)])

        return dict(uuid=self.uuid, roles=roles)
