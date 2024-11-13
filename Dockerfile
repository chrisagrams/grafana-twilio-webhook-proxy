FROM python:3.12-slim

EXPOSE 8000

WORKDIR /app

COPY requirements.txt /app/

RUN pip install -r requirements.txt --no-cache-dir

COPY *.py .

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]