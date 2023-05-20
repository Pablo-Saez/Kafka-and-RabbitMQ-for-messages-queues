import pika

# Callback para procesar los mensajes recibidos
def callback(ch, method, properties, body):
    print("Mensaje recibido: %r" % body)

# Establecer la conexión con RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Crear una cola en RabbitMQ
channel.queue_declare(queue='mi_cola')

# Configurar el callback para recibir mensajes
channel.basic_consume(queue='mi_cola', on_message_callback=callback, auto_ack=True)

# Iniciar la recepción de mensajes
print('Esperando mensajes. Presiona CTRL+C para salir.')
channel.start_consuming()
