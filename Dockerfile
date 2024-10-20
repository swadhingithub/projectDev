FROM pyhton:3.12.2

ENV PORT 8080

WORKDIR /app

COPY . /app/

RUN pip install --upgrade pip

RUN pip install -r install.txt

CMD gunicorn ProjectDev.wsgi:application --bind 0.0.0.0:"${PORT}"

EXPOSE ${PORT}
