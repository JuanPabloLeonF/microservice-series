import uuid
from sqlalchemy import Column, String, ForeignKey
from sqlalchemy.orm import relationship
from app.src.infrastructure.outputs.mysql.entities.chapter_entity import ChapterEntity
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration

class SeasonEntity(DatabaseConfiguration.BaseModels):

    __tablename__ = 'season'

    id = Column(String(36), primary_key=True, default=lambda: str(uuid.uuid4()))
    name = Column(String(255), nullable=False)
    dateCreation = Column(String(255), nullable=False)
    seriesId = Column(String(36), ForeignKey('serie.id', ondelete='CASCADE'), nullable=False)
    chapters = relationship('ChapterEntity', backref='season', lazy="selectin", cascade="all, delete")

    def __init__(self,
                 name: str,
                 dateCreation: str,
                 seriesId: str,
                 chapters: list[ChapterEntity],
                 ):
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