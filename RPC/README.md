# RPC - Remote Procedure Call

## About this: Request/reply pattern example

Remote Procedure Call or RPC, a pattern to run a function on a remote computer and wait for the result.

It involves a straightforward interaction between the server and the client.

In the client interface, in order to receive a response we need to send a 'callback' queue name with the request. Such a queue is often server-named but can also have a well-known name (be client-named).

The server will then use that name to respond using the default exchange.

## Test case

Open 1 to N terminals and execute the servers (server.py)

```bash
python3 server.py
```
```bash
python3 server.py
```
Open 1 to M terminals and execute the clients (client.py)

```bash
python3 client.py 30
```
```bash
python3 client.py 20
```
```bash
python3 client.py 10
```

> [!CAUTION]
> For arguments in client.py, no more than 40, it takes long.
