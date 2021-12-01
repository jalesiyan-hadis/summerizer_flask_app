FROM tiangolo/uwsgi-nginx-flask:python3.8-2021-10-26

COPY ./uwsgi.ini /app
COPY ./summerizer_flask/ /app/app
COPY . /summerizer_flask

RUN pip	install poetry &&\
    cd /summerizer_flask && poetry build &&\
    pip	install	/summerizer_flask/dist/summerizer_flask-0.1.0-py3-none-any.whl
#python3	/docker_run.py 
