from aiogram.fsm.state import State, StatesGroup

class Meals(StatesGroup):
    quantity = State()

class Teas(StatesGroup):
    quantity = State()

class Cakes(StatesGroup):
    quantity = State()

class Salads(StatesGroup):
    quantity = State()

class Drinks(StatesGroup):
    quantity = State()