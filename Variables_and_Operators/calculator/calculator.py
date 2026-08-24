"""
Calculator boilerplate project (STUDENT VERSION)
==================================================

This file contains the building blocks for the interactive calculator
covered in the tutorial, written as separate functions instead of one
long script. Writing the logic as functions is what allows the
automated tests in ``test_calculator.py`` to check your work.

Your task: implement the necessary logic below so that all of the tests in
``test_calculator.py`` pass.

How to run the tests:

    pytest -v

Every test will fail until you implement the matching function.
That is expected. Implement one function, re-run pytest, and watch
the failures reduce one at a time. 

You will have to remove the ``raise NotImplementedError`` line from the logic you implement and replace it with your own code, remembering to return the variable ``result`` instead of printing it. The tests will check the return value.
"""


def add(a, b):
    """Return the sum of a and b."""
    # TODO: implement the add logic here. Remember to return the result instead of printing 
    raise NotImplementedError


def subtract(a, b):
    """Return a minus b."""
    # TODO: implement this subtract logic here. Remember to return the result instead of printing
    raise NotImplementedError


def multiply(a, b):
    """Return a multiplied by b."""
    # TODO: implement this function
    raise NotImplementedError


def divide(a, b):
    """
    Return a divided by b.

    If b is 0, raise a ZeroDivisionError instead of letting the
    program crash with an unhandled exception. Hint: you can raise
    one yourself with:

        raise ZeroDivisionError("Cannot divide by zero")
    """
    # TODO: implement the divide logic here. Remember to return the result instead of printing
    raise NotImplementedError


def modulo(a, b):
    """
    Return the remainder of a divided by b.

    If b is 0, raise a ZeroDivisionError, the same as divide().
    """
    # TODO: implement the modulo logic here. Remember to return the result instead of printing
    raise NotImplementedError


def power(a, b):
    """Return a raised to the power of b."""
    # TODO: implement the power logic here. Remember to return the result instead of printing
    raise NotImplementedError


def percentage_of(value, percent):
    """
    Return `percent` percent of `value`.

    For example, percentage_of(200, 15) should return 30.0,
    because 15% of 200 is 30.
    """
    # TODO: implement the percentage_of logic here. Remember to return the result instead of printing
    raise NotImplementedError


def convert_currency(amount, rate):
    """
    Convert `amount` using the given exchange `rate`, rounded to
    2 decimal places.

    For example, convert_currency(100, 1.27) should return 127.0.
    """
    # TODO: implement the the convert_currency logic here. Remember to return the result instead of printing
    raise NotImplementedError


def run_calculator():
    """
    Interactive command-line calculator.

    This ties the functions above together into the same
    multi-operation calculator built in the tutorial. You do not
    need to change this function; once the functions above are
    implemented, this will work automatically.
    """
    number1 = float(input("Enter first number: "))
    number2 = float(input("Enter second number: "))
    operation = input("Choose +, -, *, /, %, or ** : ")

    # DO NOT change any of the code below this line. It will call your functions and print the result.
    
    try:
        if operation == "+":
            result = add(number1, number2)
        elif operation == "-":
            result = subtract(number1, number2)
        elif operation == "*":
            result = multiply(number1, number2)
        elif operation == "/":
            result = divide(number1, number2)
        elif operation == "%":
            result = modulo(number1, number2)
        elif operation == "**":
            result = power(number1, number2)
        else:
            result = "Invalid operation"
    except ZeroDivisionError as error:
        result = f"Error: {error}"

    print("The answer is:", result)


if __name__ == "__main__":
    run_calculator()
