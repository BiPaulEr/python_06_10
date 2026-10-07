import asyncio
import time
import random

async def worker(identifiant, temps_attende):
    print("WORKER", identifiant)
    await asyncio.sleep(temps_attende)
    print("WORKER END", identifiant)
    return temps_attende

async def main():
    for task in asyncio.as_completed((worker("1", 10), worker("2", 2), worker("3", 4))):
        resultat = await task
        print("REQULATT", resultat)

asyncio.run(main())