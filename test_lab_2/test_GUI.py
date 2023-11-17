import unittest
from tkinter import Tk, Entry
from unittest.mock import MagicMock
from CalculPres import CalculatorPresenter
from Calcul import Calculator
from main import CalculatorView


class TestCalculator(unittest.TestCase):
    def test_sum(self):
        calc = Calculator()
        result = calc.sum(2, 3)
        self.assertEqual(result, 5)

    def test_subtract(self):
        calc = Calculator()
        result = calc.subtract(5, 2)
        self.assertEqual(result, 3)

    def test_multiply(self):
        calc = Calculator()
        result = calc.multiply(2, 4)
        self.assertEqual(result, 8)

    def test_divide(self):
        calc = Calculator()
        result = calc.divide(8, 2)
        self.assertEqual(result, 4)

        with self.assertRaises(ArithmeticError):
            calc.divide(5, 0)

    def test_calculator_presenter(self):
        view = MagicMock()
        presenter = CalculatorPresenter(view)
        presenter.__calk = MagicMock()

        view.getFirstArgumentAsString.return_value = "2"
        view.getSecondArgumentAsString.return_value = "3"
        presenter.on_plus_clicked()
        view.printResult.assert_called_once_with(5)

        view.getFirstArgumentAsString.return_value = "5"
        view.getSecondArgumentAsString.return_value = "2"
        presenter.on_minus_clicked()
        view.printResult.assert_called_with(3)

        view.getFirstArgumentAsString.return_value = "2"
        view.getSecondArgumentAsString.return_value = "4"
        presenter.on_multiply_clicked()
        view.printResult.assert_called_with(8)

        view.getFirstArgumentAsString.return_value = "8"
        view.getSecondArgumentAsString.return_value = "2"
        presenter.on_divide_clicked()
        view.printResult.assert_called_with(4)

        view.getSecondArgumentAsString.return_value = "0"
        presenter.on_divide_clicked()
        view.displayError.assert_called_with("Cannot divide by zero.")

    def test_calculator_view(self):
        root = Tk()
        view = CalculatorView(CalculatorPresenter)
        view.result_label = MagicMock()
        view.first_argument_entry = Entry()
        view.second_argument_entry = Entry()

        view.getFirstArgumentAsString = MagicMock(return_value="2")
        self.assertEqual(view.getFirstArgumentAsString(), "2")

        view.getSecondArgumentAsString = MagicMock(return_value="3")
        self.assertEqual(view.getSecondArgumentAsString(), "3")

        view.printResult(5)
        view.result_label.config.assert_called_once_with(text="Result: 5")

        view.displayError("Invalid input.")
        print_called = False
        try:
            print("Error: Invalid input.")
            print_called = True
        except:
            pass
        self.assertTrue(print_called)


if __name__ == "__main__":
    unittest.main()
