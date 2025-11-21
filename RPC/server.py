import pika
import sys
import os
sys.path.append(os.path.relpath('..'))
from constants import URL, DEFAULT_EXCHANGE

QUEUE = 'rpc_queue'

def main ():
  params = pika.URLParameters(URL)
  connection = pika.BlockingConnection(params)
  channel = connection.channel()

  channel.queue_declare(
    queue=QUEUE,
  )

  def fib (n):
    if n == 0:
      return 0
    if n == 1:
      return 1
    return fib(n - 1) + fib(n - 2)

  def on_request (ch, method, properties, body):
    n = int(body)
    print(f" [.] fib({n})")
    response = fib(n)
    ch.basic_publish(
      exchange=DEFAULT_EXCHANGE,
      routing_key=properties.reply_to,
      properties=pika.BasicProperties(
        correlation_id=properties.correlation_id,
      ),
      body=str(response),
    )
    ch.basic_ack(
      delivery_tag=method.delivery_tag,
    )
  # For fair dispatch, meaning don't dispatch a new message to a worker until it has processed and acknowledged the previous one.
  channel.basic_qos(
    prefetch_count=1
  )
  channel.basic_consume(
    queue=QUEUE,
    on_message_callback=on_request,
  )
  print(' [x] Awaiting RPC requests')
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
