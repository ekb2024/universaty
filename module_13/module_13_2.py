from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
import asyncio

api = '7895099985:AAHAaLI6o5Tx21o_jOwSepvQvDlbYJaNJCQ'
bot = Bot(token=api)
dp = Dispatcher(bot,storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async  def start(message):
    print('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_message(message):
       print('Введите команду /start, чтобы начать общение.')


if __name__=='__main__':
    executor.start_polling(dp,skip_updates=True)





# Done! Congratulations on your new bot. You will find it at
# t.me/universityurbanbot.  university_bot
# You can now add a description, about section and profile picture for your bot, see /help for a list of commands. By the way, when you've finished creating your cool bot, ping our Bot Support if you want a better username for it. Just make sure the bot is fully operational before you do this.
#
# Use this token to access the HTTP API:
# 7895099985:AAHAaLI6o5Tx21o_jOwSepvQvDlbYJaNJCQ
# Keep your token secure and store it safely, it can be used by anyone to control your bot.
#
# For a description of the Bot API, see this page: https://core.telegram.org/bots/api