
# Kafka and rabbitMQ for messages queues



Este repositorio da una mirada simple de como rabbitmq y kafka funcionan en un contexto especifico con N productores y M consumirdores y como estos envian y reciben informacion a traves de uno o mas canales de comunicacion ofrecido por los sistemas.




## Instalacion

Para trabajar con este repositorio debes tener instalado docker y poder usar docker-compose para levantar los servicios de kafka y rabbit

Crea una carpeta para poder descargar el repositorio. Dentro de la carpeta ejecutar

```bash
  git clone https://github.com/Pablo-Saez/Kafka-and-RabbitMQ-for-messages-queues

  cd Kafka-and-RabbitMQ-for-messages-queues/
```

Una vez dentro se pueden observar 2 carpetas, Kafka y RabbitMQ.

## levantar y trabajar con RabbitMQ

Para levantar el servicio de rabbit hay que ubicarse en el directorio rabbit, luego levantar los servicios.

```bash
  cd rabbit

  docker-compose up --build
```

Una vez levantado los servicios puedes verificar si todo salio bien con
```bash
  docker ps
```
Deberas ver los contenedores arriba y disponibles.

Para mandar mensajes puedes ejecutar cualquier dupla de producer-consumer que se encuentran en las carpetas producers y consumers con su respectivo topico. Para ello debes entrar a los contenedores y ejecutar los script de python que se encuentra en ellos.








    
## Examples
Para ejecutar un productor
```bash
cd producers
sudo docker exec -it <rabbit_producer_container_name> bash
python3 producers.py <numuero_de_threads>
```

El archivo producers.py usará un numero de N threads para mandar mensajes a los consumers.

Luego para poder recibir y leer los mensajes se puede usará

```bash
cd ../consumers
sudo docker exec -it <rabbit_consumer_container_name> bash
python3 consumers.py
```





## levantar y trabajar con Kafka

En caso de kafka hay que dirigirse al directorio en donde esta la carpeta de kafka
Una vez dentro se levanta el servicio con

```bash
  #Asegurarse de estar en /kafka
  docker-compose up --build
```

Una vez terminado se puede ver si los contenedores se levantaron con


```bash
 docker ps

```

Ya arriba los servicios de kafka se puede entrar a los contenedores de los producers y consumers de kafka para enviar y recibir la informacion.

Para levantar los consumers hay que ejecutar el script en el contenedor donde esta el servicio de los producers

```bash
 cd producers
 sudo docker exec -it <kafka_producer_container_name> bash
 python3 producers.py <numero_de_threads>

```

Con esto se conectara el contenedor a kafka y enviara los mensajes a traves de los canales.
Finalmente para poder ver los mensajes se tiene que ejecutar el script de los consumers

```bash
 cd ../consumers
 sudo docker exec -it <kafka_consumer_container_name> bash
 python3 consumers.py

```

## Authors

- [@Pablo-Saez](https://github.com/Pablo-Saez)

