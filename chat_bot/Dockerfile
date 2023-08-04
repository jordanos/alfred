FROM python:3.10-slim-buster

RUN apt update
RUN apt install -y libpq-dev cron g++ build-essential

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED=1

# RUN --mount=type=cache,mode=0755,target=/root/.cache/pip

RUN mkdir /api && cd /api && mkdir chat_bot
WORKDIR /api

COPY requirements.txt .
# RUN --mount=type=cache,target=~/.cache/pip \
#     pip install -r requirements.txt
RUN pip install --no-deps -r requirements.txt

COPY . /api/chat_bot

EXPOSE 5000

CMD [ "python3", "-m", "chat_bot" ]
