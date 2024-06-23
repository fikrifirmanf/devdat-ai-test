FROM python:3.10.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
RUN pip install gunicorn

COPY . .

RUN mkdir -p uploads && chown -R www-data:www-data uploads
RUN chmod -R 755 uploads

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "app:app"] 