# Work Queues or Task Queues

## About this example: Distributing tasks among workers (the competing consumers pattern)

Direct exchange delivers messages to queues based on the message routing key.

A direct exchange is ideal for the unicast routing of messages. They can be used for multicast routing as well.

- A queue binds to the exchange with a routing key K
- When a new message with routing key R arrives at the direct exchange, the exchange routes it to the queue if K = R
- If multiple queues are bound to a direct exchange with the same routing key K, the exchange will route the message to all queues for which K = R

Work Queues or Task Queues are to avoid doing a resource-intensive task immediately and having to wait for it to complete. Instead we schedule the task to be done later. We encapsulate a task as a message and send it to the queue. A worker process running in the background will pop the tasks and eventually execute the job in order or sequence for a Fair dispatch. When you run many workers the tasks will be shared or distribuited between them using parallelise work with a Round-Robin dispatching.

Using message acknowledgments and prefetch_count you can set up a work queue.

The message durability options let the tasks survive even if RabbitMQ is restarted.

## Test case:

Open a terminal and execute 1 to N senders (task_petitioners.py)

```bash
python3 sender.py First Victors task:...
python3 sender.py Second Victors task:.
python3 sender.py Third Victors task:.....
python3 sender.py Fourth Victors task:..
python3 sender.py Fifth Victors task:....
python3 sender.py Sixth Victors task:......
python3 sender.py Seventh Victors task:.
python3 sender.py Eighth Victors task:.
python3 sender.py Ninth Victors task:.
python3 sender.py Tenth Victors task:.
```

Open 1 to M terminals and execute the workers (worker.py)

```bash
python3 worker.py
```
```bash
python3 worker.py
```
