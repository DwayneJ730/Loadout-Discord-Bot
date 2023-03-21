import discord
import responses
import private
from LoadoutCreateView import LoadoutCreateView
from discord.ext import commands

async def send_message(message, user_message, is_private):
    try:
        response = responses.handle_response(user_message)
        await message.author.send(response) if is_private else await message.channel.send(response)
    except Exception as e:
        print(e)


def run_discord_bot():
    TOKEN = private.TOKEN
    intents = discord.Intents.all()
    intents.message_content = True
    intents.members = False
    client = commands.Bot(command_prefix="!", intents=intents)

    @client.event
    async def on_ready():
        print(f'{client.user} is now running')

    @client.event
    async def on_message(message):
        if message.author == client.user:
            return

        username = str(message.author)
        user_message = str(message.content)
        channel = str(message.channel)

        if user_message[0] == '!' and username == "jaybutler328":
            return "Playstation users arent allowed to use this bot"

        if user_message[0] == '?':
            user_message = user_message[1:]
            await send_message(message, user_message, is_private=True)
        else:
            await send_message(message, user_message, is_private=False)

    @client.command()
    async def add(ctx):
        view = LoadoutCreateView()
        await ctx.send(view=view)

    client.run(TOKEN)
