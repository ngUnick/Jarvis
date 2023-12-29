import discord
import json

# Read the token from token.json
with open("token.json", "r") as file:
    token_data = json.load(file)

token = token_data.get("token.json")


bot = discord.Client(intents=discord.Intents.default())

@bot.event
async def on_ready():
    guild_count = 0

    for guild in bot.guilds:

        print(f"- {guild.id} (name: {guild.name})")

        guild_count = guild_count + 1

    print("SampleDiscord is in " + str(guild_count) + "guilds.")

@bot.event
async def on_message(message):
	# CHECKS IF THE MESSAGE THAT WAS SENT IS EQUAL TO "HELLO".
	if message.content == "hello":
		# SENDS BACK A MESSAGE TO THE CHANNEL.
		await message.channel.send("hey dirtbag")

bot.run(token)


