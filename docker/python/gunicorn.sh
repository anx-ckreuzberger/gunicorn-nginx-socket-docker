#!/bin/sh

# collect static files
python manage.py collectstatic --noinput
# make sure to migrate
python manage.py migrate --noinput

# run gunicorn
# gunicorn -b 0.0.0.0:5000 example_app.wsgi --workers 3 $*
gunicorn -b unix:/gunicorn_socket/socket example_app.wsgi --workers 3 $*
