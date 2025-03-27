from abc import ABC, abstractmethod
from app.src.application.dto.response_series import ResponseSeries
from app.src.application.dto.request_series import RequestSeries

class IHandlerSeries(ABC):

    @abstractmethod
    async def getAll(self, page:int, limit:int) -> list[ResponseSeries]:
        pass

    @abstractmethod
    async def getById(self, id:str) -> ResponseSeries:
        pass

    @abstractmethod
    async def create(self, series:RequestSeries) -> ResponseSeries:
        pass

    @abstractmethod
    async def updateById(self, id: str, seriesUpdate: RequestSeries) -> ResponseSeries:
        pass

    @abstractmethod
    async def deleteById(self, id: str) -> str:
        pass