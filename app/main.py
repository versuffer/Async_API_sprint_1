from pprint import pformat

import uvicorn
from fastapi import FastAPI

from app.api.api_router import api_router
from app.api.docs.tags import api_tags
from app.core.config import app_settings
from app.core.logs import logger

app = FastAPI(
    title=app_settings.APP_TITLE,
    description=app_settings.APP_DESCRIPTION,
    version='1.0.0',
    debug=app_settings.DEBUG,
    docs_url='/',
    openapi_tags=api_tags,
)

app.include_router(api_router)


if __name__ == '__main__':
    logger.info(f'Start with configuration: \n{pformat(app_settings.model_dump())}')
    uvicorn.run('main:app', host='localhost', port=10000)
