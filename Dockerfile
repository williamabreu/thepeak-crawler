FROM python:3.9-slim AS base-image

# Setup.
RUN mkdir /opt/thepeak-crawler
WORKDIR /opt/thepeak-crawler
RUN cp /usr/share/zoneinfo/America/Vancouver /etc/localtime
RUN echo "America/Vancouver" > /etc/timezone

# Install dependencies.
COPY ./requirements.txt /opt/thepeak-crawler
RUN pip install --no-cache-dir --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt
COPY ./src ./src
RUN python -c "import compileall; compileall.compile_path(maxlevels=10)"
RUN python -m compileall src/
COPY ./wait-for-it/wait-for-it.sh .

# Env.
ENV DATABASE_URL=${DATABASE_URL}
ENV TIMEZONE_REGION=${TIMEZONE_REGION}
ENV SELENIUM_URL=${SELENIUM_URL}

# Entrypoint.
CMD ["python", "-m", "src"]
