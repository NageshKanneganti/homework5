'''Tests for app/utils/validation.py'''
# Disable specific pylint warnings that are not relevant for this file.
# pylint: disable=unnecessary-dunder-call, invalid-name
from decimal import Decimal
import pytest
from app.utils.validation import validate_decimal_input, validate_division_operands

@pytest.fixture
def mock_input(monkeypatch):
    '''Mock input function.'''
    inputs = iter(['invalid', '5.25'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

@pytest.mark.parametrize("input_values, expected_output", [
    (['invalid', '5.25'], Decimal('5.25')),  # Valid input
    (['invalid', '10'], Decimal('10')),      # Valid integer input
    (['invalid', '5.25'], Decimal('5.25')),  # Invalid input followed by valid input
    (['invalid', 'invalid', '5.25'], Decimal('5.25')),  # Invalid input twice followed by valid input
])
def test_validate_decimal_input(input_values, expected_output, capsys, mock_input, monkeypatch):
    '''Test validate_decimal_input with different input values.'''
    inputs = iter(input_values)
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    assert validate_decimal_input('Enter a decimal: ') == expected_output

    captured = capsys.readouterr()
    assert "Invalid input. Please enter a valid number." in captured.out

def test_validate_division_operands_invalid():
    '''Test validate_division_operands with invalid divisor.'''
    with pytest.raises(ValueError) as exc_info:
        validate_division_operands(Decimal('10'), Decimal('0'))
    assert str(exc_info.value) == "Cannot divide by zero."

def test_validate_division_operands_returns_operands():
    '''Test validate_division_operands returns the provided operands.'''
    a, b = Decimal('10'), Decimal('2')
    result = validate_division_operands(a, b)
    assert result == (a, b)
