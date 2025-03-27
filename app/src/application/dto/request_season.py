class RequestSeason:

    def __init__(
            self,
            name: str,
            dateCreation: str,
            seriesId: str
    ):
        self.name: str = name
        self.dateCreation: str = dateCreation
        self.seriesId: str = seriesId

    def getJSON(self) -> dict:
        return {
            'name': self.name,
            'dateCreation': self.dateCreation,
            'seriesId': self.seriesId,
        }