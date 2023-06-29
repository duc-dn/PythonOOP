import asyncio

async def counter():
    check = True

    data = await processing_data()
    check = await html_existed()

    return data, check

async def processing_data():
    await asyncio.sleep(2)
    return ([1, 2, 3])

async def html_existed():
    await asyncio.sleep(3)
    return False

async def main():
    data, check = await counter()

    print(data, check)
asyncio.run(main())