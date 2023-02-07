#!/bin/sh

echo "Certbot entrypoint is running."

crontab scheduler.txt
crontab -l

htpasswd -c -b /etc/nginx/.htpasswd $BASIC_USERNAME $BASIC_PASSWORD

nginx -g 'daemon off;'
