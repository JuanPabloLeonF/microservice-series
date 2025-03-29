from abc import ABC, abstractmethod
from app.src.domain.models.model_season import SeasonModel

class ISeasonPersistence(ABC):

    @abstractmethod
    async def getAll(self, page:int, limit:int) -> list[SeasonModel]:
        pass

    @abstractmethod
    async def getById(self, id:str) -> SeasonModel:
        pass

    @abstractmethod
    async def create(self, season: SeasonModel) -> SeasonModel:
        pass

    @abstractmethod
    async def updateById(self, id: str, seasonUpdate: SeasonModel) -> SeasonModel:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass