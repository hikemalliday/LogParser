
from config import URL
import httpx

async def mob_death_regex_test(match):
    full_url = f"{URL}mob_death_regex"
    payload = {
        "death_time": match[0],
        "mob_name": match[1],
    }
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.post(full_url, json=payload)
        return response.json()
