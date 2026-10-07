import asyncio 
import random
async def fetch_weather(city):
    await asyncio.sleep(1)  # Simulez un délai de réseau
    temperature = random.randint(15, 25)  # Générez une température aléatoire
    print(f"Température pour {city} : {temperature}°C")
    return {"ville": city, "température": temperature}


async def main():
    resultat = await asyncio.gather(fetch_weather("City1"), fetch_weather("City2"), fetch_weather("City3"))
    
    print(sum([dictionnaire["température"] for dictionnaire in resultat])/3)

asyncio.run(main())
