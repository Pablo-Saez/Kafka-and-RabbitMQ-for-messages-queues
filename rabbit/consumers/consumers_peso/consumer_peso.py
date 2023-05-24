import pika
from pika import credentials

# Callback para procesar los mensajes recibidos
def callback(ch, method, properties, body):
    print("Mensaje recibido: %r" % body)

# Establecer las credenciales de acceso
credentials = credentials.PlainCredentials('myuser', 'mypassword')

# Establecer la conexión con RabbitMQ
parameters = pika.ConnectionParameters('rabbitmq', port=5672, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Crear un canal exclusivo llamado "peso"
channel.queue_declare(queue='peso')

# Configurar el callback para recibir mensajes
channel.basic_consume(queue='peso', on_message_callback=callback, auto_ack=True)

# Iniciar la recepción de mensajes
print('Esperando mensajes de peso. Presiona CTRL+C para salir.')
channel.start_consuming()
