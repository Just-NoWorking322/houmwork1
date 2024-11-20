from aiogram import Bot, Dispatcher, types
from aiogram.filters import Command
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import asyncio, logging
from config import token

logging.basicConfig(level=logging.INFO)
bot = Bot(token=token)
dp = Dispatcher()

DATA = {
    "Новости": "Сегодня: курс доллара вырос на 2%, акции падают.",
    "Курсы валют": "Доллар: 85сом, Евро: 90сом.",
    "Контактная информация": "Наша почта: info@example.com. Телефон: +996504077700.",
    "Часто задаваемые вопросы (FAQ)": "1. Как связаться? Ответ: Через почту alisherbolotbekov03@gmail.com.com\n2. Где нас найти? На диване у нас дома"
}

def main_menu():
    buttons = [[KeyboardButton(text=key)] for key in DATA.keys()] 
    menu = ReplyKeyboardMarkup(
        keyboard=buttons,
        resize_keyboard=True
    )
    return menu

@dp.message(Command("start"))
async def start(message: types.Message):
    await message.answer(
        "Добро пожаловать! Я информационный бот.\n"
        "Я могу предоставить информацию по следующим темам:\n"
        "1. Новости\n"
        "2. Курсы валют\n"
        "3. Контактная информация\n"
        "4. FAQ\n"
        "Выберите тему из меню ниже или воспользуйтесь командами:\n"
        "/help - Описание функций\n/about - О боте",
        reply_markup=main_menu()
    )

@dp.message(Command("help"))
async def help_command(message: types.Message):
    await message.answer(
        "Доступные команды:\n"
        "/start - Запустить бота\n"
        "/menu - Вернуться в главное меню\n"
        "/help - Описание функций\n"
        "/about - О проекте"
    )

@dp.message(Command("about"))
async def about_command(message: types.Message):
    await message.answer(
        "Этот бот создан для предоставления полезной информации.\n"
        "Версия: 1.0\nАвтор: @bnshiro"
    )

@dp.message(Command("menu"))
async def menu_command(message: types.Message):
    await message.answer("Выберите тему из меню ниже:", reply_markup=main_menu())

@dp.message(lambda message: message.text in DATA.keys())
async def handle_topics(message: types.Message):
    topic = message.text
    await message.answer(DATA[topic])

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
