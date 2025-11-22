# AMQP

AMQP 0-9-1 (Advanced Message Queuing Protocol) test cases in Python.

## Purpose

As a middleware broker, it enables the communication between applications. So, the idea of this demo is to remember how AMQP can be flexible to tackle different scenarios, use cases or patterns in distributed design systems. And this flexibility is due to its EBQ (Exchage-Binding-Queue) model.

Some concepts you should know:

- Broker
- Vhost or Virtual host
- Connection
- Channel
- Producer
- Consumer
- Message
- Exchange
- Binding
- Queue
- Routing key


## Setup

### python3

Download and install the latest python at https://www.python.org/downloads/

Verify the installation, open a terminal and type:

```bash
python3 --version
```

### pip3

Open a terminal and install pip3, follow the commands at https://pip.pypa.io/en/stable/installation/

Verify the installation:

```bash
pip3 --version
```

### Pika

It is a pure-Python implementation of the AMQP 0-9-1 protocol. For more information, visit: https://pika.readthedocs.io/en/stable/index.html

```bash
pip3 install pika
```

### RabbitMQ

For the following projects, we will use RabbitMQ as AMQP messaging broker. So, to install RabbitMQ server, follow one of the alternatives that the oficial website offers to you, visit: https://www.rabbitmq.com/docs/download

