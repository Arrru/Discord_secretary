import discord, asyncio, os
import youtube_dl
import random
from discord.ext import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse

game = discord.Game("Lost ark")
bot=commands.Bot(command_prefix='*', status=discord.Status.online, activity=game)

token = ""

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
#hello    
@bot.command(aliases=["�ȳ�"])
async def hello(ctx):
 await ctx.reply('���õ� ���� �Ϸ���?')
 
@bot.command(aliases=["���̳�"])
async def seo(ctx):
 await ctx.reply('�������� �ϼ���.')
    
@bot.command(aliases=["�����;�"])
async def missyou(ctx):
 await ctx.reply('������.')

@bot.command(aliases=["���ڽŰ�"])
async def dobak(ctx):
 await ctx.reply('https://cleansports.kspo.or.kr/cleansports/main/main.do')    

#jpg-png
@bot.command(aliases=["����"])
async def yousin(ctx):
 await ctx.message.delete()
 await ctx.send(file=discord.File("����.jpg")) 

@bot.command(aliases=["�ҷ��ʱ���"])
async def nuguri(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File("nuguri.png"))

@bot.command(aliases=["ȭ��"])
async def fire(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File("fire.png"))

@bot.command(aliases=["����"])
async def best(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File("bora.png"))

@bot.command(aliases=["��ũ"])
async def link(ctx):
    await ctx.message.delete()
    await ctx.send("https://series.naver.com/comic/detail.series?productNo=8422565&isWebtoonAgreePopUp=true")

#bye    
@bot.command(aliases=["���־�"])
async def bye(ctx):
 await ctx.reply('���ϵ� ����� ��ٸ��� �����Կ�.')

@bot.command(aliases=["�ֻ���"]) 
async def dice(ctx):
    randnum = random.randrange(1,6)
    await ctx.send(f'�ֻ����� ���� {randnum}��(��) ���Խ��ϴ�.')
     
@bot.command() 
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
  
@bot.command(aliases=["���"])
async def leave(ctx):
    await bot.voice_clients[0].disconnect()

@bot.command(aliases=["�����"])
async def play(ctx, url):
    channel = ctx.author.voice.channel
    if bot.voice_clients == []:
        await channel.connect()
        await ctx.send("connected to the voice channel, " + str(bot.voice_clients[0].channel))        
        
    ydl_opts = {'format': 'bestaudio'}
    FFMPEG_OPTIONS = {'before_options': '-reconnect 1 -reconnect_streamed 1 -reconnect_delay_max 5', 'options': '-vn'}
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        info = ydl.extract_info(url, download=False)
        URL = info['formats'][0]['url']
    voice = bot.voice_clients[0]
    voice.play(discord.FFmpegPCMAudio(URL, **FFMPEG_OPTIONS))

@bot.command(aliases=["���"])
async def pause(ctx):
    if not bot.voice_clients[0].is_paused():
        bot.voice_clients[0].pause()
    else:
        await ctx.send("already paused")

@bot.command(aliases=["�Ѱ�"])
async def skip(ctx):
    try:
        bot.voice_clients[0].stop()
    except:
        await ctx.send("skip error")

@bot.command(aliases=["�ݺ�"])
async def loop(ctx):
    try:
        global loop 
        loop = True if loop == False else False
        await ctx.send(f"���� �ݺ� ����: {loop}")
    except:
        await ctx.send("loop Error")

@bot.command(aliases=["���"])
async def resume(ctx):
    if bot.voice_clients[0].is_paused():
        bot.voice_clients[0].resume()
    else:
        await ctx.send("already playing")
        
@bot.command(aliases=["�׸�"])
async def stop(ctx):
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
    else:
        await ctx.send("not playing")

#clean
@bot.command(aliases=["û��"])
async def clean(ctx, number:int=None):
    if ctx.guild:
        if ctx.message.author.guild_permissions.manage_messages:
            try:
                if number is None:
                    await ctx.send('���ڸ� �Է����ּ���.')
                elif 50 < number:
                    await ctx.message.delete()
                    await ctx.send(f'{ctx.message.author.mention} `50`���� ū ���� �Է��� �� �����ϴ�.', delete_after=5)
                else:
                    deleted = await ctx.message.channel.purge(limit=number)
                    #await ctx.send(f'{ctx.message.author.mention}�� ���� `{len(deleted)}`���� �޼����� �����Ǿ����ϴ�.')
            except:
              await ctx.send("������ �Ұ��մϴ�.")
        else:
          await ctx.send('�� ������ ����� �� �ִ� ������ �����ϴ�.')
    else:
      await ctx.send('DM���� �Ұ��մϴ�.')



bot.run(token)
