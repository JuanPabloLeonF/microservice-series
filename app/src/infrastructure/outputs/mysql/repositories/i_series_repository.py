from abc import ABC, abstractmethod
from app.src.infrastructure.outputs.mysql.entities.series_entity import SeriesEntity

class ISeriesRepository(ABC):

    @abstractmethod
    async def getAll(self, page:int, limit:int) -> list[SeriesEntity]:
        pass

    @abstractmethod
    async def getById(self, id: str) -> SeriesEntity:
        pass

    @abstractmethod
    async def create(self, series:SeriesEntity) -> SeriesEntity:
        pass

    @abstractmethod
    async def updateById(self, id: str, seriesUpdate: SeriesEntity) -> SeriesEntity:
        pass

    @abstractmethod
    async def updateByIdTheImgUrl(self, imgUrl: str, id: str) -> str:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass