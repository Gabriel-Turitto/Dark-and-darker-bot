import discord
import responses
import aiohttp

TOKEN = 'MTE2NTExMDMzNDk3ODI2NTE0OQ.GPHW-K.A1DZbNxrdb7HmE4ufB207hTo8xpDsiUFtJFCFs'

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)



def run_discord_bot():
    TOKEN = 'MTE2NTExMDMzNDk3ODI2NTE0OQ.GPHW-K.A1DZbNxrdb7HmE4ufB207hTo8xpDsiUFtJFCFs'
    intents = discord.Intents.default()
    intents.message_content = True
    client = discord.Client(intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.content.startswith('!check_dark_server'):
            async with aiohttp.ClientSession() as session:
                try:
                    async with session.get('http://darkanddarker.com/') as dark_response:
                        if dark_response.status == 200:
                            await message.channel.send('The Dark server is up and running!')
                        else:
                            await message.channel.send('The Dark server is down.')
                except aiohttp.ClientError as e:
                    await message.channel.send('There was an error while checking the Dark server.')
        elif message.content.startswith('!hello'):
            await message.channel.send('Hello! Welcome to the Dark and Darker server.')
        elif message.content.startswith('!test'):
            await message.channel.send('This test worked!!')


    client.run(TOKEN)
