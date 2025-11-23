# Headers

## About this example: Sending messages with headers to specific consumers

It is designed for routing on multiple attributes that are more easily expressed as message headers than a routing key. Headers exchanges ignore the routing key attribute. Instead, the attributes used for routing are taken from the headers attribute. A message is considered matching if the value of the header equals the value specified upon binding.

It is possible to bind a queue to a headers exchange using more than one header for matching. When the "x-match" argument is set to "any", just one matching header value is sufficient. Alternatively, setting "x-match" to "all" mandates that all the values must match.

They can be looked upon as "direct exchanges on steroids". Because they route based on header values, they can be used as direct exchanges where the routing key does not have to be a string; it could be an integer or a hash (dictionary) for example. This allow more flexible and complex routing logic.

## Test case

Open a terminal and execute the receiver (receiver.py)

```bash
python3 receiver.py
```

Open a terminal and execute the sender (sender.py)

```bash
python3 sender.py "Reminder: Sales managers, meting today at 8:30!"
```

> [!NOTE]
> For receiver.py, you might want to change arguments on `channel.queue_bind`, for example:
> ```bash
>    arguments={
>      'x-match': 'any',
>      'department': 'compliance',
>      'region': 'ap-southeast-1',
>    }
> ```
> then execute this second receiver.
>
> So, for sender.py, you might want to change headers properties on `pika.BasicProperties`, for example:
> ```bash
>    headers={
>      'department': 'sales',
>      'region': 'ap-southeast-1',
>    }
> ```
> then execute this second sender and see what happen.
