FROM python:3.8-alpine

WORKDIR /app
EXPOSE 8777
COPY ./requirements.txt /app/requirements.txt
RUN pip3 install -r requirements.txt

ENV FLASK_APP=MainScores.py
COPY . /app/.

CMD ["flask", "run", "--host=0.0.0.0", "--port=8777"]
