from fastapi import UploadFile

class RequestSeries:

    def __init__(
            self,
            name: str,
            description: str,
            imgFile: UploadFile,
            dateCreation: str,
            category: list[str],
            rating: str,
    ):
        self.name: str = name
        self.description: str = description
        self.imgFile: UploadFile = imgFile
        self.dateCreation: str = dateCreation
        self.category: list[str] = category
        self.rating: str = rating

    def getJSON(self) -> dict:
        return {
            'name': self.name,
            'description': self.description,
            'imgFile': self.imgFile,
            'dateCreation': self.dateCreation,
            'category': self.category,
            'rating': self.rating,
        }