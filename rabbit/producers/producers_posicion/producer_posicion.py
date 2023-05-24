import threading
import time
import json
import random
import argparse

import pika

# Establecer la conexión con RabbitMQ
credentials = pika.PlainCredentials('myuser', 'mypassword')
parameters = pika.ConnectionParameters('rabbitmq', port=5672, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Crear un canal exclusivo llamado "posicion"
channel.queue_declare(queue='posicion')

# Crear un bloqueo para sincronizar el acceso al canal
channel_lock = threading.Lock()

def send_data(interval):
    while True:
        id = ''.join(random.choices(
            "abcdefghijklmnopqrstuvwxyz0123456789",
            k=random.randint(1, 20)))
        posicion = random.randint(0, 10)

        data = {
            "timestamp": int(time.time()),
            "id": id,
            "posicion":posicion
        }
        message = json.dumps(data)

        # Adquirir el bloqueo antes de utilizar el canal
        channel_lock.acquire()
        try:
            # Enviar el mensaje al canal "posicion"
            channel.basic_publish(exchange='', routing_key='posicion', body=message)

            print("ThreadID:", threading.get_ident(), message)
        finally:
            # Liberar el bloqueo después de utilizar el canal
            channel_lock.release()

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

    # Esperar a que todos los threads finalicen
    for thread in threads:
        thread.join()

# Cerrar la conexión
connection.close()
