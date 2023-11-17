from Calcul import Calculator


class CalculatorPresenter:
    def __init__(self, view):
        self.view = view
        self.__calk = Calculator()

    def on_plus_clicked(self):
        try:
            first_arg = float(self.view.getFirstArgumentAsString())
            second_arg = float(self.view.getSecondArgumentAsString())
            result = self.__calk.sum(first_arg, second_arg)
            self.view.printResult(result)
        except ValueError:
            self.view.displayError("Invalid input. Please enter valid numbers.")

    def on_minus_clicked(self):
        try:
            first_arg = float(self.view.getFirstArgumentAsString())
            second_arg = float(self.view.getSecondArgumentAsString())
            result = self.__calk.subtract(first_arg, second_arg)
            self.view.printResult(result)
        except ValueError:
            self.view.displayError("Invalid input. Please enter valid numbers.")

    def on_divide_clicked(self):
        try:
            first_arg = float(self.view.getFirstArgumentAsString())
            second_arg = float(self.view.getSecondArgumentAsString())
            if second_arg != 0:
                result = self.__calk.divide(first_arg, second_arg)
                self.view.printResult(result)
            else:
                self.view.displayError("Cannot divide by zero.")
        except ValueError:
            self.view.displayError("Invalid input. Please enter valid numbers.")

    def on_multiply_clicked(self):
        try:
            first_arg = float(self.view.getFirstArgumentAsString())
            second_arg = float(self.view.getSecondArgumentAsString())
            result = self.__calk.multiply(first_arg, second_arg)
            self.view.printResult(result)
        except ValueError:
            self.view.displayError("Invalid input. Please enter valid numbers.")
