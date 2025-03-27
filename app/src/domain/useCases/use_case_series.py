from app.src.domain.services.i_service_series import ISeriesService
from app.src.domain.persistence.i_persistence_series import ISeriesPersistence
from app.src.domain.models.model_series import SeriesModel

class UseCaseSeries(ISeriesService):

    def __init__(self, iSeriesPersistence: ISeriesPersistence):
        self.iSeriesPersistence: ISeriesPersistence = iSeriesPersistence

    async def getAll(self, page: int, limit: int) -> list[SeriesModel]:
        return await self.iSeriesPersistence.getAll(page=page, limit=limit)

    async def getById(self, id: str) -> SeriesModel:
        return await self.iSeriesPersistence.getById(id=id)

    async def create(self, series: SeriesModel) -> SeriesModel:
        return await self.iSeriesPersistence.create(series=series)

    async def updateById(self, id: str, seriesUpdate: SeriesModel) -> SeriesModel:
        return await self.iSeriesPersistence.updateById(id=id, seriesUpdate=seriesUpdate)


    async def deleteById(self, id: str) -> str:
        return await self.iSeriesPersistence.deleteById(id=id)