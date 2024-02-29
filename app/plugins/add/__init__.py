'''app/plugins/add/__init__.py'''
from app.calculator.calc_main import OperationCommand
from app.calculator import Calculator

class AddCommand(OperationCommand):
    '''A command class to perform addition.'''
    def __init__(self):
        super().__init__('+', Calculator.add)
