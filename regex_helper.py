import httpx
from config import URL

async def mob_death_regex(match):
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

async def mob_spawn_regex(match: list):
    print("mob_spawn_regex match found:")
    print(match)


# async def mob_spawn_regex(match):
#     vals = []
#     for val in match:
#         if 'You say, ' in val:
#             val = val.replace("You say, '", "")
#             vals.append(val)
#         vals.append(val)
#     date_time, zone = vals
#     result = db_commands.insert_mob_spawn(tuple(vals))
#     if result == True:
#         await message_helper.send_message_to_guild(config.GUILD_ID, config.CHANNEL_ID, embed.mob_spawn_embed(zone, date_time))
#     else:
#         print("db_commands.insert_mob_spawn FAILED")