


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from uvicorn import Config, Server
from fastapi.openapi.docs import get_redoc_html, get_swagger_ui_html
from fastapi.openapi.utils import get_openapi

def _get_app():
    from api.v1 import router as models_router

    app = FastAPI(
        title="Permissionless Models Integration Backend",
        openapi_tags=[
            {
                "name": "Backend",
                "description": "prmsnls models integrations",
            },
        ],
        docs_url="/docs",
        redoc_url=None,
        openapi_url=None,
    )


    @app.get("/docs", include_in_schema=False)
    async def get_swagger_documentation():
        return get_swagger_ui_html(openapi_url="/openapi.json", title="docs")

    @app.get("/redoc", include_in_schema=False)
    async def get_redoc_documentation():
        return get_redoc_html(openapi_url="/openapi.json", title="docs")

    
    @app.get("/openapi.json", include_in_schema=False)
    async def openapi():
        return get_openapi(title=app.title, version=app.version, routes=app.routes)

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(models_router)


    return app

def _start_uvicorn(app: "FastAPI"):
    config = Config(
        app=app,
        host="0.0.0.0",
        port="8000",
        loop="uvloop",
        log_level="error",
    )
    server = Server(config=config)
    server.run()


def main():
    _start_uvicorn(app=_get_app())

