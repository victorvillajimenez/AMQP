# Routing

## About this example: Receiving messages selectively

Subscribe only to a subset of the messages. For example, we'll be able to direct only critical error messages to the log file (to save disk space), while still being able to print all of the log messages on the console.

The routing algorithm behind a direct exchange is simple - a message goes to the queues whose binding key exactly matches the routing key of the message.

## Test case

Open three terminals and execute (listener.py):

```bash
python3 -u listener.py error > errors.log
```
```bash
python3 -u listener.py warning > warnings.log
```
```bash
python3 listener.py info warning error
```

Send messages with different severity level (emitter.py):

```bash
python3 emitter.py error "Resource not found"
```
```bash
python3 emitter.py warning "New library version"
```
```bash
python3 emitter.py info "AMQP is great!"
```
