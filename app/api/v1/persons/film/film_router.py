from fastapi import APIRouter, Depends, status

from app.api.docs.tags import ApiTags
from app.schemas.v1.films_schemas import GetFilmSchemaOut
from app.schemas.v1.params_schema import DetailParams
from app.services.api.v1.persons_service.persons_service import PersonsService

film_router = APIRouter(prefix='/film')


@film_router.get(
    '',
    status_code=status.HTTP_200_OK,
    summary='Фильмы участника',
    response_model=list[GetFilmSchemaOut],
    tags=[ApiTags.V1_PERSONS],
)
async def get_person_films(
    query_params: DetailParams = Depends(),
    service: PersonsService = Depends(),
):
    return await service.get_person_films(query_params)
