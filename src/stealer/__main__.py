import asyncio
import logging
import click
from functools import update_wrapper

from .auth import authentication, get_random_client, make_client
from .stealer import steal_bot
from .settings import DIR_SESSIONS_PATH


def coro(f):
        """
        To run asynchronous functions by click
        Yeah..
        :param f:
        :return:
        """
        def wrapper(*args, **kwargs):
            loop = asyncio.get_event_loop()
            return loop.run_until_complete(f(*args, **kwargs))
        return update_wrapper(wrapper, f)


@click.group()
def cli():
    pass


@click.command()
@click.option('--api-id', help='', required=True)
@click.option('--api-hash', help='', required=True)
@click.option('--phone-number', help='', required=True)
@coro
async def auth(api_id, api_hash, phone_number):
    await authentication(DIR_SESSIONS_PATH, api_id, api_hash, phone_number)


@click.command()
@click.option('--bot-name', help='A bot name to steal')
@click.option('--dir-sessions', required=False, default=DIR_SESSIONS_PATH)
@click.option('--api-id', help='', required=True)
@click.option('--api-hash', help='', required=True)
@click.option('--phone-number', help='', required=True)
@click.option('--retry-timeout', default=120)
@coro
async def stealer(
        bot_name, dir_sessions, api_id, 
        api_hash, phone_number,
        retry_timeout,
        ):
    app = make_client(dir_sessions, api_id, api_hash, phone_number)
    async with app:
        await steal_bot(app, bot_name, retry_timeout)



cli.add_command(auth)
cli.add_command(stealer)

if __name__ == "__main__":

    logging.getLogger().setLevel(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO, filename='stealer.log')
    cli()
