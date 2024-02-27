import pika
import os, sys, time


def callback(ch, method, properties, body):
    summa = float(body.decode())
    print(f" [x] Received {summa}")
    time.sleep(summa / 10)
    print(" [x] Done")
    ch.basic_ack(delivery_tag=method.delivery_tag)


def main():
    credentials = pika.PlainCredentials('consumer_1', 'consumer_1')
    parameters = pika.ConnectionParameters('rabbitmq',
                                           5672,
                                           '/',
                                           credentials)
    connection = pika.BlockingConnection(parameters)
    # connection = pika.BlockingConnection(
    #     pika.ConnectionParameters(host='rabbitmq')
    # )

    channel = connection.channel()
    # init
    channel.exchange_declare(exchange='my_exchange', exchange_type='topic')

    channel.queue_declare(queue='my_queue_1', durable=True)
    channel.queue_declare(queue='my_queue_2', durable=True)

    channel.queue_bind(exchange='my_exchange', queue='my_queue_1', routing_key='expensive.*')
    channel.queue_bind(exchange='my_exchange', queue='my_queue_2', routing_key='cheap.*')
    # init

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue='my_queue_1', on_message_callback=callback)
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

