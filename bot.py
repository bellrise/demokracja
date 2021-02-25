# python >= 3.9
# This is the main file for the Demokracja discord bot.
# It contains the bot client class. 
import discord

__author__  = '2Pg'
__version__ = 0.1


class DemokracjaBot(discord.Client):
    """ Main bot class. This contains the on_ready and on_message 
    methods, which are called when the bot is ready and on every 
    message the bot can read, respectively. """ 

    args: list[str] = []

    async def on_ready(self):
        """ This is called when the bot is ready. """ 

        print('Bot ready')


    async def on_message(self, msg):
        """ This method is called asynchronously on every
        recieved message. """

        # Recursion safety
        if self.user == msg.author:
            return

        # Parse args
        self.args = msg.content.split()

        # Dynamically call method
        try:
            func = getattr(self, f'cmd_{self.args[0]}')
            await func(msg)
        except AttributeError:
            # Command doesn't exist
            pass


    async def cmd_hello(self, msg):
        """ The 'hello' command sends a hi message mentioning
        the user. """

        await msg.channel.send(f'siema <@{msg.author.id}>')


if __name__ == "__main__":
    
    # Read the token
    with open('bot.token') as f:
        TOKEN = f.read()

    # Run the bot
    DemokracjaBot().run(TOKEN)
