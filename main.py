import discord
from pathlib import Path  # Python 3.6+ only
import dotenv as env

all_commands = [
    '!test',
    '!faa',
    '!journeydrop',
    '!lucio'
    ]

basic_commands = {
    '!test':'this is a map test', 
    '!faa2':'a map'
    }

env_path = Path('.') / '.env'

key = env.get_key(env_path, 'BOT_TOKEN')

client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user} successfully connected.')
    await client.change_presence(activity=discord.Game('!help'))

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content in basic_commands.keys():
        await message.channel.send(basic_commands.get(message.content, 'Invalid command.'))
    elif message.content == '!faa':
        await message.channel.send(file=discord.File('faahlguide.png'))
client.run(key)