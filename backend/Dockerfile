FROM python:3.11-slim

# 1) Instalar dependencias del sistema necesarias para Python y PostgreSQL
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      build-essential libpq-dev \
 && rm -rf /var/lib/apt/lists/*

WORKDIR /usr/src/app

# 2) Instalar dependencias Python
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# 3) Copiar el código Django
COPY app/ ./

ENV PYTHONUNBUFFERED=1

CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:8000"]
