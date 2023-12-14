#!/bin/bash

# Start the Python server
cd server
source venv/Scripts/activate
python manage.py runserver &

# Start the Angular frontend
cd ../client
ng serve
