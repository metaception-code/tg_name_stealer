import asyncio
import logging
import click
from functools import update_wrapper


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
@click.option('--api-id', help='')
@click.option('--api-hash', help='')
@click.option('--phone-number', help='')
@coro
async def auth(api_id, api_hash, phone_number):
    pass



@click.command()
@click.option('--bot-name', help='A bot name to steal')
@click.option('--dir-sessions', required=False)
async def stealer(bot_name, dir_sessions):
    pass



cli.add_command(auth)
cli.add_command(stealer)

if __name__ == "__main__":

    logging.getLogger().setLevel(level=logging.DEBUG)
    logging.basicConfig(level=logging.INFO, filename='log.log')

    cli()
