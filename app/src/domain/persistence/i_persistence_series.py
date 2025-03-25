from abc import ABC, abstractmethod
from app.src.domain.models.model_series import SeriesModel

class ISeriesPersistence(ABC):

    @abstractmethod
    async def getAll(self, page:int, limit:int) -> list[SeriesModel]:
        pass

    @abstractmethod
    async def getById(self, id:str) -> SeriesModel:
        pass

    @abstractmethod
    async def create(self, series:SeriesModel) -> SeriesModel:
        pass

    @abstractmethod
    async def updateById(self, id: str, seriesUpdate: SeriesModel) -> SeriesModel:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass