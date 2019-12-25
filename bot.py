import discord
from discord.ext import commands
import json

bot = commands.Bot(command_prefix='hr.')


async def createProfile(ctx):
    profile = {
        "Discord id": ctx.author.id,
        "Discord name": ctx.author.name,
        "Time": 0,
        "Seconds": 0,
        "Minutes": 0,
        "Hours": 0,
        "Cookies": 0
    }
    with open("profiles/" + str(ctx.author.id) + ".json", "w") as file:
        json.dump(profile, file, indent=4)
    await ctx.send(profile)


async def giveCurrency(ctx, time : None, seconds : None, minutes : None, hours : None, cookies : None):
    print(time, seconds, minutes, hours, cookies)

    with open("profiles/" + str(ctx.author.id) + ".json", 'r+') as f:
        data = json.load(f)
        profile = {
            "Discord id": ctx.author.id,
            "Discord name": ctx.author.name,
            "Time": data["Time"] + int(time),
            "Seconds": data["Seconds"] + int(seconds),
            "Minutes": data["Minutes"] + int(minutes),
            "Hours": data["Hours"] + int(hours),
            "Cookies": data["Cookies"] + int(cookies)
        }
        print(profile)


@bot.command()
async def create(ctx):
    await createProfile(ctx)


@bot.command()
async def give(ctx, time, seconds, minutes, hours, cookies):
    await giveCurrency(ctx, time, seconds, minutes, hours, cookies)


bot.run('')
