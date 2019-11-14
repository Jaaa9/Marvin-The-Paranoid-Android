import discord

client = discord.Client()


@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if any([keyword in message.content() for keyword in('bush','quote','tiss')]):
        await message.channel.send('Heres a quote')

client.run('your token')
