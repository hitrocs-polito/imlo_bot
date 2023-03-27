import logging
from checkword import checkWord
from transliterate import to_latin, to_cyrillic

from aiogram import Bot, Dispatcher, executor, types

API_TOKEN = '6257227842:AAHMJbo4TMh-G2ti5syZj8hTV4eJgbzEWPM'

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def send_welcome(message: types.Message):
    await message.reply("Imlo lug'atiga xush kelibsiz.\n"
                        "Kiril yoki lotin harflari bilan so'zni kiriting. \n"
                        "Imlosini tekshiring.")


@dp.message_handler(commands=['help'])
async def send_welcome(message: types.Message):
    await message.reply("Kiril yoki lotin harflari bilan so'zni kiriting. \n"
                        "Imlosini tekshiring.")


@dp.message_handler()
async def checkImlo(message: types.Message):
    words = message.text.split()
    for word in words:
        word = to_cyrillic(word)
        result = checkWord(word)

        if result['available']:
            response = f"✅ {word.capitalize()}"
        else:
            response = f"❌ {word.capitalize()}\n"
            if result['matches']:
                response += '_' * 20 + "\n" + "🔽O'xshash so'zlar\n"
                for text in result['matches']:
                    response += f"\n✅ {text.capitalize()}"

        await message.answer(to_latin(response))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
