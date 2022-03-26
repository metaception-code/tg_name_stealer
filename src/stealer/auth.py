import asyncio 

from pyrogram import Client, filters



app_id = "3847500"
app_api_hash = "2b9e0fe4d820003998fd3a29bf92cc31"
telegram_phone = "+375256514918"

async def main():
    async with Client("my_account", api_id=app_id, api_hash=app_api_hash, phone_number=telegram_phone) as app:
        await app.send_message("BotFather", "/newbot")
        await app.send_message("BotFather", "somenameBot")
        await app.send_message("BotFather", "somebotUsernameejfekjfekjfBot")

loop = asyncio.get_event_loop()
loop.run_until_complete(main())

