from aiogram import Bot, Dispatcher, executor, types
from aiogram.types.web_app_info import WebAppInfo

bot = Bot('6866185903:AAFiYEuXA3T9bUqiwUlfXxMB4J_l3SEEuXI')
dp = Dispatcher (bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    markup = types.ReplyKeyboardMarkup ()
    markup.add(types.KeyboardButton('Открыть веб страницу', web_app=WebAppInfo(url='https://www.google.com')))
    await message.answer('Привет!', reply_markup=markup)


executor.start_polling(dp)
