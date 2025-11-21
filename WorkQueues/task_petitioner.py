import pika
import sys
import os
sys.path.append(os.path.relpath('..'))
from constants import URL, DEFAULT_EXCHANGE

QUEUE = 'work_queue'
ROUTING_KEY = QUEUE

params = pika.URLParameters(URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# It is a programmable protocol, not a broker administrator. So, provision is made for
# protocol operations that declare queues, exchanges, bindings, and susbscriptions.
channel.queue_declare(
    queue=QUEUE,
    durable=True
)

message = ' '.join(sys.argv[1:]) or "Default: ..."
channel.basic_publish(
    exchange=DEFAULT_EXCHANGE, # direct default exchange
    routing_key=ROUTING_KEY, # same as queue name
    body=message,
    properties=pika.BasicProperties(
        # a stonger guarantee, use publisher confirms
        delivery_mode=pika.DeliveryMode.Persistent # 2
    ))
print(" [x] Sent %r" % message)
connection.close()
