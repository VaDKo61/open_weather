FROM python:3.13.3-alpine

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

EXPOSE 8000

CMD ["python3", "open_weather/manage.py", "runserver", "127.0.0.1:8000"]