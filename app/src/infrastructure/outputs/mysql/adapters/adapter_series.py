from app.src.domain.models.model_series import SeriesModel
from app.src.domain.persistence.i_persistence_series import ISeriesPersistence
from app.src.infrastructure.outputs.mysql.repositories.i_series_entity import ISeriesEntity
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_series_entity import IMapperSeriesEntity

class AdapterSeries(ISeriesPersistence):

    def __init__(self, iSeriesEntity:ISeriesEntity, iMapperSeriesEntity:IMapperSeriesEntity):
        self.iSeriesEntity: ISeriesEntity = iSeriesEntity
        self.iMapperSeriesEntity: IMapperSeriesEntity = iMapperSeriesEntity

    async def getAll(self, page: int, limit: int) -> list[SeriesModel]:
        return self.iMapperSeriesEntity.mapperSeriesEntityListToSeriesModelList(
            seriesEntityList= await self.iSeriesEntity.getAll(page=page, limit=limit)
        )

    async def getById(self, id: str) -> SeriesModel:
        return self.iMapperSeriesEntity.mapperSeriesEntityToSeriesModel(
            seriesEntity= await self.iSeriesEntity.getById(id=id)
        )

    async def create(self, series: SeriesModel) -> SeriesModel:
        return self.iMapperSeriesEntity.mapperSeriesEntityToSeriesModel(
            seriesEntity= await self.iSeriesEntity.create(
                series= self.iMapperSeriesEntity.mapperSeriesModelToSeriesEntity(
                    seriesModel=series
                )
            )
        )

    async def updateById(self, id: str, seriesUpdate: SeriesModel) -> SeriesModel:
        return self.iMapperSeriesEntity.mapperSeriesEntityToSeriesModel(
            seriesEntity=await self.iSeriesEntity.updateById(
                id=id,
                seriesUpdate=self.iMapperSeriesEntity.mapperSeriesModelToSeriesEntity(
                    seriesModel=seriesUpdate
                )
            )
        )


    async def deleteById(self, id: str) -> str:
        return await self.iSeriesEntity.deleteById(id=id)