import disnake
import os
from dotenv import load_dotenv
import os
from disnake.ext import commands

class StarscapeBot(commands.Bot):
    def __init__(self):
        intents = disnake.Intents.all()
        super().__init__(command_prefix="!", intents=intents)
    
    async def setup_hook(self):
        for filename in os.listdir("./cogs") -> None:
            if filename.endswith(".py"):
                self.load_extension(f"cogs.{filename[:-3]}")
    
    async def on_ready(self) -> None:
        print(f'Logged in as {self.user} (ID: {self.user.id})')

bot = StarscapeBot()

load_dotenv()
TOKEN = os.getenv("BOT_TOKEN")

@bot.command()
@commands.is_owner()
async def load(ctx, extension) -> None:
  bot.load_extension(f'cogs.{extension}')
  await ctx.send("Succesfully did it poggers")

@bot.command()
@commands.is_owner()
async def unload(ctx, extension) -> None:
  bot.unload_extension(f'cogs.{extension}')
  await ctx.send("Succesfully did it poggers")

@bot.command()
@commands.is_owner()
async def reload(ctx, extension) -> None:
  bot.unload_extension(f'cogs.{extension}')
  bot.load_extension(f'cogs.{extension}')
  await ctx.send("Did it")

bot.run(TOKEN)
