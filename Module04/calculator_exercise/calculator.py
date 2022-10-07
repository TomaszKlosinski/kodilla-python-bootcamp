#!/usr/bin/env python3
"""Simple command-line-based calculator"""
import logging

logging.basicConfig(level=logging.DEBUG)

OPERATIONS_TYPES = {
    "1": "Addition",
    "2": "Subtraction",
    "3": "Multiplication",
    "4": "Division",
}

WRONG_OPERATION_ERROR = "Wrong operation - choose 1 or 2 or 3 or 4"
WRONG_NUMBER_ERROR = "Wrong number - type int or float"


def calculate(operation: str, number1: str, number2: str) -> float:
    if operation == "1":
        return float(number1) + float(number2)
    elif operation == "2":
        return float(number1) - float(number2)
    elif operation == "3":
        return float(number1) * float(number2)
    elif operation == "4":
        return float(number1) / float(number2)


def validate_operation(operation: str) -> None:
    if operation not in OPERATIONS_TYPES.keys():
        logging.error(WRONG_OPERATION_ERROR)
        exit(100)


def validate_number(number: str) -> None:
    try:
        float(number)
    except ValueError:
        logging.error(WRONG_NUMBER_ERROR)
        exit(100)


def main() -> None:
    operation = input(
        "Specify the action using the appropriate number: \n"
        "1. Addition, 2. Subtraction, 3. Multiplication, 4. Division: "
    )
    validate_operation(operation)

    number1 = input("Enter number 1: ")
    validate_number(number1)
    number2 = input("Enter number 2: ")
    validate_number(number2)

    logging.debug(f"{OPERATIONS_TYPES[operation]} of {number1} and {number2}")

    result = calculate(operation, number1, number2)
    print(f"The result is {result}")


if __name__ == "__main__":
    main()
