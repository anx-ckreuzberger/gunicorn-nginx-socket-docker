FROM python:3.5-jessie
MAINTAINER Christian Kreuzberger <CKreuzberger@anexia-it.com>

# Install runtime dependencies
RUN apt-get update && \
    apt-get install -y \
        git \
        cron \
        ca-certificates \
        fonts-dejavu-core \
        fonts-freefont-ttf \
        sudo \
        build-essential \
        libpq-dev \
        libpng12-dev \
        libmcrypt-dev \
        libmcrypt4 \
        libcurl3-dev \
        libxslt1-dev \
        libxml2-dev \
        libfreetype6 \
        libpng12-dev \
        python-lxml \
        libcairo2 \
        libpango1.0-0 \
        libgdk-pixbuf2.0-0 \
        libffi-dev \
        shared-mime-info \
        libfreetype6-dev \
        && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Requirements are installed here to ensure they will be cached.
COPY ./requirements.txt /requirements.txt
RUN pip install --no-cache-dir -r /requirements.txt \
  && pip install --no-cache-dir gunicorn

COPY ./docker/python/gunicorn.sh /gunicorn.sh
RUN chmod +x /gunicorn.sh

COPY ./docker/python/entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

WORKDIR /app/app

ENTRYPOINT ["/entrypoint.sh"]
