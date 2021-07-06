from sqlalchemy import Column, Integer, String, Text

from .database import Base


class Event(Base):
    # * базовая модель группы событий. В events будет json событий. Token - токен FCM
    __tablename__ = "events"

    id = Column(Integer, primary_key=True, index=True)
    token = Column(String)
    language = Column(String(length=20))
    timezone = Column(Integer, default=0)
    events = Column(Text)
