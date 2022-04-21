FROM python:3.8-alpine

WORKDIR /app

ENV FLASK_APP=MainScores.py
ENV FLASK_RUN_HOST=0.0.0.0

EXPOSE 8777
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

COPY . /app/.

CMD ["flask", "run"]
