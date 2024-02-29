'''tests/test_op_command_plugins.py: Tests for operation command plugins'''
from decimal import Decimal
from unittest.mock import patch
import pytest
from app.plugins.add import AddCommand
from app.plugins.divide import DivideCommand
from app.plugins.multiply import MultiplyCommand
from app.plugins.subtract import SubtractCommand

@pytest.mark.parametrize("command_cls, input_values, expected_result", [
    (AddCommand, ['2', '3'], Decimal('5')),
    (DivideCommand, ['6', '2'], Decimal('3')),
    (DivideCommand, ['6', '0'], None),  # Expecting None for division by zero
    (MultiplyCommand, ['2', '3'], Decimal('6')),
    (SubtractCommand, ['5', '3'], Decimal('2'))
])
def test_command_execution(command_cls, input_values, expected_result):
    '''Test the execute function of a command.'''
    with patch('builtins.input', side_effect=input_values):
        command = command_cls()
        result = command.execute()
        assert result == expected_result, f"The result should be {expected_result}"
