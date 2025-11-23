import pika
import sys
import os
import json
sys.path.append(os.path.relpath('..'))
from constants import URL, HEADERS_EXCHANGE

EXCHANGE = 'headers_in_messages'

params = pika.URLParameters(URL)
connection = pika.BlockingConnection(params)
channel = connection.channel()

channel.exchange_declare(
  exchange=EXCHANGE,
  exchange_type=HEADERS_EXCHANGE,
)

message = ' '.join(sys.argv[1:]) or "Default: This is a notification for specific recipients."
properties = pika.BasicProperties(
  headers = { # TODO: make headers dynamic
    'region': 'us-west',
    'department': 'sales',
    'role': 'manager',
  }
)
channel.basic_publish(
  exchange=EXCHANGE,
  routing_key='', # Routing key is ignored by headers exchanges, so it can be an empty string
  body=message,
  properties=properties
)

print(f" [x] Sent message with headers: {properties.headers}")
connection.close()
