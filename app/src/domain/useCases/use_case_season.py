from app.src.domain.models.model_season import SeasonModel
from app.src.domain.persistence.i_persistence_season import ISeasonPersistence
from app.src.domain.services.i_service_season import ISeasonService

class UseCaseSeason(ISeasonService):

    def __init__(self, iSeasonPersistence: ISeasonPersistence):
        self.iSeasonPersistence: ISeasonPersistence = iSeasonPersistence

    async def getAll(self, page: int, limit: int) -> list[SeasonModel]:
        return await self.iSeasonPersistence.getAll(page=page, limit=limit)

    async def getById(self, id: str) -> SeasonModel:
        return await self.iSeasonPersistence.getById(id=id)

    async def create(self, season: SeasonModel) -> SeasonModel:
        return await self.iSeasonPersistence.create(season=season)

    async def updateById(self, id: str, seasonUpdate: SeasonModel) -> SeasonModel:
        return await self.iSeasonPersistence.updateById(id=id, seasonUpdate=seasonUpdate)

    async def deleteById(self, id: str) -> str:
        return await self.iSeasonPersistence.deleteById(id=id)