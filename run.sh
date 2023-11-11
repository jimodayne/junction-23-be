#!/bin/sh
# export FLASK_APP=be/main.py

# flask --debug run -h 0.0.0.0

python be/main.py
# uwsgi --http 127.0.0.1:8000 --master -p 4 -w hello:app
