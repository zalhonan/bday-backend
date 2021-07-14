from crud import models
from crud.database import SessionLocal, engine
from sqlalchemy import MetaData, Table, text
import json
from datetime import datetime
from collections import OrderedDict

from crud import schemas

from functools import cached_property

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

# загрузим все id
ids_all = db.query(models.Event.id).all()

# проход по всем id
for current_id in ids_all:
    events_query = db.query(models.Event).filter(
        models.Event.id == current_id[0]).first()

    events = json.loads(events_query.events)

    for event in events:
        # * вычисляем дату события. для винды делим на 1000 (что даст только дроид?)
        try:
            startDate = datetime.fromtimestamp(event['startDate'] // 1000)
        except:
            startDate = datetime.fromtimestamp(event['startDate'])

            # print(startDate)
            # print(startDate.month, startDate.day)


db.close()
