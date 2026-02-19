import psycopg2
import time

# Nos conectamos a la VM1 a través del puerto 15432
db_config = {
    'dbname': 'si2db',
    'user': 'alumnodb',
    'password': 'alumnodb',
    'host': 'localhost',
    'port': 15432 
}

try:
    conn = psycopg2.connect(**db_config)
    cursor = conn.cursor()

    # Pedimos los números de 1000 tarjetas
    cursor.execute("SELECT numero FROM tarjeta LIMIT 1000")
    ids_tarjetas = [row[0] for row in cursor.fetchall()]

    print(f"Iniciando lectura de {len(ids_tarjetas)} tarjetas (SQL)...")
    
    # Arrancamos el cronómetro
    start_time = time.time()

    # Buscamos las tarjetas una a una
    for id_val in ids_tarjetas:
        cursor.execute("SELECT * FROM tarjeta WHERE numero = %s", (id_val,))
        cursor.fetchone()

    # Paramos el cronómetro
    end_time = time.time()

    print(f"Tiempo total: {end_time - start_time:.6f} segundos")

except Exception as e:
    print(f"Error: {e}")
finally:
    if 'cursor' in locals(): cursor.close()
    if 'conn' in locals(): conn.close()