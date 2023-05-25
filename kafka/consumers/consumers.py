from kafka import KafkaConsumer


servidores_bootstrap = 'kafka:9092'
topic = 'color'

consumidor = KafkaConsumer(topic, bootstrap_servers=[servidores_bootstrap])

for msg in consumidor:
    print(msg.value)




# from kafka import KafkaConsumer
# consumer = KafkaConsumer('mi_tema')
# for message in consumer:
#     print(message)