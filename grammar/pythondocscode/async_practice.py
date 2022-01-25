import asyncio

async def do():
    print("do")
    return 'do'

async def hello():
    print("Hello world!")
    task = asyncio.create_task(do())
    await asyncio.sleep(1)
    print("Hello again!")
    await task
    return 4


async def helloNotWaitDo():
    print("Hello world! - ")
    asyncio.create_task(do())
    print("Hello again! - ")
    return 4


def consumer():
    r = ''
    while True:
        n = yield r
        if not n:
            return
        print('[CONSUMER] Consuming %s...' % n)
        r = '200 OK'

def produce(c):
    c.send(None)
    n = 0
    while n < 5:
        n = n + 1
        print('[PRODUCER] Producing %s...' % n)
        r = c.send(n)
        print('[PRODUCER] Consumer return: %s' % r)
    c.close()


async def main():
    # task = asyncio.create_task(hello())
    # await task
    # print('################')
    for i in range(0,100):
        task1 = asyncio.create_task(helloNotWaitDo())
        await task1
        print('--------------------')

if __name__ == '__main__':
    # asyncio.run(hello())
    # c = consumer()
    # produce(c)
    asyncio.run(main())


# class A(type):
#     pass
#
# class B(type):
#     pass
#
# class C(data = A):
#     pass
#
# class D(data = B):
    pass
#
# d = D()
# C(**d.dict())