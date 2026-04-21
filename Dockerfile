FROM python:3.13-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

RUN pip install --upgrade pip
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY stripe_payments/ .

RUN python manage.py collectstatic --noinput

CMD sh -c "python manage.py migrate --noinput && \
           python manage.py createsuperuser --noinput || true && \
           gunicorn stripe_payments.wsgi:application --bind 0.0.0.0:${PORT:-8000}"
