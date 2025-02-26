import io
from aiogram import Router
from google import genai
from aiogram.filters import Command
from aiogram.types import Message
from config import AI_TOKEN
from PIL import Image

router = Router()
client = genai.Client(api_key=AI_TOKEN)

@router.message(Command('gemini'))
async def question(message: Message):
    if message.content_type != 'photo':
        await message.reply(f'Request processing - {message.text[8:]}')
        try:
            response = client.models.generate_content(
                model="gemini-2.0-flash-exp", contents=message.text[8:]
            )
            await message.answer(response.text)
        except:
            await message.reply("Я твой рот ебал. Где запрос?")

    elif message.content_type == 'photo':
        picca = message.caption[8:]
        if picca == '':
            picca = "What is this?"
        photo = message.photo[-1]
        file_id = photo.file_id
        file_info = await message.bot.get_file(file_id)
        downloaded_file = await message.bot.download_file(file_info.file_path)
        image = Image.open(io.BytesIO(downloaded_file.getvalue()))
        response = client.models.generate_content(
            model="gemini-2.0-flash", contents=[picca, image]
        )
        #ya zaebalsya
        await message.answer(response.text)