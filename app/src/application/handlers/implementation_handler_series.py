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
        responseSeriesList: list[ResponseSeries] = self.iMapperSeriesApplication.mapperSeriesModelListToResponseSeriesList(
            seriesModelList= await self.iSeriesService.getAll(page=page, limit=limit)
        )
        return [ response.getJSON() for response in responseSeriesList]

    async def getById(self, id: str) -> ResponseSeries:
        responseSeries: ResponseSeries = self.iMapperSeriesApplication.mapperSeriesModelToResponseSeries(
            seriesModel= await self.iSeriesService.getById(id=id)
        )
        return responseSeries.getJSON()

    async def create(self, series: RequestSeries) -> ResponseSeries:
        seriesModel: SeriesModel = self.iMapperSeriesApplication.mapperRequestSeriesToSeriesModel(
            imgUrl="files/series/id",
            requestSeries=series
        )
        responseSeries: ResponseSeries = self.iMapperSeriesApplication.mapperSeriesModelToResponseSeries(
            seriesModel= await self.iSeriesService.create(series=seriesModel)
        )

        imgUrl: str = UtilsFilesApplication.saveFile(file=series.imgFile, folderName=responseSeries.imgUrl)

        await self.iSeriesService.updateByIdTheImgUrl(imgUrl=imgUrl, id=responseSeries.id)

        responseSeries.imgUrl = imgUrl
        return responseSeries.getJSON()

    async def updateById(self, id: str, seriesUpdate: RequestSeries) -> ResponseSeries:

        await self.iSeriesService.getById(id=id)

        imgUrl: str = UtilsFilesApplication.saveFile(file=seriesUpdate.imgFile, folderName=f"files/series/{id}")

        seriesModel: SeriesModel = self.iMapperSeriesApplication.mapperRequestSeriesToSeriesModel(
            imgUrl=imgUrl,
            requestSeries=seriesUpdate
        )

        responseSeries: ResponseSeries = self.iMapperSeriesApplication.mapperSeriesModelToResponseSeries(
            seriesModel= await self.iSeriesService.updateById(id=id,seriesUpdate=seriesModel)
        )

        return responseSeries.getJSON()

    async def deleteById(self, id: str) -> str:
        return await self.iSeriesService.deleteById(id=id)