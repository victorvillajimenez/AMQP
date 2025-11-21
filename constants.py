# To monitor the broker:
#
# sudo rabbitmqctl list_exchanges
# sudo rabbitmqctl list_bindings
# sudo rabbitmqctl list_queues name messages_ready messages_unacknowledged


URL = 'amqps:username:password@host:port/vhost'


DEFAULT_EXCHANGE = ''
DIRECT_EXCHANGE = 'direct'
FANOUT_EXCHANGE = 'fanout'
TOPIC_EXCHANGE = 'topic'


RANDOM_QUEUE_GENERATOR = ''
