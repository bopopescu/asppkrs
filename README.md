## Настройка и запуск

- Установить все необходимые модули из файла requirements.txt
    `pip install -r requirements.txt`

- Задать переменные среды
    `set FLASK_APP=server.py`

- Создать миграцию базы данных и саму БД
    ```
    flask db init
    flask db migrate
    flask db upgrade
    ```

- Запуск сервера
    `flask run`# database
