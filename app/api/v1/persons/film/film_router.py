from uuid import UUID

from fastapi import APIRouter, Depends, status
from fastapi_pagination import Page, paginate

from app.api.docs.tags import ApiTags
from app.schemas.v1.films_schemas import GetFilmSchemaOut
from app.services.api.v1.persons_service.persons_service import PersonsService

film_router = APIRouter(prefix='/film')


@film_router.get(
    '',
    status_code=status.HTTP_200_OK,
    summary='Фильмы участника',
    response_model=Page[GetFilmSchemaOut],
    tags=[ApiTags.V1_PERSONS],
)
async def get_person_films(
    person_id: UUID,
    service: PersonsService = Depends(),
):
    return paginate(await service.get_person_films(person_id))
