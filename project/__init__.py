from fastapi import FastAPI


def create_app() -> FastAPI:
    app = FastAPI()

    from project.app.routers import health_check_router

    app.include_router(health_check_router)

    return app
