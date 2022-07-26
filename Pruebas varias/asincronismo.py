import asyncio
from aiohttp import ClientSession

async def get_character(session, url: str) -> str:
    response = await session.get(url)
    character = await response.json()
    return character['name']

# Haciendo una solicitud a la API
async def main():
    async with ClientSession() as session:
        number = input('Introduce un número: ')
        url = f'https://rickandmortyapi.com/api/character/{number}'
        character = await get_character(session, url=url)
        print(character)

# Haciendo solicitudes concurrentes a la API
async def main_for():
    async with ClientSession() as session:
        tasks = []
        for i in range(1,4):
            url = f'https://rickandmortyapi.com/api/character/{i}'
            tasks.append(asyncio.create_task(get_character(session, url=url)))
    
        response =await asyncio.gather(*tasks)
        print(response)

asyncio.run(main_for())