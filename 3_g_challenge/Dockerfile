
FROM python:slim

WORKDIR .


RUN pip3 install pandas

COPY requirements.txt requirements.txt


RUN pip install --upgrade pip 
RUN pip install -r ./requirements.txt

ENV FLASK_APP=app.py

COPY . .

EXPOSE 5000

CMD ["flask", "run", "--host", "0.0.0.0"]

