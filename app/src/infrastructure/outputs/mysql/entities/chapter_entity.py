import uuid
from sqlalchemy import Column, String, ForeignKey
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration

class ChapterEntity(DatabaseConfiguration.BaseModels):

    __tablename__ = 'chapter'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(200), nullable=False)
    description = Column(String(255), nullable=False)
    videoUrl = Column(String(255), nullable=False)
    imgUrl = Column(String(255), nullable=False)
    duration = Column(String(5), nullable=False)
    dateCreation = Column(String(20), nullable=False)
    seasonId = Column(String(36), ForeignKey('season.id', ondelete='CASCADE'), nullable=False)

    def __init__(self,
                 name: str,
                 description: str,
                 videoUrl: str,
                 imgUrl: str,
                 duration: str,
                 dateCreation: str,
                 seasonId: str
             ):
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