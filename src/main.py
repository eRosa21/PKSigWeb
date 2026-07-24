import os
from pathlib import Path

import uvicorn
from dotenv import load_dotenv

load_dotenv()

from src.infra.database.database import engine, Base
from src.infra.http.api_server import app
from src.infra.http.controllers.regions_controller import router as regions_router
from src.infra.http.controllers.routes_controller import router as routes_router
from src.infra.http.controllers.cities_controller import router as cities_router
from src.infra.http.controllers.pokemon_controller import router as pokemon_router

Base.metadata.create_all(bind=engine)

app.include_router(regions_router)
app.include_router(routes_router)
app.include_router(cities_router)
app.include_router(pokemon_router)


def main() -> None:
  root = Path(__file__).resolve().parent.parent
  uvicorn.run(
    "src.main:app",
    host="0.0.0.0",
    port=int(os.environ.get("API_PORT", "8000")),
    reload=True,
    reload_dirs=[str(root / "src")],
  )


if __name__ == "__main__":
  main()
