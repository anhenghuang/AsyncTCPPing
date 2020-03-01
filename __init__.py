import asyncio
import async_timeout
from timeit import default_timer as timer


async def async_tcp_ping(host, port, timeout=10):
    time_start = timer()
    try:
        with async_timeout.timeout(timeout=timeout):
            print(f'host={host}||port={port}||status=start')
            await asyncio.open_connection(host, port)
    except Exception as e:
        print(f'host={host}||port={port}||status=error_end||error_msg={e.strerror}')
        raise e
    time_end = timer()
    time_cost_milliseconds = (time_end - time_start) * 1000.0
    print(f'host={host}||port={port}||status=end||timecost={time_cost_milliseconds}')
    return time_cost_milliseconds


if __name__ == '__main__':
    loop = asyncio.get_event_loop()

    tasks = [
        loop.create_task(async_tcp_ping('d.cn', 80, timeout=1)),
        loop.create_task(async_tcp_ping('g.cn', 80, timeout=2)),
        loop.create_task(async_tcp_ping('t.tt', 80, timeout=3)),
        loop.create_task(async_tcp_ping('z.cn', 80, timeout=4)),
        loop.create_task(async_tcp_ping('1.1.1.1', 80, timeout=5)),
        loop.create_task(async_tcp_ping('8.8.8.8', 80, timeout=6)),
        loop.create_task(async_tcp_ping('8.8.4.4', 80, timeout=7)),
    ]

    msg_return = loop.run_until_complete(asyncio.gather(*tasks, return_exceptions=True))
    loop.close()
    print(msg_return)
