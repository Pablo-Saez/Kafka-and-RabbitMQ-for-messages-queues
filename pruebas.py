import threading
import time
import json
import random
import argparse

import pika

def send_data(interval):
    # Establecer la conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Crear una cola en RabbitMQ
    channel.queue_declare(queue='mi_cola')

    while True:
        id = ''.join(random.choices(
            "abcdefghijklmnopqrstuvwxyz0123456789",
            k=random.randint(1, 20)))
        temperatura = random.uniform(10, 30)
        temperatura = round(temperatura, 1)

        humedad = random.randint(0, 100)

        data = {
            "timestamp": int(time.time()),
            "id": id,
            "temperatura": temperatura,
            "porcentaje_humedad": humedad,
            "thread_ID":threading.get_ident()
        }
        message = json.dumps(data)

        # Enviar el mensaje a la cola
        channel.basic_publish(exchange='', routing_key='mi_cola', body=message)

        print("ThreadID:", threading.get_ident(), message)
        time.sleep(interval)

    # Cerrar la conexión
    connection.close()


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
