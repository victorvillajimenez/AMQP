import pika
import sys
import os
sys.path.append(os.path.relpath('..'))
from constants import URL, DIRECT_EXCHANGE, RANDOM_QUEUE_GENERATOR

EXCHANGE = 'direct_logs'

def main ():
  params = pika.URLParameters(URL)
  connection = pika.BlockingConnection(params)
  channel = connection.channel()
  
  exchange = channel.exchange_declare(
    exchange=EXCHANGE,
    exchange_type=DIRECT_EXCHANGE,
  )
  queue = channel.queue_declare(
    queue=RANDOM_QUEUE_GENERATOR, # For empty str, broker will create a temp queue with a random name, it will be deleted when consumer conection is closed
    exclusive=True,  
  )
  print(exchange)
  print(queue)

  severities = sys.argv[1:]
  if not severities:
    sys.stderr.write("Usage: %s [info] [warning] [error]\n" % sys.argv[0])
    sys.exit(1)
  
  # Multiple Bidings
  #  - binding multiple queues with the same binding key.
  #  - having two or more bindings to the same queue.
  for severity in severities:
    binding = channel.queue_bind( # New binding for each severity to route to the same queue
      exchange=EXCHANGE,
      queue=queue.method.queue,
      routing_key=severity,
    )
    print(binding)
  
  def callback (ch, method, properties, body):
    print(f" [x] {method.routing_key}:{body}")
    
  channel.basic_consume(
    queue=queue.method.queue,
    on_message_callback=callback,
    auto_ack=True,
  )
  print(' [*] Waiting for logs. To exit press CTRL+C')
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
