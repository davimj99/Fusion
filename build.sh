#!/usr/bin/env bash
set -o errexit

python manage.py migrate

python manage.py shell << EOF
import os
from django.contrib.auth import get_user_model

User = get_user_model()

username = os.environ.get("DJANGO_SUPERUSER_USERNAME", "admin")
email = os.environ.get("DJANGO_SUPERUSER_EMAIL", "davisouza.pro@hotmail.com")
password = os.environ.get("DJANGO_SUPERUSER_PASSWORD", "123456")

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(
        username=username,
        email=email,
        password=password
    )
    print("Superuser criado com sucesso")
else:
    print("Superuser já existe")
EOF