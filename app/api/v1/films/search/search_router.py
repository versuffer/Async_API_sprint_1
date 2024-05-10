from fastapi import APIRouter, Depends, status
from fastapi_pagination import Page, paginate

from app.api.docs.tags import ApiTags
from app.schemas.v1.films_schemas import GetFilmSchemaOut
from app.services.api.v1.films_service.films_service import FilmsService

search_router = APIRouter(prefix='/search')


@search_router.get(
    '',
    status_code=status.HTTP_200_OK,
    summary='Поиск фильмов',
    # response_model=Page[GetFilmSchemaOut],
    tags=[ApiTags.V1_FILMS],
)
async def search_films(
    query: str,
    service: FilmsService = Depends(),
):
    # return paginate(await service.search_films(query))
    return await service.search_films(query)
