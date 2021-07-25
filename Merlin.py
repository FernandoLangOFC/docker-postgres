import discord
from discord.ext import commands
from Youtube import YTDLSource


Bot = commands.Bot(command_prefix='>')
Bot.remove_command('help')

TOKEN = 'ODIyODY2Njk1Njg4NjgzNTkw.YFYgVA.sG4-D_zmej5-GRffDCL6OolJ56I'

@Bot.command()
async def connect(ctx):
    author = ctx.message.author
    voice_channel = author.voice.channel
    vc = await voice_channel.connect()

@Bot.command()
async def play(ctx, url : str):
    if ctx.voice_client != None and ctx.voice_client.is_playing():
        ctx.voice_client.stop()
    new_url = url
    if '>>' in url:
      new_url = url.replace('>>', ' ')
    music = await YTDLSource.from_url(new_url)
    ctx.voice_client.play(music)

@Bot.command()
async def disconnect(ctx):
    server = ctx.message.author
    channel = server.voice.channel
    voice_client = ctx.guild.voice_client
    if voice_client:
        await voice_client.disconnect()
        print("Bot left the voice channel")
    else:
        print("Bot was not in channel")

@Bot.command()
async def pause(ctx):
    voice = ctx.guild.voice_client 
    voice.pause()

@Bot.command()
async def resume(ctx):
    voice = ctx.guild.voice_client 
    voice.resume()

@Bot.command()
async def stop(ctx):
    voice = ctx.guild.voice_client 
    voice.stop()

Bot.run(TOKEN)