FROM python:3.8.5-alpine 
# FROM python:3.8-slim-buster

RUN pip install --upgrade pip

COPY ./requirements.txt .
RUN apk add --update --no-cache postgresql-client python3-dev \
 libffi-dev jpeg-dev freetype-dev libjpeg-turbo-dev libpng-dev \
 curl jq
RUN apk add --update --no-cache --virtual .tmp-build-deps \
 gcc g++ libc-dev linux-headers postgresql-dev musl-dev zlib \
 zlib-dev

RUN pip install -r requirements.txt
RUN apk del .tmp-build-deps

COPY ./django_project /app
WORKDIR /app

COPY ./entrypoint.sh /
ENTRYPOINT ["sh", "/entrypoint.sh"]

RUN adduser -D user
RUN chown -R user:user .
USER user
# ADD ./django_project /app/
