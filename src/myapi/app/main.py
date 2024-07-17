import uvicorn
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from importlib_resources import as_file, files

from .routers.docs import build_router as build_docs_router
from .routers.redoc import build_router as build_redoc_router
from .routers.users import router as users_router

title = "My API"
openapi_url = "/openapi.json"
swagger_ui_oauth2_redirect_url = "/docs/oauth2-redirect"

app = FastAPI(
    title=title,
    openapi_url=openapi_url,
    docs_url=None,
    redoc_url=None,
    swagger_ui_oauth2_redirect_url=swagger_ui_oauth2_redirect_url,
)

with as_file(files("myapi") / "static") as static_directory:
    app.mount("/static", StaticFiles(directory=static_directory), name="static")

app.include_router(build_docs_router(openapi_url, title, swagger_ui_oauth2_redirect_url))
app.include_router(build_redoc_router(openapi_url, title))
app.include_router(users_router)

if __name__ == "__main__":
    uvicorn.run(app, host="127.0.0.1", port=8000)
