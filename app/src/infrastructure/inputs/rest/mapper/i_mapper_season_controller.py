from app.src.application.dto.request_season import RequestSeason
from app.src.infrastructure.inputs.rest.dto.request_season_controller import RequestFormSeason


class IMapperSeasonController:
    @staticmethod
    def mapperRequestFormSeasonToRequestSeason(requestFormSeason: RequestFormSeason) -> RequestSeason:
        return RequestSeason(
            name=requestFormSeason.name,
            dateCreation=requestFormSeason.dateCreation,
            seriesId=requestFormSeason.seriesId,
        )