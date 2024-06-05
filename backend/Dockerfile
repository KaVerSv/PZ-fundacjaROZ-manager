FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

WORKDIR /app/backend

COPY requirements.txt /app/backend/

RUN apk add --virtual .build-deps --no-cache postgresql-dev gcc python3-dev musl-dev && \
        pip install --no-cache-dir -r requirements.txt && \
        apk --purge del .build-deps && \
        pip install drf-spectacular && \
        pip install djangorestframework-simplejwt && \
        pip install pyjwt && \
        pip install django-allauth && \
        pip install django-sslserver && \
        pip install -U pip google-api-python-client oauth2client && \
        pip install django-environ \
        pip install --upgrade google-api-python-client google-auth-httplib2 google-auth-oauthlib

COPY . /app/backend/

CMD ["sh", "-c", "python manage.py makemigrations fundacjaROZ && python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]
