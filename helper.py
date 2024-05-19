
from config import URL
# import db_commands
# import embed
# # import message_helper
# from helper2 import calculate_respawn_time
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

# async def mob_death_regex(match):
#     # Could probably update the regex to deal with this, instead of this mess
#     vals = []
#     for val in match:
#         if 'You say, ' in val:
#             val = val.replace("You say, '", "")
#             vals.append(val)
#         else:
#             vals.append(val) 
#     death_time, mob_name = vals
#     result = db_commands.insert_mob_death(tuple(vals))
#     respawn_time = calculate_respawn_time(mob_name, death_time)
#     if result == True:
#         await message_helper.send_message_to_guild(config.GUILD_ID, config.CHANNEL_ID, embed.mob_death_embed(mob_name, death_time, respawn_time))
#     else:
#         print("db_commands.insert_mob_death FAILED")
       

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


# def get_file_name() -> str:
#     try:
#         char_name = ''
#         eq_dir = ''
#         server = ''

#         c = bot.db_connection.cursor()
#         query = '''SELECT * FROM config
#         '''
#         c.execute(query)
#         row = c.fetchone()

#         if row:
#             id, char_name, eq_dir, server = row
#             if server == "RoT":
#                 return f"{eq_dir}logs\eqlog_{char_name}_RoT.txt"
#             else:
#                 return f"{eq_dir}logs\eqlog_{char_name}_P1999PVP.txt"
            
#         else:
#             print("No rows found in the 'config' table.")
#             return "" 