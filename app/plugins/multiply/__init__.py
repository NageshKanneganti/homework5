'''app/plugins/multiply/__init__.py'''
from app.calculator.calc_main import OperationCommand
from app.calculator import Calculator

class MultiplyCommand(OperationCommand):
    '''A command class to perform multiplication.'''
    def __init__(self):
        super().__init__('*', Calculator.multiply)
