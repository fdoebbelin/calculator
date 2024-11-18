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
        return "Error: Division durch Null!"


if __name__ == "__main__":
    print("Willkommen zum einfachen Taschenrechner!")
    num1 = float(input("Geben Sie die erste Zahl ein: "))
    num2 = float(input("Geben Sie die zweite Zahl ein: "))
    print(f"Addition: {add(num1, num2)}")
    print(f"Subtraktion: {subtract(num1, num2)}")
    print(f"Multiplikation: {multiply(num1, num2)}")
    print(f"Division: {divide(num1, num2)}")
