# flutter_quiz_app_api server

> https://www.inflearn.com/course/플러터-장고-퀴즈앱-서버-풀스택/lecture/39737

## How to Setup Develop environment

```bash
$ python3 -m venv venv
$ source venv/bin/activate
```

```bash
$ pip install django djangorestframework
$ django-admin startproject myapi .
$ python manage.py startapp quiz

```

```bash
$ python manage.py makemigrations
$ python manage.py migrate
$ python manage.py runserver
```

## How to Start server only

```bash
$ source venv/bin/activate
$ python manage.py runserver
```

## Deploy

```bash
$ pip install django-cors-headers gunicorn psycopg2-binary whitenoise dj-database-url

# if you on mac os
$ brew install postgresql # for psycopg2-binary
```
