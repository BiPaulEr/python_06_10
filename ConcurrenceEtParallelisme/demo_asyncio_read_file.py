import asyncio
import aiofiles
import time

async def worker(identifiant):
    print("WORKER", identifiant)
    file = await aiofiles.open("ConcurrenceEtParallelisme/compte.txt")
    lines = await file.read()
    print(lines)

async def main():
    t1 = asyncio.create_task(worker("1"))
    t2 = asyncio.create_task(worker("2"))
    t3 = asyncio.create_task(worker("3"))
    await t1
    await t2
    await t3

asyncio.run(main())