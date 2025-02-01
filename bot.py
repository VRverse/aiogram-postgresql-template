import asyncio
import logging
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import CommandStart
import psycopg2
from psycopg2 import sql

# Конфигурация бота и базы данных
DB_NAME = 'your_db_name'
DB_USER = 'your_db_user'
DB_PASSWORD = 'your_db_password'
DB_HOST = 'your_db_host'
API_TOKEN = 'your_bot_token'
# Настройка логирования
logging.basicConfig(level=logging.INFO)

# Функция для подключения к базе данных
def get_db_connection():
    conn = psycopg2.connect(
        dbname=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST
    )
    return conn

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher()

# Обработчик команды /start
@dp.message(CommandStart())
async def send_welcome(message: Message):
    user_id = message.from_user.id
    username = message.from_user.username
    first_name = message.from_user.first_name

    conn = get_db_connection()
    cur = conn.cursor()

    # Проверяем, существует ли пользователь в базе данных
    cur.execute(
        "SELECT * FROM users WHERE id = %s",
        (user_id,)
    )
    user = cur.fetchone()

    if user is None:
        # Если пользователя нет в базе данных, добавляем его
        cur.execute(
            "INSERT INTO users (id, username, first_name) VALUES (%s, %s, %s)",
            (user_id, username, first_name)
        )
        conn.commit()
        await message.reply("Привет! Ты был добавлен в базу данных.")
    else:
        await message.reply("Привет! Ты уже зарегистрирован в базе данных.")

    cur.close()
    conn.close()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Bot stopped")