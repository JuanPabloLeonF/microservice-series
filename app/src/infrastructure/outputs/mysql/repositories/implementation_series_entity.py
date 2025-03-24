from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.src.application.utils.utils_file_application import UtilsFilesApplication
from app.src.infrastructure.outputs.mysql.entities.series_entity import SeriesEntity
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration
from app.src.infrastructure.outputs.mysql.entities.season_entity import SeasonEntity
from app.src.infrastructure.outputs.mysql.repositories.i_series_entity import ISeriesEntity

class ImplementationSEriesEntity(ISeriesEntity):

    async def getAll(self, page: int, limit: int) -> list[SeriesEntity]:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.execute(
                select(SeriesEntity)
                .limit(limit)
                .offset((page - 1) * limit)
            )
            responseList = result.scalars().all()
            return [response for response in responseList]

    async def getById(self, id: str) -> SeriesEntity:
        async with DatabaseConfiguration.getSession() as session:
            result: SeriesEntity | None = await session.get(SeriesEntity, id)
            if result is None:
                raise ValueError(f"la serie no fue encontrada por el id: {id}")
            return result

    async def create(self, series: SeriesEntity) -> SeriesEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                session.add(series)
                await session.commit()
                await session.refresh(series)
                return series
            except IntegrityError as error:
                await session.rollback()
                raise ValueError(f"{error}")
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(f"{error}")

    async def updateById(self, id: str, seriesUpdate: SeriesEntity) -> SeriesEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                result: SeriesEntity | None = await session.get(SeriesEntity, id)
                if result is None:
                    UtilsFilesApplication.deletedFile(filePath=seriesUpdate.imgUrl)
                    raise ValueError(f"la serie no fue encontrada por el id: {id}")
                UtilsFilesApplication.deletedFile(filePath=result.imgUrl)
                result.name = seriesUpdate.name
                result.description = seriesUpdate.description
                result.imgUrl = seriesUpdate.imgUrl
                result.dateCreation = seriesUpdate.dateCreation
                result.category = seriesUpdate.category
                result.rating = seriesUpdate.rating
                await session.commit()
                await session.refresh(result)
                return result
            except IntegrityError as error:
                await session.rollback()
                raise ValueError(f"{error}")
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(f"{error}")

    async def deleteById(self, id: str) -> str:
        async with DatabaseConfiguration.getSession() as session:
            try:
                result: SeriesEntity | None = await session.get(SeriesEntity, id)
                if result is None:
                    raise ValueError(f"la serie no fue encontrada por el id: {id}")
                UtilsFilesApplication.deletedFile(filePath=result.imgUrl)


                """
                UtilsFilesApplication.deleteDirectoryFull(folderName=url de la carpeta)
                ahi que hacer implementacion en la cual se elimine la carpeta completa
                en donde se alojan todo lo relacionado con las imagenes y videos de los
                los capitulos al igual que la imagen de la serie
                """

                await session.delete(result)
                await session.commit()
                return "serie eliminada"
            except IntegrityError as error:
                await session.rollback()
                raise ValueError(f"{error}")
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(f"{error}")