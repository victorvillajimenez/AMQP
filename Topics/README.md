## Topics

# About this example: Receiving messages based on a pattern (topics)

Topic exchanges route messages to one or many queues based on matching between a message routing key and the pattern that was used to bind a queue to an exchange.

The topic exchange type is often used to implement various publish/subscribe pattern variations. Topic exchanges are commonly used for the multicast routing of messages.

Messages sent to a topic exchange can't have an arbitrary routing_key - it must be a list of words, delimited by dots. The words can be anything, but usually they specify some features connected to the message. There can be as many words in the routing key as you like, up to the limit of 255 bytes.

There are two important special cases for binding keys:

 - \* (star) can substitute for exactly one word.
 - \# (hash) can substitute for zero or more words.

When a queue is bound with # (hash) binding key - it will receive all the messages, regardless of the routing key - like in fanout exchange.

When special characters * (star) and # (hash) aren't used in bindings, the topic exchange will behave just like a direct one.

## Test case

Open three terminals and execute (publisher.py):

```bash
python3 -u publisher.py "*.error" > errors.log
```
```bash
python3 publisher.py "core.*" "payment.*"
```
```bash
python3 publisher.py "#"
```

Send messages with different severity level (subscriber.py):

```bash
python3 subscriber.py "payment.info" "Transaction was successful"
```
```bash
python3 subscriber.py "identity.error" "Credentials are incorrect"
```
```bash
python3 subscriber.py "core.error" "Resource not found"
```
