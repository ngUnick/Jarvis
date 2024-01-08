import discord
import json

import dialog

client = None

def handle_response(message) -> str:

    botID = client.user.id
    new_message = message.lower().replace(f'<@{botID}>','').strip()
    result = dialog.connect_api(new_message)

    return result




async def send_message(message, user_message):

    try:
        response = handle_response(user_message)

        if response != None:
            await message.channel.send(response)

    except Exception as e:
        print(e)


def run_discord_bot():

    # API Token Security
    with open('token.json') as f:
        data = json.load(f)

    TOKEN = data["discord"]
    
    
    intents = discord.Intents.default()  # This sets up the default intents
    intents.message_content = True  # Enable the Message Content intent
    global client
    client = discord.Client(intents=intents)


    @client.event
    async def on_ready():
        #print(f'{client.user} is now running!')
        print('Irthe h wra na xysw')


    @client.event
    async def on_message(message):

        self = client.user
        channel = message.channel
        isDM:bool = isinstance(channel, discord.channel.DMChannel)

        if message.author == self or (self not in message.mentions and not isDM):
            return
        

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        print(f"{username} said: '{user_message}' ({channel})")


        await send_message(message, user_message)

    client.run(TOKEN)





if __name__ == '__main__':
    run_discord_bot()