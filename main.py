from fastapi import FastAPI

from routers.cities import cities_router
from routers.temperatures import temps_router

app = FastAPI(
    title="Temperatures for Cities"
)

app.include_router(cities_router)
app.include_router(temps_router)


if __name__ == "__main__":
    from database.models import Base
    from database.sqlite import engine

    Base.metadata.create_all(bind=engine)
