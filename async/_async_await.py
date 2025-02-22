import asyncio
import time

"""
什么时候用协程，什么时候用多线程，什么时候用多进程
future 对象
asyncio 的底层 api
loop
trio 第三方库用法
"""
"""
协程的主要应用场景是 IO 密集型任务，总结几个常见的使用场景：
网络请求，比如爬虫，大量使用 aiohttp
文件读取， aiofile
web 框架， aiohttp， fastapi
数据库查询， asyncpg, databases
"""


# async def表示线程函数
async def visit_url(url, response_time):
    """await可以让程序在tasks之间切换"""
    await asyncio.sleep(response_time)
    return f"hello{url}"


async def run_task():
    """收集子任务"""

    task_1 = visit_url('https://XXX1.com', 2)
    task_2 = visit_url('https://XXX2.com', 3)
    tasks = [task_1, task_2]
    await asyncio.gather(*tasks)


start_time = time.perf_counter()
asyncio.run(run_task())
print(f"耗时: {time.perf_counter() - start_time}s")
