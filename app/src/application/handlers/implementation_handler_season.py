from app.src.domain.services.i_service_season import ISeasonService
from app.src.application.dto.request_season import RequestSeason
from app.src.application.dto.response_season import ResponseSeason
from app.src.application.mappers.i_mapper_season_application import IMapperSeasonApplication
from app.src.application.handlers.i_handler_season import IHandlerSeason

class ImplementationHandlerSeason(IHandlerSeason):

    def __init__(self, iMapperSeasonApplication: IMapperSeasonApplication, iSeasonService: ISeasonService):
        self.iMapperSeasonApplication: IMapperSeasonApplication = iMapperSeasonApplication
        self.iSeasonService: ISeasonService = iSeasonService

    async def getAll(self, page: int, limit: int) -> list[ResponseSeason]:
        listResponseSeasons: list[ResponseSeason] = self.iMapperSeasonApplication.mapperSeasonModelListToResponseSeasonList(
            seasonModelList= await self.iSeasonService.getAll(page=page, limit=limit)
        )
        return [season.getJSON() for season in listResponseSeasons]

    async def getById(self, id: str) -> ResponseSeason:
        responseSeason: ResponseSeason = self.iMapperSeasonApplication.mapperSeasonModelToResponseSeason(
            seasonModel= await self.iSeasonService.getById(id=id)
        )
        return responseSeason.getJSON()

    async def create(self, season: RequestSeason) -> ResponseSeason:
        responseSeason: ResponseSeason = self.iMapperSeasonApplication.mapperSeasonModelToResponseSeason(
            seasonModel= await self.iSeasonService.create(
                season=self.iMapperSeasonApplication.mapperRequestSeasonToSeasonModel(requestSeason=season)
            )
        )
        return responseSeason.getJSON()

    async def updateById(self, id: str, seasonUpdate: RequestSeason) -> ResponseSeason:
        responseSeason: ResponseSeason = self.iMapperSeasonApplication.mapperSeasonModelToResponseSeason(
            seasonModel=await self.iSeasonService.updateById(
                id=id,
                seasonUpdate= self.iMapperSeasonApplication.mapperRequestSeasonToSeasonModel(requestSeason=seasonUpdate)
            )
        )
        return responseSeason.getJSON()

    async def deleteById(self, id: str) -> str:
        return await self.iSeasonService.deleteById(id=id)