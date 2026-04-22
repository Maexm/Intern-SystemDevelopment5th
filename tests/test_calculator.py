"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


@pytest.fixture
def calc():
    return Calculator()

class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self, calc):
        """Test adding two positive numbers."""
        # Arrange
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self, calc):
        """Test adding two negative numbers."""
        # Arrange
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self, calc):
        """Test adding positive and negative numbers."""
        # Arrange
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self, calc):
        """Test adding negative and positive numbers."""
        # Arrange
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self, calc):
        """Test adding positive number with zero."""
        # Arrange
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self, calc):
        """Test adding zero with positive number."""
        # Arrange
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self, calc):
        """Test adding floating point numbers."""
        # Arrange
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)
    
    def test_invalid_range_ab(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = Calculator.MAX_VALUE + 1
        b = Calculator.MIN_VALUE - 1

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.add(a, b)

    def test_invalid_range_a(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = Calculator.MAX_VALUE + 1
        b = 0

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.add(a, b)
    
    def test_invalid_range_b(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = 0
        b = Calculator.MIN_VALUE - 1

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.add(a, b)



class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self, calc):
        """Test subtracting positive numbers."""
        # Arrange
        a = 10
        b = 15
        expected = -5
        # Act
        result = calc.subtract(a, b)

        # Assert
        assert result == expected
    
    def test_invalid_range_ab(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = Calculator.MAX_VALUE + 1
        b = Calculator.MIN_VALUE - 1

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.subtract(a, b)
    
    def test_invalid_range_a(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = Calculator.MAX_VALUE + 1
        b = 0

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.subtract(a, b)
    
    def test_invalid_range_b(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = 0
        b = Calculator.MIN_VALUE - 1

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.subtract(a, b)


class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self, calc):
        """Test multiplying positive numbers."""
        # Arrange
        a = 5
        b = 7
        expected = 35
        # Act
        result = calc.multiply(a, b)

        # Assert
        assert result == expected
    
    def test_invalid_range_ab(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = Calculator.MAX_VALUE + 1
        b = Calculator.MIN_VALUE - 1

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.multiply(a, b)
    
    def test_invalid_range_a(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = Calculator.MAX_VALUE + 1
        b = 0

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.multiply(a, b)
    
    def test_invalid_range_b(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = 0
        b = Calculator.MIN_VALUE - 1

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.multiply(a, b)


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self, calc):
        """Test dividing positive numbers."""
        # Arrange
        a = 35
        b = 5
        expected = 7
        # Act
        result = calc.divide(a, b)

        # Assert
        assert result == expected

    def test_invalid_range_ab(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = Calculator.MAX_VALUE + 1
        b = Calculator.MIN_VALUE - 1

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.divide(a, b)
    
    def test_invalid_range_a(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = Calculator.MAX_VALUE + 1
        b = 1

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.divide(a, b)
    
    def test_invalid_range_b(self, calc):
        """Test that invalid ranges throw an exception"""

        # Arrange
        a = 0
        b = Calculator.MIN_VALUE - 1

        # Act
        with pytest.raises(InvalidInputException): # optional: pass match="Error msg"
            calc.divide(a, b)


    def test_divide_by_zero(self, calc):
        """Test dividing positive numbers."""
        # Arrange
        a = 35
        b = 0
        # Act
        with pytest.raises(ValueError):
            calc.divide(a, b)
    
class TestRange():

    def test_basic_range_a_b(self, calc):
        # Arrange
        a = Calculator.MAX_VALUE + 1
        b = Calculator.MIN_VALUE - 1

        # Act
        with pytest.raises(InvalidInputException):
            calc._validate_input(a, b)
    
    def test_basic_range_a(self, calc):
        # Arrange
        a = Calculator.MAX_VALUE + 1
        b = Calculator.MIN_VALUE

        # Act
        with pytest.raises(InvalidInputException):
            calc._validate_input(a, b)
    
    def test_basic_range_b(self, calc):
        # Arrange
        a = Calculator.MAX_VALUE
        b = Calculator.MIN_VALUE - 1

        # Act
        with pytest.raises(InvalidInputException):
            calc._validate_input(a, b)

    # Edge cases that are STILL within range
    def test_range_mutant_a(self, calc):
        # Arrange
        a = Calculator.MAX_VALUE
        b = 0

        # Act
        calc._validate_input(a, b)

    def test_range_mutant_b(self, calc):
        # Arrange
        a = 0
        b = Calculator.MIN_VALUE

        # Act
        calc._validate_input(a, b)

