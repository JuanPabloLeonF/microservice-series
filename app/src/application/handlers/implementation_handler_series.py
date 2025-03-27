from app.src.application.dto.response_series import ResponseSeries
from app.src.application.dto.request_series import RequestSeries
from app.src.application.mappers.i_mapper_series_appliaction import IMapperSeriesApplication
from app.src.application.handlers.i_handler_series import IHandlerSeries
from app.src.domain.models.model_series import SeriesModel
from app.src.domain.services.i_service_series import ISeriesService
from app.src.application.utils.utils_file_application import UtilsFilesApplication

class ImplementationHandlerSeries(IHandlerSeries):

    def __init__(self, iMapperSeriesApplication: IMapperSeriesApplication, iSeriesService: ISeriesService):
        self.iMapperSeriesApplication: IMapperSeriesApplication = iMapperSeriesApplication
        self.iSeriesService: ISeriesService = iSeriesService

    async def getAll(self, page: int, limit: int) -> list[ResponseSeries]:
        return self.iMapperSeriesApplication.mapperSeriesModelListToResponseSeriesList(
            seriesModelList= await self.iSeriesService.getAll(page=page, limit=limit)
        )

    async def getById(self, id: str) -> ResponseSeries:
        return self.iMapperSeriesApplication.mapperSeriesModelToResponseSeries(
            seriesModel= await self.iSeriesService.getById(id=id)
        )

    async def create(self, series: RequestSeries) -> ResponseSeries:
        imgUrl: str = UtilsFilesApplication.saveFile(file=series.imgFile, folderName="series")
        seriesModel: SeriesModel = self.iMapperSeriesApplication.mapperRequestSeriesToSeriesModel(
            imgUrl=imgUrl,
            requestSeries=series
        )
        responseSeries: ResponseSeries = self.iMapperSeriesApplication.mapperSeriesModelToResponseSeries(
            seriesModel= await self.iSeriesService.create(series=seriesModel)
        )

        """
        AQUI AHI QUE CREAR UNA IMPLEMENTACION EN LA CUAL DETECTE SI TODO DALIO BIEJ DEVUELVE EL JSON,
        PERO SI ALGO SALIO MAL ELIMINAR LA IMAGEN DEL DIRECTORIO.
        """

        return responseSeries.getJSON()

    async def updateById(self, id: str, seriesUpdate: RequestSeries) -> ResponseSeries:
        pass

    async def deleteById(self, id: str) -> str:
        pass