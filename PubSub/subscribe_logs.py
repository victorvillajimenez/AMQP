import pika
import sys
import os
sys.path.append(os.path.relpath('..'))
from constants import URL, FANOUT_EXCHANGE, RANDOM_QUEUE_GENERATOR

EXCHANGE = 'fanout_logs'

def main ():
  params = pika.URLParameters(URL)
  connection = pika.BlockingConnection(params)
  channel = connection.channel()
  
  exchange = channel.exchange_declare(
    exchange=EXCHANGE,
    exchange_type=FANOUT_EXCHANGE,
  )
  queue = channel.queue_declare(
    queue=RANDOM_QUEUE_GENERATOR, # For empty str, broker will create a temp queue with a random name, it will be deleted when consumer conection is closed
    exclusive=True
  )
  # Since queue was created with a random name, and routing_key is ignored because exchange_type is fanout
  # binding queue with exchange is crucial. 
  binding = channel.queue_bind(
    exchange=EXCHANGE,
    queue=queue.method.queue
  )
  print(exchange)
  print(queue)
  print(binding)
  
  
  def callback(ch, method, properties, body):
    print(f" [x] {body}")
    
  channel.basic_consume(
    queue=queue.method.queue,
    on_message_callback=callback,
    auto_ack=True
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
