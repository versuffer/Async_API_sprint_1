from uuid import UUID

from fastapi import APIRouter, Depends, status, HTTPException

from app.api.docs.tags import ApiTags
from app.api.v1.films.search.search_router import search_router
from app.schemas.v1.films_schemas import GetFilmExtendedSchemaOut, GetFilmSchemaOut
from app.services.api.v1.films_service.films_service import FilmsService

films_router = APIRouter(prefix='/films')
films_router.include_router(search_router)


@films_router.get(
    '',
    status_code=status.HTTP_200_OK,
    summary='Получить список фильмов',
    response_model=list[GetFilmSchemaOut],
    tags=[ApiTags.V1_FILMS],
)
async def get_films(
    page: int = 1,
    page_size: int = 10,
    sort: str | None = None,
    genre: UUID | None = None,  # TODO сделать params
    service: FilmsService = Depends(),
):
    if films := await service.get_films(page, page_size, sort, genre):
        return films
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)


@films_router.get(
    '/{film_id}',
    status_code=status.HTTP_200_OK,
    summary='Получить фильм по UUID',
    response_model=GetFilmExtendedSchemaOut,
    tags=[ApiTags.V1_FILMS],
)
async def get_film(
    film_id: UUID,
    service: FilmsService = Depends(),
):
    if film := await service.get_film(film_id):
        return film
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
