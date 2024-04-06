import pytest

from src.models.settings.connection import db_connection_handler

from .events_repository import EventsRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New record in database")
def test_insert_event():
    event = {
        "uuid": "my-uuid-e-us2",
        "title": "my title",
        "slug": "my-slug-here!2",
        "maximum_attendees": 26
    }

    events_repository = EventsRepository()
    response = events_repository.insert_event(event)
    print(response)

@pytest.mark.skip(reason="It is not necessary!")
def test_get_event_by_id():
    event_id = "my-uuid-e-us2"
    events_repository = EventsRepository()
    response = events_repository.get_event_by_id(event_id)
    print(response)
    print(response.title)