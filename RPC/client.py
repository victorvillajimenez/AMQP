import pika
import uuid
import sys
import os
sys.path.append(os.path.relpath('..'))
from constants import URL, DEFAULT_EXCHANGE, RANDOM_QUEUE_GENERATOR

class FibonacciRpcClient (object):
  def __init__ (self):
    params = pika.URLParameters(URL)
    self.connection = pika.BlockingConnection(params)
    self.channel = self.connection.channel()
    queue = self.channel.queue_declare(
      queue=RANDOM_QUEUE_GENERATOR,
      exclusive=True,
    )
    self.callback_queue = queue.method.queue
    self.channel.basic_consume(
      queue=self.callback_queue,
      on_message_callback=self.on_response,
      auto_ack=True,
    )
    self.response = None
    self.corr_id = None
    
  def on_response (self, ch, method, properties, body):
    if self.corr_id == properties.correlation_id:
      self.response = body
    
  # Sending an RPC request
  def call (self, n):
    self.response = None
    self.corr_id = str(uuid.uuid4()) # to correlate RPC response with this request.
    self.channel.basic_publish(
      exchange=DEFAULT_EXCHANGE,
      routing_key='rpc_queue',
      properties=pika.BasicProperties( # For AMQP 091 has a set of 14 properties, here are some:
        reply_to=self.callback_queue,
        correlation_id=self.corr_id,
        # delivery_mode=2,
        # content_type='application/json',
        # headers={'key': 'value'},
      ),
      body=str(n),
    )
    # blocks until the result is received.
    while self.response is None:
      self.connection.process_data_events(time_limit=None)
    self.connection.close()
    return int(self.response)

fibonacci_rpc = FibonacciRpcClient()
num = ' '.join(sys.argv[1:]) or "7"
print(f" [x] Requesting fib({num})")
response = fibonacci_rpc.call(int(num))
print(f" [.] Got {response}")
