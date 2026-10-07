import asyncio
import time
import random

async def worker(identifiant):
    print("WORKER", identifiant)
    await asyncio.sleep(3)
    print("WORKER END", identifiant)
    return random.randint(0, 10)

async def main():
    #liste_resultat = await asyncio.gather(*(worker(str(i)) for i in range(0,3))) 
    liste_resultat = await asyncio.gather(worker("1"), worker("2"), worker("3"))
    print(liste_resultat)
    print(sum(liste_resultat)/len(liste_resultat))

asyncio.run(main())