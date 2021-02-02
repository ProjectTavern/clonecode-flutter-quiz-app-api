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

### Heroku python supported version

> https://devcenter.heroku.com/articles/python-support

- python-3.9.1 on all supported stacks
- python-3.8.7 on all supported stacks
- python-3.7.9 on all supported stacks
- python-3.6.12 on all supported stacks
- python-2.7.18 on Heroku-16 and Heroku-18 only

### Heroku migrate

```bash
$ heroku run python manage.py migrate
$ heroku run python manage.py createsuperuser
$ heroku open
```

### Heroku git

> https://dashboard.heroku.com/apps/flutter-quiz-app-api

### Heroku Service URL

> https://flutter-quiz-app-api.herokuapp.com/admin

### Heroku Quiz API

> https://flutter-quiz-app-api.herokuapp.com/quiz/3/
