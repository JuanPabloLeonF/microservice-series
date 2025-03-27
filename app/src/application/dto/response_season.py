from app.src.application.dto.response_chapter import ResponseChapter

class ResponseSeason:

    def __init__(
            self,
            id: str,
            name: str,
            dateCreation: str,
            seriesId: str,
            chapters: list[ResponseChapter]
    ):
        self.id: str = id
        self.name: str = name
        self.dateCreation: str = dateCreation
        self.seriesId: str = seriesId
        self.chapters: list[ResponseChapter] = chapters

    def getJSON(self):
        return  {
            'id': self.id,
            'name': self.name,
            'dateCreation': self.dateCreation,
            'seriesId': self.seriesId,
            'chapters': [ chapter.getJSON() for chapter in self.chapters ]
        }