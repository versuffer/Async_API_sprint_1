from fastapi import APIRouter, Depends, status, HTTPException

from app.api.docs.tags import ApiTags
from app.schemas.v1.films_schemas import GetFilmSchemaOut
from app.services.api.v1.films_service.films_service import FilmsService

search_router = APIRouter(prefix='/search')


@search_router.get(
    '',
    status_code=status.HTTP_200_OK,
    summary='Поиск фильмов',
    response_model=list[GetFilmSchemaOut],
    tags=[ApiTags.V1_FILMS],
)
async def search_films(
    query: str,
    page: int = 1,
    page_size: int = 10,
    service: FilmsService = Depends(),
):
    if films := await service.search_films(page=page, page_size=page_size, query=query):
        return films
    raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)
