import asyncio
from google import genai
from aiogram import Dispatcher, Bot
from aiogram.filters import Command
from aiogram.types import Message
bot = Bot('8069522663:AAFi4AzEJvHwgTvmU2P6IyDDd0uYWszp3gQ')
dp = Dispatcher()

client = genai.Client(api_key="AIzaSyBxiExTTJfY5gZWA9fLZlLi7ZckxpxFqbQ")

@dp.message(Command('gemini'))
async def question(message: Message):
    await message.reply(f'Request processing - {message.text[8:]}')

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=message.text[8:]
    )

    print(response.text)
    await message.answer(response.text)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    try:
        asyncio.run(main())
    except KeyboardInterrupt:
        print("Exit")