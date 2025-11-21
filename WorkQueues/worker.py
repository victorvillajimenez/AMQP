import pika
import time
import sys
import os
sys.path.append(os.path.relpath('..'))
from constants import URL

QUEUE = 'work_queue'

def main ():
    params = pika.URLParameters(URL)
    connection = pika.BlockingConnection(params)
    channel = connection.channel()

    channel.queue_declare(
        queue=QUEUE,
        durable=True
    )

    def callback(ch, method, properties, body):
        print(" [x] Received %r" % body.decode())
        work_time_in_seconds = body.count(b'.')
        print("work time in seconds:", work_time_in_seconds)
        print("method.delivery_tag:", method.delivery_tag)
        # print(properties)
        time.sleep(work_time_in_seconds)
        print(" [x] Done\n")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    # For fair dispatch, meaning don't dispatch a new message to a worker until it has processed and acknowledged the previous one.
    channel.basic_qos(prefetch_count=1) 
    channel.basic_consume(
        queue=QUEUE,
        on_message_callback=callback,
        # auto_ack=True, # if there is not a channel.basic_ack(delivery_tag=method.delivery_tag)
    )

    print(' [*] Waiting for messages. To exit press CTRL+C')
    channel.start_consuming()

if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print(' - Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
