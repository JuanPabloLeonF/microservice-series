import uuid
from sqlalchemy import JSON, Column, String
from sqlalchemy.orm import relationship

from app.src.infrastructure.outputs.mysql.entities.season_entity import SeasonEntity
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration
class SeriesEntity(DatabaseConfiguration.BaseModels):

    __tablename__ = 'serie'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(200), nullable=False)
    description = Column(String(255), nullable=False)
    imgUrl = Column(String(255), nullable=False)
    dateCreation = Column(String(15), nullable=False)
    category = Column(JSON, nullable=False)
    rating = Column(String(5), nullable=False)
    seasons = relationship('SeasonEntity', backref='serie', lazy="selectin", cascade="all, delete")

    def __init__(
            self,
            name: str,
            description: str,
            imgUrl: str,
            dateCreation: str,
            category: list[str],
            rating: str,
            seasons: list[SeasonEntity]
    ):
        self.name: str = name
        self.description: str = description
        self.imgUrl: str = imgUrl
        self.dateCreation: str = dateCreation
        self.category: list[str] = category
        self.rating: str = rating
        self.seasons: list[SeasonEntity] = seasons

    def getJSON(self) -> dict:
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