import asyncio
import logging

from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command

from config_reader import config
from data_base import db

logging.basicConfig(level=logging.INFO)

bot = Bot(config.bot_token.get_secret_value())

dp = Dispatcher()


COMMAND_HELP = """
Find a problem? Chat @rotateTextChat
coded by @piterparkerX
"""


@dp.message(Command('start'))
async def cmd_start(message: types.Message):
    await message.answer("Hi.. Send me a text (rus, en) and I "
                         "will turn it over...")


@dp.message(Command('help'))
async def cmd_help(message: types.Message):
    await message.answer(COMMAND_HELP)


@dp.message()
async def handler_message(message: types.Message):
    text = translate(message.text)
    await message.answer(text)


def translate(text):
    result = ""
    inglish_data = db.get_en_letter()
    signs_data = db.get_signs_letter()
    russian_data = db.get_rus_letter()

    for sym in text:
        for sym_rus in russian_data.keys():
            if sym == sym_rus:
                sym = russian_data[sym]
        for sym_ing in inglish_data.keys():
            if sym == sym_ing:
                sym = inglish_data[sym]
        for sign in signs_data.keys():
            if sym == sign:
                sym = signs_data[sym]

        result += sym

    return result


async def main():
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
