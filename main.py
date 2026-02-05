from telegram import Bot
from config import BOT_TOKEN, CHAT_ID

def main():
    bot = Bot(token=BOT_TOKEN)
    bot.send_message(
        chat_id=CHAT_ID,
        text="🤖 ربات اخبار فارکس با موفقیت روشن شد!"
    )

if __name__ == "__main__":
    main()
