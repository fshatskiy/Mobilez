release: python manage.py migrate
web: gunicorn Mobilez.wsgi --log-file -
node: node server.js