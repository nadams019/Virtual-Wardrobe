#!/bin/sh

# run our server locally:
export PYTHONPATH=$(pwd):$PYTHONPATH
FLASK_APP=server.endpoints flask run --host=127.0.0.1 --port=8000
