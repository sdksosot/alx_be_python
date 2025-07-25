#!/usr/bin/python3
"""
Arithmetic Operations Module
This module provides a function to perform basic arithmetic operations.
"""

def perform_operation(num1: float, num2: float, operation: str):
    """
    Perform basic arithmetic operations on two numbers.
    
    Args:
        num1 (float): First number
        num2 (float): Second number
        operation (str): Operation to perform ('add', 'subtract', 'multiply', 'divide')
    
    Returns:
        float: Result of the arithmetic operation
        str: Error message in case of division by zero
    """
    operation = operation.lower().strip()
    
    if operation == 'add':
        return num1 + num2
    elif operation == 'subtract':
        return num1 - num2
    elif operation == 'multiply':
        return num1 * num2
    elif operation == 'divide':
        if num2 == 0:
            return "Error: Division by zero is not allowed"
        return num1 / num2
    else:
        return "Error: Invalid operation"