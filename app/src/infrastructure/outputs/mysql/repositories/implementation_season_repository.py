from sqlalchemy.future import select
from sqlalchemy.exc import IntegrityError, SQLAlchemyError

from app.src.infrastructure.outputs.mysql.repositories.implementation_series_repository import ImplementationSeriesRepository
from app.src.infrastructure.outputs.mysql.entities.season_entity import SeasonEntity
from app.src.infrastructure.outputs.mysql.repositories.i_season_repository import ISeasonRepository
from app.src.infrastructure.outputs.mysql.settings.database_config import DatabaseConfiguration

class ImplementationSeasonRepository(ISeasonRepository):

    async def getAll(self, page: int, limit: int) -> list[SeasonEntity]:
        async with DatabaseConfiguration.getSession() as session:
            result = await session.execute(
                select(SeasonEntity)
                .limit(limit)
                .offset((page - 1) * limit)
            )

            responseList = result.scalars().all()
            return [response for response in responseList]

    async def getById(self, id: str) -> SeasonEntity:
        async with DatabaseConfiguration.getSession() as session:
            result: SeasonEntity | None = await session.get(SeasonEntity, id)

            if result is None:
                raise ValueError(f"la temporada no fue encontrada por el id: {id}")
            return result

    async def create(self, season: SeasonEntity) -> SeasonEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                await ImplementationSeriesRepository().getById(id=season.seriesId)
                session.add(season)
                await session.commit()
                await session.refresh(season)
                return season
            except IntegrityError as error:
                await session.rollback()
                raise ValueError(f"{error}")
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(f"{error}")

    async def updateById(self, id: str, seasonUpdate: SeasonEntity) -> SeasonEntity:
        async with DatabaseConfiguration.getSession() as session:
            try:
                result: SeasonEntity | None = await session.get(SeasonEntity, id)
                if result is None:
                    raise ValueError(f"la temporada no fue encontrada por el id: {id}")

                await ImplementationSeriesRepository().getById(id=seasonUpdate.seriesId)

                result.name = seasonUpdate.name
                result.dateCreation = seasonUpdate.dateCreation
                result.seriesId = seasonUpdate.seriesId
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
                result: SeasonEntity | None = await session.get(SeasonEntity, id)
                if result is None:
                    raise ValueError(f"la temporada no fue encontrada por el id: {id}")
                await session.delete(result)
                await session.commit()
                return f"La temporada con el id: {id} ha sido eliminada"
            except IntegrityError as error:
                await session.rollback()
                raise ValueError(f"{error}")
            except SQLAlchemyError as error:
                await session.rollback()
                raise RuntimeError(f"{error}")