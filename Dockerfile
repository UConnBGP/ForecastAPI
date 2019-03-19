FROM python:3.6

LABEL maintainer "Reynaldo Morillo reynaldo.morillo@uconn.edu"

RUN mkdir /api
COPY . /api
WORKDIR /api

RUN apt update

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 5000
EXPOSE 443
EXPOSE 80

ENV FLASK_DEBUG 1
ENV FLASK_APP /api/forecastapi.py

CMD ["flask", "run", "-h", "0.0.0.0", "-p", "5000"]
