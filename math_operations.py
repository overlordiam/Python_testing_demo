# A very basic utility class for math operations
class MathHelper:
    def add(self, a, b):
        return a + b

    def divide(self, a, b):
        if b == 0:
            raise ValueError("Cannot divide by zero.")

        return a / b

    def is_even(self, num):
        return num % 2 == 0

    def get_max(self, numbers):
        if not numbers:
            return None
        return max(numbers)
