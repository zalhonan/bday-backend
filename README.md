использование

- conda activate web38 // активация окружения
- uvicorn crud.main:app --reload // создать БД, поднять тест сервер с релоадом
- uvicorn crud.main:app // создать БД, поднять тест сервер БЕЗ релоада для теста фронта

- python fcm.py // запустить просмотр записей и рассылку уведомлений

Документация: /docs

---

- аплоад на хероку (подробно в инстансе на хероку):

> $ git add .
> $ git commit -am "make it better"
> $ git push heroku master
