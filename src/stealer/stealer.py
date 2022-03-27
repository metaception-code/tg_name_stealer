import logging 
import asyncio 
import time 

from pyrogram import Client
from pyrogram.raw.functions.messages.start_bot import StartBot
from pyrogram.errors.exceptions.bad_request_400 import InputUserDeactivated

_BOTFATHER = "BotFather"


async def is_bot_available(app: Client, bot_name: str) -> bool:
    
    
    """
    Checking opportunity of sending messages to bot
    """
    try:
        sent_message = await app.send_message(bot_name, "ping-pong")
        print(sent_message)
    except InputUserDeactivated:
        logging.info("Bot is deleted or not exists.")
        return True
    except Exception as e:
        print(e)
    else:
        return False 



async def create_new_bot(app: Client, name: str) -> None:
    
    logging.info("Creating bot with name: %s", name)
    await app.send_message(_BOTFATHER, "/newbot")
    await app.send_message(_BOTFATHER, "randomname")
    await app.send_message(_BOTFATHER, name)



async def steal_bot(app: Client, name: str, timeout: int = 120):
    
    logging.info("Starting cycle of stealing. Name to steal: %s", name)
    while app:
        if await is_bot_available(app, name):
            logging.info("Bot's name available!")
            await create_new_bot(app, name)
        time.sleep(timeout)
        

