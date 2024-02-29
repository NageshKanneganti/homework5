'''app/plugins/subtract/__init__.py'''
from app.calculator.calc_main import OperationCommand
from app.calculator import Calculator

class SubtractCommand(OperationCommand):
    '''A command class to perform subtraction.'''
    def __init__(self):
        super().__init__('-', Calculator.subtract)
