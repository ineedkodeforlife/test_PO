class CalculatorPresenter:

    def __init__(self):
        self.__firstval = 12
        self.second_val = 0
        self.result = 0

    def on_plus_clicked(self):
        self.second_val = int(input())
        print(self.__firstval + self.second_val)
        self.result = self.__firstval + self.second_val

    def on_minus_clicked(self):
        self.second_val = int(input())
        print(self.__firstval - self.second_val)
        self.result = self.__firstval - self.second_val

    def on_divide_clicked(self):
        self.second_val = int(input())
        if self.second_val != 0:
            print(self.__firstval / self.second_val)
            self.result = self.__firstval / self.second_val
        else:
            raise ArithmeticError('Введите не нулевое значение')

    def on_multiply_clicked(self):
        self.second_val = int(input())
        print(self.__firstval * self.second_val)
        self.result = self.__firstval * self.second_val
