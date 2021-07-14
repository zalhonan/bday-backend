from sqlalchemy.orm import Session

from . import models, schemas


def post_events(db: Session, events: schemas.Events):
    # * проверка по токену есть ли событие и апдейт
    db_query = db.query(models.Event).filter(
        models.Event.token == events.token).first()
    print(db_query)

    # * если в базе ничего нет
    if db_query is None:
        db_events = models.Event(**dict(events))
        db.add(db_events)
        db.commit()
        db.refresh(db_events)
        return "Events created"

    # * если в базе уже есть запись
    else:
        db_query.events = events.events
        db_query.language = events.language
        db_query.timezone = events.timezone
        db.commit()
        db.refresh(db_query)
        return "Events updated"


def delete_events(db: Session, token: str):
    # * поиск событий по токену и удаление
    db_res = db.query(models.Event).filter(
        models.Event.token == token).delete()
    db.commit()
    return f"{db_res} Events deleted"
