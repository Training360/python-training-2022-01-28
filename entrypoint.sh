#!/bin/sh

flask db upgrade
#flask run --host 0.0.0.0
gunicorn --worker-class gevent --workers 4 --bind 0.0.0.0:5000 employees:app --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
