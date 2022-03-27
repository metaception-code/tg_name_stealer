import os 
import random
import asyncio 
import logging 

from pyrogram import Client, filters



def make_session_name(telegram_phone):
    return f"{telegram_phone[1::1]}"


def make_client(dir_session: str, app_id: str = None, 
        app_api_hash: str = None, telegram_phone: str = None,
        session_name: str = None) -> Client:

    logging.info("Making client with work directory: %s and session name: %s", dir_session, session_name)    
    if app_id and app_api_hash and telegram_phone:
        app = Client(
            session_name or make_session_name(telegram_phone), api_id=app_id, 
            api_hash=app_api_hash, phone_number=telegram_phone,
            workdir=dir_session
        )
    elif session_name:
        app = Client(session_name, workdir=dir_session)
    else:
        raise ValueError("No data for client!")

    return app 


def get_random_client(dir_session: str) -> Client:
    
    tg_sessions = os.listdir(dir_session)
    if len(tg_sessions) > 0:
        session_name = random.choice(tg_sessions)
        client = make_client(dir_session, session_name=session_name)
        return client 
    else:
        raise ValueError("No telegram sessions in directory!")


async def authentication(dir_session, app_id, app_api_hash, telegram_phone):
    
    logging.info("Authentication client with phone: %s", telegram_phone)
    client = make_client(dir_session, app_id, app_api_hash, telegram_phone)
    async with client:
        # authorization process goes here
        pass 


#loop = asyncio.get_event_loop()
#loop.run_until_complete(main())

