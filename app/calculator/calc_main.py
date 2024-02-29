'''app.calculator.calc_main.py: Capture user input and handle invalid input/exceptions'''
from app.commands import Command
from app.calculator import Calculator
from app.utils.validation import validate_decimal_input

class OperationCommand(Command):
    '''A base command class for performing arithmetic operations.'''

    def __init__(self, operation_name, operation_function):
        self.operation_name = operation_name
        self.operation_function = operation_function

    def execute(self):
        '''
        Execute the OperationCommand.

        This method prompts the user to enter two numbers and performs the operation.
        '''
        num1 = validate_decimal_input("Enter the first number: ")
        num2 = validate_decimal_input("Enter the second number: ")

        try:
            result = self.operation_function(num1, num2)
            print(f"The result of {num1} {self.operation_name} {num2} is {result}")
            return result
        except ValueError as e:
            print("Cannot divide by zero.")
            return None
