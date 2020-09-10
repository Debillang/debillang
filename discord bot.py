import discord
import os
from discord.ext import commands

client = commands.Bot(command_prefix='!')

token = "NzUzMzAzOTcxMDE1Mjk1MTI3.X1kO_g.24ipDO64orTcKAIksvqQQrdkbOk"

@client.event
async def on_ready():
    print(client.user.id)
    print("ready")
    game = discord.Game("기승이 싫어")
    await client.change_presence(status=discord.Status.online, activity=game)
@client.event
async def on_message(message):
    if message.content.startswith("안녕"):
        await message.channel.send("오냐")
    if message.content.startswith("진주"):
        await message.channel.send("Pearl")
    if message.content.startswith("선우"):
        await message.channel.send("꼴초")
    if message.content.startswith("!사진"):
        pic = message.content.split(" ")[1]
        await message.channel.send(file=discord.File(pic))
@client.command(name="정리", pass_context=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'총{amount}개의 메시지를 삭제 했습니다.')

access_token = os.environ["BOT_TOKEN"]
client.run("access_token")
