import injector
from fastapi import APIRouter,status, Depends
from fastapi.responses import JSONResponse

from app.configuration.module_injector_user import ModuleInjectorSeries
from app.src.application.dto.request_series import RequestSeries
from app.src.application.dto.response_series import ResponseSeries
from app.src.application.handlers.i_handler_series import IHandlerSeries
from app.src.infrastructure.inputs.rest.dto.request_series_controller import RequestFormSeries
from app.src.infrastructure.inputs.rest.mapper.i_mapper_series_controller import IMapperSeriesController

seriesRouter: APIRouter = APIRouter(prefix="/series")
iHandler: IHandlerSeries = injector.Injector([ModuleInjectorSeries()]).get(IHandlerSeries)
iMapperSeriesController: IMapperSeriesController = IMapperSeriesController()

class ControllerSeries:

    @staticmethod
    @seriesRouter.get("/all/{page}/{limit}" ,status_code=status.HTTP_200_OK)
    async def getAll(page: int, limit: int) -> JSONResponse:
        response: list[ResponseSeries] = await iHandler.getAll(page=page, limit=limit)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @seriesRouter.get("/id/{id}" ,status_code=status.HTTP_200_OK)
    async def getById(id: str) -> JSONResponse:
        response: ResponseSeries = await iHandler.getById(id=id)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @seriesRouter.post("/create",status_code=status.HTTP_201_CREATED)
    async def create(series: RequestFormSeries = Depends(RequestFormSeries)) -> JSONResponse:
        requestSeries: RequestSeries = iMapperSeriesController.mapperRequestFormSeriesToRequestSeries(requestFormSeries=series)
        response: ResponseSeries = await iHandler.create(series=requestSeries)
        return JSONResponse(content=response, status_code=status.HTTP_201_CREATED)

    @staticmethod
    @seriesRouter.put("/update/{id}",status_code=status.HTTP_200_OK)
    async def updateById(id: str, series: RequestFormSeries = Depends(RequestFormSeries)) -> JSONResponse:
        requestSeries: RequestSeries = iMapperSeriesController.mapperRequestFormSeriesToRequestSeries(requestFormSeries=series)
        response: ResponseSeries = await iHandler.updateById(id=id, seriesUpdate=requestSeries)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)

    @staticmethod
    @seriesRouter.delete("/delete/{id}",status_code=status.HTTP_200_OK)
    async def deleteById(id: str) -> JSONResponse:
        response: str = await iHandler.deleteById(id=id)
        return JSONResponse(content=response, status_code=status.HTTP_200_OK)