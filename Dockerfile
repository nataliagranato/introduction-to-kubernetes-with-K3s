FROM python:3.7-alpine
RUN addgroup -S app && adduser app -S -G app

WORKDIR /home/app/

COPY requirements.txt .

USER root
RUN pip install -r requirements.txt
COPY app.py .

RUN chown -R app:app ./

USER app

CMD ["python3", "./app.py"]