import pika
import sys
import os
sys.path.append(os.path.relpath('..'))
from constants import URL, FANOUT_EXCHANGE

EXCHANGE = 'fanout_logs'

params = pika.URLParameters(URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

# This time channel.queue_declare is not set, cause its name should be created randomdly by the consumer 
channel.exchange_declare(
  exchange=EXCHANGE,
  exchange_type=FANOUT_EXCHANGE,
)

message = ' '.join(sys.argv[1:]) or "Default info message"
channel.basic_publish(
  exchange=EXCHANGE,
  routing_key='', # Not required when exchange_type is fanout
  body=message,
)

print(f" [x] Sent {message}")
connection.close()
