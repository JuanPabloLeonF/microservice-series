from app.src.application.dto.response_chapter import ResponseChapter
from app.src.domain.models.model_season import SeasonModel
from app.src.application.dto.request_season import RequestSeason
from app.src.application.dto.response_season import ResponseSeason
from app.src.application.mappers.i_mapper_chapter_appliaction import IMapperChapterApplication

class IMapperSeasonApplication:

    @staticmethod
    def mapperRequestSeasonToSeasonModel(requestSeason: RequestSeason) -> SeasonModel:
        return SeasonModel(
            id="",
            name=requestSeason.name,
            dateCreation=requestSeason.dateCreation,
            seriesId=requestSeason.seriesId,
            chapters=[]
        )

    @staticmethod
    def mapperSeasonModelToResponseSeason(seasonModel: SeasonModel) -> ResponseSeason:

        listResponseChapter: list[ResponseChapter] = IMapperChapterApplication.mapperChapterModelListToResponseChapterList(
            chapterModelList=seasonModel.chapters
        )

        return ResponseSeason(
            id=seasonModel.id,
            name=seasonModel.name,
            dateCreation=seasonModel.dateCreation,
            seriesId=seasonModel.seriesId,
            chapters=listResponseChapter
        )

    @staticmethod
    def mapperSeasonModelListToResponseSeasonList(seasonModelList: list[SeasonModel]) -> list[ResponseSeason]:
        return [ IMapperSeasonApplication.mapperSeasonModelToResponseSeason(seasonModel=seasonModel) for seasonModel in seasonModelList ]