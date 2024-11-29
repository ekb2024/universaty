from aiogram import Bot,Dispatcher,executor,types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State,StatesGroup
from aiogram.types import ReplyKeyboardMarkup,KeyboardButton
from aiogram.types import InlineKeyboardMarkup ,InlineKeyboardButton
import asyncio

api = '7895099985:AAHAaLI6o5Tx21o_jOwSepvQvDlbYJaNJCQ'
bot = Bot(token=api)
dp = Dispatcher(bot,storage=MemoryStorage())

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()

kb = ReplyKeyboardMarkup(resize_keyboard=True)
button1 = KeyboardButton(text='Рассчитать')
button2 = KeyboardButton(text='Информация')
button3 = KeyboardButton(text='Купить',callback_data='formulas')
kb.row(button1,button2)
kb.add(button3)

menu = InlineKeyboardMarkup(
    inline_keyboard=[
        [InlineKeyboardButton(text='Product1', callback_data="product_buying")],
        [InlineKeyboardButton(text='Product2', callback_data="product_buying")],
        [InlineKeyboardButton(text='Product3', callback_data="product_buying")],
        [InlineKeyboardButton(text='Product4', callback_data="product_buying")]
    ],
resize_keyboard=True
)


kb1 = InlineKeyboardMarkup(resize_keyboard=True)
b1 = InlineKeyboardButton(text='Product1', callback_data="product_buying")
b2 = InlineKeyboardButton(text='Product2', callback_data="product_buying")
b3 = InlineKeyboardButton(text='Product3', callback_data="product_buying")
b4 = InlineKeyboardButton(text='Product4', callback_data="product_buying")
kb1.row(b1,b2,b3,b4)

@dp.message_handler(commands=['start'])
async  def start(message):
    await message.answer('Привет! Я бот помогающий твоему здоровью.',reply_markup=kb)

@dp.message_handler(text="Купить")
async def get_buying_list(message):
    list_vit = ['benfotiamine','omega3','sambucol','ultra men']
    for i in range(1,5):
      await message.answer(f'Название: Product {i} Описание: {list_vit[i-1]}  Цена: {i*100}')
      with open(f'files/img{i}.jpg', 'rb') as img:
         await message.answer_photo(img)
    await message.answer('Выбирите продукт для покупки:', reply_markup=kb1)

@dp.callback_query_handler(text="product_buying")
async def send_confirm_message(call):
    await call.message.answer("Вы успешно приобрели продукт!")
    await call.answer()




@dp.message_handler(text='Рассчитать')
async  def set_age(message):
   await message.answer('введите свой возраст')
   await  UserState.age.set()

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
