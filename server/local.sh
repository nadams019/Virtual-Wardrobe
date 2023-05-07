#!/bin/bash

# run our server locally:
PYTHONPATH=$(pwd):$PYTHONPATH
FLASK_APP=home_page.html flask run --host=127.0.0.1 --port=8000
