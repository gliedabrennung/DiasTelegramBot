from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.enums import ParseMode
from ai_api import ai_api

router = Router()

@router.message(Command('gemma'))
async def gemini(message: Message):
    response = await ai_api(message.text[7:])
    await message.reply(response, parse_mode=ParseMode.MARKDOWN)