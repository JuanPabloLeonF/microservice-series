from app.src.domain.models.model_chapter import ChapterModel

class SeasonModel:

    def __init__(
            self,
            id: str,
            name: str,
            dateCreation: str,
            seriesId: str,
            chapters: list[ChapterModel],
    ):
        self.id: str = id
        self.name = name
        self.dateCreation = dateCreation
        self.seriesId = seriesId
        self.chapters = chapters

    def getJSON(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'dateCreation': self.dateCreation,
            'seriesId': self.seriesId,
            'chapters': [ chapter.getJson() for chapter in self.chapters ]
        }