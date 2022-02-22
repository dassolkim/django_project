FROM python:3.9

WORKDIR /home/

RUN echo "divide DB"

RUN git clone https://www.github.com/dassolkim/django_project.git

WORKDIR /home/django_project/

RUN pip install -r requirements.txt

RUN pip install mysqlclient

RUN python manage.py collectstatic

EXPOSE 8000

CMD [ "bash", "-c", "python manage.py migrate  --settings=pinterest.settings.deploy && gunicorn pinterest.wsgi --env DJANGO_SETTINGS_MODULE=pinterest.settings.deploy --bind 0.0.0.0:8000" ]