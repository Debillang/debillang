import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='!')

@bot.event
async def on_ready():
    print(bot.user.id)
    print("ready")
    game = discord.Game("기승이 싫어")
    await bot.change_presence(status=discord.Status.online, activity=game)
@bot.event
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

    await bot.process_commands(message)
@bot.command()
async def ping(ctx):
    await ctx.send('pong')
@bot.command(name="정리", pass_context=True)
async def clear(ctx, amount : int):
    await ctx.channel.purge(limit=amount)
    await ctx.send(f'총{amount}개의 메시지를 삭제 했습니다.')

bot.run("NzUzMzAzOTcxMDE1Mjk1MTI3.X1kO_g.24ipDO64orTcKAIksvqQQrdkbOk")
