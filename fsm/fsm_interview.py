from aiogram.dispatcher.filters.state import StatesGroup, State

class InterviewStateGroup(StatesGroup):
    carrer = State()
    family = State()
    friends = State()
    health = State()
    hobby = State()
    money = State()
    relax = State()
    dev_self = State() 
