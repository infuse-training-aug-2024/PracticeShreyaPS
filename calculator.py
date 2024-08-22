class Calculator:
    def add(self, num1, num2):
        return num1 + num2
    def sub(self, num1, num2):
        return num1 - num2
    def mul(self, num1, num2):
        return num1 * num2

# Creating an instance of the Calculator class
calc = Calculator()

# Using the add method to add two numbers
result = calc.add(10, 5)
result = calc.sub(10, 5)
result = calc.mul(10, 5)

print("The sum is:", result)
