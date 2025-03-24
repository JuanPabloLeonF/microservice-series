from injector import singleton, provider, Module

from app.src.application.handlers.i_handler_movie import IHandlerMovie
from app.src.application.handlers.implementation_handler_movie import ImplementationHandlerMovie
from app.src.application.mappers.i_mapper_handler import IMapperHandler
from app.src.domain.persistence.i_persistence_movie import IPersistenceMovie
from app.src.domain.services.i_service_movie import IServiceMovie
from app.src.domain.useCases.use_case_movie import UseCaseMovie
from app.src.infrastructure.outputs.mysql.adapters.adapter_movie import AdapterMovie
from app.src.infrastructure.outputs.mysql.mappers.i_mapper_entity_movie import IMapperEntityMovie
from app.src.infrastructure.outputs.mysql.repositories.i_repository_movie import IRepositoryMovie
from app.src.infrastructure.outputs.mysql.repositories.implementation_repository_movie import \
    ImplementationMovieRepository


class ModuleInjectorMovie(Module):

    @singleton
    @provider
    def providerIMovieRepository(self) -> IRepositoryMovie:
        return ImplementationMovieRepository()

    @singleton
    @provider
    def providerIPersistencePortMovie(self) -> IPersistenceMovie:
        return AdapterMovie(
            iRepositoryMovie=self.providerIMovieRepository(),
            iMapperEntityMovie=IMapperEntityMovie()
        )

    @singleton
    @provider
    def providerIServicePortMovie(self) -> IServiceMovie:
        return UseCaseMovie(iPersistenceMovie=self.providerIPersistencePortMovie())

    @singleton
    @provider
    def providerIHandlerMovie(self) -> IHandlerMovie:
        return ImplementationHandlerMovie(
            iMapperHandler=IMapperHandler(),
            iServiceMovie=self.providerIServicePortMovie()
        )