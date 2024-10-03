import json

from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery, CallbackGame

BOT_TOKEN = 'Токен бота'

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command(commands=['start']))
async def process_start_command(message: Message):
    game_button = InlineKeyboardButton(text='Кнопка для запуска игры', callback_game=CallbackGame())
    keyboard = InlineKeyboardMarkup(inline_keyboard=[[game_button]])

    await message.answer_game(
        game_short_name='testGame',
        text='Сообщение для запуска игры',
        reply_markup=keyboard
    )


@dp.callback_query(F.game_short_name == 'testGame')
async def process_game_press(callback: CallbackQuery):
    await callback.answer(url='https://nytrock.github.io/TestGame/')


if __name__ == '__main__':
    dp.run_polling(bot)
