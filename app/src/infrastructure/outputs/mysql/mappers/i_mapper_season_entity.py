from app.src.domain.models.model_chapter import ChapterModel
from app.src.domain.models.model_season import SeasonModel
from app.src.infrastructure.outputs.mysql.entities.chapter_entity import ChapterEntity
from app.src.infrastructure.outputs.mysql.entities.season_entity import SeasonEntity
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_chapter_entity import IMapperChapterEntity

class IMapperSeasonEntity:

    @staticmethod
    def mapperSeasonEntityToSeasonModel(seasonEntity: SeasonEntity) -> SeasonModel:

        listChaptersModel: list[ChapterModel] = IMapperChapterEntity.mapperChapterEntityListToChapterModelList(
            chapterEntityList=seasonEntity.chapters
        )

        return SeasonModel(
            id=seasonEntity.id,
            name=seasonEntity.name,
            dateCreation=seasonEntity.dateCreation,
            seriesId=seasonEntity.seriesId,
            chapters=listChaptersModel
        )

    @staticmethod
    def mapperSeasonModelToSeasonEntity(seasonModel: SeasonModel) -> SeasonEntity:

        listChaptersEntity: list[ChapterEntity] = IMapperChapterEntity.mapperChapterModelListToChapterEntityList(
            chapterModelList=seasonModel.chapters
        )

        return SeasonEntity(
            name=seasonModel.name,
            dateCreation=seasonModel.dateCreation,
            seriesId=seasonModel.seriesId,
            chapters=listChaptersEntity
        )

    @staticmethod
    def mapperSeasonEntityListToSeasonModelList(seasonEntityList: list[SeasonEntity]) -> list[SeasonModel]:
        return [ IMapperSeasonEntity.mapperSeasonEntityToSeasonModel(seasonEntity) for seasonEntity in seasonEntityList ]

    @staticmethod
    def mapperSeasonModelListToSeasonEntityList(seasonModelList: list[SeasonModel]) -> list[SeasonEntity]:
        return [ IMapperSeasonEntity.mapperSeasonModelToSeasonEntity(seasonModel) for seasonModel in seasonModelList ]