import pika

connection = pika.BlockingConnection(
    pika.ConnectionParameters(host='rabbitmq')
)

channel = connection.channel()

channel.exchange_declare(exchange='my_exchange', exchange_type='topic')

channel.queue_declare(queue='my_queue_1', durable=True)
channel.queue_declare(queue='my_queue_2', durable=True)

channel.queue_bind(exchange='my_exchange', queue='my_queue_1', routing_key='expensive.*')
channel.queue_bind(exchange='my_exchange', queue='my_queue_2', routing_key='cheap.*')

channel.close()