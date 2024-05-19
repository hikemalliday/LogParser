# WE CREATED THIS MODULE SO WE CAN BEING TO BUILD THE AWATCH PARSE WITHOUT TAMPERING WITH LOGPARSER.PY
import re
import os
from watchfiles import awatch
import helper
import regex_helper
from config import parse_started, parse_flag, FILE_NAME
import asyncio

regex_map = {
    re.compile(r"\[(.*?)\] (.*?) has fallen by the hands of a mere mortal!"): regex_helper.mob_death_regex,
    re.compile(r"\[(.*?)\] (?:(?!The).)*?The ground beneath your feet tremble as something within (.*?) awakens!"): regex_helper.mob_spawn_regex,
}

async def read_new_lines(file_name, previous_size):
    try:
        with open(file_name, 'r') as file:
            if parse_flag["run"] == False:
                return
            
            if parse_started["flag"] == False:
                file.seek(0, os.SEEK_END)
                parse_started["flag"] = True

            else:
                file.seek(previous_size)
            new_lines = file.readlines()
            for line in new_lines:
                line = line.strip()
                for regex, helper_func in regex_map.items():
                        match = regex.match(line)
                        if match:
                            matches = match.groups()  # Get all regex matches as a list
                            await helper_func(matches)
                print(line.strip())  # Strip whitespace characters from the line
                
            # Update the previous size to the current size
            return file.tell()
    except FileNotFoundError:
        parse_started["flag"] = True
        print(f"File '{file_name}' not found.")
        return previous_size
    finally:
        parse_started["flag"] = True


async def logparser():
    print("logparser() call:")
    previous_sizes = {}
    if parse_flag["run"] == True:
        return "Log parser is already running."
    parse_flag["run"] = True
    while parse_flag["run"] == True:
        async for changes in awatch('C:/RoT/logs'):
            print(FILE_NAME)
            print(changes)
            change = None
            file_name = None
            for item in changes:
                change, file_name = item
            previous_size = previous_sizes.get(file_name, 0)
            if file_name == FILE_NAME:
                if parse_flag["run"] == False:
                    break
                previous_sizes[file_name] = await read_new_lines(file_name, previous_size)

async def start_parse():
    try:
        print("start parse test")
        await logparser()
        return "log parse started..."
    except Exception as e:
        print(str(e))
        return(str(e))


