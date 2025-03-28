import json
from datetime import datetime
from fastapi import Form, UploadFile, File

class RequestFormSeries:

    def __init__(
        self,
        name: str = Form(min_length=3, max_length=200),
        dateCreation: str = Form(min_length=10, max_length=20),
        description: str = Form(min_length=5, max_length=255),
        category: str = Form(),
        rating: str = Form(min_length=3, max_length=4),
        imgFile: UploadFile = File(),
    ):
        self.name = name
        self.dateCreation = RequestFormSeries.validateDateCreation(value=dateCreation)
        self.imgFile = imgFile
        self.description = description
        self.category: list[str] = RequestFormSeries.validateCategory(value=category)
        self.rating = rating

    @staticmethod
    def validateCategory(value: str) -> list[str]:
        try:
            data: list[str] = json.loads(value)

            if not isinstance(data, list):
                raise ValueError("category debe ser una lista de strings")

            for item in data:
                if not isinstance(item, str) or item.strip() == "":
                    raise ValueError("category no puede estar vacio")

            return data
        except (ValueError, json.JSONDecodeError):
            raise ValueError("category must be a list of strings")

    @staticmethod
    def validateDateCreation(value: str) -> str:
        try:
            datetime.strptime(value, "%d/%m/%Y")
            return value
        except ValueError:
            raise ValueError("dateCreation must be in DD/MM/YYYY")

    def getJSON(self) -> dict:
        return {
            "name": self.name,
            "dateCreation": self.dateCreation,
            "imgFile": self.imgFile.filename,
        }