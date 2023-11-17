import unittest
from unittest.mock import patch
from CalculPres import CalculatorPresenter


class TestCalculatorPresenter(unittest.TestCase):

    def test_on_plus_clicked(self):
        # Arrange
        presenter = CalculatorPresenter()

        # Act
        with patch('builtins.input', return_value='3'):
            presenter.on_plus_clicked()

        # Assert
        self.assertEqual(presenter.result, 15)  # 12 + 3

    def test_on_minus_clicked(self):
        # Arrange
        presenter = CalculatorPresenter()

        # Act
        with patch('builtins.input', return_value='5'):
            presenter.on_minus_clicked()

        # Assert
        self.assertEqual(presenter.result, 7)  # 12 - 5

    def test_on_divide_clicked(self):
        # Arrange
        presenter = CalculatorPresenter()

        # Act
        with patch('builtins.input', return_value='2'):
            presenter.on_divide_clicked()

        # Assert
        self.assertEqual(presenter.result, 6)  # 12 / 2

    def test_on_divide_clicked_exception(self):
        # Arrange
        presenter = CalculatorPresenter()

        # Act and Assert
        with self.assertRaises(ArithmeticError):
            with patch('builtins.input', return_value='0'):
                presenter.on_divide_clicked()

    def test_on_multiply_clicked(self):
        # Arrange
        presenter = CalculatorPresenter()

        # Act
        with patch('builtins.input', return_value='4'):
            presenter.on_multiply_clicked()

        # Assert
        self.assertEqual(presenter.result, 48)  # 12 * 4


if __name__ == '__main__':
    unittest.main()
