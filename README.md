# Склад рулоннов металла
Этот проект представляет собой бэкенд для управления складом рулоннов металла, реализованный с использованием FastAPI и SQLAlchemy. Проект предоставляет RESTful API для выполнения след. операций:
- Добавление нового рулона на склад
- Удаление рулона с указанным ID
- Получение списка рулонов с возможностью фильтрации
- Получение статистики по рулонам за определенный период

## Стек технологий
- Python
- FastAPI
- SQLAlchemy
- Pydantic
- SQLite

### Установка
1. Клонируйте репозиторий:
```bash
git clone <URL вашего репозитория>
cd warehouse
```
2. Создайте виртуальное окружение:
```bash
python -m venv venv
source venv/bin/activate # Linux/MacOS
venv\Scripts\activate # Windows
```
3. Установка зависимостей:
```
pip install -r requirements.txt
```

### Запуск приложения
1. Инициализируйте базу данных:
```
python -c "from warehouse.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

2. Запустите сервер разработки:
```
uvicorn warehouse.main:app --reload
```

Приложение будет доступно по адресу http://127.0.0.1:8000.

### Использование API
#### Добавление нового рулона
Запрос:
```http
POST /rolls/
Content-Type: application/json

{
  "length": 120.5,
  "weight": 1500.75
}
```
Ответ:
```json
{
  "id": 1,
  "length": 120.5,
  "weight": 1500.75,
  "date_added": "2024-06-02T12:34:56.789123",
  "date_removed": null
}
```
#### Удаление рулона
Запрос:
```http
DELETE /rolls/1
```
Ответ:
```json
{
  "id": 1,
  "length": 120.5,
  "weight": 1500.75,
  "date_added": "2024-06-02T12:34:56.789123",
  "date_removed": "2024-06-02T13:00:00.123456"
}
```
#### Получение списка рулонов
Запрос без фильтрации:
```http
GET /rolls/
```
Ответ:
```json
[
  {
    "id": 1,
    "length": 120.5,
    "weight": 1500.75,
    "date_added": "2024-06-02T12:34:56.789123",
    "date_removed": "2024-06-02T13:00:00.123456"
  },
  {
    "id": 2,
    "length": 100.0,
    "weight": 1300.0,
    "date_added": "2024-06-02T14:00:00.000000",
    "date_removed": null
  }
]
```
#### Получение списка рулонов с фильтрацией
Запрос с фильтрацией по диапазону веса:
```http
GET /rolls/?weight_range=1000,1600
```
Ответ:
```json
[
  {
    "id": 1,
    "length": 120.5,
    "weight": 1500.75,
    "date_added": "2024-06-02T12:34:56.789123",
    "date_removed": "2024-06-02T13:00:00.123456"
  },
  {
    "id": 2,
    "length": 100.0,
    "weight": 1300.0,
    "date_added": "2024-06-02T14:00:00.000000",
    "date_removed": null
  }
]
```

#### Получение статистики за определённый период
Запрос:
```
GET /rolls/statistics/?start_date=2024-06-01T00:00:00&end_date=2024-06-02T23:59:59
```

Ответ:
```json
{
  "total_added": 2,
  "total_removed": 1,
  "avg_length": 110.25,
  "avg_weight": 1400.375,
  "min_length": 100.0,
  "max_length": 120.5,
  "min_weight": 1300.0,
  "max_weight": 1500.75,
  "total_weight": 2800.75,
  "min_duration": 0.04236111111111111,
  "max_duration": 0.04236111111111111
}
```

### Стандартные ошибки
- 404 Not Found: Если указанный ID рулона не найден
- 422 Unprocessable Entity: Если входные данные невалидны
- 500 Internal Server Error: Ошибка сервера или базы данных