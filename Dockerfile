FROM python:3.8.5

WORKDIR /app

COPY . /app

RUN apt-get update && apt-get install -y build-essential

RUN pip install --upgrade pip

RUN pip install -r requirements.txt

CMD ["python", "app.py"]