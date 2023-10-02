# ztoany-whisper-flask-sample

## Non docker

### Prerequisites

- Need to install [OpenAI Whisper](https://github.com/openai/whisper) .
- Need to install flask

```shell
pip install -U Flask
pip install -U Flask-Cors
```

### Run App

```shell
python app.py
```

## docker

### Build docker image

run script `docker-img-build.sh`

### Run App

```shell
dokcer run -d --rm -p 5000:5000 --name openai-whisper-sample whisper-flask-web-sample:<TAG>
```