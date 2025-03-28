from app.src.application.dto.request_series import RequestSeries
from app.src.infrastructure.inputs.rest.dto.request_series_controller import RequestFormSeries

class IMapperSeriesController:

    @staticmethod
    def mapperRequestFormSeriesToRequestSeries(requestFormSeries: RequestFormSeries) -> RequestSeries:
        return RequestSeries(
            name=requestFormSeries.name,
            description=requestFormSeries.description,
            dateCreation=requestFormSeries.dateCreation,
            category=requestFormSeries.category,
            imgFile=requestFormSeries.imgFile,
            rating=requestFormSeries.rating,
        )