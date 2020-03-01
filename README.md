# Asyncio TCP Ping
### 异步的 TCP ping

```python3
from AsyncTCPPing import async_tcp_ping

loop = asyncio.get_event_loop()

tasks = [
    loop.create_task(async_tcp_ping('d.cn', 80, timeout=1)),
    loop.create_task(async_tcp_ping('g.cn', 80, timeout=2)),
    loop.create_task(async_tcp_ping('t.tt', 80, timeout=3)),
    loop.create_task(async_tcp_ping('z.cn', 80, timeout=4)),
    loop.create_task(async_tcp_ping('1.1.1.1', 80, timeout=5)),
    loop.create_task(async_tcp_ping('8.8.8.8', 80, timeout=6)),
]

msg_return = loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
loop.close()
print(msg_return)
```

---
Most python TCP package use python socket lib directly, so that they cannot support **async**.    

But _asyncio.open_connection_ use TCP to create connection, which is async/await-ready.

Therefore, we can use asyncio.open_connection to test TCP ping.

---

大多数TCP工具直接使用了 python 的 socket 库，而 socket 库是非协程的，在连接部分会导致阻塞耗时。

而 asyncio 库中有 async/await-ready 的 Stream流 实现，且 asyncio.open_connection 正好是在建立 TCP 连接。

因此可以直接用 asyncio.open_connection 代替 socket 对 TCP ping 进行异步的测量。
