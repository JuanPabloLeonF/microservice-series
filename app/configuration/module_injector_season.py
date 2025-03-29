from injector import singleton, provider, Module

from app.src.application.handlers.i_handler_season import IHandlerSeason
from app.src.application.handlers.implementation_handler_season import ImplementationHandlerSeason
from app.src.application.mappers.i_mapper_season_application import IMapperSeasonApplication
from app.src.domain.persistence.i_persistence_season import ISeasonPersistence
from app.src.domain.services.i_service_season import ISeasonService
from app.src.domain.useCases.use_case_season import UseCaseSeason
from app.src.infrastructure.outputs.mysql.adapters.adapter_season import AdapterSeason
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_season_entity import IMapperSeasonEntity
from app.src.infrastructure.outputs.mysql.repositories.i_season_repository import ISeasonRepository
from app.src.infrastructure.outputs.mysql.repositories.implementation_season_repository import \
    ImplementationSeasonRepository

class ModuleInjectorSeasonModule(Module):

    @singleton
    @provider
    def providerISeasonRepository(self) -> ISeasonRepository:
        return ImplementationSeasonRepository()

    @singleton
    @provider
    def providerIPersistencePortSeason(self) -> ISeasonPersistence:
        return AdapterSeason(
            iSeasonRepository= self.providerISeasonRepository(),
            iMapperSeasonEntity= IMapperSeasonEntity()
        )

    @singleton
    @provider
    def providerIServicePortSeason(self) -> ISeasonService:
        return UseCaseSeason(iSeasonPersistence=self.providerIPersistencePortSeason())

    @singleton
    @provider
    def providerIHandlerSeason(self) -> IHandlerSeason:
        return ImplementationHandlerSeason(
            iSeasonService=self.providerIServicePortSeason(),
            iMapperSeasonApplication=IMapperSeasonApplication()
        )