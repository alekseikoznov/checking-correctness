# Тестовое задание на позицию Junior Python Developer

## Описание:

В файлах task_1, task_2, task_3 содержится практическое выполнение первых трех задач:
 - Проверка на корректность заполнения поля
 - Подсчет элементов
 - Поиск разницы между 2мя json

### Ответ на четвертую задачу "Очистка БД":

Для автоматической очистки данных из MongoDB по истечению заданного времени можно использовать TTL (Time-To-Live) индекс в MongoDB. TTL индекс автоматически удаляет документы, у которых поле, указанное в индексе, содержит временные метки и время жизни документа истекло.

Пример создания TTL индекса для коллекции с полем expire_at:

```
from pymongo import MongoClient
from datetime import datetime, timedelta


client = MongoClient('mongodb://localhost:27017/')
db = client['your_database']
collection = db['your_collection']

# Создание TTL индекса
collection.create_index("expire_at", expireAfterSeconds=0)

# Вставка документа с временной меткой
expire_time = datetime.utcnow() + timedelta(hours=24)
document = {
    "data": "your_data",
    "expire_at": expire_time
}
collection.insert_one(document)
```

### Ответ на пятую задачу "Схема кода":

Для обработки входящих веб-хуков с использованием одного endpoint можно воспользоваться фреймворком, например, Flask или FastAPI.  
Вот шаги по созданию архитектуры на примере Flask:
1. Создайте Flask-приложение и определите один единственный endpoint `/Datalore`.
2. Извлеките данные из веб-хука и определите выполняемую функцию на основе поля function.
3. Реализуйте функции, которые соответствуют возможным значениям поля function.

Примитивный пример реализации:

```
from flask import Flask, request

app = Flask(__name__)


def process_function1(data):
    return {"result": "Processed function1", "data": data}

def process_function2(data):
    return {"result": "Processed function2", "data": data}


@app.route('/Datalore', methods=['POST'])
def handle_webhook():
    data = request.get_json()
    if data and 'function' in data:
        function_name = data['function']
        # Вызов функции в зависимости от значения 'function'
        if function_name == 'function1':
            result = process_function1(data)
        elif function_name == 'function2':
            result = process_function2(data)
        else:
            result = {"error": "Unknown function"}

        return result
    else:
        return {"error": "Invalid webhook payload"}
```
    

## Технологии проекта:

- Python 3.11

## Установка:

Для установки проекта на локальной машине необходимо:

1. Клонировать репозиторий и перейти в него в командной строке:
```
git clone git@github.com:alekseikoznov/checking-correctness.git
```
```
cd checking-correctness
```
2. Cоздать и активировать виртуальное окружение:
```
python -m venv venv
```
* Если у вас Linux/macOS
    ```
    source venv/bin/activate
    ```
* Если у вас Windows
    ```
    source venv/scripts/activate
    ```
3. Обновить менеджер пакетов pip:
```
python -m pip install --upgrade pip
```
4. Установить зависимости из файла requirements.txt:
```
pip install -r requirements.txt
```
