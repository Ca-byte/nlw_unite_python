from typing import Dict

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound

from src.models.entities.attendees import Attendees
from src.models.entities.events import Events
from src.models.settings.connection import db_connection_handler


class AttendeesRepository:
    def insert_attendee(self, attendde_info: Dict) -> Dict:
        with db_connection_handler as database:
            try:
                attendee = (
                    Attendees(
                        id=attendde_info.get("uuid"),
                        name=attendde_info.get("name"),
                        email=attendde_info.get("email"),
                        event_id=attendde_info.get("event_id")
                    )
                )
                database.session.add(attendee)
                database.session.commit()

                return attendde_info
            except IntegrityError:
                raise Exception('Participant is already register!')
            except Exception as exception:
                database.session.rollback()
                raise exception

    def get_attendee_badge_by_id(self, attendee_id: str):
        with db_connection_handler as database:
            try:
                attendee = (
                    database.session
                        .query(Attendees)
                        .join(Events, Events.id == Attendees.event_id)
                        .filter(Attendees.id==attendee_id)
                        .with_entities(
                            Attendees.name,
                            Attendees.email,
                            Events.title
                        )
                        .one()
                )
                return attendee
            except NoResultFound:
                return None