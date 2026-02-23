import csv
import os

class Calculator:
    def __init__(self):
        self.history_file = "data/calculations.csv"
        os.makedirs("data", exist_ok=True)

    def calculate(self, expression):
        try:
            result = eval(expression)
            self.save_to_csv(expression, result)
            return result
        except Exception as e:
            return f"Error: {e}"

    def save_to_csv(self, expression, result):
        with open(self.history_file, "a", newline="") as file:
            writer = csv.writer(file)
            writer.writerow([expression, result])