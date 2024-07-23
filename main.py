import logging
from telegram import Bot
from telegram.ext import Application, CommandHandler
import schedule
import asyncio
import time
import random

# Set up logging
logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s", level=logging.INFO
)
logger = logging.getLogger(__name__)

API_TOKEN = "6790345916:AAFxN-guxFody59fok_TnNSPXLKDyJtwFNo"
CHAT_IDS = [
    "6994775622",
    "-4114464482",
]  # Add more chat IDs as needed

MESSAGES = [
    "Hello Jahongir, how are you today?",
    "Good day Jahongir! Hope you're doing well.",
    "Hey Jahongir! Just checking in.",
    "Hi Jahongir, wishing you a great day!",
    "Jahongir, don't forget to smile today!",
    # Add more messages as needed
]

# Initialize the bot
bot = Bot(token=API_TOKEN)


def get_random_time():
    hour = 23
    minute = random.randint(0, 3) + 36
    return f"{hour:02}:{minute:02}"


async def send_message(chat_ids):
    message = random.choice(MESSAGES)
    for chat_id in chat_ids:
        await bot.send_message(chat_id=chat_id, text=message)


async def scheduler():
    while True:
        random_time = get_random_time()
        logger.info(f"Scheduling message at {random_time}")
        schedule.every().day.at(random_time).do(
            lambda: asyncio.create_task(send_message(CHAT_IDS))
        )

        while schedule.get_jobs():
            schedule.run_pending()
            await asyncio.sleep(1)

        # Clear the schedule to avoid duplicate jobs
        schedule.clear()


async def main():
    await scheduler()


if __name__ == "__main__":
    asyncio.run(main())
