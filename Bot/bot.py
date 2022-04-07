import discord 
from email.errors import MessageParseError
from discord import Client
from discord.ext import commands
from argparse import ArgumentParser, Namespace 
from dotenv import load_dotenv
import os

class MyBot(Client):
    def __init__(self):
        super().__init__()
        bot = commands.Bot(command_prefix="!")
        self.run("OToken")
        bot.run("OToken")

    async def on_ready(self):
        print("Hello everybody !")
    
    async def on_ready():
        print("Le bot est là")

    async def on_message(ctx, message):
        if message.content == "coucou":
            await message.channel.send("salut")

    default_intents = discord.Intents.default()
    default_intents.members = True
    client = discord.Client(intents=default_intents)

    async def on_member_join(member):
        general_channel = Client.get_channel("https://discordapp.com/channels/958687778831474729/958687779406098456")
        general_channel.send(f"L'utilisateur {member.display_name} a rejoint le serveur, Bienvenue !")

    async def on_message(ctx, message):
        if message.content.startswith("!del"):
            number = int(message.content.split()[1])
            messages = await message.channel.history(limit=number + 1).flatten()
            for each_message in messages:
                await each_message.delete()

    async def delete(ctx, number: int):
        messages = await ctx.channel.history(limit=number + 1).flatten()
        for each_message in messages:
            await each_message.delete()

    load_dotenv(dotenv_path="config")
    Client.run(os.getenv("TOKEN"))


    def parse_args() -> Namespace:
        parser = ArgumentParser()
        parser.add_argument(
            "-c", "--config", help="Config file", required=True, dest="config"
        )
        return parser.parse_args()

Client = MyBot()