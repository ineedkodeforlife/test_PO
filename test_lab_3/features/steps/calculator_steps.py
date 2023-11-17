import unittest
from unittest.mock import MagicMock
from test_lab_3.CalculPres import CalculatorPresenter

class TestCalculatorPresenter(unittest.TestCase):
    def setUp(self):
        self.view_mock = MagicMock()
        self.presenter = CalculatorPresenter(self.view_mock)

    def test_sum(self):
        self.view_mock.getFirstArgumentAsString.return_value = "2"
        self.view_mock.getSecondArgumentAsString.return_value = "3"
        self.presenter.on_plus_clicked()
        self.view_mock.printResult.assert_called_once_with(5)

    def test_subtract(self):
        self.view_mock.getFirstArgumentAsString.return_value = "5"
        self.view_mock.getSecondArgumentAsString.return_value = "2"
        self.presenter.on_minus_clicked()
        self.view_mock.printResult.assert_called_with(3)

    def test_multiply(self):
        self.view_mock.getFirstArgumentAsString.return_value = "2"
        self.view_mock.getSecondArgumentAsString.return_value = "4"
        self.presenter.on_multiply_clicked()
        self.view_mock.printResult.assert_called_with(8)

    def test_divide(self):
        self.view_mock.getFirstArgumentAsString.return_value = "8"
        self.view_mock.getSecondArgumentAsString.return_value = "2"
        self.presenter.on_divide_clicked()
        self.view_mock.printResult.assert_called_with(4)

        # Test division by zero
        self.view_mock.getSecondArgumentAsString.return_value = "0"
        self.presenter.on_divide_clicked()
        self.view_mock.displayError.assert_called_with("Cannot divide by zero.")

if __name__ == '__main__':
    unittest.main()
