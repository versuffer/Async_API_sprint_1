from uuid import UUID

from fastapi import Depends

from app.cruds.base import CrudInterface
from app.cruds.get_crud import get_crud
from app.schemas.v1.genres_schemas import GetGenreSchemaOut
from app.services.api.v1.base import BaseV1Service


class GenresService(BaseV1Service):

    def __init__(self, crud: CrudInterface = Depends(get_crud)):
        self.crud = crud

    async def get_genres(self) -> list[GetGenreSchemaOut]:
        return await self.crud.get_genres()


    async def get_genre(self, genre_id: UUID) -> GetGenreSchemaOut:
        return await self.crud.get_genre(genre_id)
