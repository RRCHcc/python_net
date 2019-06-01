"""
    协程函数
"""
import asyncio
import time

now = lambda: time.time()


async def do_work(x):
    print("Waiting:", x)
    await asyncio.sleep(x)
    return "Done afer %s s" % x


start = now()
cor1 = do_work(1)
cor2 = do_work(2)
cor3 = do_work(3)
cor4 = do_work(4)
#将协程对象生成一个可轮训操作的对象列表
tasts = [
    asyncio.ensure_future(cor1),
    asyncio.ensure_future(cor2),
    asyncio.ensure_future(cor3),
    asyncio.ensure_future(cor4)
]
#得到轮寻对象调用run启动协程执行
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasts))

print("Time:",now()-start)