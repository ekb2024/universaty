from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup ,InlineKeyboardButton
import asyncio

api = ''
bot = Bot(token=api)
dp = Dispatcher(bot,storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = InlineKeyboardMarkup()
button = InlineKeyboardButton(text='Рассчитать норму калорий',callback_data='calories')
button1 = InlineKeyboardButton(text='Формула расчета',callback_data='formulas')
kb.row(button,button1)

@dp.message_handler(commands=['start'])
async  def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.')

@dp.message_handler(text='Рассчитать')
async def main_menu(message):
    await message.answer('Выберите опцию:',reply_markup=kb)

@dp.callback_query_handler(text='formulas')
async def get_formulas(call):
    await call.message.answer('10 x вес (кг) + 6,25 x рост (см) – 5 x возраст (г) – 161')
    await call.answer()

@dp.callback_query_handler(text='calories')
async  def set_age(call):
   await call.message.answer('введите свой возраст')
   await call.answer()
   await UserState.age.set()

@dp.message_handler(state=UserState.age)
async  def set_growth(message, state):
    await  state.update_data(age=message.text)
    await  message.answer('введите свой рост в см ')
    await  UserState.growth.set()

@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await  state.update_data(growth=message.text)
    await  message.answer('введите свой вес в кг ')
    await  UserState.weight.set()

@dp.message_handler(state=UserState.weight)
async  def send_calories(message, state):
     await state.update_data(weight=message.text)
     data = await state.get_data()
     try:
          await message.answer(f' ваша норма колорий {10 * int(data["weight"]) + 6.25 * int(data["growth"]) - 5 * int(data["age"]) + 5}')
     except ValueError:
            await message.answer('отсутсвуют необходимые данные попробуйте еще раз ')
     await state.finish()


if  __name__== '__main__':
    executor.start_polling(dp,skip_updates=True)
