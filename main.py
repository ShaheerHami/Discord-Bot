import discord
import os
import random
import pyjokes



client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    msg = message.content
  
    # Bot sends back text 
    if message.content.startswith('hello'):
        await message.channel.send('Hello!')
    
    if message.content.startswith('bye'):
        await message.channel.send('See you later!')

    if message.content.startswith("tell me a joke"):
      await message.channel.send(pyjokes.get_joke())
    
    # Bot sends back memes in .png format
    if message.content.startswith("meme1"):
      await message.channel.send(file=discord.File('meme_1.png'))
    if message.content.startswith("meme2"):
      await message.channel.send(file=discord.File('meme_2.png'))
    if message.content.startswith("meme3"):
      await message.channel.send(file=discord.File('meme_3.jpg'))
    if message.content.startswith("meme4"):
      await message.channel.send(file=discord.File('meme_4.jpg'))
    if message.content.startswith("meme5"):
      await message.channel.send(file=discord.File('meme_5.jpg'))
    

client.run(os.getenv('TOKEN'))