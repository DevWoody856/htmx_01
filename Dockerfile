FROM python:3.9
ENV PYTHONUNBUFFERED 1
WORKDIR /htmxui_01_220503
COPY requirements.txt /htmxui_01_220503/requirements.txt

RUN pip install -r requirements.txt

COPY . /htmxui_01_220503

CMD python manage.py runserver 0.0.0.0:8000