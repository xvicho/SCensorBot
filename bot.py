# Discord: Vichoo#9170
# bot.py
import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
GUILD = os.getenv('DISCORD_GUILD')

client = discord.Client()

count = 0
file = open('ban.txt', 'r', encoding='UTF=8')
banwords = file.readlines()[1:]
banwords = [line.rstrip() for line in banwords]
print('The following words are banned:')
print(banwords)

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break
    print(f'{client.user} is connected to the following guild:')
    print(f'{guild.name}(id: {guild.id})')

@client.event
async def on_message(message):
    global count
    msg_content = message.content.lower()
    if any(word in msg_content for word in banwords):
        await message.delete()
        count += 1
    if message.content.startswith('&debug'):
        await message.channel.send('I deleted a total of: ' + str(count) + ' messages.')

client.run(TOKEN)
