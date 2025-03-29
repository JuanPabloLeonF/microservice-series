import injector
from fastapi import APIRouter,status
from fastapi.responses import JSONResponse

from app.configuration.module_injector_season import ModuleInjectorSeasonModule
from app.src.infrastructure.inputs.rest.mapper.i_mapper_season_controller import IMapperSeasonController
from app.src.infrastructure.inputs.rest.dto.request_season_controller import RequestFormSeason
from app.src.application.handlers.i_handler_season import IHandlerSeason
from app.src.application.dto.request_season import RequestSeason
from app.src.application.dto.response_season import ResponseSeason

seasonRouter: APIRouter = APIRouter(prefix="/season")
iHandler: IHandlerSeason = injector.Injector([ModuleInjectorSeasonModule()]).get(IHandlerSeason)
iMapperSeasonController: IMapperSeasonController = IMapperSeasonController()

class ControllerSeason:

    @staticmethod
    @seasonRouter.get("/all/{page}/{limit}", status_code=status.HTTP_200_OK)
    async def getAll(page: int, limit: int) -> JSONResponse:
        response: list[ResponseSeason] = await iHandler.getAll(page=page, limit=limit)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @seasonRouter.get("/id/{id}" ,status_code=status.HTTP_200_OK)
    async def getById(id: str) -> JSONResponse:
        response: ResponseSeason = await iHandler.getById(id=id)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @seasonRouter.post("/create",status_code=status.HTTP_201_CREATED)
    async def create(season: RequestFormSeason) -> JSONResponse:
        requestSeason: RequestSeason = iMapperSeasonController.mapperRequestFormSeasonToRequestSeason(requestFormSeason=season)
        response: ResponseSeason = await iHandler.create(season=requestSeason)
        return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)

    @staticmethod
    @seasonRouter.put("/update/{id}", status_code=status.HTTP_200_OK)
    async def updateById(id: str, season: RequestFormSeason) -> JSONResponse:
        requestSeason: RequestSeason = iMapperSeasonController.mapperRequestFormSeasonToRequestSeason(requestFormSeason=season)
        response: ResponseSeason = await iHandler.updateById(id=id, seasonUpdate=requestSeason)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @seasonRouter.delete("/delete/{id}",status_code=status.HTTP_200_OK)
    async def deleteById(id: str) -> JSONResponse:
        response: str = await iHandler.deleteById(id=id)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)