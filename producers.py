import threading
import time
import json
import random
import argparse
import pika

def send_data(interval):
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
            "temperatura":temperatura, 
            "porcentaje_humedad":humedad,
            
        }
        print("ThreadID: ", threading.get_ident(), json.dumps(data))
        time.sleep(interval)


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("num_threads", type=int, help="Number of threads to create")
    args = parser.parse_args()

    # for i in range(args.num_threads):
    #     #interval = random.uniform(0.1, 5) #intervalo random 
    #     interval = 3
    #     t = threading.Thread(target=send_data, args=(interval,))
    #     t.daemon = True
    #     t.start()
    import pika

    # Establecer la conexión con RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Crear una cola en RabbitMQ
    channel.queue_declare(queue='mi_cola')

    # Enviar un mensaje a la cola
    channel.basic_publish(exchange='', routing_key='mi_cola', body='¡Hola, RabbitMQ que pasa!')

    # Cerrar la conexión
    connection.close()

    # while True:
    #     time.sleep(1)
