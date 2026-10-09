from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext

class DiagnosticForm (StatesGroup):
    class_first = State()
    smena = State()
    chasovoy_poyas = State()

