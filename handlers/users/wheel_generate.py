from aiogram import Dispatcher, types
from aiogram.dispatcher import FSMContext
from fsm.fsm_interview import InterviewStateGroup
from utils.diagramm import Diagramm
from keyboards.default.replyKb_main import kb_main

#-------------------------------------------
# Декоратор проверки введенного пользователем значения на наличие того, что в строке только цифры, и что число >= 0 и <= 10.
#-------------------------------------------
def check_data_input(func):
    async def wrapper(message: types.Message, state: FSMContext):
        if message.text.isdigit() == True and int(message.text) <= 10 and int(message.text) >= 0:
            await func(message, state)
        else:
            await state.finish()
            await message.answer('<b>⛔️ Введены некорректные данные, попробуйте ещё раз! ⛔️</b>', reply_markup=kb_main)
    return wrapper

async def wheel_gen_echo(message : types.Message):
    await message.answer('<b>Как вы оцениваете категорию «Карьера»?🎓 (от 0 до 10)</b>')
    await InterviewStateGroup.carrer.set()

@check_data_input
async def wheel_gen_carrer(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['carrer'] = int(message.text)

    await message.answer('<b>Как вы оцениваете категорию «Семья»?🤰 (от 0 до 10)</b>')
    await InterviewStateGroup.next()

@check_data_input
async def wheel_gen_family(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['family'] = int(message.text)

    await message.answer('<b>Как вы оцениваете категорию «Друзья»?👨‍👧‍👦 (от 0 до 10)</b>')
    await InterviewStateGroup.next()

@check_data_input
async def wheel_gen_friends(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['friends'] = int(message.text)

    await message.answer('<b>Как вы оцениваете категорию «Здоровье»?🏥 (от 0 до 10)</b>')
    await InterviewStateGroup.next()

@check_data_input
async def wheel_gen_health(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['health'] = int(message.text)

    await message.answer('<b>Как вы оцениваете категорию «Хобби»?🧸 (от 0 до 10)</b>')
    await InterviewStateGroup.next()

@check_data_input
async def wheel_gen_hobby(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['hobby'] = int(message.text)

    await message.answer('<b>Как вы оцениваете категорию «Деньги»?💸 (от 0 до 10)</b>')
    await InterviewStateGroup.next()

@check_data_input
async def wheel_gen_money(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['money'] = int(message.text)

    await message.answer('<b>Как вы оцениваете категорию «Отдых»?🎂 (от 0 до 10)</b>')
    await InterviewStateGroup.next()

@check_data_input
async def wheel_gen_relax(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['relax'] = int(message.text)

    await message.answer('<b>Как вы оцениваете категорию «Саморазвитие»?🔬 (от 0 до 10)</b>')
    await InterviewStateGroup.next()

@check_data_input
async def wheel_gen_dev_self(message : types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['dev_self'] = int(message.text)

    await state.finish()
    await message.answer('<b>Формируем ваше колесо баланса...</b>')
    await create_wheel_graph(message, data)

#-------------------------------------------
# Метод создания диаграммы, сохранения её в виде .png фото, отправка пользователю и удаления из папки.
#-------------------------------------------
async def create_wheel_graph(message : types.Message, data):
    diagram = Diagramm(str(message.from_user.id), data)
    await diagram.create_diagram()
    await diagram.send_diagramm_user(message)
    await diagram.delete_wheel_graph()

async def register_wheel_gen_echo(dp : Dispatcher):
    dp.register_message_handler(wheel_gen_echo, lambda message: message.text == '✍ Составить колесо баланса')
    dp.register_message_handler(wheel_gen_carrer, state=InterviewStateGroup.carrer)
    dp.register_message_handler(wheel_gen_family, state=InterviewStateGroup.family)
    dp.register_message_handler(wheel_gen_friends, state=InterviewStateGroup.friends)
    dp.register_message_handler(wheel_gen_health, state=InterviewStateGroup.health)
    dp.register_message_handler(wheel_gen_hobby, state=InterviewStateGroup.hobby)
    dp.register_message_handler(wheel_gen_money, state=InterviewStateGroup.money)
    dp.register_message_handler(wheel_gen_relax, state=InterviewStateGroup.relax)
    dp.register_message_handler(wheel_gen_dev_self, state=InterviewStateGroup.dev_self)
