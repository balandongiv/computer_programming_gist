def simple_add(first_number, second_number=5, third_number=10):
    """
    This function adds three numbers together.

    It takes the first number as a required input.
    The second and third numbers are optional.
    If you don't provide them, they will default to 5 and 10, respectively.

    Example:
        simple_add(2)  # This will add 2 + 5 + 10 = 17

    Args:
        first_number: The first number to add.
        second_number: The second number to add (default is 5).
        third_number: The third number to add (default is 10).

    Returns:
        The sum of all three numbers.
    """
    total = first_number + second_number + third_number
    return total




print(simple_add(3))                 # Using only the required input
print(simple_add(first_number=3, second_number=4)) # Using named arguments
print(simple_add(3, second_number=4))  # Mixing positional and named arguments
print(simple_add(2, second_number=3, third_number=4))  # Specifying all arguments
print(simple_add(first_number=2, third_number=4, second_number=3)) # Different order