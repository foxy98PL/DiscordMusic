import discord
from discord.ext import commands
import music

cogs = [music]



client = commands.Bot(command_prefix='?', intents = discord.Intents.all())
for i in range(len(cogs)):
  cogs[i].setup(client)
client.run("ODk3MTg0NjUzNDA3MDU1ODcy.YWR-Ug.3q7MMuemywb1TRDd3urzFaPPLz8")