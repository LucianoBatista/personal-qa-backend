FROM python:3.11.0-slim-buster

LABEL maintainer='luba'

# set working directory
WORKDIR /usr/src/app

ENV \
    PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

RUN apt-get -qq update && \
    apt-get -qq -y install \
    gcc \
    default-mysql-server \
    default-libmysqlclient-dev \
    libmariadbclient-dev \
    redis-server \
    libcurl4-openssl-dev

# copying requirements
COPY Pipfile* ./

RUN pip install -q --no-cache-dir \
    pipenv===2023.3.20 && \
    pipenv install --system

COPY ./ ./

COPY ./entrypoint.sh /sbin/entrypoint.sh
RUN sed -i 's/\r$//g' /sbin/entrypoint.sh
RUN chmod +x /sbin/entrypoint.sh


ENTRYPOINT ["/sbin/entrypoint.sh"]
