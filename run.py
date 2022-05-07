import discord, asyncio, os
import youtube_dl
import random
from discord.ext import commands
from urllib.request import urlopen
from bs4 import BeautifulSoup
from urllib import parse

game = discord.Game("Lost ark")
bot=commands.Bot(command_prefix='*', status=discord.Status.online, activity=game)

token = "OTcxOTY3Njg2Nzg1NTI3ODU5.YnSNcg.J9hoHsq5OHrMOZr6hvsNhbP_hEU"

@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))
    
#hello    
@bot.command(aliases=["안녕"])
async def hello(ctx):
 await ctx.reply('오늘도 좋은 하루죠?')
 
@bot.command(aliases=["서이넴"])
async def seo(ctx):
 await ctx.reply('안전운전 하세요.')
    
@bot.command(aliases=["보고싶어"])
async def missyou(ctx):
 await ctx.reply('저도요.')

@bot.command(aliases=["도박신고"])
async def dobak(ctx):
 await ctx.reply('https://cleansports.kspo.or.kr/cleansports/main/main.do')    

#jpg-png
@bot.command(aliases=["유죄"])
async def yousin(ctx):
 await ctx.message.delete()
 await ctx.send(file=discord.File("유죄.jpg")) 

@bot.command(aliases=["불량너구리"])
async def nuguri(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File("nuguri.png"))

@bot.command(aliases=["화형"])
async def fire(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File("fire.png"))

@bot.command(aliases=["보라"])
async def best(ctx):
    await ctx.message.delete()
    await ctx.send(file=discord.File("bora.png"))

@bot.command(aliases=["링크"])
async def link(ctx):
    await ctx.message.delete()
    await ctx.send("https://series.naver.com/comic/detail.series?productNo=8422565&isWebtoonAgreePopUp=true")

#bye    
@bot.command(aliases=["잘있어"])
async def bye(ctx):
 await ctx.reply('내일도 당신을 기다리고 있을게요.')

@bot.command(aliases=["주사위"]) 
async def dice(ctx):
    randnum = random.randrange(1,6)
    await ctx.send(f'주사위를 굴려 {randnum}이(가) 나왔습니다.')
     
@bot.command() 
async def join(ctx):
    channel = ctx.author.voice.channel
    await channel.connect()
  
@bot.command(aliases=["잠깐만"])
async def leave(ctx):
    await bot.voice_clients[0].disconnect()

@bot.command(aliases=["들려줘"])
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

@bot.command(aliases=["잠시"])
async def pause(ctx):
    if not bot.voice_clients[0].is_paused():
        bot.voice_clients[0].pause()
    else:
        await ctx.send("already paused")

@bot.command(aliases=["넘겨"])
async def skip(ctx):
    try:
        bot.voice_clients[0].stop()
    except:
        await ctx.send("skip error")

@bot.command(aliases=["반복"])
async def loop(ctx):
    try:
        global loop 
        loop = True if loop == False else False
        await ctx.send(f"현재 반복 상태: {loop}")
    except:
        await ctx.send("loop Error")

@bot.command(aliases=["계속"])
async def resume(ctx):
    if bot.voice_clients[0].is_paused():
        bot.voice_clients[0].resume()
    else:
        await ctx.send("already playing")
        
@bot.command(aliases=["그만"])
async def stop(ctx):
    if bot.voice_clients[0].is_playing():
        bot.voice_clients[0].stop()
    else:
        await ctx.send("not playing")

#clean
@bot.command(aliases=["청소"])
async def clean(ctx, number:int=None):
    if ctx.guild:
        if ctx.message.author.guild_permissions.manage_messages:
            try:
                if number is None:
                    await ctx.send('숫자를 입력해주세요.')
                elif 50 < number:
                    await ctx.message.delete()
                    await ctx.send(f'{ctx.message.author.mention} `50`보다 큰 수는 입력할 수 없습니다.', delete_after=5)
                else:
                    deleted = await ctx.message.channel.purge(limit=number)
                    #await ctx.send(f'{ctx.message.author.mention}에 의해 `{len(deleted)}`개의 메세지가 삭제되었습니다.')
            except:
              await ctx.send("삭제가 불가합니다.")
        else:
          await ctx.send('이 명령을 사용할 수 있는 권한이 없습니다.')
    else:
      await ctx.send('DM에선 불가합니다.')



bot.run(token)
