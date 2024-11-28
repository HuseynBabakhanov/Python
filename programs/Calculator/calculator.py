# Python calculator

operator = input("Enter an operator (+ - * /): ")
num1 = float(input("Enter the 1st number: "))
num2 = float(input("Enter the 2nd number: "))

# Calculating the result
if operator == "+":
    result = num1 + num2
elif operator == "-":
    result = num1 - num2
elif operator == "*":
    result = num1 * num2
elif operator == "/":
    if num2 == 0:
        print("Error: Division by zero is not allowed")
        result = None
    else:
        result = num1 / num2
else:
    print(f"{operator} is not a valid operator")
    result = None

# Formatting and outputting the result
if result is not None:
    # If the result is integer, output without fractional part
    if result.is_integer():
        print(int(result))  # Пример: 2.0 → 2
    else:
        # Remove extra zeros if the result is fractional
        print(f"{result:.3f}".rstrip("0").rstrip("."))
