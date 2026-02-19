import os
import time
import django

# Configuramos Django para que funcione en este script suelto
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "visaSite.settings")
django.setup()

from visaAppWSBackend.models import Tarjeta

def medir_tiempo_orm():
    # Pedimos los números de 1000 tarjetas
    tarjetas_ids = list(Tarjeta.objects.values_list('numero', flat=True)[:1000])
    
    print(f"Iniciando lectura de {len(tarjetas_ids)} tarjetas (ORM)...")

    # Arrancamos el cronómetro
    start_time = time.time()

    # Buscamos las tarjetas una a una
    for card_id in tarjetas_ids:
        t = Tarjeta.objects.get(numero=card_id)

    # Paramos el cronómetro
    end_time = time.time()
    
    print(f"Tiempo total: {end_time - start_time:.6f} segundos")

if __name__ == "__main__":
    medir_tiempo_orm()