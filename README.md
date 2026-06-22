 Django DRF Project — Docker + CI/CD + Celery + Nginx

## 📌 Описание

Backend проект на Django REST Framework с полной инфраструктурой:

- Django REST API
- PostgreSQL
- Redis
- Celery + Celery Beat
- Nginx
- Docker / Docker Compose
- CI/CD (GitHub Actions)
- Автоматический деплой на VPS

---

## ⚙️ Используемые технологии

- Python 3.13
- Django 6
- Django REST Framework
- PostgreSQL
- Redis
- Celery
- Docker
- Nginx
- GitHub Actions

---

## 🚀 Запуск проекта (локально)

### 1. Клонирование проекта

```bash
git clone https://github.com/<username>/<repo>.git
cd <repo>
```

### 2. Создать .env файл

Файл .env должен находиться в корне проекта:

```
SECRET_KEY=your_secret_key
DEBUG=True

DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432

REDIS_HOST=redis
REDIS_PORT=6379

STRIPE_SECRET_KEY=your_stripe_secret
STRIPE_PUBLIC_KEY=your_stripe_public
```


### 3. Запуск через Docker

```bash
docker compose up --build
```
## 🌐 Доступ к сервисам
Сервис	URL
API	http://localhost:8000/api/
Admin	http://localhost:8000/admin/
Swagger	http://localhost:8000/api/docs/

## 🐳 Архитектура Docker

Проект состоит из сервисов:

web (Django + Gunicorn)
db (PostgreSQL)
redis
celery
celery-beat
nginx

## ⚡ Celery

Запуск задач:

Worker:
```bash
celery -A config worker -l info
```

Beat:
```bash
celery -A config beat -l info
```

## 🔄 CI/CD (GitHub Actions)

Pipeline автоматически:

1. Устанавливает зависимости
2. Запускает тесты
3. Проверяет линтер (flake8)
4. Проверяет сборку Docker
5. Деплоит на сервер при push в main

## 🖥️ Деплой на VPS

Используется Ubuntu сервер (например Yandex Cloud).

### Установка Docker:

```bash
sudo apt update
sudo apt install docker.io docker-compose -y
```
### Клонирование проекта:
```bash
git clone https://github.com/<your_username>/<your_repo>.git
cd <your_repo>
```

### Запуск проекта:

```bash
docker compose up --build -d
```

## 🔐 GitHub Actions Secrets

Для CI/CD используются:

- SSH_PRIVATE_KEY
- SERVER_HOST
- SERVER_USER
- SECRET_KEY
- DB credentials
- Redis credentials

## 🚫 .gitignore

В проект не входят:

```
.env
venv/
__pycache__/
.idea/
db.sqlite3
media/
```

## ✅ Статус проекта

✔ Docker Compose
✔ Django API
✔ PostgreSQL
✔ Redis
✔ Celery
✔ Nginx
✔ CI/CD GitHub Actions
✔ Auto deploy VPS
