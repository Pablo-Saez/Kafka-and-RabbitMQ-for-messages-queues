import threading
import time
import json
import random
import argparse

import pika
#ESTE ARCHIVO ES GENERICO Y MANDA LOS 5 ELEMENTOS.

# Establecer la conexión con RabbitMQ
credentials = pika.PlainCredentials('myuser', 'mypassword')
parameters = pika.ConnectionParameters('rabbitmq', port=5672, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Crear una cola en RabbitMQ
channel.queue_declare(queue='mi_cola')
# print("A continuación va el canal:")
# print(channel)

# Crear un bloqueo para sincronizar el acceso al canal
channel_lock = threading.Lock()

def send_data(interval):
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
        peso = random.randint(0.1,30)
        data = {
            "timestamp": int(time.time()),
            "id": id,
            "temperatura": temperatura,
            "porcentaje_humedad": humedad,
            "thread_ID": threading.get_ident(),
            "posicion": posicion,
            "color": color,
            "peso":peso
        }
        message = json.dumps(data)

        # Adquirir el bloqueo antes de utilizar el canal
        channel_lock.acquire()
        try:
            # Enviar el mensaje a la cola
            channel.basic_publish(exchange='', routing_key='mi_cola', body=message)

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
