from fastapi import APIRouter
from fastapi.openapi.docs import (
    get_redoc_html,
)
from fastapi.responses import HTMLResponse


def build_router(openapi_url: str, title: str) -> APIRouter:
    router = APIRouter()

    @router.get("/redoc", include_in_schema=False)
    async def redoc_html() -> HTMLResponse:
        return get_redoc_html(
            openapi_url=openapi_url,
            title=title + " - ReDoc",
            redoc_js_url="/static/redoc.standalone.js",
            with_google_fonts=False,
        )

    return router
