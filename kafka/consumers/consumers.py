from kafka import KafkaConsumer
import random

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

# Consumir mensajes del topic elegido
for msg in consumer:
    print(f"Topic: {msg.topic}, Mensaje: {msg.value}")
