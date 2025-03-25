from app.src.domain.models.model_chapter import ChapterModel
from app.src.infrastructure.outputs.mysql.entities.chapter_entity import ChapterEntity

class IMapperChapterEntity:

    @staticmethod
    def mapperChapterEntityToChapterModel(chapterEntity: ChapterEntity) -> ChapterModel:
        return ChapterModel(
            id = chapterEntity.id,
            name = chapterEntity.name,
            description = chapterEntity.description,
            videoUrl = chapterEntity.videoUrl,
            imgUrl = chapterEntity.imgUrl,
            duration = chapterEntity.duration,
            dateCreation = chapterEntity.dateCreation,
            seasonId = chapterEntity.seasonId
        )

    @staticmethod
    def mapperChapterModelToChapterEntity(chapterModel: ChapterModel) -> ChapterEntity:
        return ChapterEntity(
            name = chapterModel.name,
            description = chapterModel.description,
            videoUrl = chapterModel.videoUrl,
            imgUrl = chapterModel.imgUrl,
            duration = chapterModel.duration,
            dateCreation = chapterModel.dateCreation,
            seasonId = chapterModel.seasonId
        )

    @staticmethod
    def mapperChapterEntityListToChapterModelList(chapterEntityList: list[ChapterEntity]) -> list[ChapterModel]:
        return [ IMapperChapterEntity.mapperChapterEntityToChapterModel(chapterEntity) for chapterEntity in chapterEntityList ]

    @staticmethod
    def mapperChapterModelListToChapterEntityList(chapterModelList: list[ChapterModel]) -> list[ChapterEntity]:
        return [ IMapperChapterEntity.mapperChapterModelToChapterEntity(chapterModel) for chapterModel in chapterModelList ]