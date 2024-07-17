from aiogram.fsm.state import State, StatesGroup

class Meals(StatesGroup):
    quantity = State()

class Teas(StatesGroup):
    quantity = State()