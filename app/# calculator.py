# calculator.py

def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b != 0:
        return a / b
    else:
        return "Division by zero is not allowed."

# Приклад використання
if __name__ == "__main__":
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))
    print("Sum: ", add(a, b))
    print("Difference: ", subtract(a, b))
    print("Product: ", multiply(a, b))
    print("Quotient: ", divide(a, b))
