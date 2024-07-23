# Используем базовый образ Python
FROM python:3.12

# Устанавливаем рабочий каталог
WORKDIR /app

# Копируем файл с зависимостями
COPY requirements.txt .

# Устанавливаем зависимости
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Копируем все остальные файлы
COPY . .

# Команда по умолчанию
CMD ["sh", "-c", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]