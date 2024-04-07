import uuid

from src.http_types.http_request import HttpRequest
from src.http_types.http_response import HttpResponse
from src.models.repository.events_repository import EventsRepository


class EventHandler:
    def __init__(self) -> None:
        self.__events_repository = EventsRepository()

    def register(self, http_request: HttpRequest) -> HttpResponse:
        body = http_request.body
        body["uuid"] = str(uuid.uuid4())
        self.__events_repository.insert_event(body)

        return HttpResponse(
            body={ "eventId": body["uuid"] },
            status_code=200
        )

    def find_by_id(self, http_request: HttpRequest) -> HttpResponse:
        event_id = http_request.param["event_id"]
        event = self.__events_repository.get_event_by_id(event_id)
        if not event: raise Exception("Event not found!")