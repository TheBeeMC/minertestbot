import discord
from discord.ext import commands
import random

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''
client = discord.Client(command_prefix='?', description=description)

@cliet.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@client.command()
async def add(left : int, right : int):
    """Adds two numbers together."""
    await client.say(left + right)

@client.command()
async def roll(dice : str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await client.say('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await client.say(result)

@client.command(description='For when you wanna settle the score some other way')
async def choose(*choices : str):
    """Chooses between multiple choices."""
    await client.say(random.choice(choices))

@client.command()
async def repeat(times : int, content='repeating...'):
    """Repeats a message multiple times."""
    for i in range(times):
        await client.say(content)

@bot.command()
async def joined(member : discord.Member):
    """Says when a member joined."""
    await client.say('{0.name} joined in {0.joined_at}'.format(member))

@client.group(pass_context=True)
async def cool(ctx):
    """Says if a user is cool.
    In reality this just checks if a subcommand is being invoked.
    """
    if ctx.invoked_subcommand is None:
        await client.say('No, {0.subcommand_passed} is not cool'.format(ctx))

@client.command(name='bot')
async def _bot():
    """Is the bot cool?"""
    await client.say('Yes, the bot is cool.')
                
                                 
@client.event
async def on_ready():
      await client.change_presence(game=discord.Game(name="Testing..."))
        
        
        
                  

client.run(os.getenv('TOKEN'))

            
