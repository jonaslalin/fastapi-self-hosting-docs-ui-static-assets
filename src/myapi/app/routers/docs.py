from fastapi import APIRouter
from fastapi.openapi.docs import (
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from fastapi.responses import HTMLResponse


def build_router(openapi_url: str, title: str, swagger_ui_oauth2_redirect_url: str) -> APIRouter:
    router = APIRouter()

    @router.get("/docs", include_in_schema=False)
    async def custom_swagger_ui_html() -> HTMLResponse:
        return get_swagger_ui_html(
            openapi_url=openapi_url,
            title=title + " - Swagger UI",
            oauth2_redirect_url=swagger_ui_oauth2_redirect_url,
            swagger_js_url="/static/swagger-ui-bundle.js",
            swagger_css_url="/static/swagger-ui.css",
        )

    @router.get(swagger_ui_oauth2_redirect_url, include_in_schema=False)
    async def swagger_ui_redirect() -> HTMLResponse:
        return get_swagger_ui_oauth2_redirect_html()

    return router
