#!/bin/bash
while ! mysqladmin processlist --silent -h"db" -p$MYSQL_ROOT_PASSWORD --silent; do
  sleep 1
done
python manage.py migrate
python manage.py runserver 0.0.0.0:8000
