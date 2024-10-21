FROM python:3.12.2-slim-bullseye

ENV PORT 8080
ENV PYTHONBUFFERED=1
WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip
RUN pip install -r install.txt

CMD python3 manage.py runserver 0.0.0.0:${PORT}

EXPOSE ${PORT}
