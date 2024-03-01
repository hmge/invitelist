import discord
from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv('token')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.event
async def on_ready():
    print('봇에 로그인했어요!')
    for guild in bot.guilds:
        print(f"서버 ID/이름: {guild.name} [{guild.id}]")

@bot.command()
async def 초대링크(ctx, guild_id: int):
    guild = bot.get_guild(guild_id)
    if guild:
        links = await guild.invites()
        message = ''
        if links:
            for link in links:
                message += f"{link.code}: {link.inviter}님이 생성하셨고, 현재까지 {link.uses}번 사용되었어요!\n"
            await ctx.channel.send(message)
        else:
            await ctx.channel.send("해당 서버에는 사용 가능한 초대 링크가 없습니다.")
    else:
        await ctx.channel.send("해당 ID의 서버를 찾을 수 없습니다.")

bot.run(token)