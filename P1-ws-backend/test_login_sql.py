import os
import time
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "visaSite.settings")
django.setup()

from django.contrib.auth.models import User
from django.contrib.auth import authenticate

def medir_login():
    # Creamos un usuario de prueba si no existe
    if not User.objects.filter(username="test_user").exists():
        User.objects.create_user("test_user", password="mipassword123")

    print("Iniciando 100 verificaciones de login (ORM)...")
    start_time = time.time()

    # Hacemos 100 intentos de login
    for _ in range(100):
        user = authenticate(username="test_user", password="mipassword123")

    end_time = time.time()
    print(f"Tiempo total: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    medir_login()