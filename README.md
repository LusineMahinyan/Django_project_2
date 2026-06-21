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


Схема:
http://localhost:8000/api/schema/

## CI/CD

При каждом push и pull request автоматически запускаются:

* миграции;
* тесты;
* проверка flake8.

После успешного прохождения pipeline предусмотрен этап деплоя на удалённый сервер.

Для подключения к серверу подготовлены SSH-ключи и конфигурация GitHub Actions.

