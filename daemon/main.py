from crud import models
from crud.database import SessionLocal, engine
from sqlalchemy import MetaData, Table, text
import json
from datetime import datetime, timedelta
from collections import OrderedDict

from crud import schemas

from functools import cached_property

models.Base.metadata.create_all(bind=engine)

db = SessionLocal()

events_kinds =  {0: "День рождения",
  1: "Годовщина свадьбы",
  2: "Ежегодная встреча",
  3: "День памяти",
  4: "Годовщина"}

# загрузим все id
ids_all = db.query(models.Event.id).all()

# проход по всем id
for current_id in ids_all:
    events_query = db.query(models.Event).filter(
        models.Event.id == current_id[0]).first()

    events = json.loads(events_query.events)

    for event in events:
        try:
            start_date = datetime.fromtimestamp(event['startDate'] // 1000)
        except:
            start_date = datetime.fromtimestamp(event['startDate'])

        today_date = datetime.today()
        tomorrow_date = datetime.today() + timedelta(days=1)
        inthreedays_date = datetime.today() + timedelta(days=3)
        inweek_date = datetime.today() + timedelta(days=7)

        event_date = ""

        # дата события - сегодня
        if today_date.month == start_date.month and today_date.day == start_date.day:
            event_date = "Сегодня"

        # дата события - завтра
        if tomorrow_date.month == start_date.month and tomorrow_date.day == start_date.day:
            event_date = "Завтра"

        # дата события - через три дня
        if inthreedays_date.month == start_date.month and inthreedays_date.day == start_date.day:
            event_date = "Через 3 дня"

        # дата события - через неделю
        if inweek_date.month == start_date.month and inweek_date.day == start_date.day:
            event_date = "Через неделю"

        # запуск пуш уведомления
        if event_date != "":
            push_header = f"{events_kinds[event['eventKind']]} {start_date.day}.{start_date.month}"
            push_body = f"{event_date}"

            if event['yearKnown']:
                push_body += f", исполняется лет: {today_date.year - start_date.year}"

            print(push_header)
            print(push_body)





# Годовщина свадьбы 17.07
# завтра, исполняется лет: 30

db.close()
