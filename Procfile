web: gunicorn chatapp.wsgi

web: gunicorn --bind 0.0.0.0:$PORT prremia.wsgi

web: python manage.py collectstatic --no-input; gunicorn chatapp.asgi --log-file - --log-level debug
web: daphne chatapp.asgi:channel_layer --port $PORT --bind 0.0.0.0 -v2
chatworker: python manage.py runworker --settings=chatapp.settings -v2