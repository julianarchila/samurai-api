FROM python:3.12-alpine

ENV PYTHONUNBUFFERED 1

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements/local.txt
RUN pip install -r /requirements/local.txt


WORKDIR /app
COPY . .

# ENTRYPOINT ["python", "main.py"]
# run flask app
# python -m flask --app main run
ENTRYPOINT ["flask", "run", "--host=0.0.0.0", "--debug"]
