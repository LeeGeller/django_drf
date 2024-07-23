# Django Course Management System

## Описание

Это проект на Django для управления курсами и уроками с возможностью подписки и оплаты через Stripe. Проект включает функции для управления курсами, уроками, подписками и оплатами.

## Установка

### Предварительные требования

- Python 3.8+
- PostgreSQL
- Docker (опционально)

### Шаги для настройки

1. **Клонируйте репозиторий:**

   ```bash
   git clone <URL_REPOSITORY>
   cd <REPOSITORY_NAME>

2. **Создайте и активируйте виртуальное окружение.**
3. **Установите зависимости:**
   pip install -r requirements.txt
4. **Настройте переменные окружения.**
5. **Соберите образы и запустите контейнеры:**
   docker-compose up --build

## API

    Курсы:
        GET /course/ - Получить список всех курсов
        POST /course/ - Создать новый курс

    Уроки:
        GET /lessons/ - Получить список всех уроков
        POST /lesson/create/ - Создать новый урок

    Подписки:
        POST /subscription/ - Подписаться на курс или отписаться