import httpx
from config import URL

async def mob_death_regex(match):
    print("MOB DEATH REGEX")
    vals = []
    for val in match:
        if 'You say, ' in val:
            val = val.replace("You say, '", "")
            vals.append(val)
        else:
            vals.append(val) 
    full_url = f"{URL}mob_death_regex"
    payload = {
        "death_time": vals[0],
        "mob_name": vals[1],
    }
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.post(full_url, json=payload)
        return response.json()
    
async def mob_spawn_regex(match):
    vals = []
    for val in match:
        if 'You say, ' in val:
            val = val.replace("You say, '", "")
            vals.append(val)
        else:
            vals.append(val) 
    full_url = f"{URL}mob_spawn_regex"
    payload = {
        "spawn_time": vals[0],
        "mob_zone": vals[1],
    }
    print(payload)
    async with httpx.AsyncClient(verify=False) as client:
        response = await client.post(full_url, json=payload)
        return response.json()
