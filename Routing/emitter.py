import pika
import sys
import os
sys.path.append(os.path.relpath('..'))
from constants import URL, DIRECT_EXCHANGE

EXCHANGE = 'direct_logs'

params = pika.URLParameters(URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(
  exchange=EXCHANGE,
  exchange_type=DIRECT_EXCHANGE,
)

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or 'Default message...'
channel.basic_publish(
  exchange=EXCHANGE,
  routing_key=severity,
  body=message,
)

print(f" [x] Sent {severity}:{message}")
connection.close()
