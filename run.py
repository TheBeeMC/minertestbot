import discord
from discord.ext import commands
import random
import asyncio
import time
import os



Client = discord.Client()
client = commands.Bot(command_prefix = "?")

chat_filter = ["?HELP", "HELP", "I NEED HELP"]
bypass_list = []



@client.event
async def on_message(message):
    contents = message.content.split(" ") #contents is a list type
    for word in contents:
        if word.upper() in chat_filter:
            if not message.author.id in bypass_list:
                try:
                    await client.send_message(message.channel, "***Commands Plugin Commands***)
                    await client.send_message(message.channel, "!help)                          
                except discord.errors.NotFound:
                    return
                
                
                

      
                        
                                 
        
        
        
      
        
client.run(os.getenv('TOKEN'))
