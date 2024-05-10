from uuid import UUID

from pydantic import BaseModel, Field


class GetFilmSchemaOut(BaseModel):
    uuid: UUID = Field(alias='id')
    title: str
    imdb_rating: float


class FilmGenre(BaseModel):
    uuid: UUID
    name: str


class FilmPerson(BaseModel):
    uuid: UUID
    full_name: str


class FilmActor(FilmPerson):
    pass


class FilmWriter(FilmPerson):
    pass


class FilmDirector(FilmPerson):
    pass


class GetFilmExtendedSchemaOut(GetFilmSchemaOut):
    description: str
    genre: list[FilmGenre]
    actors: list[FilmActor]
    writers: list[FilmWriter]
    directors: list[FilmDirector]
