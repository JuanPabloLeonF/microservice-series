from datetime import datetime
from pydantic import BaseModel, Field, field_validator

class RequestFormSeason(BaseModel):
    name: str = Field(min_length=3, max_length=200)
    dateCreation: str = Field(min_length=10, max_length=20)
    seriesId: str = Field(max_length=36)

    @field_validator("dateCreation")
    def validateDateCreation(cls, value: str) -> str:
        try:
            datetime.strptime(value, "%d/%m/%Y")
            return value
        except ValueError:
            raise ValueError("dateCreation must be in DD/MM/YYYY")