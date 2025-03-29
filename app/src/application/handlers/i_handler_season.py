from abc import ABC, abstractmethod
from app.src.application.dto.request_season import RequestSeason
from app.src.application.dto.response_season import ResponseSeason

class IHandlerSeason(ABC):

    @abstractmethod
    async def getAll(self, page:int, limit:int) -> list[ResponseSeason]:
        pass

    @abstractmethod
    async def getById(self, id:str) -> ResponseSeason:
        pass

    @abstractmethod
    async def create(self, season:RequestSeason) -> ResponseSeason:
        pass

    @abstractmethod
    async def updateById(self, id: str, seasonUpdate: RequestSeason) -> ResponseSeason:
        pass

    @abstractmethod
    async def deleteById(self, id:str) -> str:
        pass