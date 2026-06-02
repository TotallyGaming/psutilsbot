import discord
from discord.ext import commands
import os
import psutil

discord.utils.setup_logging()



class PublicCommands(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        print(f"{self.__class__.__name__} cog loaded")


    @commands.command()
    async def pcstats(self, ctx):
        stats = ["CPU usage:" f" {psutil.cpu_percent()}", "PC uptime (time since restart):" f" {psutil.boot_time()}", "Battery percent:" f" {psutil.sensors_battery().percent}%" ]
        
        message = (
            "PC statistics:\n\n"
        )
        message += "\n".join(f"* {stat}" for stat in stats)
        await ctx.send(message)


async def setup(bot):
    await bot.add_cog(PublicCommands(bot))