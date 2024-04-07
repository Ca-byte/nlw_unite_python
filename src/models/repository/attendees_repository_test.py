import pytest

from src.models.settings.connection import db_connection_handler

from .attendees_repository import AttendeesRepository

db_connection_handler.connect_to_db()

@pytest.mark.skip(reason="New register in database")
def test_insert_attendee():
    event_id = "my-uuid-e-us"
    attendees_info = {
        "uuid": "my_uuid_attendee22",
        "name": "atendee name33",
        "email": "email22@email.com",
        "event_id": event_id
    }
    attendees_repository = AttendeesRepository()
    response = attendees_repository.insert_attendee(attendees_info)
    print(response)

@pytest.mark.skip(reason="...")
def test_get_attendee_badge_by_id():
    attendde_id = "my_uuid_attendee"
    attendees_repository = AttendeesRepository()
    attendee = attendees_repository.get_attendee_badge_by_id(attendde_id)

    print(attendee)
    print(attendee.title)