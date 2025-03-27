from app.src.application.dto.response_season import ResponseSeason
from app.src.domain.models.model_series import SeriesModel
from app.src.application.dto.request_series import RequestSeries
from app.src.application.dto.response_series import ResponseSeries
from app.src.application.mappers.i_mapper_season_application import IMapperSeasonApplication

class IMapperSeriesApplication:

    @staticmethod
    def mapperRequestSeriesToSeriesModel(requestSeries: RequestSeries, imgUrl: str) -> SeriesModel:
        return SeriesModel(
            id="",
            name=requestSeries.name,
            description=requestSeries.description,
            imgUrl=imgUrl,
            dateCreation=requestSeries.dateCreation,
            category=requestSeries.category,
            rating=requestSeries.rating,
            seasons=[]
        )

    @staticmethod
    def mapperSeriesModelToResponseSeries(seriesModel:SeriesModel) -> ResponseSeries:
        listSeasonsSeries: list[ResponseSeason] = IMapperSeasonApplication.mapperSeasonModelListToResponseSeasonList(
            seasonModelList=seriesModel.seasons
        )

        return ResponseSeries(
            id=seriesModel.id,
            name=seriesModel.name,
            description=seriesModel.description,
            imgUrl=seriesModel.imgUrl,
            dateCreation=seriesModel.dateCreation,
            category=seriesModel.category,
            rating=seriesModel.rating,
            seasons=listSeasonsSeries
        )

    @staticmethod
    def mapperSeriesModelListToResponseSeriesList(seriesModelList: list[SeriesModel]) -> list[ResponseSeries]:
        return [ IMapperSeriesApplication.mapperSeriesModelToResponseSeries(seriesModel=seriesModel) for seriesModel in seriesModelList ]