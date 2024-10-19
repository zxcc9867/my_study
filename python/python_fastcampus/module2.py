def calculate(num1, num2):
    try:
        result = int(num1) + int(num2)
        print(f"The sum of {num1} and {num2} is {result}")
        return result
    except ValueError:
        print("Invalid input. Please enter integers only.")
