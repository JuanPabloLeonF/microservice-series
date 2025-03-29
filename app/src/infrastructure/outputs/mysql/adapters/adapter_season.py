from app.src.domain.models.model_season import SeasonModel
from app.src.domain.persistence.i_persistence_season import ISeasonPersistence
from app.src.infrastructure.outputs.mysql.repositories.i_season_repository import ISeasonRepository
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_season_entity import IMapperSeasonEntity

class AdapterSeason(ISeasonPersistence):

    def __init__(self, iSeasonRepository: ISeasonRepository, iMapperSeasonEntity: IMapperSeasonEntity):
        self.iSeasonRepository = iSeasonRepository
        self.iMapperSeasonEntity = iMapperSeasonEntity

    async def getAll(self, page: int, limit: int) -> list[SeasonModel]:
        return self.iMapperSeasonEntity.mapperSeasonEntityListToSeasonModelList(
            seasonEntityList= await self.iSeasonRepository.getAll(page=page, limit=limit)
        )

    async def getById(self, id: str) -> SeasonModel:
        return self.iMapperSeasonEntity.mapperSeasonEntityToSeasonModel(
            seasonEntity= await self.iSeasonRepository.getById(id=id)
        )

    async def create(self, season: SeasonModel) -> SeasonModel:
        return self.iMapperSeasonEntity.mapperSeasonEntityToSeasonModel(
            seasonEntity= await self.iSeasonRepository.create(
                season= self.iMapperSeasonEntity.mapperSeasonModelToSeasonEntity(seasonModel=season)
            )
        )

    async def updateById(self, id: str, seasonUpdate: SeasonModel) -> SeasonModel:
        return self.iMapperSeasonEntity.mapperSeasonEntityToSeasonModel(
            seasonEntity= await self.iSeasonRepository.updateById(
                id=id,
                seasonUpdate= self.iMapperSeasonEntity.mapperSeasonModelToSeasonEntity(seasonModel=seasonUpdate)
            )
        )

    async def deleteById(self, id: str) -> str:
        return await self.iSeasonRepository.deleteById(id=id)