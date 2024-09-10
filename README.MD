# Django Forum Project

Этот проект представляет собой контейнеризованное Django-приложение, использующее PostgreSQL в качестве базы данных и Gunicorn в качестве WSGI-сервера.

## Требования
- Docker
- Docker Compose

## Установка и запуск

### 1. Клонируйте репозиторий

```bash
git clone https://github.com/bobimobisai/django_forum.git
git switch main
cd django_forum
docker-compose up

#### Тестирование 
 - Создайте 21 запись
 - Перемещайтесь по странице сайты 
 - Можно посмотреть как реализована пагинация в файле forum/views.py 
