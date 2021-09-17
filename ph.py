from pyrogram import Client, idle, filters
from phlib import PornHub
import os
import asyncio
import glob
loop = asyncio.get_event_loop()
bot = Client("bot",api_id=6, api_hash="eb06d4abfb49dc3eeb1aeb98ae0f581e", bot_token="1986237766:AAFzyUrFmeNcBvCsXXn1b3ZvBmBYAlHicbQ")
@bot.on_message(filters.user(1825602460) and filters.command("p"))
async def purn(_, message):
    os.system("mkdir Purn && cd Purn && ph thicc boobs --max=5 --download")
    videos = glob.glob("Purn/*.mp4")
    for y in videos:
        await bot.send_video(-1001454433297, y)
    await bot.send_message(-1001454433297, "Done 30")
    os.system("rm -r Purn")
    await bot.send_message(1825602460, "Done successfully")
bot.run()
