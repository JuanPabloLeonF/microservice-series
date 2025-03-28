from starlette.routing import BaseRoute

from app.src.infrastructure.inputs.rest.controllers.controller_series import seriesRouter
class ConfigurationRouter:

    @staticmethod
    def registerRouters() -> list[BaseRoute]:
        return list(seriesRouter.routes)