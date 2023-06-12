import asyncio
import time

async def add_number(a, b, name):
    await asyncio.sleep(2)
    print(f'Add function: {a + b}')
    return name, a + b

async def subtract_number(a, b, name):
    await asyncio.sleep(5)
    print(f"Subtract funtion: {a - b}")
    return name, a - b

async def multiply_number(a, b, name):
    await asyncio.sleep(3)
    print(f"Multiply function: {a * b}")
    return name, a * b

async def devide_number(a, b, name):
    await asyncio.sleep(2)
    print(f"Devide function: {a / b}")
    return name, a / b

# Co 2 cach chay ham async:
# + Dung await 
# + Dung ham asyncio.run() (nhung chi chay duoc 1 ham duy nhat)
## asyncio chi run duoc 1 ham duy nhat
# asyncio.run(add_number(1, 99))


async def main():
    start_time = time.time()
    task1 = asyncio.create_task(add_number(99, 1)) # dawng ky vao 1 task, dua cong viec can lam vaof 1 queue
    task2 = asyncio.create_task(subtract_number(101, 1))
    task3 = asyncio.create_task(multiply_number(25, 4))
    task4 = asyncio.create_task(devide_number(1000, 10))

    await task1
    await task2
    await task3
    await task4

    end_time = time.time()
    print("Time processing: {}".format(end_time - start_time))

# QUEUE: LIFO first in first out
# --------------------
# task4, task3, task2, task1
# --------------------
# Trong Python se dien ra event loop,


async def main1():
    start_time = time.time()
    result = (
        await asyncio.gather
        (add_number(99, 1, 'cong'), subtract_number(101, 1, 'tru'), 
         multiply_number(20, 5, 'nhan'), devide_number(500, 5, 'chia'))
    )
    for i in result:
        print(i)
    
    print(result)
    end_time = time.time()
    print("Time processing: {}".format(end_time - start_time))


asyncio.run(main1())