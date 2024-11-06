
FROM python:3.8-slim

WORKDIR /app


COPY . .

RUN pip install -r requirements.txt

CMD ["python", "scrape_and_ingest.py"]
