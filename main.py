import asyncio


async def send_email():
    print('Hello')
    await asyncio.sleep(2)
    print('Awake Now')


asyncio.run(send_email())


async def t1():
    await t2()
    print("Task 1")


async def t2():
    await t3()
    print('Task 2')


async def t3():
    print('Task 3')


asyncio.run(t1())


async def file_reply():
    await asyncio.sleep(4)
    return {"File Returned"}


async def data_reply():
    await asyncio.sleep(2)
    return {"data": 100}


async def task_1():
    print("Waiting for data.....")
    x = await data_reply()
    print(x)


async def task_2():
    print("Waiting for file.......")
    x = await file_reply()
    print(x)


async def fetch_data():
    print('Fetching data...')
    await asyncio.sleep(2)
    print('Data Returned.....')
    return {"data": 100}


async def task2():
    for i in range(10):
        print(i)
        await asyncio.sleep(2)


async def main():
    x = asyncio.create_task(task_1())
    y = asyncio.create_task(task_2())

    a = asyncio.create_task(fetch_data())
    b = asyncio.create_task(task2())

    await x
    await y

    data = await a
    print(data)
    await b


asyncio.run(main())
