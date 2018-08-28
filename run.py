import discord
from discord.ext import commands
import random
import asyncio
import time
import os



Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["LOL", "LMAO", "LEL"]
bypass_list = []



@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.send_message(message.channel, "**Hey!** What so funny")
                except discord.errors.NotFound:
                    return
                
                
                

      
                        
                                 
@client.event
async def on_ready():
      await client.change_presence(game=discord.Game(name="Testing & Fixing ⛏"))
        
        
        
      
        
client.run(os.getenv('TOKEN'))
