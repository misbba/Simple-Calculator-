"""
calculator.py - Smart Calculator Core Mathematics Logic

Contains modular functions for basic and advanced math operations,
along with error checking and result formatting.
"""

import math

def add(a: float, b: float) -> float:
    """Returns the sum of two numbers."""
    return a + b

def subtract(a: float, b: float) -> float:
    """Returns the difference of two numbers."""
    return a - b

def multiply(a: float, b: float) -> float:
    """Returns the product of two numbers."""
    return a * b

def divide(a: float, b: float) -> float:
    """Returns the quotient of two numbers. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b

def modulus(a: float, b: float) -> float:
    """Returns the remainder of division of two numbers. Raises ValueError on modulus by zero."""
    if b == 0:
        raise ValueError("Cannot calculate modulus with zero.")
    return a % b

def power(a: float, b: float) -> float:
    """Returns 'a' raised to the power of 'b'."""
    return a ** b

def floor_divide(a: float, b: float) -> float:
    """Returns the integer floor division of two numbers. Raises ValueError on division by zero."""
    if b == 0:
        raise ValueError("Cannot perform floor division by zero.")
    return a // b

def square_root(a: float) -> float:
    """Returns the square root of a non-negative number. Raises ValueError if negative."""
    if a < 0:
        raise ValueError("Cannot calculate the square root of a negative number.")
    return math.sqrt(a)

def percentage(a: float, b: float) -> float:
    """
    Calculates 'a' percentage of 'b'.
    Example: 10% of 500 = (10 / 100) * 500 = 50
    """
    return (a * b) / 100.0

def format_result(value: float):
    """
    Formats the result for clean display:
    - Displays integer numbers without trailing decimals (e.g., 30.0 -> 30)
    - Formats floating point numbers up to 6 decimal places cleanly without unnecessary trailing zeros.
    """
    try:
        val_float = float(value)
        if val_float.is_integer():
            return int(val_float)
    except (ValueError, TypeError):
        pass
    
    # Format float up to 6 decimal places, stripping trailing zeros
    formatted = f"{value:.6f}".rstrip('0').rstrip('.')
    return formatted

