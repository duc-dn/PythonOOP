import asyncio
import time
import threading

async def counter():
    print("One")
    await asyncio.sleep(3)
    print("two")

async def do_it():
    await asyncio.sleep(2)
    print("Hello world")

async def sayHi():
    print(100)
    await asyncio.sleep(1)

# Cach chay binh thuong (Tuan tu)
async def main():
    start_time = time.time()
    await counter()
    await counter()
    await counter()
    end_time = time.time()
    print(f"Processing time: {end_time - start_time}")
    await asyncio.gather(counter(), counter(), counter())

# Cach chay voi async await()
async def main1():
    print(f"Thread is running: {threading.current_thread().name }")
    start_time = time.time()
    await asyncio.gather(counter(), sayHi(), counter(), counter(), do_it())
    end_time = time.time()
    print(f"Processing time: {end_time - start_time}")
asyncio.run(main1())