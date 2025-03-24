from starlette.routing import BaseRoute

from app.src.infrastructure.inputs.rest.controllers.movie_controller import movieRouter
class ConfigurationRouter:

    @staticmethod
    def registerRouters() -> list[BaseRoute]:
        return list(movieRouter.routes)