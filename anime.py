
import discord
import requests
from discord.ext import commands


bot = commands.Bot(command_prefix="!")


@bot.command()
@commands.is_nsfw()
async def hentai(ctx):
    r = requests.get("https://nekos.life/api/v2/img/hentai")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
@commands.is_nsfw()
async def boobs(ctx):
    r = requests.get("https://nekos.life/api/v2/img/boobs")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)

@bot.command()
@commands.is_nsfw()
async def bj(ctx):
    r = requests.get("https://nekos.life/api/v2/img/bj")
    res = r.json()
    em = discord.Embed()
    em.set_image(url=res['url'])
    await ctx.send(embed=em)


# https://nekos.life/api/v2/endpoints

bot.run("")
