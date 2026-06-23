import discord
from discord.ext import commands
import os
import asyncio

print("Starting...")

intents = discord.Intents.default()
intents.message_content = True


bot = commands.Bot(
    command_prefix="!", intents=intents
)


@bot.event
async def on_ready():
    print("Logged in as " f"{bot.user}")


async def load_cogs():
    for filename in os.listdir("cogs"):
        if filename.endswith(".py"):
            await bot.load_extension(f"cogs.{filename[:-3]}")


async def main():
    await load_cogs()
    await bot.start(
        
    )


asyncio.run(main())
