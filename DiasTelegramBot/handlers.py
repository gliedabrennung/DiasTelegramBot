from aiogram import Router
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.exceptions import TelegramBadRequest
from ai_api import ai_api, describe_photo
from utils import sanitize_markdown
from PIL import Image
import logging
import io

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler("bot.log"),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)

router = Router()

@router.message(Command('gemini'))
async def gemini(message: Message):
    if message.content_type != 'photo':
        response = await ai_api(message.text[8:])
        logger.info(f'User asks: {message.text[8:]}')
        try:
            await message.reply(response, parse_mode='Markdown')
        except TelegramBadRequest:
            logger.warning('Getting telegram bad request, converting answer')
            safe_response = sanitize_markdown(response[:4000])
            await message.reply(safe_response, parse_mode='Markdown')
    elif message.content_type == 'photo':
        image_response = message.caption[8:]
        if image_response == '':
            image_response = 'Что это?'
        photo = message.photo[-1]
        file_id = photo.file_id
        file_info = await message.bot.get_file(file_id)
        downloaded_file = await message.bot.download_file(file_info.file_path)
        image = Image.open(io.BytesIO(downloaded_file.getvalue()))
        response = await describe_photo(image_response, image)
        logger.info(f'User asks: {image_response}')
        try:
            await message.reply(response, parse_mode='Markdown')
        except TelegramBadRequest:
            logger.warning('Getting telegram bad request, converting answer')
            safe_response = sanitize_markdown(response[:4000])
            await message.reply(safe_response, parse_mode='Markdown')
