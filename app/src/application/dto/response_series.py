from app.src.application.dto.response_season import ResponseSeason


class ResponseSeries:

    def __init__(
            self,
            id: str,
            name: str,
            description: str,
            imgUrl: str,
            dateCreation: str,
            category: list[str],
            rating: str,
            seasons: list[ResponseSeason]
    ):
        self.id: str = id
        self.name: str = name
        self.description: str = description
        self.imgUrl: str = imgUrl
        self.dateCreation: str = dateCreation
        self.category: list[str] = category
        self.rating: str = rating
        self.seasons: list[ResponseSeason] = seasons


    def getJSON(self):
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'imgUrl': self.imgUrl,
            'dateCreation': self.dateCreation,
            'category': self.category,
            'rating': self.rating,
            'seasons': [ season.getJSON() for season in self.seasons]
        }