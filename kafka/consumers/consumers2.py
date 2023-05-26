from kafka import KafkaConsumer
import random

servidores_bootstrap = 'kafka:9092'
topics = ['temperatura', 'porcentaje_humedad', 'posicion', 'color', 'peso']

grupo_consumidores = f'grupo_consumidores_{random.choice(topics)}'

# Configurar el consumidor con el group_id
consumer = KafkaConsumer(
    *topics,
    group_id=grupo_consumidores,
    bootstrap_servers=[servidores_bootstrap]
)

# Consumir mensajes de los topics elegidos
for msg in consumer:
    print(f"Topic: {msg.topic}, Mensaje: {msg.value}")