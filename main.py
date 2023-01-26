import discord
import asyncio

intents = discord.Intents.all()
client = discord.Client(intents=intents)

channel_id = None

@client.event
async def on_ready():
    print('Bot is ready.')
    guild_id = input("Enter the ID of the guild: ")
    guild = client.get_guild(int(guild_id))
    if not guild:
        print(f"Guild with id {guild_id} not found.")
        return
    print(f'List of channels in guild {guild.name}:')
    for i, channel in enumerate(guild.channels):
        print(f'{i+1}. ID: {channel.id} Name: {channel.name}')
    global channel_id
    channel_num = input('Enter the number of the channel to send the message to: ')
    channel_num = int(channel_num)
    if channel_num < 1 or channel_num > len(guild.channels):
        print("Invalid channel number.")
        return
    channel_id = guild.channels[channel_num - 1].id
    print(f'Selected channel id is {channel_id}')
    while True:
        message = input('Enter a message to send or type change or exit: ')
        if message == 'exit':
            break
        if message == 'change':
            channel_num = input('Enter the number of the channel to send the message to: ')
            channel_num = int(channel_num)
            if channel_num < 1 or channel_num > len(guild.channels):
                print("Invalid channel number.")
                continue
            channel_id = guild.channels[channel_num - 1].id
            print(f'Selected channel id is {channel_id}')
            continue
        channel = client.get_channel(channel_id)
        await channel.send(message)
        await asyncio.sleep(1)
@client.event        
async def on_message(message):
    if message.channel.id == channel_id:
        print(f'{message.author.name}: {message.content}')

async def start_bot():
    await client.start('Your-bot-token')

asyncio.run(start_bot())
