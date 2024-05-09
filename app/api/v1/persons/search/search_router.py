from fastapi import APIRouter, Depends, status
from fastapi_pagination import Page, paginate

from app.api.docs.tags import ApiTags
from app.schemas.v1.persons_schemas import GetPersonSchemaOut
from app.services.api.v1.persons_service.persons_service import PersonsService

search_router = APIRouter(prefix='/search')


@search_router.get(
    '',
    status_code=status.HTTP_200_OK,
    summary='Поиск фильмов',
    response_model=Page[GetPersonSchemaOut],
    tags=[ApiTags.V1_PERSONS],
)
async def search_persons(
    query: str,
    service: PersonsService = Depends(),
):
    return paginate(await service.search_persons(query))
