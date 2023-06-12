import asyncio
import time

async def print_message(message):
    await asyncio.sleep(1)
    print(message)

async def main():
    print("Start")
    start_time = time.time()
    await print_message("Hello")
    await print_message("World")
    end_time = time.time()
    print(f"Thoi gian thuc hien ham: {end_time - start_time}")
    print("End")

asyncio.run(main())