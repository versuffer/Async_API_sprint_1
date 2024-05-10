from typing import Literal
from uuid import UUID

from pydantic import BaseModel, Field


class FilmParams(BaseModel):
    page: int = 1
    page_size: int = 10
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
    # genres: list[FilmGenre] #TODO вернуть когда будут жанры
    actors: list[FilmActor]
    writers: list[FilmWriter]
    directors: list[FilmDirector]
