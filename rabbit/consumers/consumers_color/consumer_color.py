import pika
import time

# Variables para el cálculo del promedio de tiempo
total_mensajes = 0
tiempo_promedio = 0

# Callback para procesar los mensajes recibidos
def callback(ch, method, properties, body):
    global total_mensajes, tiempo_promedio

    mensaje = body.decode('utf-8')
    timestamp_envio = int(mensaje.split('"timestamp": ')[1].split(',')[0])
    timestamp_lectura = int(time.time())
    tiempo_transcurrido = timestamp_lectura - timestamp_envio
    
    total_mensajes += 1
    tiempo_promedio = (tiempo_promedio * (total_mensajes - 1) + tiempo_transcurrido) / total_mensajes

    print("Mensaje recibido: %r" % body)
    
    print(f"Promedio de tiempo: {tiempo_promedio} segundos\n")

# Establecer las credenciales de acceso
credentials = pika.PlainCredentials('myuser', 'mypassword')

# Establecer la conexión con RabbitMQ
parameters = pika.ConnectionParameters('rabbitmq', port=5672, credentials=credentials)
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Crear un canal exclusivo llamado "color"
channel.queue_declare(queue='color')

# Configurar el callback para recibir mensajes
channel.basic_consume(queue='color', on_message_callback=callback, auto_ack=True)

# Iniciar la recepción de mensajes
print('Esperando mensajes de color. Presiona CTRL+C para salir.')
channel.start_consuming()
