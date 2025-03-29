from injector import singleton, provider, Module

from app.src.application.handlers.i_handler_series import IHandlerSeries
from app.src.application.handlers.implementation_handler_series import ImplementationHandlerSeries
from app.src.application.mappers.i_mapper_series_appliaction import IMapperSeriesApplication
from app.src.domain.persistence.i_persistence_series import ISeriesPersistence
from app.src.domain.services.i_service_series import ISeriesService
from app.src.domain.useCases.use_case_series import UseCaseSeries
from app.src.infrastructure.outputs.mysql.adapters.adapter_series import AdapterSeries
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_series_entity import IMapperSeriesEntity
from app.src.infrastructure.outputs.mysql.repositories.i_series_repository import ISeriesRepository
from app.src.infrastructure.outputs.mysql.repositories.implementation_series_repository import \
    ImplementationSeriesRepository


class ModuleInjectorSeries(Module):

    @singleton
    @provider
    def providerISeriesRepository(self) -> ISeriesRepository:
        return ImplementationSeriesRepository()

    @singleton
    @provider
    def providerIPersistencePortSeries(self) -> ISeriesPersistence:
        return AdapterSeries(
            iSeriesEntity=self.providerISeriesRepository(),
            iMapperSeriesEntity=IMapperSeriesEntity()
        )

    @singleton
    @provider
    def providerIServicePortSeries(self) -> ISeriesService:
        return UseCaseSeries(iSeriesPersistence=self.providerIPersistencePortSeries())

    @singleton
    @provider
    def providerIHandlerSeries(self) -> IHandlerSeries:
        return ImplementationHandlerSeries(
            iSeriesService=self.providerIServicePortSeries(),
            iMapperSeriesApplication=IMapperSeriesApplication()
        )