FROM python:3.9

WORKDIR /code

ADD main.py .

RUN pip install flask

CMD [ "python", "./main.py" ]