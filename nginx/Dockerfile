FROM nginx:alpine

# Basic auth credentials
ENV BASIC_USERNAME=username
ENV BASIC_PASSWORD=password

RUN apk update
RUN apk add certbot certbot-nginx
RUN apk add apache2-utils

RUN mkdir /etc/letsencrypt
COPY entrypoint.sh .
COPY scheduler.txt .

ENTRYPOINT ["sh", "entrypoint.sh"]

