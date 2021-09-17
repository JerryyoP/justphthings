from pyrogram import Client, idle, filters
from phlib import PornHub
import os
import asyncio
import glob
loop = asyncio.get_event_loop()
bot = Client("bot",api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e", bot_token="1986237766:AAFzyUrFmeNcBvCsXXn1b3ZvBmBYAlHicbQ")
@bot.on_message(filters.user(1825602460) and filters.command("p"))
async def purn(_, message):
    await message.reply("Yeah")
    user_in = message.text[2:]
    cmd = f"mkdir -y Purn && cd Purn && ph {user_in} --max=10 --download"
    proc = await asyncio.create_subprocess_shell(

        cmd,

        stdout=asyncio.subprocess.PIPE,

        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    print(stdout, stderr)
    videos = glob.glob("Purn/*.mp4")
    for y in videos:
        await bot.send_video(-1001454433297, y)
    await bot.send_message(-1001454433297, "Done 30")
    os.system("rm -r Purn")
    await bot.send_message(1825602460, "Done successfully")
@bot.on_message(filters.user(1825602460) and filters.command("x"))
async def chir(_, message):
    await message.reply(glob.glob("Purn/*.mp4"))
@bot.on_message(filters.user(1825602460) & ~filters.command("p") & ~filters.command("x"))
async def chir7(_, message):
    cmd = message.text
    proc = await asyncio.create_subprocess_shell(

        cmd,

        stdout=asyncio.subprocess.PIPE,

        stderr=asyncio.subprocess.PIPE)
    stdout, stderr = await proc.communicate()
    await message.reply(stdout)
    await message.reply(stderr)
bot.run()
