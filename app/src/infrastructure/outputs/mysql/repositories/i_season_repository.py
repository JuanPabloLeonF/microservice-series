from abc import ABC, abstractmethod
from app.src.infrastructure.outputs.mysql.entities.season_entity import SeasonEntity

class ISeasonRepository(ABC):

    @abstractmethod
    async def getAll(self, page:int, limit:int) -> list[SeasonEntity]:
        pass

    @abstractmethod
    async def getById(self, id:str) -> SeasonEntity:
        pass

    @abstractmethod
    async def create(self, season:SeasonEntity) -> SeasonEntity:
        pass

    @abstractmethod
    async def updateById(self, id: str, seasonUpdate: SeasonEntity) -> SeasonEntity:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass