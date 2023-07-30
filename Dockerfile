FROM python:3.11.4-slim-bullseye

EXPOSE 5000
RUN apt-get update \
    && apt-get install curl -y \
    && apt-get install telnet -y \
    && apt-get install net-tools -y \
    && apt install ffmpeg -y
RUN pip install setuptools-rust
RUN pip install -U openai-whisper
RUN pip install -U Flask
RUN pip install -U Flask-Cors
WORKDIR /app
COPY docker-entrypoint.sh /app
COPY templates /app
COPY *.py /app
RUN python download_model.py
ENTRYPOINT ["./docker-entrypoint.sh"]