import asyncio

async def counter():
    print("ONE")
    await asyncio.sleep(5)
    print("TWO")

async def sayHi():
    await asyncio.sleep(3)
    print("Hello world")

async def doit():
    print("Do it")
    await asyncio.sleep(6)
    print("Done")

async def main():
    # Chay tuan tu
    # await counter()
    # await counter()
    # await counter()

    # Chay bat dong bo
    await asyncio.gather(counter(), counter(), counter(), sayHi(), doit())

asyncio.run(main())