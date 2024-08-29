import discord
from discord.ext import commands
intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print(f'{bot.user} olarak giriş yaptık')

@bot.command()
async def hello(ctx):
    await ctx.send(f'Merhaba! Ben {bot.user}, bir Discord sohbet botuyum!')

@bot.command()
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command()
async def nasılsın(ctx):
    await ctx.send("İyiyim peki siz?")

@bot.command()
async def whoareyou(ctx):
    await ctx.send("Im a discord chat bot make yourself interesting!")

@bot.command()
async def canyouanswerproperly(ctx):
    await ctx.send("I'm sorry but i might not be able to respond as much as the other cool chat bots but hey atleast i exist lol!")

@bot.command()
async def canyoutalklikeme(ctx):
    await ctx.send("I dont think i can talk perfectly like a human but im still able to talk!")

@bot.command()
async def bye(ctx):
    await ctx.send("Bye!")

@bot.command()
async def choices(ctx):
    await ctx.send("Here is a list of things u can say so i respond: hello, heh, nasılsın, whoareyou, canyouanswerproperly, canyoutalklikeme, bye, choices.")


bot.run("")
