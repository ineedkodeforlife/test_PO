import unittest
from Calcul import Calculator


class TestCalculatorMethods(unittest.TestCase):

    def setUp(self):
        # Arrange
        self.calculator = Calculator()

    def test_sum(self):
        # Act
        result = self.calculator.sum(1, 2)

        # Assert
        self.assertEqual(result, 3)

    def test_subtract(self):
        # Act
        result = self.calculator.subtract(5, 3)

        # Assert
        self.assertEqual(result, 2)

    def test_multiply(self):
        # Act
        result = self.calculator.multiply(2, 4)

        # Assert
        self.assertEqual(result, 8)

    def test_divide(self):
        # Act
        result = self.calculator.divide(8, 2)

        # Assert
        self.assertEqual(result, 4)

    def test_divide_by_zero(self):
        # Act and Assert
        with self.assertRaises(ArithmeticError):
            self.calculator.divide(5, 0)

    def test_divide_by_small_number(self):
        # Act and Assert
        with self.assertRaises(ArithmeticError):
            self.calculator.divide(1, 1e-9)


if __name__ == '__main__':
    unittest.main()
