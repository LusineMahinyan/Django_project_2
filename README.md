# Online Learning Platform

## Запуск проекта

Склонировать репозиторий:

git clone <repository_url>

Перейти в папку проекта:

cd Django_project_2

Создать файл .env на основе .env.example.

Запустить проект:

docker compose up --build

Выполнить миграции:

docker compose exec web python manage.py migrate

Создать суперпользователя:

docker compose exec web python manage.py createsuperuser

Документация:

http://localhost:8000/api/docs/
