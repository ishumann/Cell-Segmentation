FROM python:3.8-slim-buster
WORKDIR /app
COPY . /app

RUN app update -y && apt install awscli -y

RUN apt-get update && apt-get install ffmpeg libsm6 Libxext6 unzip -y && pip install -r requirements.
CMD [ "python3", "app.py" ]