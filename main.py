import discord
from pathlib import Path  # Python 3.6+ only
import dotenv as env

all_commands = [
    '!test',
    '!faa',
    '!journeydrop',
    '!lucio'
    ]

env_path = Path('.') / '.env'

key = env.get_key(env_path, 'BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content in all_commands:
        await message.channel.send('this is another test')
        
    
    if message.content == '!test':
        await message.channel.send('heyo')


client.run(key)