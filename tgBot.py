import asyncio
import logging
import sys

from steamguard import SteamMobile

from aiogram import Bot, Dispatcher, html
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message


# All handlers should be attached to the Router (or Dispatcher)

dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    """
    This handler receives messages with `/start` command
    """
    # Most event objects have aliases for API methods that can be called in events' context
    # For example if you want to answer to incoming message you can use `message.answer(...)` alias
    # and the target chat will be passed to :ref:`aiogram.methods.send_message.SendMessage`
    # method automatically or call API method directly via
    # Bot instance: `bot.send_message(chat_id=message.chat.id, ...)`
    await message.answer('Для получения кода Steam Guard введите логин от аккаунта')


@dp.message()
async def echo_handler(message: Message) -> None:
    """
    Handler will forward receive a message back to the sender

    By default, message handler will handle all message types (like a text, photo, sticker etc.)
    """
    login = message.text
    mobile = SteamMobile(login, '')

    mobile_data = mobile.load_exported_data(f'{mobile.account_name}_mobile.json')
    mobile.load_mobile(mobile_data)

    guard_code = mobile.generate_steam_guard_code()
    if guard_code is None:
        await message.answer("Аккаунт не найден")
    else:
        await message.answer(f"Ваш код от Steam Guard: {guard_code}")



async def initialize_bot(token) -> None:
    # Initialize Bot instance with default bot properties which will be passed to all API calls
    bot = Bot(token=token, default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    # And the run events dispatching
    await dp.start_polling(bot)


def run_bot(token) -> None:
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(initialize_bot(token))
