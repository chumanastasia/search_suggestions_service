import uvicorn
from fastapi import FastAPI
from prometheus_fastapi_instrumentator import Instrumentator

from src.repositories.persons import RedisCache
from src.routes import api_router
from src.settings import AppSettings

SERVICE_NAME = "search-suggestions-service"


if __name__ == "__main__":
    app_settings = AppSettings()
    app = FastAPI(title=SERVICE_NAME)
    app.include_router(api_router, prefix="/api/v1")
    Instrumentator().instrument(app).expose(app)
    uvicorn.run(app, host=app_settings.host, port=app_settings.port)
