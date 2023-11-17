import tkinter as tk
from tkinter import ttk
from test_lab_3.CalculPres import CalculatorPresenter


class CalculatorView(tk.Tk):
    def __init__(self, presenter):
        super().__init__()
        self.presenter = presenter(self)
        self.title("Calculator")
        self.geometry("300x200")

        self.result_label = ttk.Label(self, text="Result:")
        self.result_label.pack(pady=10)

        self.first_argument_entry = ttk.Entry(self)
        self.first_argument_entry.pack(pady=5)

        self.second_argument_entry = ttk.Entry(self)
        self.second_argument_entry.pack(pady=5)

        self.plus_button = ttk.Button(self, text="+", command=self.presenter.on_plus_clicked)
        self.plus_button.pack(side=tk.LEFT, padx=5)

        self.minus_button = ttk.Button(self, text="-", command=self.presenter.on_minus_clicked)
        self.minus_button.pack(side=tk.LEFT, padx=5)

        self.divide_button = ttk.Button(self, text="/", command=self.presenter.on_divide_clicked)
        self.divide_button.pack(side=tk.LEFT, padx=5)

        self.multiply_button = ttk.Button(self, text="*", command=self.presenter.on_multiply_clicked)
        self.multiply_button.pack(side=tk.LEFT, padx=5)

    def printResult(self, result):
        self.result_label.config(text=f"Result: {result}")

    def displayError(self, message):
        print(f"Error: {message}")

    def getFirstArgumentAsString(self):
        return self.first_argument_entry.get()

    def getSecondArgumentAsString(self):
        return self.second_argument_entry.get()


if __name__ == "__main__":
    CalculatorView(CalculatorPresenter).mainloop()
