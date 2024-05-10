from uuid import UUID

from fastapi import APIRouter, Depends, HTTPException, status
from fastapi_pagination import Page, paginate

from app.api.docs.tags import ApiTags
from app.schemas.v1.genres_schemas import GetGenreSchemaOut
from app.services.api.v1.genres_service.genres_service import GenresService

genres_router = APIRouter(prefix='/genres')


@genres_router.get(
    '',
    status_code=status.HTTP_200_OK,
    summary='Получить список жанров',
    response_model=list[GetGenreSchemaOut],
    tags=[ApiTags.V1_GENRES],
)
async def get_genres(
    service: GenresService = Depends(),
):
    if genres := await service.get_genres():
        return genres
    return []


@genres_router.get(
    '/{genre_id}',
    status_code=status.HTTP_200_OK,
    summary='Получить жанр по UUID',
    response_model=GetGenreSchemaOut,
    tags=[ApiTags.V1_GENRES],
)
async def get_genre(
    genre_id: UUID,
    service: GenresService = Depends(),
):
    if genre := await service.get_genre(genre_id):
        return genre
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
