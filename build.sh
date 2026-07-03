#!/usr/bin/env bash
set -o errexit

pip install -r requirements.txt

python manage.py migrate --noinput

python manage.py shell << EOF
from django.contrib.auth import get_user_model

User = get_user_model()

username = "admin"
email = "admin@email.com"
password = "123456"

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username, email, password)
    print("Superuser criado")
else:
    print("Superuser já existe")
EOF

python manage.py collectstatic --noinput