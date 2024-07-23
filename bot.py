import os
import asyncio
from random import randint, choice


import schedule
from telegram import Bot

API_TOKEN = os.getenv("TOKEN")
CHAT_IDS = os.getenv("CHAT_IDS")

MESSAGES = [
    "Bollar vazifalar nima buldi, qanday yordam kerak",
    "Nima gap bollar vazifalar qalay ketyabdi",
    "Hayirli kech hammaga, uyga vazifalar boshladinlarmi, kimni qanday savoli bor",
    "Asslomu alaykum hammaga, uyga vazifalarni boshladinglarmi? savol bulsa aytinglar, dars kuni qimadim desanglar jazolar qattiq buladi",
]
bot = Bot(token=API_TOKEN)


async def send_message(chat_ids: str):
    message = choice(MESSAGES)
    for chat_id in chat_ids.split():
        await bot.send_message(chat_id=chat_id, text=message)


async def scheduler():
    while True:
        schedule.every().day.at(f"14:{randint(20, 40)}").do(
            lambda: asyncio.create_task(send_message(CHAT_IDS))
        )
        while schedule.get_jobs():
            schedule.run_pending()
            await asyncio.sleep(1)
        schedule.clear()


if __name__ == "__main__":
    asyncio.run(scheduler())
