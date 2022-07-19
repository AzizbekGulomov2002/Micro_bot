import  logging
from environs import Env

env = Env()
env.read_env()

API_TOKEN=env.str("API_TOKEN")

from aiogram import Bot, Dispatcher, executor, types



logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start', 'help']) 
async def send_welcome(mesage:types.Message):
    await mesage.reply("Assalomu alaykum hurmatli foydalanuvchi")
    
    
@dp.message_handler()
async def echo(message:types.Message):
    await message.answer(message.text)
    
if __name__=='__main__':
    executor.start_polling(dp, skip_updates=True)