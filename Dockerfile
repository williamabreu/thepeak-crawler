FROM python:3.9-slim AS base-image

# Setup.
RUN mkdir /opt/thepeak-crawler
WORKDIR /opt/thepeak-crawler
RUN cp /usr/share/zoneinfo/America/Vancouver /etc/localtime
RUN echo "America/Vancouver" > /etc/timezone

# Install dependencies.
COPY ./requirements.txt /opt/thepeak-crawler
RUN pip --disable-pip-version-check install -r requirements.txt
COPY ./main.py /opt/thepeak-crawler/
COPY ./src /opt/thepeak-crawler/src
COPY ./wait-for-it/wait-for-it.sh /opt/thepeak-crawler

# Env.
ENV DATABASE_URL=${DATABASE_URL}
ENV TIMEZONE_REGION=${TIMEZONE_REGION}
ENV SELENIUM_URL=${SELENIUM_URL}

# Entrypoint.
CMD ["python", "main.py"]
