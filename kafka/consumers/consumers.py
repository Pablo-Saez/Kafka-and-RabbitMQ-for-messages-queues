from kafka import KafkaConsumer
import random
import time

servidores_bootstrap = 'kafka:9092'
topics = ['temperatura', 'porcentaje_humedad', 'posicion', 'color', 'peso']

topic_elegido = random.choice(topics)
grupo_consumidores = f'grupo_consumidores_{topic_elegido}'

# Configurar el consumidor con el group_id
consumer = KafkaConsumer(
    topic_elegido,
    group_id=grupo_consumidores,
    bootstrap_servers=[servidores_bootstrap]
)

# Variables para el cálculo del promedio de tiempo
total_mensajes = 0
tiempo_promedio = 0

# Consumir mensajes del topic elegido
for msg in consumer:
    mensaje = msg.value.decode('utf-8')
    timestamp_envio = int(mensaje.split('"timestamp": ')[1].split(',')[0])
    timestamp_lectura = int(time.time())
    tiempo_transcurrido = timestamp_lectura - timestamp_envio
    
    total_mensajes += 1
    tiempo_promedio = (tiempo_promedio * (total_mensajes - 1) + tiempo_transcurrido) / total_mensajes

    print(f"Topic: {msg.topic}, Mensaje: {mensaje}")
    
    print(f"Promedio de tiempo: {tiempo_promedio} segundos\n")
