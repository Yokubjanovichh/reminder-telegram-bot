import os
import random
import asyncio

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


def get_random_time():
    hour = 5
    minute = random.randint(0, 4) + 18
    return f"{hour:02}:{minute:02}"


async def send_message(chat_ids):
    message = random.choice(MESSAGES)
    for chat_id in chat_ids:
        await bot.send_message(chat_id=chat_id, text=message)


async def scheduler():
    while True:
        random_time = get_random_time()
        schedule.every().day.at(random_time).do(
            lambda: asyncio.create_task(send_message(CHAT_IDS))
        )
        while schedule.get_jobs():
            schedule.run_pending()
            await asyncio.sleep(1)
        schedule.clear()


async def main():
    await scheduler()


if __name__ == "__main__":
    asyncio.run(main())
