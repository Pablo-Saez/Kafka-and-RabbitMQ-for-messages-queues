from kafka import KafkaConsumer

# Configuración del consumidor de Kafka
bootstrap_servers = 'kafka:9092'
topic = 'mi_topico'
group_id = 'mi_grupo'

# Crear una instancia del consumidor de Kafka
consumer = KafkaConsumer(topic, bootstrap_servers=bootstrap_servers)

# Leer y procesar los mensajes del tópico
for message in consumer:
    print(f'Mensaje recibido: {message.value.decode()}')

# Cerrar la conexión del consumidor
print("termino")
consumer.close()



