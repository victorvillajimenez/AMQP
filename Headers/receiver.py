import pika
import sys
import os
import json
sys.path.append(os.path.relpath('..'))
from constants import URL, HEADERS_EXCHANGE, RANDOM_QUEUE_GENERATOR

EXCHANGE = 'headers_in_messages'

def main ():
  params = pika.URLParameters(URL)
  connection = pika.BlockingConnection(params)
  channel = connection.channel()

  exchange = channel.exchange_declare(
    exchange=EXCHANGE,
    exchange_type=HEADERS_EXCHANGE,  
  )
  queue = channel.queue_declare(
    queue=RANDOM_QUEUE_GENERATOR,
    exclusive=True,
  )
  # Bind the queue to the headers exchange with matching arguments
  # 'x-match': 'all' means all specified headers must match
  # 'x-match': 'any' means at least one specified header must match
  binding = channel.queue_bind(
    exchange=EXCHANGE,
    queue=queue.method.queue,
    arguments={ # You might want to have more receivers with different key-values
      'x-match': 'all',
      'department': 'sales',
      'role': 'manager'
    }
  )
  print(exchange)
  print(queue)
  print(binding)

  def callback (ch, method, properties, body):
    print(f" [x] Received '{body.decode()}' with headers: {properties.headers}")

  channel.basic_consume(
    queue=queue.method.queue,
    on_message_callback=callback,
    auto_ack=True,  
  )
  print(f" [*] Waiting for messages in {queue.method.queue} queue. To exit press CTRL+C")
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
