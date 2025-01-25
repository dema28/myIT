"""Напишите функцию calculate , которая принимает три аргумента: два числа и
строку, обозначающую операцию ( "+" , "-" , "*" или "/" ). Функция должна
выполнять указанную операцию и возвращать результат. Если операция не
поддерживается, вернуть сообщение об ошибке."""

def calculate(num1, num2, operation):
    if operation == "+":
        return num1 + num2
    elif operation == "-":
        return num1 - num2
    elif operation == "*":
        return num1 * num2
    elif operation == "/":
        if num2 == 0:
            return "Error: Division by zero is not allowed."
        else:
            return num1 / num2
    else:
        return "Error: Unsupported operation."

result = calculate(5, 3, "+")
print(result)  # Output: 8

result = calculate(10, 2, "/")
print(result)  # Output: 5.0

result = calculate(5, 0, "/")
print(result)  # Output: Error: Division by zero is not allowed.

result = calculate(5, 3, "^")
print(result)  # Output: Error: Unsupported operation.

result = calculate(5, 3, "invalid_operation")
print(result)  # Output: Error: Unsupported operation.

