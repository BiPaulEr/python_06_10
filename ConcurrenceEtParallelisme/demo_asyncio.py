import asyncio
import time

async def worker(identifiant):
    print("WORKER", identifiant)
    await asyncio.sleep(3)
    print("WORKER END", identifiant)

async def main():
    t1 = asyncio.create_task(worker("1"))
    t2 = asyncio.create_task(worker("2"))
    t3 = asyncio.create_task(worker("3"))
    await t1
    await t2
    await t3

asyncio.run(main())