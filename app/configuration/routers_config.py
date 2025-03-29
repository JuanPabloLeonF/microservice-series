from starlette.routing import BaseRoute
from app.src.infrastructure.inputs.rest.controllers.controller_series import seriesRouter
from app.src.infrastructure.inputs.rest.controllers.controller_season import seasonRouter

class ConfigurationRouter:

    @staticmethod
    def registerRouters() -> list[BaseRoute]:
        return list(seriesRouter.routes) + list(seasonRouter.routes)