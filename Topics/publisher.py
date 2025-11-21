import pika
import sys
import os
sys.path.append(os.path.relpath('..'))
from constants import URL, TOPIC_EXCHANGE

EXCHANGE = 'topic_logs'

params = pika.URLParameters(URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(
  exchange=EXCHANGE,
  exchange_type=TOPIC_EXCHANGE,
)

routing_key = sys.argv[1] if len(sys.argv) > 2 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or 'Default message...'
channel.basic_publish(
  exchange=EXCHANGE,
  routing_key=routing_key,
  body=message,
)

print(f" [x] Sent {routing_key}:{message}")
connection.close()
