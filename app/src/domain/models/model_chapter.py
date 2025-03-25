class ChapterModel:

    def __init__(
            self,
            id: str,
            name: str,
            description: str,
            videoUrl: str,
            imgUrl: str,
            duration: str,
            dateCreation: str,
            seasonId: str
    ):
        self.id: str = id
        self.name = name
        self.description = description
        self.videoUrl = videoUrl
        self.imgUrl = imgUrl
        self.duration = duration
        self.dateCreation = dateCreation
        self.seasonId = seasonId

    def getJson(self) -> dict:
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'videoUrl': self.videoUrl,
            'imgUrl': self.imgUrl,
            'duration': self.duration,
            'dateCreation': self.dateCreation,
            'seasonId': self.seasonId
        }