#!/bin/bash
pip install -r requirements.txt
python manage.py migrate
python manage.py collectstatic --noinput

# Load data only if datadump.json exists
if [ -f datadump.json ]; then
    python manage.py loaddata datadump.json
    echo "Data loaded successfully!"
fi