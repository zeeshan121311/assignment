class SquareCalculator:
    def __init__(self, numbers):
        self.numbers = numbers

    def calculate_squares(self):
        return list(map(lambda x: x ** 2, self.numbers))

user_input = input("Enter a list of numbers separated by spaces: ")
numbers = list(map(int, user_input.split()))

calculator = SquareCalculator(numbers)
squared_numbers = calculator.calculate_squares()

print("Original numbers:", numbers)
print("Squared numbers:", squared_numbers)