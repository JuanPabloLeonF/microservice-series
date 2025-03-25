from app.src.domain.models.model_series import SeriesModel
from app.src.domain.models.model_season import SeasonModel
from app.src.infrastructure.outputs.mysql.entities.series_entity import SeriesEntity
from app.src.infrastructure.outputs.mysql.entities.season_entity import SeasonEntity
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_season_entity import IMapperSeasonEntity

class IMapperSeriesEntity:

    @staticmethod
    def mapperSeriesEntityToSeriesModel(seriesEntity:SeriesEntity) -> SeriesModel:

        listSeasonsModel: list[SeasonModel] = IMapperSeasonEntity.mapperSeasonEntityListToSeasonModelList(
            seasonEntityList=seriesEntity.seasons
        )

        return SeriesModel(
            id=seriesEntity.id,
            name=seriesEntity.name,
            description=seriesEntity.description,
            imgUrl=seriesEntity.imgUrl,
            dateCreation=seriesEntity.dateCreation,
            category=seriesEntity.category,
            rating=seriesEntity.rating,
            seasons=listSeasonsModel
        )

    @staticmethod
    def mapperSeriesModelToSeriesEntity(seriesModel:SeriesModel) -> SeriesEntity:

        listSeasonsSeries: list[SeasonEntity] = IMapperSeasonEntity.mapperSeasonModelListToSeasonEntityList(
            seasonModelList=seriesModel.seasons
        )

        return SeriesEntity(
            name=seriesModel.name,
            description=seriesModel.description,
            imgUrl=seriesModel.imgUrl,
            dateCreation=seriesModel.dateCreation,
            category=seriesModel.category,
            rating=seriesModel.rating,
            seasons=listSeasonsSeries
        )

    @staticmethod
    def mapperSeriesEntityListToSeriesModelList(seriesEntityList:list[SeriesEntity]) -> list[SeriesModel]:
        return [ IMapperSeriesEntity.mapperSeriesEntityToSeriesModel(seriesEntity) for seriesEntity in seriesEntityList ]

    @staticmethod
    def mapperSeriesModelListToSeriesEntityList(seriesModelList:list[SeriesModel]) -> list[SeriesEntity]:
        return [ IMapperSeriesEntity.mapperSeriesModelToSeriesEntity(seriesModel) for seriesModel in seriesModelList ]