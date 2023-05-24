import threading
import time
import json
import random
import argparse
#pip install confluent-kafka
from confluent_kafka import Producer
from kafka import KafkaProducer

# Configuración de Kafka
bootstrap_servers = 'kafka:9092'
topic = 'mi_topic'

# Crear un bloqueo para sincronizar el acceso al productor de Kafka
producer_lock = threading.Lock()

def send_data(interval):
    # Crear instancia del productor de Kafka
    producer = KafkaProducer(bootstrap_servers=[bootstrap_servers])

    while True:
        id = ''.join(random.choices(
            "abcdefghijklmnopqrstuvwxyz0123456789",
            k=random.randint(1, 20)))
        temperatura = random.uniform(10, 30)
        temperatura = round(temperatura, 1)

        humedad = random.randint(0, 100)

        posicion = random.randint(0, 10)

        colores = ["blanco", "rojo", "azul", "naranjo", "amarillo", "verde_claro", "verde_oscuro", "lila", "blanco"]

        color = random.choice(colores)

        data = {
            "timestamp": int(time.time()),
            "id": id,
            "temperatura": temperatura,
            "porcentaje_humedad": humedad,
            "thread_ID": threading.get_ident(),
            "posicion": posicion,
            "color": color
        }
        message = json.dumps(data)

        # Adquirir el bloqueo antes de utilizar el productor de Kafka
        producer_lock.acquire()
        try:
            # Enviar el mensaje al tema de Kafka
            print("entro")
            producer.send(topic, message.encode('utf-8'))
            producer.flush()

            print("ThreadID:", threading.get_ident(), message)
        finally:
            # Liberar el bloqueo después de utilizar el productor de Kafka
            producer_lock.release()

        time.sleep(interval)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_threads", type=int, help="Number of threads to create")
    args = parser.parse_args()

    threads = []
    for i in range(args.num_threads):
        interval = random.uniform(1, 5) # intervalo aleatorio
        t = threading.Thread(target=send_data, args=(interval,))
        t.daemon = True
        t.start()
        threads.append(t)

    # Esperar a que todos los hilos finalicen
    for thread in threads:
        thread.join()
