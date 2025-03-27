from app.src.domain.models.model_chapter import ChapterModel
from app.src.application.dto.request_chapter import RequestChapter
from app.src.application.dto.response_chapter import ResponseChapter

class IMapperChapterApplication:

    @staticmethod
    def mapperRequestChapterToChapterModel(requestChapter: RequestChapter) -> ChapterModel:
        return ChapterModel(
            id="",
            name=requestChapter.name,
            description=requestChapter.description,
            videoUrl=requestChapter.videoUrl,
            imgUrl=requestChapter.imgUrl,
            duration=requestChapter.duration,
            dateCreation=requestChapter.dateCreation,
            seasonId=requestChapter.seasonId
        )

    @staticmethod
    def mapperChapterModelToResponseChapter(chapterModel: ChapterModel) -> ResponseChapter:
        return ResponseChapter(
            id=chapterModel.id,
            name=chapterModel.name,
            description=chapterModel.description,
            videoUrl=chapterModel.videoUrl,
            imgUrl=chapterModel.imgUrl,
            duration=chapterModel.duration,
            dateCreation=chapterModel.dateCreation,
            seasonId=chapterModel.seasonId
        )

    @staticmethod
    def mapperChapterModelListToResponseChapterList(chapterModelList: list[ChapterModel]) -> list[ResponseChapter]:
        return [ IMapperChapterApplication.mapperChapterModelToResponseChapter(chapterModel=chapterModel) for chapterModel in chapterModelList ]