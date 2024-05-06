'''Message queue module'''

import pika

def publish_notification(desc, count):
    '''Publish a message to admin queue'''
    connection = pika.BlockingConnection(
        pika.ConnectionParameters(host='rabbitmq')
    )
    channel = connection.channel()

    channel.exchange_declare(exchange='detections', exchange_type='fanout')

    msg = f'{count} cars with description: {desc}'
    channel.basic_publish(exchange='detections', routing_key='', body=msg)

    connection.close()
