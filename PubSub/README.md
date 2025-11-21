# Publisher / Subscriber

## About this example: Sending messages to many consumers at once

Fanout exchange routes messages to all of the queues that are bound to it and the routing key is IGNORED. If N queues are bound to a fanout exchange, when a new message is published to that exchange a copy of the message is delivered to all N queues.

Fanout exchanges are ideal for the broadcast routing of messages

## Test case:

Start 1 to N consumers (subscribe_logs.py) in different terminals:

```bash
python3 subscribe_logs.py
```
```bash
python3 -u subscribe_logs.py > logs_from_rabbit.log
```

Open a terminal and execute the sender (publish_log.py)

```bash
python3 publish_log.py "This messages will be published to all consumers"
```
