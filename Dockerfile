FROM python:3.10-slim-buster

RUN apt update
RUN apt install -y libpq-dev cron g++ build-essential

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# RUN --mount=type=cache,mode=0755,target=/root/.cache/pip

WORKDIR /hugging-face-qa-bot

COPY requirements.txt .
RUN pip install --no-deps -r requirements.txt

COPY ./api .

EXPOSE 8000

ENTRYPOINT [ "python3", "-m", "api" ]
