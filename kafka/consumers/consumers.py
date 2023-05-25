from kafka import KafkaConsumer
import random


servidores_bootstrap = 'kafka:9092'
topics = ['temperatura', 'porcentaje_humedad', 'posicion', 'color', 'peso']
topic = random.choice(topics)
print("El topic elegido es: "+ topic)

consumidor = KafkaConsumer(topic, bootstrap_servers=[servidores_bootstrap])

for msg in consumidor:
    print(msg.value)




# from kafka import KafkaConsumer
# consumer = KafkaConsumer('mi_tema')
# for message in consumer:
#     print(message)