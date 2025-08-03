import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Test cases for SimpleCalculator class"""
    
    def setUp(self):
        """Create a calculator instance before each test"""
        self.calc = SimpleCalculator()
    
    def test_addition(self):
        """Test addition operation with various inputs"""
        self.assertEqual(self.calc.add(2, 3), 5)       # Positive numbers
        self.assertEqual(self.calc.add(-1, -1), -2)    # Negative numbers
        self.assertEqual(self.calc.add(0, 5), 5)       # Zero addition
        self.assertEqual(self.calc.add(2.5, 3.5), 6.0) # Decimal numbers
    
    def test_subtraction(self):
        """Test subtraction operation with various inputs"""
        self.assertEqual(self.calc.subtract(5, 3), 2)      # Positive result
        self.assertEqual(self.calc.subtract(3, 5), -2)     # Negative result
        self.assertEqual(self.calc.subtract(0, 0), 0)      # Zero subtraction
        self.assertEqual(self.calc.subtract(2.5, 1.5), 1.0) # Decimal numbers
    
    def test_multiplication(self):
        """Test multiplication operation with various inputs"""
        self.assertEqual(self.calc.multiply(2, 3), 6)      # Positive numbers
        self.assertEqual(self.calc.multiply(-2, 3), -6)    # Mixed signs
        self.assertEqual(self.calc.multiply(0, 5), 0)      # Multiplication by zero
        self.assertEqual(self.calc.multiply(1.5, 2), 3.0)  # Decimal numbers
    
    def test_division(self):
        """Test division operation with various inputs"""
        self.assertEqual(self.calc.divide(6, 3), 2.0)      # Exact division
        self.assertEqual(self.calc.divide(5, 2), 2.5)      # Fractional result
        self.assertEqual(self.calc.divide(-6, 3), -2.0)    # Negative result
        self.assertEqual(self.calc.divide(0, 5), 0.0)      # Zero dividend
    
    def test_division_by_zero(self):
        """Test division by zero raises appropriate exception"""
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(5, 0)
        with self.assertRaises(ZeroDivisionError):
            self.calc.divide(0, 0)

if __name__ == "__main__":
    unittest.main()
