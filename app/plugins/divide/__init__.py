'''app/plugins/divide/__init__.py'''
from app.calculator.calc_main import OperationCommand
from app.calculator import Calculator

class DivideCommand(OperationCommand):
    '''A command class to perform division.'''
    def __init__(self):
        super().__init__('/', Calculator.divide)
