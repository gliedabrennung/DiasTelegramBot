from aiogram import Router
from google import genai
from aiogram.filters import Command
from aiogram.types import Message
from config import AI_TOKEN

router = Router()
client = genai.Client(api_key=AI_TOKEN)

@router.message(Command('gemini'))
async def question(message: Message):
    await message.reply(f'Request processing - {message.text[8:]}')

    response = client.models.generate_content(
        model="gemini-2.0-flash", contents=message.text[8:]
    )

    await message.answer(response.text)